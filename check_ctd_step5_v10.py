import streamlit as st

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 1
    page = st.session_state['page']

    st.title("MFDS 허가 후 제조방법 변경 자동화")

    # Step 1~3: 한 화면에서 순차 노출
    if page == 1:
        st.header("Step 1. CTD 작성대상 완제의약품 해당 여부")
        step1 = st.radio(
            "제6조제1항에 따라 국제공통기술문서(CTD)로 작성하여 허가를 받거나 신고한 의약품의 제조원 또는 제조방법을 변경하는 경우에 해당합니까?",
            ("선택하세요", "예", "아니오"),
            key="step1_radio"
        )
        if step1 == "아니오":
            st.warning("CTD 작성대상 완제의약품 해당여부를 확인하고, 해당시 먼저 CTD 3부 품질평가 자료(3.2.S.2 등) 심사 필요.\n(근거 : 「의약품의 품목허가·신고·심사 규정」제6조, 제3조의2)")
            st.stop()
        if step1 == "예":
            st.header("Step 2. 제조방법 변경 항목 여부")
            step2 = st.radio(
                "제조에 관한 항목(CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3, 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7)을 변경하는 경우에 해당합니까?",
                ("선택하세요", "예", "아니오"),
                key="step2_radio"
            )
            if step2 == "아니오":
                st.warning("가이드라인 적용 대상에 해당하지 않습니다.\n(근거 : 「의약품의 품목허가·신고·심사 규정」[별표 19])")
                st.stop()
            if step2 == "예":
                st.header("Step 3. 제조방법 CTD 적용(또는 전환) 품목 해당 여부")
                step3 = st.radio(
                    "품목의 허가(신고) 사항 중 제조방법에 해당하는 자료(CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3, 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7)를 국제공통기술문서(CTD)로 제출하여 심사받은 '제조방법 CTD 적용(또는 전환)' 품목에 해당합니까?",
                    ("선택하세요", "예", "아니오"),
                    key="step3_radio"
                )
                if step3 == "아니오":
                    st.warning("CTD 3부 품질평가 자료를 제출하여 제조방법 자료로서 심사받으시기 바랍니다.\n(근거 : 「의약품의 품목허가·신고·심사 규정」[별표 19])")
                    st.stop()
                if step3 == "예":
                    if st.button("다음단계로"):
                        st.session_state['page'] = 2
                        st.rerun()

    elif page == 2:
        st.header("Step 4. 변경사항에 해당하는 항목을 선택하세요.")
        categories = [
            ("3.2.S 원료의약품", None),
            ("3.2.S.1 일반정보", "3.2.S.1"),
            ("3.2.S.2 제조", "3.2.S.2"),
            ("3.2.P 완제의약품", None),
            ("3.2.P.1 완제의약품의 성상 및 조성", "3.2.P.1"),
            ("3.2.P.3 제조", "3.2.P.3"),
            ("3.2.P.4 첨가제의 관리", "3.2.P.4"),
            ("3.2.P.7 용기-마개 시스템", "3.2.P.7"),
            ("디자인스페이스(Design Space) 변경", "DS")
        ]
        step4_result = {}
        for name, code in categories:
            if code is None:
                st.markdown(f"**{name}**")
            else:
                sel = st.radio(
                    f"{name}",
                    ("변경 없음", "변경 있음"),
                    key=f"step4_{code}"
                )
                step4_result[code] = sel

        if all(sel in ("변경 없음", "변경 있음") for sel in step4_result.values()):
            if st.button("다음단계로"):
                st.session_state['step4_result'] = step4_result
                st.session_state['page'] = 3
                st.rerun()
        if st.button("이전단계로"):
            st.session_state['page'] = 1
            st.rerun()

    elif page == 3:
        st.header("Step 5. 선택한 변경항목 중 변경사항을 선택하세요.")

        # 계층형 카테고리 정의
        category_hierarchy = {
            "3.2.S.1": {
                "top": "3.2.S 원료의약품",
                "mid": "3.2.S.1 일반정보",
                "subs": [
                    ("1. 원료의약품 명칭변경", "S1_1")
                ]
            },
            "3.2.S.2": {
                "top": "3.2.S 원료의약품",
                "mid": "3.2.S.2 제조",
                "subs": [
                    ("2. 원료의약품의 제조소 또는 제조업자 변경 또는 추가", "S2_2"),
                    ("3. 원료의약품 제조 공정의 변경", "S2_3"),
                    ("4. 원료의약품 제조 공정관리 규격의 변경", "S2_4"),
                    ("5. 원료의약품 또는 중간체의 제조 규모 변경", "S2_5"),
                    ("6. 원료의약품의 제조에 사용되는 원료(출발물질, 중간체, 용매, 시약 등)의 규격변경", "S2_6"),
                ]
            },
            "3.2.P.1": {
                "top": "3.2.P 완제의약품",
                "mid": "3.2.P.1 완제의약품의 성상 및 조성",
                "subs": [
                    ("7. 완제의약품 중 고형제제의 조성 변경", "P1_7"),
                    ("8. 완제의약품 중 고형제제의 코팅층 무게 변경", "P1_8"),
                    ("9. 완제의약품 중 고형제제를 제외한 그 외 제형의 조성 변경", "P1_9"),
                    ("10. 완제의약품 중 고형제제를 제외한 그 외 제형에 쓰이는 착색제 또는 착향제의 종류와 분량의 변경", "P1_10"),
                ]
            },
            "3.2.P.3": {
                "top": "3.2.P 완제의약품",
                "mid": "3.2.P.3 제조",
                "subs": [
                    ("11. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경(단 잉크, 그림, 글자체 등 식별표시를 위한 변경은 제외)", "P3_11"),
                    ("12. 완제의약품 제조공정 중 일부공정 제조소 또는 전체공정 제조소의, 추가 또는 변경", "P3_12"),
                    ("13. 비무균제제의 제조 규모 변경", "P3_13"),
                    ("14. 무균제제의 제조 규모 변경", "P3_14"),
                    ("15. 완제의약품의 제조공정 변경", "P3_15"),
                    ("16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경", "P3_16"),
                ]
            },
            "3.2.P.4": {
                "top": "3.2.P 완제의약품",
                "mid": "3.2.P.4 첨가제의 관리",
                "subs": [
                    ("17. 첨가제 기원의 변경", "P4_17"),
                    ("18. 별규에 해당하는 첨가제의 규격 또는 시험방법변경", "P4_18"),
                    ("19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경", "P4_19"),
                ]
            },
            "3.2.P.7": {
                "top": "3.2.P 완제의약품",
                "mid": "3.2.P.7 용기-마개 시스템",
                "subs": [
                    ("20. 비무균제제의 직접용기 및 포장재질, 종류 변경", "P7_20"),
                    ("21. 무균제제의 직접용기 및 포장 재질, 종류 변경", "P7_21"),
                    ("22. 직접 포장의 규격 변경", "P7_22"),
                    ("23. 포장단위 변경", "P7_23"),
                ]
            },
            "DS": {
                "top": "",
                "mid": "디자인스페이스(Design Space) 변경",
                "subs": []
            },
        }

        step4_result = st.session_state.get('step4_result', {})
        targets = [code for code, sel in step4_result.items() if sel == "변경 있음"]
        step5_result = {}

        for code in targets:
            if code == "DS":
                st.markdown("**디자인스페이스(Design Space) 변경**")
                st.radio("디자인스페이스(Design Space) 변경", ("변경 있음",), index=0, disabled=True, key="step5_DS")
                step5_result[code] = "변경 있음"
            elif code in category_hierarchy:
                top = category_hierarchy[code]['top']
                mid = category_hierarchy[code]['mid']
                subs = category_hierarchy[code]['subs']
                if top:
                    st.markdown(f"**{top}**")
                if mid:
                    st.markdown(f"**{mid}**")
                for q_text, q_code in subs:
                    sel = st.radio(
                        f"{q_text}",
                        ("변경 없음", "변경 있음"),
                        key=f"step5_{q_code}"
                    )
                    step5_result[q_code] = sel

        if st.button("이전단계로"):
            st.session_state['page'] = 2
            st.rerun()

if __name__ == "__main__":
    main()
