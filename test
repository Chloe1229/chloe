import streamlit as st

def main():
    st.set_page_config(page_title="MFDS 변경 16번 자동화 예시", layout="wide")
    if 'page' not in st.session_state:
        st.session_state['page'] = 1
    page = st.session_state['page']

    # 스타일
    st.markdown("""
        <style>
        .main-title {font-size:2.2rem;font-weight:900;color:#055280;line-height:1.2;margin-bottom:1.2rem;}
        .subtitle {font-size:1.14rem;font-weight:700;color:#227a6b;margin-top:1rem;}
        .step-label {font-size:1.05rem;font-weight:600;color:#3b444d;margin-top:0.9rem;}
        .doc-box {background:#f3f9f9;padding:0.57rem 1rem 0.57rem 1.15rem;border-radius:0.7rem;margin:0.4rem 0;}
        .report-box {background:#fff9ee;padding:0.57rem 1rem;border-radius:0.7rem;margin:0.4rem 0;}
        .explain-box {background:#f8f6fa;padding:0.59rem 1rem;border-radius:0.7rem;margin:0.6rem 0 1.2rem 0;}
        .sheet-preview {background:#f7faff;border:1.1px solid #d0e2f1;padding:1.03rem 1.2rem;border-radius:1rem;margin-top:1rem;}
        .sheet-title {font-size:1.08rem;font-weight:700;color:#334;}
        </style>
    """, unsafe_allow_html=True)

    step6_options = {
        "P3_16": {
            "label": "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
            "options": ["충족", "미충족"],
            "note": "변경 사유와 구체적 관리기준이 반드시 첨부되어야 합니다."
        }
    }
    step7_results = {
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

    # STEP 1~3: 적용대상 판단
    if page == 1:
        st.markdown('<div class="main-title">STEP 1~3. 적용대상 판단</div>', unsafe_allow_html=True)
        st.header("Step 1. CTD 작성대상 완제의약품 해당 여부")
        step1 = st.radio(
            "제6조제1항에 따라 국제공통기술문서(CTD)로 작성하여 허가받거나 신고한 의약품의 제조원 또는 제조방법을 변경하는 경우에 해당합니까?",
            ("선택하세요", "예", "아니오"),
            key="step1_radio"
        )
        if step1 == "아니오":
            st.warning("CTD 작성대상 완제의약품 해당여부를 확인하고, 해당시 먼저 CTD 3부 품질평가 자료(3.2.S.2 등) 심사 필요.")
            st.stop()
        if step1 == "예":
            st.header("Step 2. 제조방법 변경 항목 여부")
            step2 = st.radio(
                "제조에 관한 항목(CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3, 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7)을 변경하는 경우에 해당합니까?",
                ("선택하세요", "예", "아니오"),
                key="step2_radio"
            )
            if step2 == "아니오":
                st.warning("가이드라인 적용 대상에 해당하지 않습니다.")
                st.stop()
            if step2 == "예":
                st.header("Step 3. 제조방법 CTD 적용(또는 전환) 품목 해당 여부")
                step3 = st.radio(
                    "품목의 허가(신고) 사항 중 제조방법에 해당하는 자료(CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3, 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7)를 국제공통기술문서(CTD)로 제출하여 심사받은 '제조방법 CTD 적용(또는 전환)' 품목에 해당합니까?",
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

    # STEP 4: 변경항목 선택 (오류 없는 방식)
    elif page == 2:
        st.markdown('<div class="main-title">STEP 4. 변경사항 선택</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">3.2.P.3 제조</div>', unsafe_allow_html=True)
        st.markdown('<div class="step-label">16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경</div>', unsafe_allow_html=True)
        chg16 = st.radio(
            "공정관리시험(IPC) 기준 변경",
            ("변경 없음", "변경 있음"),
            key="s4_P3_16"
        )
        if chg16 == "변경 있음":
            if st.button("다음단계로", key="to5"):
                st.session_state['page'] = 3
                st.rerun()

    # STEP 5: 선택항목 하위내용(여기서는 곧바로 1개 항목 자동 '변경 있음')
    elif page == 3:
        st.markdown('<div class="main-title">STEP 5. 선택한 변경항목 중 변경사항 선택</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">3.2.P.3 제조</div>', unsafe_allow_html=True)
        st.markdown('<div class="step-label">16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경</div>', unsafe_allow_html=True)
        st.success("변경 있음으로 선택됨")
        if st.button("다음단계로", key="to6"):
            st.session_state['page'] = 4
            st.rerun()

    # STEP 6: 충족조건(조건 2개)
    elif page == 4:
        st.markdown('<div class="main-title">STEP 6. 충족요건 선택</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">3.2.P.3 제조</div>', unsafe_allow_html=True)
        item = step6_options["P3_16"]
        col1, col2 = st.columns([3,6])
        with col1:
            cond = st.radio(item["label"], item["options"], key="s6_P3_16")
        with col2:
            st.markdown(f'<div class="doc-box">{item["note"]}</div>', unsafe_allow_html=True)
        if cond in item["options"]:
            if st.button("다음단계로", key="to7"):
                st.session_state['s6_P3_16'] = cond
                st.session_state['page'] = 5
                st.rerun()
        if st.button("이전단계로", key="back5"):
            st.session_state['page'] = 3
            st.rerun()

    # STEP 7: 필요서류/보고유형 안내
    elif page == 5:
        st.markdown('<div class="main-title">STEP 7. 필요서류 및 보고유형 안내</div>', unsafe_allow_html=True)
        cond = st.session_state.get('s6_P3_16', '')
        res = step7_results["P3_16"][cond]
        colA, colB = st.columns([5,5])
        with colA:
            st.markdown('<div class="sheet-title">제출 필요서류</div>', unsafe_allow_html=True)
            for idx, doc in enumerate(res["필요서류"], 1):
                st.markdown(f'<div class="doc-box">{idx}. {doc}</div>', unsafe_allow_html=True)
        with colB:
            st.markdown('<div class="sheet-title">보고유형</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="report-box"><b>{res["보고유형"]}</b> | {res["보고유형명"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="explain-box">{res["설명"]}</div>', unsafe_allow_html=True)
        if st.button("다음단계로", key="to8"):
            st.session_state['page'] = 6
            st.rerun()
        if st.button("이전단계로", key="back6"):
            st.session_state['page'] = 4
            st.rerun()

    # STEP 8: 신청양식 미리보기/인쇄/저장
    elif page == 6:
        st.markdown('<div class="main-title">STEP 8. 신청양식 미리보기</div>', unsafe_allow_html=True)
        st.markdown('<div class="sheet-preview">', unsafe_allow_html=True)
        st.markdown('**[신청양식 자동생성 미리보기]**')
        st.markdown('- **변경항목:** 16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경')
        st.markdown(f'- **충족요건:** {st.session_state.get("s6_P3_16","")}')
        st.markdown(f'- **필요서류:**')
        for idx, doc in enumerate(step7_results["P3_16"][st.session_state.get("s6_P3_16","")]["필요서류"], 1):
            st.markdown(f'  {idx}. {doc}')
        st.markdown(f'- **보고유형:** {step7_results["P3_16"][st.session_state.get("s6_P3_16","")]["보고유형"]} | {step7_results["P3_16"][st.session_state.get("s6_P3_16","")]["보고유형명"]}')
        st.markdown('</div>', unsafe_allow_html=True)

        colP, colQ = st.columns([2,2])
        with colP:
            st.button("인쇄하기 🖨️", key="print_btn")
        with colQ:
            st.download_button("저장하기(임시)", data="신청서 예시", file_name="mfds_sheet_sample.txt")
        if st.button("이전단계로", key="back7"):
            st.session_state['page'] = 5
            st.rerun()

if __name__ == "__main__":
    main()
