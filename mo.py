import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 7:

    st.markdown("### 보고유형 및 필요자료 도출")

    step6_selected_keys = list(st.session_state.step6_selections.keys())
    title_keys = []

    for key in step6_selected_keys:
        if "_sub_" in key:
            parts = key.split("_sub_")
            group_key = parts[0]
            sub_key = parts[1]
            full_title_key = f"{group_key}_{sub_key}"
            if full_title_key not in title_keys:
                title_keys.append(full_title_key)
        elif "_req_" in key:
            group_key = key.split("_req_")[0]
            if group_key not in title_keys:
                title_keys.append(group_key)

    title_keys = sorted(title_keys)
    total_titles = len(title_keys)

    if "step7_page" not in st.session_state:
        st.session_state.step7_page = 0

    if total_titles == 0:
        st.warning("Step6에서 선택된 항목이 없습니다.")
        st.stop()

    current_key = title_keys[st.session_state.step7_page]

    st.markdown(f"**선택된 항목 {st.session_state.step7_page + 1} / {total_titles}**")
    st.markdown("---")

    if "step7_results" not in st.session_state:
        st.session_state.step7_results = []

    def display_report_type(result_type):
        if result_type == "AR":
            st.markdown("보고유형은 다음과 같습니다.\n\nAR, 연차보고\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 제2항 및 제4항에 따른 연차보고(Annual Report, AR) 수준의 변경사항입니다.")
        elif result_type == "IR":
            st.markdown("보고유형은 다음과 같습니다.\n\nIR, 시판전보고\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2제4항 단서조항에 따른 시판전 보고(Immediate Report, IR) 수준의 변경사항입니다.")
        elif result_type == "Cmaj":
            st.markdown("보고유형은 다음과 같습니다.\n\nCmaj, 변경허가(신고)\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 및 제6조에 따라 품질에 중요한 영향을 미치는 변경허가(신고) 신청 대상이며, 중요도 등을 고려하였을 때 Major change(Cmaj) 수준의 변경사항입니다.")
        elif result_type == "Cmin":
            st.markdown("보고유형은 다음과 같습니다.\n\nCmin, 변경허가(신고)\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 및 제6조에 따라 품질에 중요한 영향을 미치는 변경허가(신고) 신청 대상이며, Minor change(Cmin) 수준의 변경사항입니다.")

    col1, col2, col3 = st.columns(3)

    if total_titles == 1:
        with col2:
            if st.button("이전단계로"):
                st.session_state.step = 6
                st.experimental_rerun()
        with col3:
            if st.button("신청서 출력"):
                st.session_state.step = 8
                st.experimental_rerun()
    elif st.session_state.step7_page < total_titles - 1:
        with col1:
            if st.button("이전단계로"):
                st.session_state.step7_page = max(st.session_state.step7_page - 1, 0)
                st.experimental_rerun()
        with col3:
            if st.button("다음항목 확인하기"):
                st.session_state.step7_page += 1
                st.experimental_rerun()
    else:
        with col1:
            if st.button("이전단계로"):
                st.session_state.step7_page = max(st.session_state.step7_page - 1, 0)
                st.experimental_rerun()
        with col3:
            if st.button("신청서 출력"):
                st.session_state.step = 8
                st.experimental_rerun()

    # Title1: s1_1 - 3.2.S.1 일반정보 > 1. 원료의약품 명칭변경
    if current_key == "s1_1":
        st.markdown("3.2.S.1 일반정보")
        st.markdown("1. 원료의약품 명칭변경")

        key_req = f"{current_key}_req_1"
        req_selected = st.session_state.step6_selections.get(key_req, "")

        if req_selected == "충족함":
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (S.1.1) 공정서 또는 국제 의약품 일반명 리스트(INN) 등 근거서류")
            st.markdown("2. 개정된 제품정보")

            display_report_type("AR")

        elif req_selected == "미충족":
            st.markdown("「의약품 허가 후 제조방법 변경관리 가이드라인(민원인 안내서)」에 포함되지 않은 변경의 경우 위험평가를 수행하여 품질에 영향을 미치지 않거나 경미한 영향을 미치는 변경의 경우 제조사의 문서화된 절차 및 의약품품질시스템에 따라 처리하고 해당 변경이 제제의 품질 및 안전성‧유효성에 영향을 미치지 않도록 관리해야 하며, 그 외의 사항은 기본적으로 품질에 영향을 미치는 중요한 변경사항으로 간주 되어야 합니다.")

    # Title2: s2_2 - 3.2.S.2 제조 > 2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가
    if current_key == "s2_2":
        st.markdown("3.2.S.2 제조")
        st.markdown("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가")

        matched = False

        # 2a 판단 조건 1
        if (
            st.session_state.step6_selections.get("s2_2_sub_2a", "") == "해당함"
            and st.session_state.step6_selections.get("s2_2_2a_1req_", "") == "충족함"
        ):
            matched = True
            st.markdown("2a. 출발물질의 제조소 추가")
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 출발물질 제조소 GMP 인증서")
            display_report_type("Cmin")

        # 2a 판단 조건 2
        elif (
            st.session_state.step6_selections.get("s2_2_sub_2a", "") == "해당함"
            and st.session_state.step6_selections.get("s2_2_2a_req_1", "") == "미충족"
        ):
            matched = True
            st.markdown("2a. 출발물질의 제조소 추가")
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. 출발물질 시험성적서 및 위험평가 보고서")
            display_report_type("Cmaj")

        # 2b 판단 조건 1
        elif (
            st.session_state.step6_selections.get("s2_2_sub_2b", "") == "해당함"
            and st.session_state.step6_selections.get("s2_2_2b_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("2b. 중간체의 제조소 변경")
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("3. 중간체 제조소 GMP 인증서")
            display_report_type("Cmin")

        # 2b 판단 조건 2
        elif (
            st.session_state.step6_selections.get("s2_2_sub_2b", "") == "해당함"
            and st.session_state.step6_selections.get("s2_2_2b_req_1", "") == "미충족"
        ):
            matched = True
            st.markdown("2b. 중간체의 제조소 변경")
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("4. 중간체 시험성적서 및 생산공정 개요")
            display_report_type("Cmaj")

        # 2c 판단 조건 1
        elif (
            st.session_state.step6_selections.get("s2_2_sub_2c", "") == "해당함"
            and st.session_state.step6_selections.get("s2_2_2c_req_1", "") == "충족함"
            and st.session_state.step6_selections.get("s2_2_2c_req_2", "") == "충족함"
        ):
            matched = True
            st.markdown("2c. 원료의약품의 제조소 변경")
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("5. 변경 제조소의 품질보증 체계 설명자료")
            display_report_type("AR")

        # 2c 판단 조건 2
        elif (
            st.session_state.step6_selections.get("s2_2_sub_2c", "") == "해당함"
            and st.session_state.step6_selections.get("s2_2_2c_req_1", "") == "충족함"
            and st.session_state.step6_selections.get("s2_2_2c_req_2", "") == "미충족"
        ):
            matched = True
            st.markdown("2c. 원료의약품의 제조소 변경")
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("6. 제조소별 비교자료 및 입자크기 분포 검토자료")
            display_report_type("IR")

        # 2c 판단 조건 3
        elif (
            st.session_state.step6_selections.get("s2_2_sub_2c", "") == "해당함"
            and st.session_state.step6_selections.get("s2_2_2c_req_1", "") == "미충족"
        ):
            matched = True
            st.markdown("2c. 원료의약품의 제조소 변경")
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("7. 제조소 변경 관련 전체 평가자료")
            display_report_type("Cmaj")

        # 규정에 없는 판단조건의 경우
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

    # Title3: s2_3 - 3.2.S.2 제조 > 3. 원료의약품 제조 공정의 변경
    if current_key == "s2_3":
        st.markdown("3.2.S.2 제조")
        st.markdown("3. 원료의약품 제조 공정의 변경")

        matched = False

        # 판단조건 1: 충족요건 1,2,3,4,5,6,7,8
        if all(
            st.session_state.step6_selections.get(f"s2_3_req_{i}", "") == "충족함"
            for i in [1, 2, 3, 4, 5, 6, 7, 8]
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료")
            st.markdown("3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료")
            st.markdown("4. (S.2.3)(해당되는 경우) 변경하고자 하는 원료의약품 제조에 사용된 원료(예 : 원료약품, 출발 물질, 용매, 시약, 촉매)의 규격 및 시험 성적서")
            st.markdown("11. (S.4.4) 변경 전·후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 배치분석 자료")
            display_report_type("IR")

        # 판단조건 2: 충족요건 1,2,3,5,7,8,9
        elif all(
            st.session_state.step6_selections.get(f"s2_3_req_{i}", "") == "충족함"
            for i in [1, 2, 3, 5, 7, 8, 9]
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료")
            st.markdown("3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료")
            st.markdown("10. (S.4.1) 변경 후 원료의약품 기준 및 시험방법에 관한 자료. (변경되는 경우, 출발물질 및 중간체의 기준 및 시험방법)")
            st.markdown("11. (S.4.4) 변경 전·후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 배치분석 자료")
            display_report_type("Cmin")

        # 판단조건 3: 충족요건 1,2,3,4,5,6
        elif all(
            st.session_state.step6_selections.get(f"s2_3_req_{i}", "") == "충족함"
            for i in [1, 2, 3, 4, 5, 6]
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료")
            st.markdown("3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료")
            st.markdown("10. (S.4.1) 변경 후 원료의약품 기준 및 시험방법에 관한 자료. (변경되는 경우, 출발물질 및 중간체의 기준 및 시험방법)")
            st.markdown("11. (S.4.4) 변경 전·후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 배치분석 자료")
            display_report_type("Cmin")

        # 판단조건 4: 모든 충족요건을 미충족으로 선택한 경우
        elif all(
            st.session_state.step6_selections.get(f"s2_3_req_{i}", "") == "미충족"
            for i in range(1, 10)
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 후 원료의약품이 완제의약품의 안전성, 유효성 및 품질에 미치는 영향에 대한 고찰자료. (완제의약품의 불순물 프로파일, 배치분석자료, 필요한 경우 안정성 자료 등)")
            st.markdown("2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료")
            st.markdown("3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료")
            st.markdown("4. (S.2.3)(해당되는 경우) 변경하고자 하는 원료의약품 제조에 사용된 원료의 규격 및 시험 성적서")
            st.markdown("5. (S.2.3) BSE/TSE 위험 적합성 평가 자료")
            st.markdown("6. (S.2.4)(해당되는 경우) 주요 공정 및 중간체 관리에 관한 자료")
            st.markdown("7. (S.2.5) 멸균 공정 밸리데이션 자료 또는 멸균 평가 시험 자료")
            st.markdown("8. (S.3.1) 원료의약품의 구조 결정 자료(IR, UV 등) 및 물리화학적 성질에 관한 자료")
            st.markdown("9. (S.3.2) 불순물에 대한 고찰 및 근거자료")
            st.markdown("10. (S.4.1) 변경 후 원료의약품 기준 및 시험방법에 관한 자료")
            st.markdown("11. (S.4.4) 변경 전·후 원료의약품 최소 2배치에 대한 배치분석 자료")
            st.markdown("12. (S.7.1) 가속시험 및 장기 보존 시험 자료")
            st.markdown("13. (난용성 원료) 결정형 또는 입자도 변경의 영향 평가자료")
            display_report_type("Cmaj")

        # 매칭 실패한 경우
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

    # Title4: s2_4 - 3.2.S.2 제조 > 4. 원료의약품 제조 공정관리 규격의 변경
    if current_key == "s2_4":
        st.markdown("3.2.S.2 제조")
        st.markdown("4. 원료의약품 제조 공정관리 규격의 변경")

        matched = False

        # 판단조건 1: 4a / 충족요건 1,2,3
        if (
            st.session_state.step6_selections.get("s2_4_sub_4a", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_4_req_{i}", "") == "충족함" for i in [1, 2, 3])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료")
            st.markdown("2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료")
            st.markdown("3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료")
            display_report_type("AR")

        # 판단조건 2: 4b / 충족요건 1
        elif (
            st.session_state.step6_selections.get("s2_4_sub_4b", "") == "해당함" and
            st.session_state.step6_selections.get("s2_4_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료")
            st.markdown("2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료")
            st.markdown("3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료")
            st.markdown("4. 해당되는 경우, 분석 방법 상세 자료")
            st.markdown("5. 공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료")
            display_report_type("AR")

        # 판단조건 3: 4c / 모든 충족요건 미충족
        elif (
            st.session_state.step6_selections.get("s2_4_sub_4c", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_4_req_{i}", "") == "미충족" for i in [1, 2, 3, 4, 5])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료")
            st.markdown("2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료")
            st.markdown("3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료")
            st.markdown("4. 해당되는 경우, 분석 방법 상세 자료")
            st.markdown("5. 공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료")
            st.markdown("7. (S.2.5) 무균원료의약품인 경우, 해당 공정기준 변경이 제품의 무균 및 멸균공정에 영향을 미칠 경우(위험도 평가 결과에 따른), 해당 공정에 대한 밸리데이션 자료 또는 평가 자료")
            st.markdown("8. (S.3.2) 해당변경이 불순물에 영향을 미칠 경우, 불순물에 대한 고찰 및 근거자료")
            st.markdown("9. (S.4.1) 변경 후 원료의약품(해당되는 경우 중간체) 규격에 관한 자료")
            st.markdown("10. (S.4.4) 변경 전·후 원료의약품 최소 1배치(파일럿 배치 이상)의 배치분석자료")
            display_report_type("Cmin")

        # 판단조건 4: 4d / 충족요건 1,4,5
        elif (
            st.session_state.step6_selections.get("s2_4_sub_4d", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_4_req_{i}", "") == "충족함" for i in [1, 4, 5])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료")
            st.markdown("2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료")
            st.markdown("3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료")
            st.markdown("6. 삭제되는 공정관리시험이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료)")
            display_report_type("AR")

        # 판단조건 5: 4d / 충족요건 1
        elif (
            st.session_state.step6_selections.get("s2_4_sub_4d", "") == "해당함" and
            st.session_state.step6_selections.get("s2_4_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료")
            st.markdown("2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료")
            st.markdown("3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료")
            st.markdown("5. 공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료")
            st.markdown("7. (S.2.5) 무균원료의약품인 경우, 해당 공정기준 변경이 제품의 무균 및 멸균공정에 영향을 미칠 경우(위험도 평가 결과에 따른), 해당 공정에 대한 밸리데이션 자료 또는 평가 자료")
            st.markdown("8. (S.3.2) 해당변경이 불순물에 영향을 미칠 경우, 불순물에 대한 고찰 및 근거자료")
            st.markdown("9. (S.4.1) 변경 후 원료의약품(해당되는 경우 중간체) 규격에 관한 자료")
            st.markdown("10. (S.4.4) 변경 전·후 원료의약품 최소 1배치(파일럿 배치 이상)의 배치분석자료")
            display_report_type("Cmaj")

        # 판단조건 6: 4e / 충족요건 1
        elif (
            st.session_state.step6_selections.get("s2_4_sub_4e", "") == "해당함" and
            st.session_state.step6_selections.get("s2_4_req_1", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료")
            st.markdown("2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료")
            st.markdown("3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료")
            st.markdown("5. 공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료")
            st.markdown("7. (S.2.5) 무균원료의약품인 경우, 해당 공정기준 변경이 제품의 무균 및 멸균공정에 영향을 미칠 경우(위험도 평가 결과에 따른), 해당 공정에 대한 밸리데이션 자료 또는 평가 자료")
            st.markdown("8. (S.3.2) 해당변경이 불순물에 영향을 미칠 경우, 불순물에 대한 고찰 및 근거자료")
            st.markdown("9. (S.4.1) 변경 후 원료의약품(해당되는 경우 중간체) 규격에 관한 자료")
            st.markdown("10. (S.4.4) 변경 전·후 원료의약품 최소 1배치(파일럿 배치 이상)의 배치분석자료")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

    # Title5: s2_5 - 3.2.S.2 제조 > 5. 원료의약품 또는 중간체의 제조 규모 변경
    if current_key == "s2_5":
        st.markdown("3.2.S.2 제조")
        st.markdown("5. 원료의약품 또는 중간체의 제조 규모 변경")

        matched = False

        # 판단조건 1: 5a / 충족요건 1,2,3
        if (
            st.session_state.step6_selections.get("s2_5_sub_5a", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_5_req_{i}", "") == "충족함" for i in [1, 2, 3])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.")
            st.markdown("2. (S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.")
            st.markdown("3. (S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).")
            st.markdown("4. (S.4.4) 변경 전·후 제조 규모에서 각 최소 1배치에 대한 배치 분석 자료.")
            display_report_type("AR")

        # 판단조건 2: 5b / 충족요건 1,2,3
        elif (
            st.session_state.step6_selections.get("s2_5_sub_5b", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_5_req_{i}", "") == "충족함" for i in [1, 2, 3])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.")
            st.markdown("2. (S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.")
            st.markdown("3. (S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).")
            st.markdown("4. (S.4.4) 변경 전·후 제조 규모에서 각 최소 1배치에 대한 배치 분석 자료.")
            display_report_type("AR")

        # 판단조건 3: 5c / 충족요건 1,2
        elif (
            st.session_state.step6_selections.get("s2_5_sub_5c", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_5_req_{i}", "") == "충족함" for i in [1, 2])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.")
            st.markdown("2. (S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.")
            st.markdown("3. (S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).")
            st.markdown("5. (S.4.4) 변경 전·후 제조 규모에서 각 최소 2배치에 대한 배치 분석 자료.")
            display_report_type("Cmin")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

    # Title6: s2_6 - 3.2.S.2 제조 > 6. 원료의약품의 제조에 사용되는 원료의 규격변경
    if current_key == "s2_6":
        st.markdown("3.2.S.2 제조")
        st.markdown("6. 원료의약품의 제조에 사용되는 원료의 규격변경")

        matched = False

        # 판단조건 1: 6a / 충족요건 1,2,3
        if (
            st.session_state.step6_selections.get("s2_6_sub_6a", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_6_req_{i}", "") == "충족함" for i in [1, 2, 3])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 기준 및 시험방법 비교표")
            st.markdown("2. 변경 후 기준 및 시험방법 설정 근거자료")
            st.markdown("3. 변경 전·후 시험결과 비교자료 또는 적합성 확인자료")
            display_report_type("AR")

        # 판단조건 2: 6b / 충족요건 4,5,6
        elif (
            st.session_state.step6_selections.get("s2_6_sub_6b", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_6_req_{i}", "") == "충족함" for i in [4, 5, 6])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 기준 및 시험방법 비교표")
            st.markdown("2. 변경 후 기준 및 시험방법 설정 근거자료")
            st.markdown("3. 시험법 밸리데이션 자료")
            st.markdown("4. 변경 전·후 시험결과 비교자료 또는 적합성 확인자료")
            display_report_type("AR")

        # 판단조건 3: 6c / 충족요건 1,5,6,7
        elif (
            st.session_state.step6_selections.get("s2_6_sub_6c", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_6_req_{i}", "") == "충족함" for i in [1, 5, 6, 7])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 기준 및 시험방법 비교표")
            st.markdown("2. 시험법 밸리데이션 자료")
            st.markdown("3. 변경 전·후 시험결과 비교자료 또는 적합성 확인자료")
            st.markdown("4. 불순물 프로파일 또는 관리전략 자료")
            display_report_type("Cmin")

        # 판단조건 4: 6d / 충족요건 1,8,9
        elif (
            st.session_state.step6_selections.get("s2_6_sub_6d", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_6_req_{i}", "") == "충족함" for i in [1, 8, 9])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 기준 및 시험방법 비교표")
            st.markdown("2. 변경 후 기준 및 시험방법 설정 근거자료")
            st.markdown("3. 시험법 삭제 사유에 대한 설명자료")
            display_report_type("AR")

        # 판단조건 5: 6e / 모든 충족요건 미충족
        elif (
            st.session_state.step6_selections.get("s2_6_sub_6e", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_6_req_{i}", "") == "미충족" for i in range(1, 10))
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 시험법 설정 근거자료")
            st.markdown("2. 시험법 밸리데이션 자료")
            st.markdown("3. 변경 전·후 시험결과 비교자료")
            st.markdown("4. 유전독성 불순물 및 불순물 관리전략 관련 고찰자료")
            display_report_type("Cmaj")

        # 판단조건 6: 6f / 충족요건 3,6,7,9
        elif (
            st.session_state.step6_selections.get("s2_6_sub_6f", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_6_req_{i}", "") == "충족함" for i in [3, 6, 7, 9])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 기준 완화 사유 및 설정 근거자료")
            st.markdown("2. 시험법 밸리데이션 자료")
            st.markdown("3. 변경 전·후 시험결과 비교자료")
            display_report_type("Cmin")

        # 판단조건 7: 6g / 모든 충족요건 미충족
        elif (
            st.session_state.step6_selections.get("s2_6_sub_6g", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"s2_6_req_{i}", "") == "미충족" for i in range(1, 10))
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 기준 완화 사유 및 설정 근거자료")
            st.markdown("2. 시험법 밸리데이션 자료")
            st.markdown("3. 변경 전·후 시험결과 비교자료")
            st.markdown("4. 유전독성 불순물 및 불순물 관리전략 관련 고찰자료")
            display_report_type("Cmaj")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

    # Title7: p1_7 - 3.2.P.1 완제의약품의 성상 및 조성 > 7. 완제의약품 중 고형 제제의 조성 변경
    if current_key == "p1_7":
        st.markdown("3.2.P.1 완제의약품의 성상 및 조성")
        st.markdown("7. 완제의약품 중 고형 제제의 조성 변경")

        matched = False

        # 판단조건 1: 7a / 충족요건 1,4
        if (
            st.session_state.step6_selections.get("p1_7_sub_7a", "") == "해당함" and
            st.session_state.step6_selections.get("p1_7_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p1_7_req_4", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 조성 비교표")
            st.markdown("2. 품질에 미치는 영향에 대한 고찰자료")
            st.markdown("3. 시험결과 비교자료")
            display_report_type("Cmin")

        # 판단조건 2: 7b / 충족요건 1,2,3,4,5
        elif (
            st.session_state.step6_selections.get("p1_7_sub_7b", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p1_7_req_{i}", "") == "충족함" for i in [1,2,3,4,5])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 조성 비교표")
            st.markdown("2. 품질에 미치는 영향에 대한 고찰자료")
            st.markdown("3. 시험결과 비교자료")
            display_report_type("Cmin")

        # 판단조건 3: 7b / 모든 충족요건 미충족
        elif (
            st.session_state.step6_selections.get("p1_7_sub_7b", "") == "해당함" and
            all(st.session_state.step6_selections.get(f"p1_7_req_{i}", "") == "미충족" for i in [1,2,3,4,5])
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 조성 비교표")
            st.markdown("2. 안정성 시험자료 또는 품질 영향 평가자료")
            st.markdown("3. 시험결과 비교자료")
            display_report_type("Cmaj")

        # 판단조건 4: 7c / 충족요건 1,4
        elif (
            st.session_state.step6_selections.get("p1_7_sub_7c", "") == "해당함" and
            st.session_state.step6_selections.get("p1_7_req_1", "") == "충족함" and
            st.session_state.step6_selections.get("p1_7_req_4", "") == "충족함"
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. 변경 전·후 조성 비교표")
            st.markdown("2. 시험결과 비교자료")
            display_report_type("IR")

        # 예외처리
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

    elif current_key == "p1_8":
        show_result(
            "8. 고형제제의 코팅층 무게 변경",
            [
                "1. (P.2 또는 R) 품목허가·신고·심사 규정 별표2(변경사유별 제출자료)에 따른 제출자료.",
                "2. (P.1) 완제의약품의 성상 및 원료약품 분량.",
                "3. (P.2) 코팅에 사용된 첨가제의 성분 및 조성에 대한 자료.",
                "4. (P.5) 완제의약품의 기준 및 시험방법, 최소 1배치(파일럿 배치 이상)에 대한 시험 성적서."
            ],
            "Cmin"
        )

    # Title9: P1_9 - 3.2.P.1 완제의약품의 성상 및 조성 > 9. 변경 후 원료의약품이 완제의약품의 안전성, 유효성 및 품질에 미치는 영향에 대한 고찰자료
    elif current_key == "p1_9":
        st.markdown("3.2.P.1 완제의약품의 성상 및 조성")
        st.markdown("9. 변경 후 원료의약품이 완제의약품의 안전성, 유효성 및 품질에 미치는 영향에 대한 고찰자료")

        matched = False

        # 판단조건 1: 충족요건 1~7, 9 충족
        if all(
            st.session_state.step6_selections.get(f"p1_9_req_{i}", "") == "충족"
            for i in [1, 2, 3, 4, 5, 6, 7, 9]
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (P.2 또는 R) 이화학적동등성시험자료")
            st.markdown("2. (P.1) 완제의약품의 성상 및 조성")
            st.markdown("3. (P.2) 구성 성분 검토 자료")
            st.markdown("4. (P.3) 제조공정 관련 자료 및 공정 밸리데이션 자료")
            st.markdown("5. (P.4) 첨가제 규격 자료")
            st.markdown("6. (P.4.5) BSE/TSE 위해 적합성 자료")
            st.markdown("7. (P.5) 시험성적서")
            st.markdown("8. (P.5.3) 분석 절차 방해 여부 입증 자료")
            st.markdown("9. (P.8.1) 안정성 시험 3개월 자료")
            st.markdown("10. (P.8.2) 생산규모 배치 안정성 시험 계획서 및 이행서약")

            display_report_type("Cmaj")

        # 판단조건 2: 충족요건 8, 9 충족
        elif all(
            st.session_state.step6_selections.get(f"p1_9_req_{i}", "") == "충족"
            for i in [8, 9]
        ):
            matched = True
            st.markdown("필요서류는 다음과 같습니다.")
            st.markdown("1. (P.2 또는 R) 생동성시험자료 또는 대체자료")
            st.markdown("2. (P.1) 완제의약품의 성상 및 조성")
            st.markdown("3. (P.2) 구성 성분 검토 자료")
            st.markdown("4. (P.3) 제조공정 관련 자료 및 공정 밸리데이션 자료")
            st.markdown("5. (P.4) 첨가제 규격 자료")
            st.markdown("6. (P.4.5) BSE/TSE 위해 적합성 자료")
            st.markdown("7. (P.5) 시험성적서")
            st.markdown("8. (P.5.3) 분석 절차 방해 여부 입증 자료")
            st.markdown("9. (P.8.1) 안정성 시험 3개월 자료")
            st.markdown("10. (P.8.2) 생산규모 배치 안정성 시험 계획서 및 이행서약")

            display_report_type("Cmaj")

        # 기타 모든 경우
        if not matched:
            st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

# Title 10: p1_10 - 3.2.P.1 완제의약품의 성상 및 조성 > 10. 타르색소 또는 첨가제의 변경
if current_key == "p1_10":
    st.markdown("3.2.P.1 완제의약품의 성상 및 조성")
    st.markdown("10. 타르색소 또는 첨가제의 변경")

    matched = False

    # 판단조건 1: 10a / 충족요건 1, 2, 3, 4
    if (
        st.session_state.step6_selections.get("p1_10_sub_10a", "") == "해당함" and
        all(st.session_state.step6_selections.get(f"p1_10_req_{i}", "") == "충족함" for i in [1, 2, 3, 4])
    ):
        matched = True
        st.markdown("10a. 타르색소의 종류 변경(황색4호 제외)")
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 변경 전·후 조성 비교표")
        st.markdown("2. 품질에 미치는 영향에 대한 고찰자료")
        st.markdown("3. 시험결과 비교자료")
        display_report_type("Cmin")

    # 판단조건 2: 10b / 충족요건 1, 2, 3, 4, 6, 7, 8, 9
    elif (
        st.session_state.step6_selections.get("p1_10_sub_10b", "") == "해당함" and
        all(st.session_state.step6_selections.get(f"p1_10_req_{i}", "") == "충족함" for i in [1, 2, 3, 4, 6, 7, 8, 9])
    ):
        matched = True
        st.markdown("10b. 타르색소의 종류 및 분량 변경")
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 변경 전·후 조성 비교표")
        st.markdown("2. 품질에 미치는 영향에 대한 고찰자료")
        st.markdown("3. 시험결과 비교자료")
        display_report_type("Cmin")

    # 판단조건 3: 10c / 충족요건 1, 2, 3, 5
    elif (
        st.session_state.step6_selections.get("p1_10_sub_10c", "") == "해당함" and
        all(st.session_state.step6_selections.get(f"p1_10_req_{i}", "") == "충족함" for i in [1, 2, 3, 5])
    ):
        matched = True
        st.markdown("10c. 타르색소 외 착색제, 착향제의 변경")
        st.markdown("필요서류는 다음과 같습니다.")
        st.markdown("1. 변경 전·후 조성 비교표")
        st.markdown("2. 품질에 미치는 영향에 대한 고찰자료")
        st.markdown("3. 시험결과 비교자료")
        display_report_type("Cmin")

    # 예외처리
    if not matched:
        st.markdown("해당 변경사항은 이 가이드라인에서 정하고 있는 범위에 해당하지 않는 것으로 판단됩니다.")

