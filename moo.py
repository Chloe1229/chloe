# Title11: p3_11 - 3.2.P.3 제조 > 11. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경
if current_key == "p3_11":
    st.markdown("3.2.P.3 제조")
    st.markdown("11. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경")

    matched = False

    # 판단조건 1: 11a / 충족요건 1,2,3 모두 충족
    if (
        st.session_state.step6_selections.get("p3_11_sub_11a", "") == "해당함" and
        st.session_state.step6_selections.get("p3_11_req_1", "") == "충족함" and
        st.session_state.step6_selections.get("p3_11_req_2", "") == "충족함" and
        st.session_state.step6_selections.get("p3_11_req_3", "") == "충족함"
    ):
        matched = True
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 완제의약품의 성상.")
        st.markdown("2. (P.3) 배치 조성에 대한 자료, 제조공정 및 공정관리의 설명자료, 해당되는 경우, 제조공정 파라미터 변경을 확인할 수 있는 자료.")
        st.markdown("3. (P.5) 변경된 기준 및 시험방법.")
        st.markdown("4. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement).")
        display_report_type("Cmin")

    # 판단조건 2: 11b / 충족요건 1,2,3 모두 충족
    elif (
        st.session_state.step6_selections.get("p3_11_sub_11b", "") == "해당함" and
        st.session_state.step6_selections.get("p3_11_req_1", "") == "충족함" and
        st.session_state.step6_selections.get("p3_11_req_2", "") == "충족함" and
        st.session_state.step6_selections.get("p3_11_req_3", "") == "충족함"
    ):
        matched = True
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료의 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.")
        st.markdown("2. 완제의약품의 성상.")
        st.markdown("3. (P.3) 배치 조성에 대한 자료, 제조공정 및 공정관리의 설명자료, 해당되는 경우, 제조공정 파라미터 변경을 확인할 수 있는 자료.")
        st.markdown("4. (P.5) 변경된 기준 및 시험방법.")
        st.markdown("5. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement).")
        display_report_type("Cmaj")

    # 예외처리
    if not matched:
        st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title12: p3_12 - 3.2.P.3 제조 > 12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경
    if current_key == "p3_12":
        st.markdown("3.2.P.3 제조")
        st.markdown("12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경")

        matched = False

        # 판단조건 1: 12a / 충족요건 2
        if (
            st.session_state.step6_selections.get("p3_12_sub_12a", "") == "해당함" and
            st.session_state.step6_selections.get("p3_12_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 제조소 일반현황")
            st.markdown("2. 변경사항 요약표")
            st.markdown("3. 제조공정도 및 제조방법서")
            display_report_type("Cmin")

        # 판단조건 2: 12b.1 / 충족요건 2, 3, 4
        elif (
            st.session_state.step6_selections.get("p3_12_sub_12b.1", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_12_req_{i}", "") == "충족함" for i in [2, 3, 4])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 제조소 일반현황")
            st.markdown("2. 변경사항 요약표")
            st.markdown("3. 제조공정도 및 제조방법서")
            st.markdown("4. 품질에 미치는 영향에 대한 고찰자료")
            display_report_type("Cmin")

        # 판단조건 3: 12b.2 / 충족요건 2, 3, 4
        elif (
            st.session_state.step6_selections.get("p3_12_sub_12b.2", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_12_req_{i}", "") == "충족함" for i in [2, 3, 4])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 제조소 일반현황")
            st.markdown("2. 변경사항 요약표")
            st.markdown("3. 제조공정도 및 제조방법서")
            st.markdown("4. 품질에 미치는 영향에 대한 고찰자료")
            display_report_type("Cmaj")

        # 판단조건 4: 12c1 / 충족요건 1, 2
        elif (
            st.session_state.step6_selections.get("p3_12_sub_12c1", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_12_req_{i}", "") == "충족함" for i in [1, 2])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 제조소 일반현황")
            st.markdown("2. 변경사항 요약표")
            st.markdown("3. 제조공정도 및 제조방법서")
            display_report_type("Cmin")

        # 판단조건 5: 12c1 / 충족요건 1, 2, 5
        elif (
            st.session_state.step6_selections.get("p3_12_sub_12c1", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_12_req_{i}", "") == "충족함" for i in [1, 2, 5])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 제조소 일반현황")
            st.markdown("2. 변경사항 요약표")
            st.markdown("3. 제조공정도 및 제조방법서")
            st.markdown("4. 품질에 미치는 영향에 대한 고찰자료")
            display_report_type("Cmin")

        # 판단조건 6: 12c2 / 충족요건 2
        elif (
            st.session_state.step6_selections.get("p3_12_sub_12c2", "") == "해당함" and
            st.session_state.step6_selections.get("p3_12_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 제조소 일반현황")
            st.markdown("2. 변경사항 요약표")
            st.markdown("3. 제조공정도 및 제조방법서")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


# Title13: p3_13 - 3.2.P.3 제조 > 13. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경
if current_key == "p3_13":
    st.markdown("3.2.P.3 제조")
    st.markdown("13. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경")

    matched = False

    # 판단조건 1: 13a / 충족요건 1,2,3,4
    if (
        st.session_state.step6_selections.get("p3_13_sub_13a", "") == "해당함" and
        all(st.session_state.step6_selections.get(f"p3_13_req_{i}", "") == "충족함" for i in [1, 2, 3, 4])
    ):
        matched = True
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 성상 비교자료")
        display_report_type("Cmin")

    # 판단조건 2: 13b / 충족요건 1,2,3,4,5
    elif (
        st.session_state.step6_selections.get("p3_13_sub_13b", "") == "해당함" and
        all(st.session_state.step6_selections.get(f"p3_13_req_{i}", "") == "충족함" for i in [1, 2, 3, 4, 5])
    ):
        matched = True
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 성상 비교자료")
        st.markdown("2. 성능 비교자료")
        display_report_type("Cmin")

    # 판단조건 3: 13b / 충족요건 1,2,3,4,6
    elif (
        st.session_state.step6_selections.get("p3_13_sub_13b", "") == "해당함" and
        all(st.session_state.step6_selections.get(f"p3_13_req_{i}", "") == "충족함" for i in [1, 2, 3, 4, 6])
    ):
        matched = True
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 성상 비교자료")
        st.markdown("2. 성능 비교자료")
        display_report_type("Cmin")

    # 판단조건 4: 13c / 충족요건 1,2,3,4
    elif (
        st.session_state.step6_selections.get("p3_13_sub_13c", "") == "해당함" and
        all(st.session_state.step6_selections.get(f"p3_13_req_{i}", "") == "충족함" for i in [1, 2, 3, 4])
    ):
        matched = True
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 성상 비교자료")
        st.markdown("2. 시험결과 비교자료")
        display_report_type("IR")

    # 예외 처리
    if not matched:
        st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title14: p3_14 - 3.2.P.3 제조 > 14. 무균제제의 제조 규모 변경
    if current_key == "p3_14":
        st.markdown("3.2.P.3 제조")
        st.markdown("14. 무균제제의 제조 규모 변경")

        matched = False

        # 판단조건 1: 충족요건 1,2,3,4 → AR
        if (
            st.session_state.step6_selections.get("p3_14_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_2", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_3", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_4", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.")
            st.markdown("2. (P.3.5) (위험도 평가에 따른) 공정밸리데이션 자료 또는 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.")
            st.markdown("3. (P.5.1) 완제의약품의 기준 및 시험방법.")
            st.markdown("4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치 분석 자료(비교표 형식).")
            st.markdown("5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            display_report_type("AR")

        # 판단조건 2: 충족요건 1,2,3,4,5 → IR
        elif (
            st.session_state.step6_selections.get("p3_14_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_2", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_3", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_4", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_5", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.")
            st.markdown("2. (P.3.5) (위험도 평가에 따른) 공정밸리데이션 자료 또는 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.")
            st.markdown("3. (P.5.1) 완제의약품의 기준 및 시험방법.")
            st.markdown("4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치 분석 자료(비교표 형식).")
            st.markdown("5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            display_report_type("IR")

        # 판단조건 3: 충족요건 1,2,3,4,6 → Cmaj
        elif (
            st.session_state.step6_selections.get("p3_14_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_2", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_3", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_4", "") == "충족함" and
            st.session_state.step6_selections.get("p3_14_req_6", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.")
            st.markdown("2. (P.3.5) (위험도 평가에 따른) 공정밸리데이션 자료 또는 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.")
            st.markdown("3. (P.5.1) 완제의약품의 기준 및 시험방법.")
            st.markdown("4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치 분석 자료(비교표 형식).")
            st.markdown("5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            st.markdown("6. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title15: p3_15 - 3.2.P.3 제조 > 15. 완제의약품의 제조공정 변경
    if current_key == "p3_15":
        st.markdown("3.2.P.3 제조")
        st.markdown("15. 완제의약품의 제조공정 변경")

        matched = False

        # 판단조건 1: 15a / 충족요건 1,2,3,4,5,6,7
        if (
            st.session_state.step6_selections.get("p3_15_sub_15a", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_15_req_{i}", "") == "충족함" for i in [1,2,3,4,5,6,7])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(In-Vitro 비교시험 자료, 고형 제제 단위의 기준 및 시험방법에서의 용출 프로파일, 원료의약품을 용해/비용해 상태로 함유하는 비무균 반고형 제형의 In-Vitro 멤브레인 확산시험, 비용해 액상제제의 형상 가시적 변화 확인 자료와 입자 크기 분포 비교자료 등).")
            st.markdown("3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.")
            st.markdown("6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            st.markdown("7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement).")
            display_report_type("AR")

        # 판단조건 2: 15b / 충족요건 1,2,3,5,6,7,8
        elif (
            st.session_state.step6_selections.get("p3_15_sub_15b", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_15_req_{i}", "") == "충족함" for i in [1,2,3,5,6,7,8])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료의 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.")
            st.markdown("2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(...)")
            st.markdown("3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.")
            st.markdown("4. (P.5) 변경 전·후 생산 규모 1배치에 대한 규격 및 시험성적서.")
            st.markdown("5. (P.8.1) 최소 2배치(파일럿배치이상)에 대한 3개월 가속 및 장기안정성 시험결과 ...")
            st.markdown("6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            st.markdown("7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement).")
            display_report_type("IR")

        # 판단조건 3: 15b / 충족요건 1,2,3,5,6,7,8,9
        elif (
            st.session_state.step6_selections.get("p3_15_sub_15b", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_15_req_{i}", "") == "충족함" for i in [1,2,3,5,6,7,8,9])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(...)")
            st.markdown("3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.")
            st.markdown("4. (P.5) 변경 전·후 생산 규모 1배치에 대한 규격 및 시험성적서.")
            st.markdown("5. (P.8.1) 최소 2배치(파일럿배치이상)에 대한 3개월 가속 및 장기안정성 시험결과 ...")
            st.markdown("6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            st.markdown("7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement).")
            display_report_type("IR")

        # 판단조건 4: 15c / 모든 충족요건 미충족
        elif (
            st.session_state.step6_selections.get("p3_15_sub_15c", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p3_15_req_{i}", "") == "미충족함" for i in [1,2,3,4,5,6,7,8,9])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(...)")
            st.markdown("3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.")
            st.markdown("4. (P.5) 변경 전·후 생산 규모 1배치에 대한 규격 및 시험성적서.")
            st.markdown("5. (P.8.1) 최소 2배치(파일럿배치이상)에 대한 3개월 가속 및 장기안정성 시험결과 ...")
            st.markdown("6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            st.markdown("7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement).")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title16: p3_16 - 3.2.P.3 제조 > 16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경
    if current_key == "p3_16":
        st.markdown("3.2.P.3 제조")
        st.markdown("16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경")

        matched = False

        # 판단조건 1: 16a / 충족요건 1,2,4
        if (
            st.session_state.step6_selections.get("p3_16_sub_16a", "") == "해당함" and
            st.session_state.step6_selections.get("p3_16_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p3_16_req_2", "") == "충족함" and
            st.session_state.step6_selections.get("p3_16_req_4", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. (P.3.3/P.3.4) 공정 중 시험의 규격 비교표 등 변경 전·후에 관한 자료.")
            display_report_type("AR")

        # 판단조건 2: 16b / 충족요건 2
        elif (
            st.session_state.step6_selections.get("p3_16_sub_16b", "") == "해당함" and
            st.session_state.step6_selections.get("p3_16_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료의 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.")
            st.markdown("2. (P.3.3/P.3.4) 공정 중 시험의 규격 비교표 등 변경 전·후에 관한 자료.")
            st.markdown("3. (P.3.3/P.3.4) 새로운 공정관리 시험방법을 사용하는 경우, 시험방법에 관한 자료.")
            st.markdown("4. 새로운 시험방법을 사용하는 경우, 필요 시 밸리데이션 실시 보고서 또는 요약문.")
            st.markdown("5. (P.5.4) 변경 전후 최소 1배치(파일럿 배치 이상)에 대한 시험성적 비교자료.")
            st.markdown("6. 공정관리시험 및 기준의 추가, 삭제, 변경에 대한 타당성 입증 자료.")
            display_report_type("Cmaj")

        # 판단조건 3: 16c / 충족요건 2,3
        elif (
            st.session_state.step6_selections.get("p3_16_sub_16c", "") == "해당함" and
            st.session_state.step6_selections.get("p3_16_req_2", "") == "충족함" and
            st.session_state.step6_selections.get("p3_16_req_3", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("6. 공정관리시험 및 기준의 추가, 삭제, 변경에 대한 타당성 입증 자료.")
            display_report_type("AR")

        # 판단조건 4: 16d / 충족요건 2
        elif (
            st.session_state.step6_selections.get("p3_16_sub_16d", "") == "해당함" and
            st.session_state.step6_selections.get("p3_16_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. (P.3.3/P.3.4) 공정 중 시험의 규격 비교표 등 변경 전·후에 관한 자료.")
            st.markdown("3. (P.3.3/P.3.4) 새로운 공정관리 시험방법을 사용하는 경우, 시험방법에 관한 자료.")
            st.markdown("4. 새로운 시험방법을 사용하는 경우, 필요 시 밸리데이션 실시 보고서 또는 요약문.")
            st.markdown("5. (P.5.4) 변경 전후 최소 1배치(파일럿 배치 이상)에 대한 시험성적 비교자료.")
            st.markdown("6. 공정관리시험 및 기준의 추가, 삭제, 변경에 대한 타당성 입증 자료.")
            display_report_type("AR")

        # 판단조건 5: 16e / 충족요건 2
        elif (
            st.session_state.step6_selections.get("p3_16_sub_16e", "") == "해당함" and
            st.session_state.step6_selections.get("p3_16_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. (P.3.3/P.3.4) 공정 중 시험의 규격 비교표 등 변경 전·후에 관한 자료.")
            st.markdown("3. (P.3.3/P.3.4) 새로운 공정관리 시험방법을 사용하는 경우, 시험방법에 관한 자료.")
            st.markdown("4. 새로운 시험방법을 사용하는 경우, 필요 시 밸리데이션 실시 보고서 또는 요약문.")
            st.markdown("5. (P.5.4) 변경 전후 최소 1배치(파일럿 배치 이상)에 대한 시험성적 비교자료.")
            st.markdown("6. 공정관리시험 및 기준의 추가, 삭제, 변경에 대한 타당성 입증 자료.")
            display_report_type("AR")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title17: p4_17 - 3.2.P.4 첨가제의 관리 > 17. 첨가제 기원의 변경
    if current_key == "p4_17":
        st.markdown("3.2.P.4 첨가제의 관리")
        st.markdown("17. 첨가제 기원의 변경")

        matched = False

        # 판단조건 1: 17a / 충족요건 1
        if (
            st.session_state.step6_selections.get("p4_17_sub_17a", "") == "해당함" and
            st.session_state.step6_selections.get("p4_17_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 첨가제가 식물 또는 합성 기원임을 입증하는 제조업자의 확인서(statement).")
            display_report_type("AR")

        # 판단조건 2: 17b / 충족요건 1 미충족
        elif (
            st.session_state.step6_selections.get("p4_17_sub_17b", "") == "해당함" and
            st.session_state.step6_selections.get("p4_17_req_1", "") == "미충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. (P.4) 첨가제의 관리에 관한 자료(기준 및 시험방법 등, 기 사용 예가 있는 경우 관련 자료 포함).")
            st.markdown("3. (A.2) 외인성 물질에 대한 안전성 평가 자료(필요 시).")
            st.markdown("4. 변경 전·후 첨가제의 규격(비교표 등 변경 전·후에 관한 자료) 및 성적서.")
            display_report_type("Cmin")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title18: p4_18 - 3.2.P.4 첨가제의 관리 > 18. 별규에 해당하는 첨가제의 규격 또는 시험방법 변경
    if current_key == "p4_18":
        st.markdown("3.2.P.4 첨가제의 관리")
        st.markdown("18. 별규에 해당하는 첨가제의 규격 또는 시험방법 변경")

        matched = False

        # 판단조건 1: 충족요건 1
        if (
            st.session_state.step6_selections.get("p4_18_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 해당 변경에 대한 타당성 입증 자료.")
            st.markdown("2. (P.4) 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료, 변경하고자 하는 규격의 기준설정 근거자료, 시험방법에 관한 자료 및 밸리데이션 자료, 성적서.")
            display_report_type("Cmin")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title19: p4_19 - 3.2.P.4 첨가제의 관리 > 19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경
    if current_key == "p4_19":
        st.markdown("3.2.P.4 첨가제의 관리")
        st.markdown("19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경")

        matched = False

        # 판단조건 1: 충족요건 1
        if (
            st.session_state.step6_selections.get("p4_19_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 첨가제의 규격 비교표 등 변경 전·후에 관한 자료.")
            display_report_type("AR")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title20: p7_20 - 3.2.P.7 용기-마개 시스템 > 20. 비무균제제의 직접용기 및 포장 재질, 종류 변경
    if current_key == "p7_20":
        st.markdown("3.2.P.7 용기-마개 시스템")
        st.markdown("20. 비무균제제의 직접용기 및 포장 재질, 종류 변경")

        matched = False

        # 판단조건 1: 충족요건 1 충족
        if (
            st.session_state.step6_selections.get("p7_20_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 용기·포장 재질 변경이 반영된 의약품의 성상.")
            st.markdown("2. (P.2) (해당하는 경우) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료, 기허가 의약품에서 변경하고자 하는 용기·포장 재질의 사용례 등.")
            st.markdown("3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.")
            st.markdown("4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).")
            st.markdown("6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            display_report_type("IR")

        # 판단조건 2: 충족요건 1 미충족
        elif (
            st.session_state.step6_selections.get("p7_20_req_1", "") == "미충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 용기·포장 재질 변경이 반영된 의약품의 성상.")
            st.markdown("2. (P.2) (해당하는 경우) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료, 기허가 의약품에서 변경하고자 하는 용기·포장 재질의 사용례 등.")
            st.markdown("3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.")
            st.markdown("4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).")
            st.markdown("5. (P.8.1) 안정성 요약문과 결론, 2배치(파일럿배치 이상) 이상에 대한 3개월 이상의 장기보존 및 가속 시험. 해당되는 경우, 광 가혹 시험 결과.")
            st.markdown("6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title21: p7_21 - 3.2.P.7 용기-마개 시스템 > 21. 무균제제의 직접용기 및 포장 재질, 종류 변경
    if current_key == "p7_21":
        st.markdown("3.2.P.7 용기-마개 시스템")
        st.markdown("21. 무균제제의 직접용기 및 포장 재질, 종류 변경")

        matched = False

        # 판단조건 1: 충족요건 1 충족
        if st.session_state.step6_selections.get("p7_21_req_1", "") == "충족함":
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 용기·포장 재질 변경이 반영된 의약품의 성상.")
            st.markdown("2. (P.2) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료.")
            st.markdown("3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.")
            st.markdown("4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).")
            st.markdown("5. (P.8.1) 안정성 요약문과 결론, 2배치(파일럿배치 이상)에 대한 3개월 이상의 장기보존 및 가속 시험.")
            st.markdown("7. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            display_report_type("Cmin")

        # 판단조건 2: 모든 충족요건 미충족
        elif st.session_state.step6_selections.get("p7_21_req_1", "") == "미충족함":
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 용기·포장 재질 변경이 반영된 의약품의 성상.")
            st.markdown("2. (P.2) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료.")
            st.markdown("3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.")
            st.markdown("4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).")
            st.markdown("6. (P.8.1) 안정성 요약문과 결론, 생산 규모 3배치(최소 2배치 파일럿배치 이상)에 대한 6개월 이상의 장기보존 및 가속 시험. 해당되는 경우, 광 가혹 시험 결과.")
            st.markdown("7. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title22: p7_22 - 3.2.P.7 용기-마개 시스템 > 22. 직접 포장의 규격 변경
    if current_key == "p7_22":
        st.markdown("3.2.P.7 용기-마개 시스템")
        st.markdown("22. 직접 포장의 규격 변경")

        matched = False

        # 판단조건 1: 22a / 충족요건 1, 2
        if (
            st.session_state.step6_selections.get("p7_22_sub_22a", "") == "해당함" and
            st.session_state.step6_selections.get("p7_22_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p7_22_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (P.7) 규격 비교표 등 변경 전·후에 관한 자료, 변경하고자 하는 규격의 타당성 입증 자료.")
            display_report_type("AR")

        # 판단조건 2: 22b / 충족요건 2
        elif (
            st.session_state.step6_selections.get("p7_22_sub_22b", "") == "해당함" and
            st.session_state.step6_selections.get("p7_22_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (P.7) 규격 비교표 등 변경 전·후에 관한 자료, 변경하고자 하는 규격의 타당성 입증 자료.")
            st.markdown("2. (P.7) 추가 또는 삭제된 시험방법에 관한 자료.")
            display_report_type("AR")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")


    # Title23: p7_23 - 3.2.P.7 용기-마개 시스템 > 23. 포장단위 변경
    if current_key == "p7_23":
        st.markdown("3.2.P.7 용기-마개 시스템")
        st.markdown("23. 포장단위 변경")

        matched = False

        # 판단조건: 충족요건 1,2
        if (
            st.session_state.step6_selections.get("p7_23_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p7_23_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (R.1) 포장단위 비교표 등 변경 전·후에 관한 자료")
            display_report_type("IR")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

    # Title24: ds_24 - 디자인스페이스(Design Space) > 24. 새로운 디자인스페이스 도입 또는 허가된 디자인스페이스의 확장
    if current_key == "ds_24":
        st.markdown("디자인스페이스(Design Space)")
        st.markdown("24. 새로운 디자인스페이스 도입 또는 허가된 디자인스페이스의 확장")

        matched = False

        # 판단조건 1: 24a / 하위항목 변경 있음
        if st.session_state.step6_selections.get("ds_24_sub_24a", "") == "변경 있음":
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경에 따른 디자인 스페이스가 타당함을 입증하는 자료(위해평가 및 다변량 연구를 포함하여 디자인 스페이스를 구성하는 다양한 파라미터들의 상호작용에 대한 연구결과를 통해 도출되었음을 입증하는 자료)")
            st.markdown("2. 표 형식으로 디자인 스페이스를 설명한 자료.")
            st.markdown("3. 신청 서류의 변경과 관련된 CTD 자료.")
            display_report_type("Cmaj")

        # 판단조건 2: 24b / 하위항목 변경 있음
        if st.session_state.step6_selections.get("ds_24_sub_24b", "") == "변경 있음":
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경에 따른 디자인 스페이스가 타당함을 입증하는 자료(위해평가 및 다변량 연구를 포함하여 디자인 스페이스를 구성하는 다양한 파라미터들의 상호작용에 대한 연구결과를 통해 도출되었음을 입증하는 자료)")
            st.markdown("2. 표 형식으로 디자인 스페이스를 설명한 자료.")
            st.markdown("3. 신청 서류의 변경과 관련된 CTD 자료.")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")
