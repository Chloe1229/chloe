import streamlit as st

st.set_page_config(page_title="MFDS 제조방법 변경 자동화", layout="wide")

# ---- 데이터: 실제 프롬프트 업무표 내용을 Python dict로 정리 ----
categories = [
    # 대분류, 코드, 중분류, 세부항목 코드, 세부항목명
    ("3.2.S 원료의약품", None, None, None, None),
    ("3.2.S.1 일반정보", "S1_1", None, "S1_1", "1. 원료의약품 명칭변경"),
    ("3.2.P 완제의약품", None, None, None, None),
    ("3.2.P.3 제조", None, None, None, None),
    ("3.2.P.3 제조", "P3_16", None, "P3_16", "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경")
]

# Step6 충족조건, Step7 필요서류/보고유형/설명
step6_options = {
    "S1_1": {
        "label": "1. 원료의약품 명칭변경",
        "options": ["충족"],  # 실제 프롬프트 기준
    },
    "P3_16": {
        "label": "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
        "options": ["충족", "미충족"],
    }
}
step7_results = {
    "S1_1": {
        "충족": {
            "필요서류": [
                "(S.1.1) 공정서 또는 국제 의약품 일반명 리스트(INN) 등 근거서류",
                "개정된 제품정보"
            ],
            "보고유형": "AR",
            "보고유형명": "연차보고 (Annual Report, AR)",
            "설명": "이 변경은 「의약품의 품목허가‧신고‧심사 규정」 제3조의2 제2항 및 제4항에 따른 연차보고(AR) 수준의 변경사항입니다."
        }
    },
    "P3_16": {
        "충족": {
            "필요서류": [
                "공정관리시험(IPC) 변경 관련 근거서류",
                "관리기준 개정 내역/사유서"
            ],
            "보고유형": "Cmin",
            "보고유형명": "경미변경 (Minor Change, Cmin)",
            "설명": "해당 변경은 경미변경(Cmin)으로 분류되며, '의약품의 품목허가·신고·심사 규정' 별표 19를 참고하세요."
        },
        "미충족": {
            "필요서류": [
                "공정관리시험(IPC) 변경 관련 상세 설명자료",
                "사유서 및 추가자료"
            ],
            "보고유형": "Cmaj",
            "보고유형명": "중대한 변경 (Major Change, Cmaj)",
            "설명": "충족조건 미달 시 중대한 변경(Cmaj)으로 분류되며, 식약처 추가 심사 및 자료 제출이 필요합니다."
        }
    }
}

# ---- 상태관리 ----
if 'page' not in st.session_state:
    st.session_state['page'] = 1
page = st.session_state['page']

# ---- STEP 1~3: 적용대상 판단 ----
if page == 1:
    st.header("STEP 1~3. 적용대상 판단")
    step1 = st.radio(
        "제6조제1항에 따라 국제공통기술문서(CTD)로 작성하여 허가받거나 신고한 의약품의 제조원 또는 제조방법을 변경하는 경우에 해당합니까?",
        ("선택하세요", "예", "아니오"),
        key="step1_radio"
    )
    if step1 == "아니오":
        st.warning("CTD 작성대상 완제의약품 해당여부를 확인하고, 해당시 먼저 CTD 3부 품질평가 자료(3.2.S.2 등) 심사 필요.")
        st.stop()
    if step1 == "예":
        step2 = st.radio(
            "제조에 관한 항목(CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3, 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7)을 변경하는 경우에 해당합니까?",
            ("선택하세요", "예", "아니오"),
            key="step2_radio"
        )
        if step2 == "아니오":
            st.warning("가이드라인 적용 대상에 해당하지 않습니다.")
            st.stop()
        if step2 == "예":
            step3 = st.radio(
                "제조방법에 해당하는 자료를 CTD로 제출하여 심사받은 '제조방법 CTD 적용(또는 전환)' 품목에 해당합니까?",
                ("선택하세요", "예", "아니오"),
                key="step3_radio"
            )
            if step3 == "아니오":
                st.warning("CTD 3부 품질평가 자료를 제출하여 제조방법 자료로서 심사받으시기 바랍니다.")
                st.stop()
            if step3 == "예":
                if st.button("다음단계로", key="to4"):
                    st.session_state['page'] = 2
                    st.rerun()

# ---- STEP 4: 변경항목 선택 ----
elif page == 2:
    st.header("STEP 4. 변경사항 선택")
    chg = {}
    for _, code, _, detail_code, label in categories:
        if detail_code is not None:
            chg[detail_code] = st.radio(label, ("변경 없음", "변경 있음"), key=f"s4_{detail_code}")
    if st.button("다음단계로", key="to5"):
        st.session_state['s4_result'] = chg
        st.session_state['page'] = 3
        st.rerun()

# ---- STEP 5: 세부 변경항목 표시 ----
elif page == 3:
    st.header("STEP 5. 선택한 변경항목 중 변경사항 선택")
    s4_result = st.session_state.get('s4_result', {})
    targets = [code for code, val in s4_result.items() if val == "변경 있음"]
    if not targets:
        st.warning("변경 있음으로 선택한 항목이 없습니다.")
        st.stop()
    st.session_state['step5_targets'] = targets
    for code in targets:
        label = step6_options.get(code, {}).get("label", code)
        st.write(f"**{label}** - 변경 있음")
    if st.button("다음단계로", key="to6"):
        st.session_state['page'] = 4
        st.rerun()

# ---- STEP 6: 충족요건 선택 ----
elif page == 4:
    st.header("STEP 6. 충족요건 선택")
    step5_targets = st.session_state.get('step5_targets', [])
    step6_selection = {}
    for code in step5_targets:
        item = step6_options.get(code, {})
        cond = st.radio(item.get("label", code), item.get("options", []), key=f"s6_{code}")
        step6_selection[code] = cond
    if st.button("다음단계로", key="to7"):
        st.session_state['step6_selection'] = step6_selection
        st.session_state['page'] = 5
        st.rerun()

# ---- STEP 7: 필요서류/보고유형 안내 ----
elif page == 5:
    st.header("STEP 7. 필요서류 및 보고유형 안내")
    step6_selection = st.session_state.get('step6_selection', {})
    step7_display = {}
    for code, cond in step6_selection.items():
        res = step7_results.get(code, {}).get(cond, {})
        st.write(f"### {step6_options.get(code, {}).get('label', code)}")
        st.write(f"- **필요서류:**")
        for idx, doc in enumerate(res.get("필요서류", []), 1):
            st.write(f"  {idx}. {doc}")
        st.write(f"- **보고유형:** {res.get('보고유형','')} | {res.get('보고유형명','')}")
        st.info(res.get("설명", ""))
        step7_display[code] = res
    if st.button("다음단계로", key="to8"):
        st.session_state['step7_display'] = step7_display
        st.session_state['page'] = 6
        st.rerun()

# ---- STEP 8: 신청양식 미리보기/저장 ----
elif page == 6:
    st.header("STEP 8. 신청양식 미리보기")
    step6_selection = st.session_state.get('step6_selection', {})
    step7_display = st.session_state.get('step7_display', {})
    for code in step6_selection:
        label = step6_options.get(code, {}).get("label", code)
        res = step7_display.get(code, {})
        st.subheader(label)
        st.write(f"- **충족요건:** {step6_selection[code]}")
        st.write(f"- **필요서류:**")
        for idx, doc in enumerate(res.get("필요서류", []), 1):
            st.write(f"  {idx}. {doc}")
        st.write(f"- **보고유형:** {res.get('보고유형','')} | {res.get('보고유형명','')}")
        st.info(res.get("설명", ""))
    st.download_button("신청서 저장 (임시)", data="신청서 미리보기", file_name="mfds_application.txt")
    if st.button("이전단계로", key="back7"):
        st.session_state['page'] = 5
        st.rerun()
