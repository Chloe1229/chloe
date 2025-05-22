import streamlit as st

# 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 1
if "step1_answer" not in st.session_state:
    st.session_state.step1_answer = None

# 다음 단계로 이동 함수
def go_to_step2():
    if st.session_state.step1_answer == "예":
        st.session_state.step = 2

# STEP 1 화면
if st.session_state.step == 1:
    st.markdown("## Step 1")
    st.write("제6조제1항에 따라 국제공통기술문서(CTD)로 작성하여 허가를 받거나 신고한 의약품의 제조원 또는 제조방법을 변경하는 경우에 해당한다.")

    st.session_state.step1_answer = st.radio("답변을 선택하세요.", ["예", "아니오"], key="step1_radio")

    if st.session_state.step1_answer == "예":
        st.success("""CTD 작성대상 완제의약품 해당합니다.
(근거 : 「의약품의 품목허가·신고·심사 규정」제6조(국제공통기술문서 작성) 제1항, 제3조의2(의약품의 허가ㆍ신고의 변경 처리) 제6항)""")
        st.button("다음단계로", on_click=go_to_step2)

    elif st.session_state.step1_answer == "아니오":
        st.warning("""CTD 작성대상 완제의약품 해당여부를 확인하고, 작성 대상에 해당하는 경우 먼저, CTD 제3부 품질평가 자료 중
3.2.S.2, 3.2.S.3 및 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7를 제출하여 제조방법 자료로서 심사 받으시기 바랍니다.
(근거 : 「의약품의 품목허가·신고·심사 규정」제6조(국제공통기술문서 작성) 제1항, 제3조의2(의약품의 허가ㆍ신고의 변경 처리) 제6항)""")

# STEP 2 이동 함수
def go_to_step3():
    if st.session_state.step2_answer == "예":
        st.session_state.step = 3

# STEP 2
if st.session_state.step == 2:
    st.markdown("## Step 2")
    st.write("제조에 관한 항목 (CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3 및 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7)을 변경 하는 경우에 해당한다.")

    st.session_state.step2_answer = st.radio("답변을 선택하세요.", ["예", "아니오"], key="step2_radio")

    if st.session_state.step2_answer == "예":
        st.success("""「의약품 허가 후 제조방법 변경관리 가이드라인(민원인 안내서)」의 적용 대상 항목의 변경에 해당합니다.
(근거 : 「의약품의 품목허가·신고·심사 규정」[별표 19])""")
        st.button("다음단계로", on_click=go_to_step3)

    elif st.session_state.step2_answer == "아니오":
        st.warning("""제조에 관한 항목은 CTD 제3부 품질평가 자료 중
3.2.S.2, 3.2.S.3 및 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7에 해당하며
「의약품 허가 후 제조방법 변경관리 가이드라인(민원인 안내서)」는 해당 항목에 대한 변경에 대해 안내하고 있으므로,
가이드라인 적용 대상에 해당하지 않습니다.
(근거 : 「의약품의 품목허가·신고·심사 규정」[별표 19])""")

# STEP 3 이동 함수
def go_to_step4():
    if st.session_state.step3_answer == "예":
        st.session_state.step = 4

# STEP 3
if st.session_state.step == 3:
    st.markdown("## Step 3")
    st.write("품목의 허가(신고) 사항 중 제조방법에 해당하는 자료(CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3 및 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7)를 국제공통기술문서(CTD)로서 제출하여 심사받은 ‘제조방법 CTD 적용(또는 전환)’ 품목에 해당한다.")

    st.session_state.step3_answer = st.radio("답변을 선택하세요.", ["예", "아니오"], key="step3_radio")

    if st.session_state.step3_answer == "예":
        st.success("""「의약품 허가 후 제조방법 변경관리 가이드라인(민원인 안내서)」에 따라 변경수준을 확인할 수 있습니다.  
(근거 : 「의약품의 품목허가·신고·심사 규정」[별표 19])""")
        st.button("다음단계로", on_click=go_to_step4)

    elif st.session_state.step3_answer == "아니오":
        st.warning("""먼저, CTD 제3부 품질평가 자료 중 3.2.S.2, 3.2.S.3 및 3.2.P.2, 3.2.P.3, 3.2.P.4, 3.2.P.7를 제출하여 제조방법 자료로서 심사 받으시기 바랍니다.  
(근거 : 「의약품의 품목허가·신고·심사 규정」[별표 19])""")

# Step 4 준비
if "step4_selections" not in st.session_state:
    st.session_state.step4_selections = {}
if "step5_targets" not in st.session_state:
    st.session_state.step5_targets = []

# Step 4 항목 (프롬프트 문구 그대로)
step4_items = {
    "s1": "3.2.S.1 일반정보",
    "s2": "3.2.S.2 제조",
    "p1": "3.2.P.1 완제의약품의 성상 및 조성",
    "p3": "3.2.P.3 제조",
    "p4": "3.2.P.4 첨가제의 관리",
    "p7": "3.2.P.7 용기-마개 시스템",
    "ds": "디자인스페이스(Design Space)"
}

# Step 3 → Step 4 이동 함수
def go_to_step4():
    if st.session_state.step3_answer == "예":
        st.session_state.step = 4

# Step 4 → Step 5 이동 함수
def go_to_step5():
    st.session_state.step5_targets = [
        code for code, val in st.session_state.step4_selections.items() if val == "변경 있음"
    ]
    st.session_state.step = 5

# Step 4 이전단계 복귀 함수
def go_back_to_step3():
    st.session_state.step = 3

# Step 4 실행
if st.session_state.step == 4:
    st.markdown("## Step 4")
    st.write("Step 4. 변경사항에 해당하는 상위 항목을 선택하세요.")

    st.markdown("#### 3.2.S 원료의약품")
    st.session_state.step4_selections["s1"] = st.radio(
        "3.2.S.1 일반정보",
        ["변경 있음", "변경 없음"],
        key="step4_radio_s1"
    )
    st.session_state.step4_selections["s2"] = st.radio(
        "3.2.S.2 제조",
        ["변경 있음", "변경 없음"],
        key="step4_radio_s2"
    )

    st.markdown("#### 3.2.P 완제의약품")
    st.session_state.step4_selections["p1"] = st.radio(
        "3.2.P.1 완제의약품의 성상 및 조성",
        ["변경 있음", "변경 없음"],
        key="step4_radio_p1"
    )
    st.session_state.step4_selections["p3"] = st.radio(
        "3.2.P.3 제조",
        ["변경 있음", "변경 없음"],
        key="step4_radio_p3"
    )
    st.session_state.step4_selections["p4"] = st.radio(
        "3.2.P.4 첨가제의 관리",
        ["변경 있음", "변경 없음"],
        key="step4_radio_p4"
    )
    st.session_state.step4_selections["p7"] = st.radio(
        "3.2.P.7 용기-마개 시스템",
        ["변경 있음", "변경 없음"],
        key="step4_radio_p7"
    )

    st.markdown("#### 디자인스페이스")
    st.session_state.step4_selections["ds"] = st.radio(
        "디자인스페이스(Design Space)",
        ["변경 있음", "변경 없음"],
        key="step4_radio_ds"
    )

    # 모든 항목 선택 여부 확인
    all_selected = all(
        v in ["변경 있음", "변경 없음"]
        for v in st.session_state.step4_selections.values()
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button("이전단계로", on_click=go_back_to_step3)
    with col2:
        st.button("다음단계로", on_click=go_to_step5, disabled=not all_selected)
        
# Step 5 상태 초기화
if "step5_selections" not in st.session_state:
    st.session_state.step5_selections = {}
if "step6_targets" not in st.session_state:
    st.session_state.step6_targets = []

# Step 4에서 선택된 항목에 따른 중위항목 정의 (프롬프트 내용 그대로)
step5_items = {
    "s1": {
        "title": "3.2.S.1 일반정보",
        "items": {
            "1": "1. 원료의약품 명칭변경"
        }
    },
    "s2": {
        "title": "3.2.S.2 제조",
        "items": {
            "2": "2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가",
            "3": "3. 원료의약품 제조 공정의 변경",
            "4": "4. 원료의약품 제조 공정관리 규격의 변경",
            "5": "5. 원료의약품 또는 중간체의 제조 규모 변경",
            "6": "6. 원료의약품의 제조에 사용되는 원료(출발물질, 중간체, 용매, 시약 등)의 규격변경"
        }
    }
}

def go_to_step6():
    st.session_state.step6_targets = [
        key for key, val in st.session_state.step5_selections.items() if val == "변경 있음"
    ]
    st.session_state.step = 6

def go_back_to_step4():
    st.session_state.step = 4

# STEP 5 시작
if st.session_state.step == 5:
    st.markdown("## Step 5")
    st.write("Step 5. 선택한 변경항목 중 변경사항을 선택하세요.")

    for code in st.session_state.step5_targets:
        if code in step5_items:
            section = step5_items[code]
            st.markdown(f"#### {section['title']}")
            for num, label in section["items"].items():
                radio_key = f"step5_radio_{code}_{num}"
                if radio_key not in st.session_state:
                    st.session_state[radio_key] = None
                st.session_state.step5_selections[f"{code}_{num}"] = st.radio(
                    label, ["변경 있음", "변경 없음"], key=radio_key
                )

    # 전체 선택 확인
    all_selected = all(
        v in ["변경 있음", "변경 없음"] for v in st.session_state.step5_selections.values()
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button("이전단계로", on_click=go_back_to_step4)
    with col2:
        st.button("다음단계로", on_click=go_to_step6, disabled=not all_selected)
        
# Step 5 상태 초기화
if "step5_selections" not in st.session_state:
    st.session_state.step5_selections = {}
if "step6_targets" not in st.session_state:
    st.session_state.step6_targets = []

# Step 4에서 선택된 항목에 따른 중위항목 정의 (프롬프트 내용 그대로)
step5_items = {
    "s1": {
        "title": "3.2.S.1 일반정보",
        "items": {
            "1": "1. 원료의약품 명칭변경"
        }
    },
    "s2": {
        "title": "3.2.S.2 제조",
        "items": {
            "2": "2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가",
            "3": "3. 원료의약품 제조 공정의 변경",
            "4": "4. 원료의약품 제조 공정관리 규격의 변경",
            "5": "5. 원료의약품 또는 중간체의 제조 규모 변경",
            "6": "6. 원료의약품의 제조에 사용되는 원료(출발물질, 중간체, 용매, 시약 등)의 규격변경"
        }
    },
# Step 5 중위항목 정의 계속 추가
step5_items.update({
    "p1": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성",
        "items": {
            "7": "7. 완제의약품 중 고형 제제의 조성 변경",
            "8": "8. 완제의약품 중 고형 제제의 코팅층 무게 변경",
            "9": "9. 완제의약품 중 고형제제를 제외한 그 외 제형의 조성 변경",
            "10": "10. 완제의약품 중 고형제제를 제외한 그 외 제형에 쓰이는 착색제 또는 착향제의 종류와 분량의 변경"
        }
    },
    "p3": {
        "title": "3.2.P.3 제조",
        "items": {
            "11": "11. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경(단 잉크, 그림, 글자체 등 식별표시를 위한 변경은 제외)",
            "12": "12. 완제의약품 제조공정 중 일부공정 제조소 또는 전체공정 제조소의, 추가 또는 변경",
            "13": "13. 비무균제제의 제조 규모 변경",
            "14": "14. 무균제제의 제조 규모 변경",
            "15": "15. 완제의약품의 제조공정 변경",
            "16": "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경"
        }
    },
    "p4": {
        "title": "3.2.P.4 첨가제의 관리",
        "items": {
            "17": "17. 첨가제 기원의 변경",
            "18": "18. 별규에 해당하는 첨가제의 규격 또는 시험방법변경",
            "19": "19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경"
        }
    },
    "p7": {
        "title": "3.2.P.7 용기-마개 시스템",
        "items": {
            "20": "20. 비무균제제의 직접용기 및 포장재질, 종류 변경",
            "21": "21. 무균제제의 직접용기 및 포장 재질, 종류 변경",
            "22": "22. 직접 포장의 규격 변경",
            "23": "23. 포장단위 변경"
        }
    },
    "ds": {
        "title": "디자인스페이스(Design Space)",
        "items": {
            "24": "24. 디자인스페이스(Design Space) 변경"  # 무조건 '변경 있음' 선택됨
        }
    }
})


def go_to_step6():
    st.session_state.step6_targets = [
        key for key, val in st.session_state.step5_selections.items() if val == "변경 있음"
    ]
    st.session_state.step = 6

def go_back_to_step4():
    st.session_state.step = 4

# STEP 5 시작
if st.session_state.step == 5:
    st.markdown("## Step 5")
    st.write("Step 5. 선택한 변경항목 중 변경사항을 선택하세요.")

    for code in st.session_state.step5_targets:
        if code in step5_items:
            section = step5_items[code]
            st.markdown(f"#### {section['title']}")
            for num, label in section["items"].items():
                radio_key = f"step5_radio_{code}_{num}"
                if radio_key not in st.session_state:
                    st.session_state[radio_key] = None
                st.session_state.step5_selections[f"{code}_{num}"] = st.radio(
                    label, ["변경 있음", "변경 없음"], key=radio_key
                )
    # STEP 5 실행 계속...
    for code in st.session_state.step5_targets:
        if code in step5_items:
            section = step5_items[code]
            st.markdown(f"#### {section['title']}")
            for num, label in section["items"].items():
                key = f"{code}_{num}"
                if code == "ds":
                    st.markdown(f"**{label}** → 변경 있음 (자동 선택됨)")
                    st.session_state.step5_selections[key] = "변경 있음"
                else:
                    radio_key = f"step5_radio_{key}"
                    if radio_key not in st.session_state:
                        st.session_state[radio_key] = None
                    st.session_state.step5_selections[key] = st.radio(
                        label,
                        ["변경 있음", "변경 없음"],
                        key=radio_key
                    )
                

    # 전체 선택 확인
    all_selected = all(
        v in ["변경 있음", "변경 없음"] for v in st.session_state.step5_selections.values()
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button("이전단계로", on_click=go_back_to_step4)
    with col2:
        st.button("다음단계로", on_click=go_to_step6, disabled=not all_selected)

import streamlit as st

# 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 5

if "step5_targets" not in st.session_state:
    st.session_state.step5_targets = ["s1_1", "s2_2", "s2_3", "s2_4", "s2_5", "s2_6"]

if "step6_targets" not in st.session_state:
    st.session_state.step6_targets = []

if "step6_selections" not in st.session_state:
    st.session_state.step6_selections = {}

# Step 간 이동
def go_to_step6():
    st.session_state.step6_targets = st.session_state.step5_targets.copy()
    st.session_state.step = 6

def go_to_step7():
    st.session_state.step = 7

def go_back_to_step5():
    st.session_state.step = 5

# Title 1~3 하드코딩
step6_items = {
    "s1_1": {
        "title": "3.2.S.1 일반정보\n1. 원료의약품 명칭변경",
        "subitems": {},
        "requirements": {
            "1": "1. 유효성분은 그대로 유지된다."
        }
    },
    "s2_2": {
        "title": "3.2.S.2 제조\n2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가",
        "subitems": {
            "2a": "2a. 원료의약품의 출발물질 생산",
            "2b": "2b. 원료의약품의 중간체 생산",
            "2c": "2c. 원료의약품의 생산"
        },
        "requirements": {
            "1": "1. 무균 원료의약품이 아니다.",
            "2": "2. 변경된 제조소의 원료의약품은 완제연계심사로서 DMF 품질심사를 완료하였다.",
            "3": "3. 원료의약품 규격에는 변경이 없다.",
            "4": "4. 출발 물질의 규격, 불순물 프로파일 및 합성경로는 변경이 없다.",
            "5": "5. 규격(공정 중 관리, 모든 원료의 분석 방법 포함), 제조 방법, 상세한 합성 경로 및 중간체 규격의 변경이 없다.",
            "6": "6. 원료의약품의 경우, 그 결정형이 동일하고, 입자크기가 중요한 경우 입자 크기 분포에 유의한 차이가 없다.",
            "7": "7. 원료의약품의 규격 (공정 중 관리, 모든 원료의 분석 방법 포함), 제조 방법 (배치 크기 포함) 및 상세한 합성 경로는 변경이 없다.",
            "8": "8. 사람 또는 동물 유래 물질이 사용되는 경우, BSE/TSE 위험에 대한 평가가 필요한 새로운 공급자를 이용하지 않는다.",
            "9": "9. 출발물질은 조품의 원료, 등록대상 원료의약품의 성분, 등록하고자 하는 원료의약품과 화학구조가 유사한 성분에 해당하지 않는다.",
            "10": "10. 실제 제조장소의 변경이 없는 제조소의 명칭 변경이다."
        }
    },
    "s2_3": {
        "title": "3.2.S.2 제조\n3. 원료의약품 제조 공정의 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 원료의약품의 물리적 성질(결정형, 비결정형 등)에 변경이 없다.",
            "2": "2. 난용성 원료의약품의 경우, 결정다형이 동일하고 입자 크기가 중요한 경우 입자 크기 분포에 유의한 차이가 없다.",
            "3": "3. 사람 또는 동물 유래 물질이 사용되는 경우, 바이러스 안정성 평가 및 BSE/TSE 위험에 대한 평가가 필요한 새로운 공정이 포함되지 않는다.",
            "4": "4. 합성경로의 변경이 없고(중간체는 동일하게 유지됨) 새로운 시약, 촉매 혹은 용매가 사용되지 않는다.",
            "5": "5. 원료의약품의 정성적 및 정량적 불순물 프로파일이나 물리 화학적 성질의 변경이 없다.",
            "6": "6. 무균 원료의약품의 멸균 또는 무균 공정에 영향을 미치지 않는다.",
            "7": "7. 최종 중간체 이전 공정의 변경이다.",
            "8": "8. 변경 전·후, 출발물질 규격, 중간체 규격 또는 원료의약품 규격의 변경이 없다.",
            "9": "9. 원료의약품 규격에 변경이 없다."
        }
    }
}
# 이어지는 Title 4~6 하드코딩 추가
step6_items.update({

    "s2_4": {
        "title": "3.2.S.2 제조\n4. 원료의약품 제조 공정관리 규격의 변경",
        "subitems": {
            "4a": "4a. 공정관리 기준 강화",
            "4b": "4b. 공정관리 시험 및 기준 추가",
            "4c": "4c. 안전성이나 품질 문제로 인한 공정 관리 시험의 추가 또는 교체",
            "4d": "4d. 공정관리 시험 삭제",
            "4e": "4e. 공정관리 시험 기준 완화"
        },
        "requirements": {
            "1": "1. 해당 변경은 제조 중 예기치 않은 사례로 발생한 것이 아니다.",
            "2": "2. 해당 변경은 현재 승인된 기준 범위 내에 있다.",
            "3": "3. 분석 절차는 동일하다. (분석절차의 경미한 변경은 허용)",
            "4": "4. 삭제되는 공정관리 시험은 품질에 영향을 미치지 않는다.",
            "5": "5. 해당 변경은 무균 원료의약품의 멸균 공정에 영향을 주지 않는다."
        }
    },

    "s2_5": {
        "title": "3.2.S.2 제조\n5. 원료의약품 또는 중간체의 제조 규모 변경",
        "subitems": {
            "5a": "5a. 제조 규모의 10배 이하 확대",
            "5b": "5b. 제조 규모의 축소",
            "5c": "5c. 제조 규모의 10배 초과 확대"
        },
        "requirements": {
            "1": "1. 제조방법 및 공정관리의 변경은 제조규모 변경에 따른 변경만을 포함한다.",
            "2": "2. 제조 공정의 재현성에 영향이 없다.",
            "3": "3. 제조과정에서 예상하지 못한 사유로 기준을 충족하지 못한 경우 또는 안정성 문제 때문에 발생한 변경이 아니다."
        }
    },

    "s2_6": {
        "title": "3.2.S.2 제조\n6. 원료의약품의 제조에 사용되는 원료의 규격변경",
        "subitems": {
            "6a": "6a. 규격 기준의 강화",
            "6b": "6b. 시험방법의 변경",
            "6c": "6c. 기준 및 시험방법 추가",
            "6d": "6d. 기준 또는 시험방법의 삭제",
            "6e": "6e. 안전성이나 품질관리 문제로 인한 기준의 추가 또는 교체",
            "6f": "6f. 원료약품(용매, 시약, 촉매 등)에 대한 기준 완화",
            "6g": "6g. 원료의약품 출발물질 및 핵심중간체에 대한 기준 완화"
        },
        "requirements": {
            "1": "1. 제조과정에서 예상하지 못한 사유로 기준을 충족하지 못한 경우 또는 안정성 문제 때문에 발생한 변경이 아니다.",
            "2": "2. 모든 변경 사항은 현재의 허용 기준범위 내에 있다.",
            "3": "3. 시험방법의 변경은 없다.",
            "4": "4. 변경 후 시험방법은 동일한 분석 기술 또는 원리로 수행된다.",
            "5": "5. 변경 후 시험법 밸리데이션은 적절하게 수행되었으며, 이전 시험방법과 동등 이상이다.",
            "6": "6. 원료의약품의 총 불순물 기준 변경은 없으며, 새로 검출되는 불순물은 없다.",
            "7": "7. 변경은 유전독성 불순물의 관리전략에 영향을 미치지 않는다.",
            "8": "8. 변경되는 시험항목은 중요하지 않거나 승인된 대체 시험항목이 있다.",
            "9": "9. 회수용매의 기준과 관련되어 있지 않다."
        }
    }
})
step6_items.update({

    "s3_1": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n7. 완제의약품 중 고형 제제의 조성 변경",
        "subitems": {
            "7a": "7a. 타르색소(황색4호 제외)의 종류 변경",
            "7b": "7b. 착색제 또는 착향제의 종류 및 분량 변경",
            "7c": "7c. 첨가제의 종류 및 분량 변경"
        },
        "requirements": {
            "1": "1. 제형의 기능적 특성 및 제품 품질(붕해시간 혹은 용출프로파일 등)에 미치는 영향은 없다.",
            "2": "2. 단위제형 총 중량 중 착색제, 착향제간의 함유율의 차는 없으며, 기허가 품목(동일투여경로)에 사용된 예가 있다.",
            "3": "3. 해당 변경은 안정성 문제로 인한 것이 아니며, 잠재적인 안전성 우려, 즉 용량 간의 구별 문제를 야기하지 않는다.",
            "4": "4. 변경/추가되는 첨가제는 「의약품의 품목허가·신고·심사 규정」 제25조제2항제1호에 따른 새로운 첨가제가 아니다.",
            "5": "5. 변경/추가되는 첨가제의 규격은 공정서 규격에 해당한다."
        }
    },

    "s3_2": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n8. 고형제제의 코팅층 무게 변경",
        "subitems": {},
        "requirements": {}  # 선택사항 없음 (프롬프트 상 N/A)
    },

    "s3_3": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n9. 완제의약품(고형제제 제외)의 조성 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 시럽제, 엘릭서제, 틴크제 등 경구용 액제 및 외용액제(유제 및 현탁제 제외)",
            "2": "2. 주사제, 점안제, 점이제로 원료약품의 종류가 동일하거나 허가된 첨가제가 다른 경우",
            "3": "3. 흡입 전신마취제",
            "4": "4. 국소적용 외용제제로서 원료약품 종류 동일하고, 첨가제가 다른 경우",
            "5": "5. 유효성분을 기체나 증기 형태로 흡입하는 국소요법 제제",
            "6": "6. 수액제, 혈액증량제 및 인공관류액 제제",
            "7": "7. 폐에 적용하는 흡입제",
            "8": "8. 위 충족조건에 포함되지 않는 경우",
            "9": "9. 첨가제는 새로운 첨가제가 아니다."
        }
    }
})
step6_items.update({

    "s3_4": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n10. 완제의약품(고형제제 제외)에 쓰이는 착색제 또는 착향제의 종류와 분량의 변경",
        "subitems": {
            "10a": "10a. 타르색소의 종류 변경(황색4호 제외)",
            "10b": "10b. 타르색소의 종류 및 분량 변경",
            "10c": "10c. 타르색소 외 착색제, 착향제의 변경"
        },
        "requirements": {
            "1": "1. 제형의 성능에 관한 시험결과(예: 붕해시간 및 용출프로파일)에 변화가 없다.",
            "2": "2. 총 중량을 유지하기 위해 주요 첨가제를 써서 처방 조성이 경미하게 조정되어 있다.",
            "3": "3. 완제의약품의 규격은 성상, 냄새 및/또는 맛에 대해서만 개정되었거나 확인시험 변경에 국한된다.",
            "4": "4. 타르색소 착색제는 지정 고시에 적합하다.",
            "5": "5. 착향제는 기허가 품목(동일 투여경로)에 사용된 예가 있다.",
            "6": "6. 첨가제는 국제공통기술문서 3.2.P.4를 준수한다.",
            "7": "7. 유래물질이 있을 경우, BSE/TSE 위해 적합성 평가 자료가 있다.",
            "8": "8. 변경 사항은 용량 간 식별에 영향을 미치지 않는다.",
            "9": "9. 새로운 첨가제가 아니다."
        }
    },

    "s4_1": {
        "title": "3.2.P.3 제조\n11. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경",
        "subitems": {
            "11a": "11a. 11b에 언급된 것 이외의 정제, 캡슐, 좌제",
            "11b": "11b. 장용성, 서방성 완제의약품"
        },
        "requirements": {
            "1": "1. 완제의약품의 규격은 모양에 대해서만 변경되어 있다.",
            "2": "2. 변경 전·후 최소 1배치의 용출 프로파일은 동등하다.",
            "3": "3. 성형공정의 변경으로 인한 외형 변화이며 식별표시는 해당하지 않는다."
        }
    },

    "s4_2": {
        "title": "3.2.P.3 제조\n12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
        "subitems": {
            "12a": "12a. 이차 포장 제조소",
            "12b1": "12b.1. 일차 포장 제조소 – 고형(정제, 캡슐제), 반고형(연고제, 크림제) 및 액상 제제",
            "12b2": "12b.2. 일차 포장 제조소 – 그 밖의 액상 제제(유제, 현탁제)",
            "12c1": "12c1. 원료칭량 공정 및 완제품 포장공정 제조소 제외한 그 밖의 제조소",
            "12c2": "12c2. 기타 제조소(조합 상황 등)"
        },
        "requirements": {
            "1": "1. 배치 조성, 제조 공정 및 공정 관리, 장비 및 반제품/완제품 규격에 변경이 없다.",
            "2": "2. GMP 적합 판정서(국내) 또는 유효 제조증명서(해외)가 있다.",
            "3": "3. 무균제제가 아니다.",
            "4": "4. 포장 재질의 변경이 없다.",
            "5": "5. 액상제제, 흡입제, 반고형제제에 해당한다. (유제/현탁제 제외)"
        }
    }
})
step6_items.update({

    "s4_3": {
        "title": "3.2.P.3 제조\n13. 비무균제제의 제조 규모 변경",
        "subitems": {
            "13a": "13a. 대조약과 의약품동등성 입증 또는 임상시험을 실시한 제제의 10배수 이하 변경",
            "13b": "13b. 일반 제제에서 10배 초과 생산 규모 변경",
            "13c": "13c. 특수성이 인정되는 제제 및 반고형제제에서 10배 초과 생산규모 변경"
        },
        "requirements": {
            "1": "1. 해당 변경은 제제의 재현성 및/또는 일관성에 영향을 미치지 않는다.",
            "2": "2. 제조장비의 작동원리 및 디자인이 동일하고, 제조 공정의 변경은 제조 규모에 따른 것이다.",
            "3": "3. 위험도 평가 또는 밸리데이션 실시 계획서에 따라 생산 규모 3배치 밸리데이션이 성공적으로 수행되었다.",
            "4": "4. 변경은 예기치 않은 사례나 안정성 문제로 인한 것이 아니다.",
            "5": "5. 일반제제에 해당한다.",
            "6": "6. 액상제제에 해당한다."
        }
    },

    "s4_4": {
        "title": "3.2.P.3 제조\n14. 무균제제의 제조 규모 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 해당 변경은 생산 일관성에 영향을 주지 않는다.",
            "2": "2. 원료약품 및 그 분량에는 변경이 없다.",
            "3": "3. 의약품의 규격 변경이 없다.",
            "4": "4. 위험도 평가 또는 밸리데이션 실시 계획서에 따라 생산 규모 3배치 밸리데이션이 성공적으로 수행되었다.",
            "5": "5. 액상제제로서 제조 규모 변경이 10배 초과이다.",
            "6": "6. 특수성이 인정되는 제제, 반고형제제 또는 분말형 주사제로서 제조 규모 변경이 10배 초과이다."
        }
    },

    "s4_5": {
        "title": "3.2.P.3 제조\n15. 완제의약품의 제조공정 변경",
        "subitems": {
            "15a": "15a. 제조공정 변경",
            "15b1": "15b-1. 첨가제 등급/투입순서 변경 등",
            "15b2": "15b-2. 결합액의 용매 종류 변경",
            "15c": "15c. 기타 공정 변경"
        },
        "requirements": {
            "1": "1. 불순물 프로파일 및 물리화학적 성질에 변경이 없고, 용출 프로파일은 유사하다.",
            "2": "2. 제조공정은 동일 원리이며, 반제품 동일, 제조 용매 변경 없음.",
            "3": "3. 제조장비는 동일 계열이며, 작동원리와 디자인이 같다.",
            "4": "4. 주요 제조공정 조건은 변동이 없다.",
            "5": "5. 반제품 또는 완제의약품의 규격 변경이 없다.",
            "6": "6. 변경은 예기치 않은 사례나 안정성 문제로 인한 것이 아니다.",
            "7": "7. 변경은 포장 및 라벨링 공정을 포함하지 않는다.",
            "8": "8. 일반제제에 해당한다.",
            "9": "9. 액상제제에 해당한다."
        }
    }
})
step6_items.update({

    "s4_6": {
        "title": "3.2.P.3 제조\n16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
        "subitems": {
            "16a": "16a. 공정관리시험 기준의 변경",
            "16b": "16b. 공정관리시험 기준의 변경(보고유형: Cmaj)",
            "16c": "16c. 공정관리시험 항목의 삭제",
            "16d": "16d. 새로운 공정관리시험 기준의 추가",
            "16e": "16e. 공정관리시험 방법의 변경"
        },
        "requirements": {
            "1": "1. 해당 변경은 공정관리 기준(예: 마손도, 경도, 입도, 밀도, 수분 등) 범위 내에 있다.",
            "2": "2. 해당 변경은 제조 중 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제로 인한 것이 아니다.",
            "3": "3. 삭제된 공정관리 항목은 불필요하거나 생략 가능하다는 것이 입증되었으며, 제제의 주요 품질 특성에 영향을 미치지 않는다.",
            "4": "4. 시험방법에는 변경이 없다."
        }
    },

    "s5_1": {
        "title": "3.2.P.4 첨가제의 관리\n17. 첨가제 기원의 변경",
        "subitems": {
            "17a": "17a. 동물성 기원 → 식물 또는 합성 기원",
            "17b": "17b. 식물 또는 합성 기원 → 동물성 기원 또는 다른 동물성 기원"
        },
        "requirements": {
            "1": "1. 첨가제와 완제의약품의 규격에는 변경이 없다."
        }
    },

    "s5_2": {
        "title": "3.2.P.4 첨가제의 관리\n18. 별규에 해당하는 첨가제의 규격 또는 시험방법 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 해당 변경은 제조 과정 중 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제로 인해 발생한 변경이 아니다."
        }
    }
})
step6_items.update({

    "s5_3": {
        "title": "3.2.P.4 첨가제의 관리\n19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 공정서를 준수하기 위해 요구되는 규격 이외에는 변경이 없다. (예: 입자 크기 분포의 변경 없음)"
        }
    },

    "s6_1": {
        "title": "3.2.P.7 용기-마개 시스템\n20. 비무균제제의 직접용기 및 포장 재질, 종류 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 고형제제로서 주성분, 제형, 투여경로가 동일한 기허가 의약품에서 사용례가 확인되는 용기 재질로의 변경 또는 동일한 종류/보호성 동등 이상인 재질로의 변경이며, 사용기간은 기허가의약품 사용기간을 초과하지 않는다."
        }
    },

    "s6_2": {
        "title": "3.2.P.7 용기-마개 시스템\n21. 무균제제의 직접용기 및 포장 재질, 종류 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 변경 후 용기의 보호성 등이 동등 이상이고 상호작용 위험이 없다."
        }
    }
})
step6_items.update({

    "s6_3": {
        "title": "3.2.P.7 용기-마개 시스템\n22. 직접 포장의 규격 변경",
        "subitems": {
            "22a": "22a. 규격 기준의 강화",
            "22b": "22b. 시험 항목의 추가 또는 삭제"
        },
        "requirements": {
            "1": "1. 모든 변경 사항은 현재의 허용 기준범위 내에 있다.",
            "2": "2. 해당 변경은 제조 과정에서 발생하는 예기치 않은 사례로 인한 규격 미충족 혹은 안정성 문제 때문에 발생한 변경이 아니다."
        }
    },

    "s6_4": {
        "title": "3.2.P.7 용기-마개 시스템\n23. 포장단위 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 해당 변경은 제조 과정에서 발생하는 예기치 않은 사례로 인한 규격 미충족 혹은 안정성 문제 때문에 발생한 변경이 아니다.",
            "2": "2. 이외 허가사항의 변경은 없다."
        }
    },

    "s6_5": {
        "title": "3.2.P.7 용기-마개 시스템\n24. 새로운 디자인스페이스 도입 또는 허가된 디자인스페이스의 확장",
        "subitems": {},
        "requirements": {}  # 프롬프트 명시: N/A
    }
})

if st.session_state.step == 6:
    st.markdown("## Step 6")
    st.write("Step 6. Step5에서 '변경 있음'으로 선택된 항목에 대해 하위항목과 충족요건을 모두 선택하세요.")

    for key in st.session_state.step6_targets:
        if key in step6_items:
            block = step6_items[key]
            st.markdown(f"### {block['title']}")

            # 하위항목(선택사항1)
            for sub_key, sub_text in block.get("subitems", {}).items():
                full_key = f"{key}_sub_{sub_key}"
                st.session_state.step6_selections[full_key] = st.radio(
                    f"{sub_text}",
                    ["변경 있음", "변경 없음"],
                    key=full_key
                )

            # 충족요건(선택사항2)
            for req_key, req_text in block.get("requirements", {}).items():
                full_key = f"{key}_req_{req_key}"
                st.session_state.step6_selections[full_key] = st.radio(
                    f"{req_text}",
                    ["충족", "미충족"],
                    key=full_key
                )

    # 모든 항목이 선택되었는지 확인
    all_selected = all(
        value in ["변경 있음", "변경 없음", "충족", "미충족"]
        for value in st.session_state.step6_selections.values()
    )

    # 네비게이션 버튼
    col1, col2 = st.columns(2)
    with col1:
        st.button("이전단계로", on_click=go_back_to_step5)
    with col2:
        st.button("다음단계로", on_click=go_to_step7, disabled=not all_selected)

# STEP 7 - 보고유형 및 필요서류 도출
import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 7

if "step6_selections" not in st.session_state:
    st.session_state.step6_selections = {}

def go_to_step6():
    st.session_state.step = 6

def go_to_step8():
    st.session_state.step = 8

step7_results = []

# 도출 결과 출력 함수
def show_result(title, required_docs, report_type_desc):
    st.markdown(f"### {title}")
    st.markdown("**필요서류는 다음과 같습니다.**")
    for i, doc in enumerate(required_docs, 1):
        st.markdown(f"{i}. {doc}")
    st.markdown("**보고유형은 다음과 같습니다.**")
    st.markdown(report_type_desc)

# 보고유형 문구 (하드코딩)
report_types = {
    "AR": "AR, 연차보고  \n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 제2항 및 제4항에 따른 연차보고(Annual Report, AR) 수준의 변경사항입니다.",
    "IR": "IR, 시판전보고  \n「의약품의 품목허가‧신고‧심사 규정」 제3조의2제4항 단서조항에 따른 시판전 보고(Immediate Report, IR) 수준의 변경사항입니다.",
    "Cmaj": "Cmaj, 변경허가(신고)  \n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 및 제6조에 따라 품질에 중요한 영향을 미치는 변경허가(신고) 신청(Change, C) 대상이며, 중요도 및 제출자료 요건을 고려할 때 Major change(Cmaj) 수준의 변경사항입니다.",
    "Cmin": "Cmin, 변경허가(신고)  \n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 및 제6조에 따라 품질에 중요한 영향을 미치는 변경허가(신고) 신청(Change, C) 대상이며, 중요도 및 제출자료 요건을 고려할 때 Minor change(Cmin) 수준의 변경사항입니다."
}

if st.session_state.step == 7:
    st.markdown("## Step 7")
    st.markdown("**제조방법 변경에 따른 필요서류와 보고유형을 도출합니다.**")

    selections = st.session_state.step6_selections

    # s1_1: 원료의약품 명칭변경
    key = "s1_1_req_1"
    if key in selections:
        req1 = selections[key]

        if req1 == "충족":
            required_docs = [
                "(S.1.1) 공정서 또는 국제 의약품 일반명 리스트〔The International Nonproprietary Name(INN)〕 등 근거서류.",
                "개정된 제품정보."
            ]
            show_result(
                "3.2.S.1 일반정보\n1. 원료의약품 명칭변경",
                required_docs,
                report_types["AR"]
            )
        else:
            st.markdown("### 3.2.S.1 일반정보\n1. 원료의약품 명칭변경")
            st.markdown("「의약품 허가 후 제조방법 변경관리 가이드라인(민원인 안내서)」에 포함되지 않은 변경의 경우 위험평가를 수행하여 품질에 영향을 미치지 않거나 경미한 영향을 미치는 변경의 경우 제조사의 문서화된 절차 및 의약품품질시스템에 따라 처리하고 해당 변경이 제제의 품질 및 안전성‧유효성에 영향을 미치지 않도록 관리해야 하며, 그 외의 사항은 기본적으로 품질에 영향을 미치는 중요한 변경사항으로 간주 되어야 한다.")
   
    # s2_2: 원료의약품 제조소 또는 제조업자의 변경 또는 추가

    # --- 2a. 출발물질 생산 ---
    if "s2_2_sub_2a" in selections and selections["s2_2_sub_2a"] == "변경 있음":
        r3 = selections.get("s2_2_req_3")
        r4 = selections.get("s2_2_req_4")
        r9 = selections.get("s2_2_req_9")

        if r3 == "충족" and r4 == "충족" and r9 == "충족":
            show_result(
                "3.2.S.2 제조\n2a. 원료의약품의 출발물질 생산",
                [
                    "(해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "(S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료."
                ],
                report_types["IR"]
            )
        elif r3 == "미충족" and r4 == "미충족" and r9 == "미충족":
            show_result(
                "3.2.S.2 제조\n2a. 원료의약품의 출발물질 생산",
                [
                    "(해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "(S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "(S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.",
                    "변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "(S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.",
                    "변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료.",
                    "(S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."
                ],
                report_types["Cmaj"]
            )

    # --- 2b. 중간체 생산 ---
    if "s2_2_sub_2b" in selections and selections["s2_2_sub_2b"] == "변경 있음":
        r3 = selections.get("s2_2_req_3")
        r5 = selections.get("s2_2_req_5")

        if r3 == "충족" and r5 == "충족":
            show_result(
                "3.2.S.2 제조\n2b. 원료의약품의 중간체 생산",
                [
                    "(해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "(S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "(S.2) 원료의약품 및 핵심(최종) 중간체(해당되는 경우) 합성 경로, 사용 원료, 품질 관리 절차 및 규격 변경이 없다는 확인서(statement).",
                    "변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료."
                ],
                report_types["IR"]
            )
        elif r3 == "미충족" and r5 == "미충족":
            show_result(
                "3.2.S.2 제조\n2b. 원료의약품의 중간체 생산",
                [
                    "(해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "(S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "(S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.",
                    "변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "(S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.",
                    "변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료.",
                    "(S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."
                ],
                report_types["Cmaj"]
            )
            
    # --- 2c. 원료의약품의 생산 ---
    if "s2_2_sub_2c" in selections and selections["s2_2_sub_2c"] == "변경 있음":
        r1 = selections.get("s2_2_req_1")
        r2 = selections.get("s2_2_req_2")
        r3 = selections.get("s2_2_req_3")
        r6 = selections.get("s2_2_req_6")
        r7 = selections.get("s2_2_req_7")
        r8 = selections.get("s2_2_req_8")
        r10 = selections.get("s2_2_req_10")

        if all(r == "충족" for r in [r1, r2, r3, r6, r7, r8]):
            show_result(
                "3.2.S.2 제조\n2c. 원료의약품의 생산",
                [
                    "(해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "(S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "(S.4.4) 변경 전·후 원료의약품 2배치(파일럿 배치 이상)에 대한 배치분석자료.",
                    "(S.2) 원료의약품 및 핵심(최종) 중간체(해당되는 경우) 합성 경로, 사용 원료, 품질 관리 절차 및 규격 변경이 없다는 확인서(statement)."
                ],
                report_types["IR"]
            )

        elif all(r == "미충족" for r in [r1, r2, r3, r6, r7, r8]):
            show_result(
                "3.2.S.2 제조\n2c. 원료의약품의 생산",
                [
                    "(해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "(S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "(S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.",
                    "변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "(S.4.4) 변경 전·후 원료의약품 2배치(파일럿 배치 이상)에 대한 배치분석자료.",
                    "(P.8.2) 원료의약품의 품질 특성이 완제의약품의 안정성에 영향을 미칠 수 있는 변경의 경우, 완제의약품 1배치(실제 생산 규모의)에 대한 안정성 시험 이행 계획서.",
                    "(S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.",
                    "변경 후 원료의약품이 완제의약품의 안전성, 유효성 및 품질에 미치는 영향에 대한 고찰자료.",
                    "(S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."
                ],
                report_types["Cmaj"]
            )

        elif r10 == "충족":
            show_result(
                "3.2.S.2 제조\n2c. 원료의약품의 생산",
                [
                    "해당국가의 공식기관에서 발급받은 문서(GMP 증명서 등 포함) 또는 인증여부를 확인할 수 있는 자료(제조소의 책임자가 서명하고 공증받은 자료 등)."
                ],
                report_types["Cmin"]
            )
            
    # s2_3: 원료의약품 제조 공정의 변경
    if "s2_3" in selections:

        r1 = selections.get("s2_3_req_1")
        r2 = selections.get("s2_3_req_2")
        r3 = selections.get("s2_3_req_3")
        r4 = selections.get("s2_3_req_4")
        r5 = selections.get("s2_3_req_5")
        r6 = selections.get("s2_3_req_6")
        r7 = selections.get("s2_3_req_7")
        r8 = selections.get("s2_3_req_8")
        r9 = selections.get("s2_3_req_9")

        cond_all = all(r == "충족" for r in [r1, r2, r3, r4, r5, r6, r7, r8])
        cond_cmin_1 = all(r == "충족" for r in [r1, r2, r3, r5, r7, r8, r9])
        cond_cmin_2 = all(r == "충족" for r in [r1, r2, r3, r4, r5, r6])
        cond_all_fail = all(r == "미충족" for r in [r1, r2, r3, r4, r5, r6, r7, r8, r9])

        if cond_all:
            show_result(
                "3.2.S.2 제조\n3. 원료의약품 제조 공정의 변경",
                [
                    "변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료",
                    "(S.2.3)(해당되는 경우) 변경하고자 하는 원료의약품 제조에 사용된 원료(예 : 원료약품, 출발 물질, 용매, 시약,촉매)의 규격 및 시험 성적서",
                    "(S.4.4) 변경 전·후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 배치분석 자료"
                ],
                report_types["IR"]
            )

        elif cond_cmin_1 or cond_cmin_2:
            show_result(
                "3.2.S.2 제조\n3. 원료의약품 제조 공정의 변경",
                [
                    "변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료",
                    "(S.4.1) 변경 후 원료의약품 기준 및 시험방법에 관한 자료.(변경되는 경우, 출발물질 및 중간체의 기준 및 시험방법)",
                    "(S.4.4) 변경 전·후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 배치분석 자료"
                ],
                report_types["Cmin"]
            )

        elif cond_all_fail:
            show_result(
                "3.2.S.2 제조\n3. 원료의약품 제조 공정의 변경",
                [
                    "변경 후 원료의약품이 완제의약품의 안전성, 유효성 및 품질에 미치는 영향에 대한 고찰자료. (완제의약품의 불순물 프로파일, 배치분석자료, 필요한 경우 안정성 자료 등)",
                    "변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료",
                    "(S.2.3)(해당되는 경우)변경하고자 하는 원료의약품 제조에 사용된 원료(예 : 원료약품, 출발 물질, 용매, 시약,촉매)의 규격 및 시험 성적서",
                    "(S.2.3) 사람 또는 동물 유래 물질이 사용되는 경우, 출처가 새로운 원료약품에 대한 BSE/TSE(소해면상뇌증/전염성해면상뇌증) 위험 적합성 평가 자료",
                    "(S.2.4)(해당되는 경우) 주요 공정 및 중간체 관리에 관한 자료",
                    "(S.2.5) (위험도 평가에 따른) 멸균 공정 밸리데이션 자료 또는 멸균 평가 시험 자료",
                    "(S.3.1) 원료의약품의 구조 결정 자료(IR, UV 등) 및 물리화학적 성질에 관한 자료",
                    "(S.3.2) 불순물에 대한 고찰 및 근거자료",
                    "(S.4.1) 변경 후 원료의약품 기준 및 시험방법에 관한 자료.(변경되는 경우, 출발물질 및 중간체의 기준 및 시험방법)",
                    "(S.4.4) 변경 전·후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 배치분석 자료",
                    "(S.7.1) 변경 후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 3개월 이상 가속 시험 (필요한 경우, 중간조건시험) 및 장기 보존 시험 자료",
                    "난용성 원료의약품의 결정형 또는 입자도의 변경이 발생한 경우, 완제의약품의 품질과 생체이용률에 영향을 미치지 않는다는 입증 자료"
                ],
                report_types["Cmaj"]
            )
            
    # s2_4: 원료의약품 제조 공정관리 규격의 변경
    if "s2_4" in selections:

        r1 = selections.get("s2_4_req_1")
        r2 = selections.get("s2_4_req_2")
        r3 = selections.get("s2_4_req_3")
        r4 = selections.get("s2_4_req_4")
        r5 = selections.get("s2_4_req_5")

        # 4a: 공정관리 기준 강화, 요건 1,2,3 충족 시 AR
        if all(r == "충족" for r in [r1, r2, r3]):
            show_result(
                "3.2.S.1 일반정보\n4. 원료의약품 제조 공정관리 규격의 변경 (기준 강화)",
                [
                    "변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "(S.2.4) 변경 후 공정관리 시험 규격에 관한 자료"
                ],
                report_types["AR"]
            )

        # 4b: 공정관리 시험 및 기준 추가, 요건 1 충족 시 AR
        elif r1 == "충족" and selections.get("s2_4_sub_4b") == "변경 있음":
            show_result(
                "3.2.S.1 일반정보\n4. 원료의약품 제조 공정관리 규격의 변경 (시험/기준 추가)",
                [
                    "변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "(S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "해당되는 경우, 분석 방법 상세 자료",
                    "공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료"
                ],
                report_types["AR"]
            )

        # 4c: 안전성/품질문제로 인한 추가/교체, 전부 미충족 시 Cmin
        elif all(r == "미충족" for r in [r1, r2, r3]) and selections.get("s2_4_sub_4c") == "변경 있음":
            show_result(
                "3.2.S.1 일반정보\n4. 원료의약품 제조 공정관리 규격의 변경 (품질문제에 의한 추가/교체)",
                [
                    "변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "(S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "해당되는 경우, 분석 방법 상세 자료",
                    "공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료",
                    "(S.2.5) 무균원료의약품인 경우, 해당 공정기준 변경이 제품의 무균 및 멸균공정에 영향을 미칠 경우(위험도 평가 결과에 따른), 해당 공정에 대한 밸리데이션 자료 또는 평가 자료",
                    "(S.3.2) 해당변경이 불순물에 영향을 미칠 경우, 불순물에 대한 고찰 및 근거자료",
                    "(S.4.1) 변경 후 원료의약품(해당되는 경우 중간체) 규격에 관한 자료",
                    "(S.4.4) 변경 전·후 원료의약품 최소 1배치(파일럿 배치 이상)의 배치분석자료"
                ],
                report_types["Cmin"]
            )

        # 4d: 시험 삭제, 1,4,5 충족 시 AR
        elif all(r == "충족" for r in [r1, r4, r5]) and selections.get("s2_4_sub_4d") == "변경 있음":
            show_result(
                "3.2.S.1 일반정보\n4. 원료의약품 제조 공정관리 규격의 변경 (시험 삭제, 타당성 입증)",
                [
                    "변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "(S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "삭제되는 공정관리시험이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료)"
                ],
                report_types["AR"]
            )

        # 4d: 시험 삭제, 1만 충족 시 Cmaj
        elif r1 == "충족" and selections.get("s2_4_sub_4d") == "변경 있음":
            show_result(
                "3.2.S.1 일반정보\n4. 원료의약품 제조 공정관리 규격의 변경 (시험 삭제, 불충분)",
                [
                    "변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "(S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료",
                    "(S.2.5) 무균원료의약품인 경우, 해당 공정기준 변경이 제품의 무균 및 멸균공정에 영향을 미칠 경우(위험도 평가 결과에 따른), 해당 공정에 대한 밸리데이션 자료 또는 평가 자료",
                    "(S.3.2) 해당변경이 불순물에 영향을 미칠 경우, 불순물에 대한 고찰 및 근거자료",
                    "(S.4.1) 변경 후 원료의약품(해당되는 경우 중간체) 규격에 관한 자료",
                    "(S.4.4) 변경 전·후 원료의약품 최소 1배치(파일럿 배치 이상)의 배치분석자료"
                ],
                report_types["Cmaj"]
            )

        # 4e: 기준 완화, 1 충족 시 Cmaj
        elif r1 == "충족" and selections.get("s2_4_sub_4e") == "변경 있음":
            show_result(
                "3.2.S.1 일반정보\n4. 원료의약품 제조 공정관리 규격의 변경 (기준 완화)",
                [
                    "변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "(S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "(S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "공정관리 시험(추가, 교체, 삭제, 완화되는) 규격에 대한 타당성 입증 자료 또는 설명자료",
                    "(S.2.5) 무균원료의약품인 경우, 해당 공정기준 변경이 제품의 무균 및 멸균공정에 영향을 미칠 경우(위험도 평가 결과에 따른), 해당 공정에 대한 밸리데이션 자료 또는 평가 자료",
                    "(S.3.2) 해당변경이 불순물에 영향을 미칠 경우, 불순물에 대한 고찰 및 근거자료",
                    "(S.4.1) 변경 후 원료의약품(해당되는 경우 중간체) 규격에 관한 자료",
                    "(S.4.4) 변경 전·후 원료의약품 최소 1배치(파일럿 배치 이상)의 배치분석자료"
                ],
                report_types["Cmaj"]
            )
            
    # s2_5: 원료의약품 또는 중간체의 제조 규모 변경
    if "s2_5" in selections:

        r1 = selections.get("s2_5_req_1")
        r2 = selections.get("s2_5_req_2")
        r3 = selections.get("s2_5_req_3")

        # 5a: 제조 규모의 10배 이하 확대, 요건 1,2,3 충족 시 AR
        if all(r == "충족" for r in [r1, r2, r3]) and selections.get("s2_5_sub_5a") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n5. 원료의약품 또는 중간체의 제조 규모 변경 (10배 이하 확대)",
                [
                    "(S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.",
                    "(S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "(S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).",
                    "(S.4.4) 변경 전·후 제조 규모에서 각 최소 1배치에 대한 배치 분석 자료."
                ],
                report_types["AR"]
            )

        # 5b: 제조 규모의 축소, 요건 1,2,3 충족 시 AR
        elif all(r == "충족" for r in [r1, r2, r3]) and selections.get("s2_5_sub_5b") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n5. 원료의약품 또는 중간체의 제조 규모 변경 (축소)",
                [
                    "(S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.",
                    "(S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "(S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).",
                    "(S.4.4) 변경 전·후 제조 규모에서 각 최소 1배치에 대한 배치 분석 자료."
                ],
                report_types["AR"]
            )

        # 5c: 제조 규모 10배 초과 확대, 요건 1,2 충족 시 Cmin
        elif r1 == "충족" and r2 == "충족" and selections.get("s2_5_sub_5c") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n5. 원료의약품 또는 중간체의 제조 규모 변경 (10배 초과 확대)",
                [
                    "(S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.",
                    "(S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "(S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).",
                    "(S.4.4) 변경 전·후 제조 규모에서 각 최소 2배치에 대한 배치 분석 자료."
                ],
                report_types["Cmin"]
            )
            
    # s2_6: 원료의약품 제조에 사용되는 원료의 규격변경
    if "s2_6" in selections:

        r1 = selections.get("s2_6_req_1")
        r2 = selections.get("s2_6_req_2")
        r3 = selections.get("s2_6_req_3")
        r4 = selections.get("s2_6_req_4")
        r5 = selections.get("s2_6_req_5")
        r6 = selections.get("s2_6_req_6")
        r7 = selections.get("s2_6_req_7")
        r8 = selections.get("s2_6_req_8")
        r9 = selections.get("s2_6_req_9")

        # 6a: 규격 기준 강화, 요건 1,2,3 충족 → AR
        if all(r == "충족" for r in [r1, r2, r3]) and selections.get("s2_6_sub_6a") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n6. 원료의약품의 제조에 사용되는 원료의 규격 기준 강화",
                [
                    "변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "(S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "(S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서)."
                ],
                report_types["AR"]
            )

        # 6b: 시험방법의 변경, 요건 4,5,6 충족 → AR
        elif all(r == "충족" for r in [r4, r5, r6]) and selections.get("s2_6_sub_6b") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n6. 원료의약품의 제조에 사용되는 원료 시험방법 변경",
                [
                    "(S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "(S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서)."
                ],
                report_types["AR"]
            )

        # 6c: 기준 및 시험방법 추가, 요건 1,5,6,7 충족 → AR
        elif all(r == "충족" for r in [r1, r5, r6, r7]) and selections.get("s2_6_sub_6c") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n6. 원료의약품의 제조에 사용되는 원료 기준 및 시험방법 추가",
                [
                    "변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "(S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "(S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서)."
                ],
                report_types["AR"]
            )

        # 6d: 기준 또는 시험방법의 삭제, 요건 1,8,9 충족 → AR
        elif all(r == "충족" for r in [r1, r8, r9]) and selections.get("s2_6_sub_6d") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n6. 원료의약품의 제조에 사용되는 원료 기준/시험방법 삭제",
                [
                    "변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "(S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "(S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서).",
                    "해당 변경이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료)."
                ],
                report_types["AR"]
            )

        # 6e: 안전성이나 품질관리 문제로 인한 기준 추가/교체, 모든 요건 미충족 → Cmaj
        elif all(v == "미충족" for v in [r1, r2, r3, r4, r5, r6, r7, r8, r9]) and selections.get("s2_6_sub_6e") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n6. 안전성/품질관리 문제로 인한 기준 추가/교체",
                [
                    "변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "(S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "(S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서).",
                    "해당 변경이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료).",
                    "(S.3.2) (해당하는 경우) 불순물에 대한 고찰 및 근거자료."
                ],
                report_types["Cmaj"]
            )

        # 6f: 원료약품(용매, 시약 등) 기준 완화, 요건 3,6,7,9 충족 → AR
        elif all(r == "충족" for r in [r3, r6, r7, r9]) and selections.get("s2_6_sub_6f") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n6. 원료약품 기준 완화",
                [
                    "변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "(S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서)."
                ],
                report_types["AR"]
            )

        # 6g: 출발물질 및 핵심중간체 기준 완화, 모든 요건 미충족 → Cmaj
        elif all(v == "미충족" for v in [r1, r2, r3, r4, r5, r6, r7, r8, r9]) and selections.get("s2_6_sub_6g") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n6. 출발물질 및 핵심중간체 기준 완화",
                [
                    "변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "(S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "(S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서).",
                    "해당 변경이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료).",
                    "(S.3.2) (해당하는 경우) 불순물에 대한 고찰 및 근거자료."
                ],
                report_types["Cmaj"]
            )
    # s2_7: 완제의약품 중 고형 제제의 조성 변경
    if "s2_7" in selections:

        r1 = selections.get("s2_7_req_1")
        r2 = selections.get("s2_7_req_2")
        r3 = selections.get("s2_7_req_3")
        r4 = selections.get("s2_7_req_4")
        r5 = selections.get("s2_7_req_5")

        # 7a: 타르색소 종류 변경, 요건 1,4 충족 → AR
        if all(r == "충족" for r in [r1, r4]) and selections.get("s2_7_sub_7a") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n7. 고형 제제 타르색소 종류 변경",
                [
                    "(P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "(P.2) 변경 제제의 성분에 대한 검토 자료.",
                    "(P.4) 첨가제 종류 변경/추가 시 규격 자료.",
                    "(P.5) 기준 및 시험방법, 최소 1배치 시험성적서.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약."
                ],
                report_types["AR"]
            )

        # 7b-1: 착색제/착향제 종류/분량, 요건 1~5 충족 → IR
        elif all(r == "충족" for r in [r1, r2, r3, r4, r5]) and selections.get("s2_7_sub_7b") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n7. 착색제 또는 착향제 종류/분량 변경 (요건 1~5 충족)",
                [
                    "(P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "(P.4) 첨가제 규격 자료.",
                    "(P.5) 기준 및 시험방법, 최소 1배치 시험성적서.",
                    "(P.5.3) 분석 절차 방해 없음 입증 자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약."
                ],
                report_types["IR"]
            )

        # 7b-2: 착색제/착향제 종류/분량, 요건 1~4 충족 → Cmin
        elif all(r == "충족" for r in [r1, r2, r3, r4]) and selections.get("s2_7_sub_7b") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n7. 착색제 또는 착향제 종류/분량 변경 (요건 1~4 충족)",
                [
                    "(P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "(P.4) 첨가제 규격 자료.",
                    "(P.5) 기준 및 시험방법, 최소 1배치 시험성적서.",
                    "(P.5.3) 분석 절차 방해 없음 입증 자료."
                ],
                report_types["Cmin"]
            )

        # 7c: 첨가제 종류/분량 변경, 요건 1,4 충족 → Cmaj
        elif all(r == "충족" for r in [r1, r4]) and selections.get("s2_7_sub_7c") == "변경 있음":
            show_result(
                "3.2.S.2 제조\n7. 첨가제 종류 및 분량 변경",
                [
                    "(P.2 또는 R) 의약품동등성시험 관련 자료.",
                    "(P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "(P.2) 제제 성분에 대한 검토 자료.",
                    "(P.3) 배치 조성 자료.",
                    "(P.4) 첨가제 규격 자료.",
                    "(P.4.5) BSE/TSE 적합성 평가 자료 (해당 시).",
                    "(P.5) 기준 및 시험방법, 최소 1배치 시험성적서.",
                    "(P.5.3) 분석 절차 방해 없음 입증 자료.",
                    "(P.8.1) 안정성 시험 자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약."
                ],
                report_types["Cmaj"]
            )
            
    # s3_1: 고형제제의 코팅층 무게 변경
    if "s3_1" in selections:
        if selections.get("s3_1_sub_8") == "변경 있음":
            show_result(
                "3.2.P.1 완제의약품의 성상 및 조성\n8. 고형제제의 코팅층 무게 변경",
                [
                    "(P.2 또는 R) 품목허가·신고·심사 규정 별표2에 따른 제출자료.",
                    "(P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "(P.2) 코팅에 사용된 첨가제 성분 및 조성 자료.",
                    "(P.5) 기준 및 시험방법, 최소 1배치 시험 성적서."
                ],
                report_types["Cmin"]
            )
            
    # s3_2: 고형제제 제외 완제의약품 조성 변경
    if "s3_2" in selections:

        r1 = selections.get("s3_2_req_1")
        r2 = selections.get("s3_2_req_2")
        r3 = selections.get("s3_2_req_3")
        r4 = selections.get("s3_2_req_4")
        r5 = selections.get("s3_2_req_5")
        r6 = selections.get("s3_2_req_6")
        r7 = selections.get("s3_2_req_7")
        r8 = selections.get("s3_2_req_8")
        r9 = selections.get("s3_2_req_9")

        # 조건 1: 1~7, 9 충족 → Cmaj
        if all(r == "충족" for r in [r1, r2, r3, r4, r5, r6, r7, r9]):
            show_result(
                "3.2.P.1 완제의약품의 성상 및 조성\n9. 고형제제 제외 완제의약품 조성 변경",
                [
                    "(P.2 또는 R) 동등성시험 자료 및 이화학적 동등성 입증 자료.",
                    "(P.1) 성상 및 조성.",
                    "(P.2) 첨가제 선택 및 포장 적합성 자료.",
                    "(P.3) 배치 조성, 제조공정, 밸리데이션 계획서.",
                    "(P.4) 첨가제 규격 자료.",
                    "(P.4.5) BSE/TSE 적합성 자료.",
                    "(P.5) 기준 및 시험방법, 1배치 시험 성적서.",
                    "(P.5.3) 분석 절차 방해 없음 입증 자료.",
                    "(P.8.1) 안정성시험 최소 3~6개월 자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약."
                ],
                report_types["Cmaj"]
            )

        # 조건 2: 8, 9 충족 → Cmaj
        elif all(r == "충족" for r in [r8, r9]):
            show_result(
                "3.2.P.1 완제의약품의 성상 및 조성\n9. 조성 변경 - 8,9 충족",
                [
                    "(P.2 또는 R) 생동시험자료 또는 타당한 대체자료.",
                    "(P.1) 성상 및 조성.",
                    "(P.2) 첨가제 선택 및 포장 적합성 자료.",
                    "(P.3) 배치 조성, 제조공정, 밸리데이션 계획서.",
                    "(P.4) 첨가제 규격 자료.",
                    "(P.4.5) BSE/TSE 적합성 자료.",
                    "(P.5) 기준 및 시험방법, 1배치 시험 성적서.",
                    "(P.5.3) 분석 절차 방해 없음 입증 자료.",
                    "(P.8.1) 장기 및 가속 안정성 시험 3~6개월 자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약."
                ],
                report_types["Cmaj"]
            )
    # s3_3: 고형제제 제외 착색제 또는 착향제의 변경
    if "s3_3" in selections:
        r1 = selections.get("s3_3_req_1")
        r2 = selections.get("s3_3_req_2")
        r3 = selections.get("s3_3_req_3")
        r4 = selections.get("s3_3_req_4")
        r5 = selections.get("s3_3_req_5")
        r6 = selections.get("s3_3_req_6")
        r7 = selections.get("s3_3_req_7")
        r8 = selections.get("s3_3_req_8")
        r9 = selections.get("s3_3_req_9")

        # 조건1: 10a. 타르색소(황색4호 제외) 변경, 1, 3, 4, 8, 9 충족 → AR
        if all(r == "충족" for r in [r1, r3, r4, r8, r9]):
            show_result(
                "3.2.P.1 완제의약품의 성상 및 조성\n10. 타르색소 변경",
                [
                    "(P.1) 원료약품 분량.",
                    "(P.3) 배치 조성.",
                    "(P.5) 기준 및 시험방법 및 최소 1배치 시험 성적서.",
                    "(P.8.2) 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "(R.1) 제조 관련 문서 변경 없음 확인서."
                ],
                report_types["AR"]
            )

        # 조건2: 10b. 타르색소 종류 및 분량 변경, 1~4, 8, 9 충족 → Cmin
        elif all(r == "충족" for r in [r1, r2, r3, r4, r8, r9]):
            show_result(
                "3.2.P.1 완제의약품의 성상 및 조성\n10. 타르색소 종류 및 분량 변경",
                [
                    "(P.1) 원료약품 분량.",
                    "(P.3) 배치 조성.",
                    "(P.5) 기준 및 시험방법 및 최소 1배치 시험 성적서.",
                    "(P.8.2) 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "(R.1) 제조 관련 문서 변경 없음 확인서."
                ],
                report_types["Cmin"]
            )

        # 조건3: 10c. 타르색소 외 착색제/착향제 변경, 1~3, 5~9 충족 → Cmin
        elif all(r == "충족" for r in [r1, r2, r3, r5, r6, r7, r8, r9]):
            show_result(
                "3.2.P.1 완제의약품의 성상 및 조성\n10. 타르색소 외 착색제 또는 착향제 변경",
                [
                    "(P.1) 원료약품 분량.",
                    "(P.3) 배치 조성.",
                    "(P.2) 성분 조성 및 배합 적합성 자료.",
                    "(P.4) 규격 및 성적서, BSE/TSE 적합성 자료.",
                    "(P.5) 기준 및 시험방법 및 최소 1배치 시험 성적서.",
                    "(P.5.3) 분석 절차 방해 없음 입증 자료.",
                    "(P.8.2) 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "(R.1) 제조 관련 문서 변경 없음 확인서."
                ],
                report_types["Cmin"]
            )
            
    # s3_5: 제조소 추가 또는 변경
    if "s3_5" in selections:
        r1 = selections.get("s3_5_req_1")
        r2 = selections.get("s3_5_req_2")
        r3 = selections.get("s3_5_req_3")
        r4 = selections.get("s3_5_req_4")
        r5 = selections.get("s3_5_req_5")

        # 12a. 이차 포장 제조소이고, 조건 2 충족 → Cmin
        if r2 == "충족":
            show_result(
                "3.2.P.3 제조\n12. 이차 포장 제조소 변경",
                [
                    "해당 제조소의 제조 및 품질관리기준 적합판정서 또는 유효한 제조증명서.",
                    "(P.3.1) 수탁업소 포함 제조원 정보."
                ],
                report_types["Cmin"]
            )

        # 12b.1 일차 포장 제조소(정제, 크림 등) → 조건 2,3,4 충족 → Cmin
        elif all(r == "충족" for r in [r2, r3, r4]):
            show_result(
                "3.2.P.3 제조\n12. 일차 포장 제조소(고형, 반고형, 액상)",
                [
                    "해당 제조소의 제조 및 품질관리기준 적합판정서 또는 유효한 제조증명서.",
                    "(P.3.1) 제조원, 주소, 책임소재 등.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약 (생동성시험 있는 경우 2배치 장기+가속 6개월 자료 포함)."
                ],
                report_types["Cmin"]
            )

        # 12b.2 일차 포장 제조소(유제, 현탁제) → 조건 2,3,4 충족 → Cmaj
        elif all(r == "충족" for r in [r2, r3, r4]):
            show_result(
                "3.2.P.3 제조\n12. 일차 포장 제조소(유제, 현탁제)",
                [
                    "해당 제조소의 제조 및 품질관리기준 적합판정서 또는 유효한 제조증명서.",
                    "(P.3.1) 제조원, 주소, 책임소재 등.",
                    "(P.3.5) 위험도 평가에 따른 3배치 공정 밸리데이션.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약 (생동성시험 있는 경우 2배치 장기+가속 6개월 자료 포함)."
                ],
                report_types["Cmaj"]
            )

        # 12c1. 기타 제조소이고 조건 1,2 충족 → Cmin
        elif r1 == "충족" and r2 == "충족":
            show_result(
                "3.2.P.3 제조\n12. 기타 제조소(조건 1,2 충족)",
                [
                    "제조소의 적합판정서 또는 제조증명서.",
                    "(P.3.1) 제조원 정보.",
                    "(P.2) 제형 특성에 따른 시험자료.",
                    "(P.2 또는 R) 동등성 시험자료.",
                    "(P.3.5) 위험도 평가에 따른 3배치 공정 밸리데이션 계획서.",
                    "(P.5.1) 완제의약품 규격 자료.",
                    "(P.5.4) 최소 1배치 배치분석자료.",
                    "(R.1) 문서 변경 없음 확인서."
                ],
                report_types["Cmin"]
            )

        # 12c1. 기타 제조소이고 조건 1,2,5 충족 → Cmin
        elif all(r == "충족" for r in [r1, r2, r5]):
            show_result(
                "3.2.P.3 제조\n12. 기타 제조소(조건 1,2,5 충족)",
                [
                    "제조소의 적합판정서 또는 제조증명서.",
                    "(P.3.1) 제조원 정보.",
                    "(P.2) 제형 특성에 따른 시험자료.",
                    "(P.3.5) 3배치 공정 밸리데이션 계획서.",
                    "(P.5.1) 완제의약품 규격 자료.",
                    "(P.5.4) 최소 1배치 배치분석자료.",
                    "(R.1) 문서 변경 없음 확인서."
                ],
                report_types["Cmin"]
            )

        # 12c2. 기타 제조소이며 조건 2 충족 → Cmaj
        elif r2 == "충족":
            show_result(
                "3.2.P.3 제조\n12. 기타 제조소(조건 2 충족)",
                [
                    "제조소의 적합판정서 또는 제조증명서.",
                    "(P.3.1) 제조원 정보.",
                    "(P.2) 제형 특성 시험자료.",
                    "(P.2 또는 R) 동등성 시험자료.",
                    "(P.3.5) 3배치 공정 밸리데이션 계획서.",
                    "(P.5.1) 완제의약품 규격.",
                    "(P.5.4) 최소 1배치 배치분석자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약 (생동 시 2배치 장기+가속 6개월 포함).",
                    "(R.1) 제조 관련 문서 변경 없음 확인서."
                ],
                report_types["Cmaj"]
            )
            
    # s3_6: 비무균제제 제조규모 변경
    if "s3_6" in selections:
        r1 = selections.get("s3_6_req_1")
        r2 = selections.get("s3_6_req_2")
        r3 = selections.get("s3_6_req_3")
        r4 = selections.get("s3_6_req_4")
        r5 = selections.get("s3_6_req_5")
        r6 = selections.get("s3_6_req_6")

        # 13a: 10배수 이하 변경, 조건 1~4 충족 → AR
        if all(r == "충족" for r in [r1, r2, r3, r4]):
            show_result(
                "3.2.P.3 제조\n13. 비무균제제 제조규모 변경(10배수 이하)",
                [
                    "(P.3.5) 3배치 공정 밸리데이션 실시보고서 또는 계획서.",
                    "(P.5.4) 최소 1배치 배치분석자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약.",
                    "(R.1) 제조 관련 문서 변경 없음 확인서."
                ],
                report_types["AR"]
            )

        # 13b: 일반 제제, 10배 초과, 조건 1~5 충족 → IR
        elif all(r == "충족" for r in [r1, r2, r3, r4, r5]):
            show_result(
                "3.2.P.3 제조\n13. 비무균제제 제조규모 변경(10배 초과, 일반제제)",
                [
                    "(P.2 또는 R) 제조방법 변경에 따른 동등성 시험자료.",
                    "(P.3.5) 3배치 공정 밸리데이션 실시보고서 또는 계획서.",
                    "(P.5.1) 완제의약품 규격.",
                    "(P.5.4) 최소 1배치 배치분석자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약.",
                    "(R.1) 문서 변경 없음 확인서."
                ],
                report_types["IR"]
            )

        # 13b: 일반 제제, 조건 1,2,3,4,6 충족 → IR
        elif all(r == "충족" for r in [r1, r2, r3, r4, r6]):
            show_result(
                "3.2.P.3 제조\n13. 비무균제제 제조규모 변경(조건 1,2,3,4,6 충족)",
                [
                    "(P.3.5) 3배치 공정 밸리데이션 실시보고서 또는 계획서.",
                    "(P.5.1) 완제의약품 규격.",
                    "(P.5.4) 최소 1배치 배치분석자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약.",
                    "(R.1) 문서 변경 없음 확인서."
                ],
                report_types["IR"]
            )

        # 13c: 특수 제형 또는 반고형 제제, 조건 1~4 충족 → Cmaj
        elif all(r == "충족" for r in [r1, r2, r3, r4]):
            show_result(
                "3.2.P.3 제조\n13. 특수제형 또는 반고형제제 제조규모 변경(10배 초과)",
                [
                    "(P.2 또는 R) 제조방법 변경에 따른 동등성 시험자료.",
                    "(P.3.5) 3배치 공정 밸리데이션 실시보고서 또는 계획서.",
                    "(P.5.1) 완제의약품 규격.",
                    "(P.5.4) 최소 1배치 배치분석자료.",
                    "(P.8.2) 안정성 시험 계획 및 이행서약.",
                    "(R.1) 문서 변경 없음 확인서."
                ],
                report_types["Cmaj"]
            )
            
    # s3_7: 무균제제 제조 규모 변경
    if "s3_7" in selections:
        r1 = selections.get("s3_7_req_1")
        r2 = selections.get("s3_7_req_2")
        r3 = selections.get("s3_7_req_3")
        r4 = selections.get("s3_7_req_4")
        r5 = selections.get("s3_7_req_5")
        r6 = selections.get("s3_7_req_6")

        # 판단조건 1: 1~4 충족 → AR
        if all(r == "충족" for r in [r1, r2, r3, r4]):
            show_result(
                "3.2.P.3 제조\n14. 무균제제의 제조 규모 변경 (1~4 충족)",
                [
                    "1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.",
                    "2. (P.3.5) 공정밸리데이션 또는 무균공정/멸균 공정에 대한 밸리데이션 또는 평가 결과.",
                    "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                    "4. (P.5.4) 최소 1배치에 대한 배치 분석 자료.",
                    "5. (P.8.2) 안정성 시험 계획 및 이행서약."
                ],
                report_types["AR"]
            )

        # 판단조건 2: 1~5 충족 → IR
        elif all(r == "충족" for r in [r1, r2, r3, r4, r5]):
            show_result(
                "3.2.P.3 제조\n14. 무균제제의 제조 규모 변경 (1~5 충족)",
                [
                    "1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.",
                    "2. (P.3.5) 공정밸리데이션 또는 무균공정/멸균 공정에 대한 밸리데이션 또는 평가 결과.",
                    "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                    "4. (P.5.4) 최소 1배치에 대한 배치 분석 자료.",
                    "5. (P.8.2) 안정성 시험 계획 및 이행서약."
                ],
                report_types["IR"]
            )

        # 판단조건 3: 1,2,3,4,6 충족 → Cmaj
        elif all(r == "충족" for r in [r1, r2, r3, r4, r6]):
            show_result(
                "3.2.P.3 제조\n14. 무균제제의 제조 규모 변경 (1,2,3,4,6 충족)",
                [
                    "1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.",
                    "2. (P.3.5) 공정밸리데이션 또는 무균공정/멸균 공정에 대한 밸리데이션 또는 평가 결과.",
                    "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                    "4. (P.5.4) 최소 1배치에 대한 배치 분석 자료.",
                    "5. (P.8.2) 안정성 시험 계획 및 이행서약.",
                    "6. (P.2 또는 R) 제조방법 변경에 따른 의약품동등성시험자료."
                ],
                report_types["Cmaj"]
            )
            
    # s3_8: 완제의약품 제조공정 변경
    if "s3_8" in selections:
        r1 = selections.get("s3_8_req_1")
        r2 = selections.get("s3_8_req_2")
        r3 = selections.get("s3_8_req_3")
        r4 = selections.get("s3_8_req_4")
        r5 = selections.get("s3_8_req_5")
        r6 = selections.get("s3_8_req_6")
        r7 = selections.get("s3_8_req_7")
        r8 = selections.get("s3_8_req_8")
        r9 = selections.get("s3_8_req_9")

        # 판단조건 1: 1~7 충족 → AR
        if all(r == "충족" for r in [r1, r2, r3, r4, r5, r6, r7]):
            show_result(
                "3.2.P.3 제조\n15. 완제의약품의 제조공정 변경 (1~7 충족)",
                [
                    "2. (P.2) 제조공정 개발에 관한 검토자료",
                    "3. (P.3) 제조공정 및 공정관리의 설명 자료",
                    "6. (P.8.2) 안정성 시험 계획 및 이행서약",
                    "7. (R.1) 문서 변경 없음 확인서"
                ],
                report_types["AR"]
            )

        # 판단조건 2: 1~3, 5~8 충족 → IR
        elif all(r == "충족" for r in [r1, r2, r3, r5, r6, r7, r8]):
            show_result(
                "3.2.P.3 제조\n15. 완제의약품의 제조공정 변경 (1~3,5~8 충족)",
                [
                    "1. (P.2 또는 R) 동등성시험자료",
                    "2. (P.2) 제조공정 검토자료",
                    "3. (P.3) 제조공정 및 공정관리 설명",
                    "4. (P.5) 생산규모 배치 성적서",
                    "5. (P.8.1) 최소 2배치 3개월 안정성시험",
                    "6. (P.8.2) 안정성 시험 계획 및 이행서약",
                    "7. (R.1) 문서 변경 없음 확인서"
                ],
                report_types["IR"]
            )

        # 판단조건 3: 1~3, 5~9 충족 → IR
        elif all(r == "충족" for r in [r1, r2, r3, r5, r6, r7, r8, r9]):
            show_result(
                "3.2.P.3 제조\n15. 완제의약품의 제조공정 변경 (1~3,5~9 충족)",
                [
                    "2. (P.2) 제조공정 검토자료",
                    "3. (P.3) 제조공정 및 공정관리 설명",
                    "4. (P.5) 생산규모 배치 성적서",
                    "5. (P.8.1) 최소 2배치 3개월 안정성시험",
                    "6. (P.8.2) 안정성 시험 계획 및 이행서약",
                    "7. (R.1) 문서 변경 없음 확인서"
                ],
                report_types["IR"]
            )

        # 판단조건 4: 전부 미충족 → Cmaj
        elif all(r == "미충족" for r in [r1, r2, r3, r4, r5, r6, r7, r8, r9]):
            show_result(
                "3.2.P.3 제조\n15. 완제의약품의 제조공정 변경 (전부 미충족)",
                [
                    "2. (P.2) 제조공정 검토자료",
                    "3. (P.3) 제조공정 및 공정관리 설명",
                    "4. (P.5) 생산규모 배치 성적서",
                    "5. (P.8.1) 최소 2배치 3개월 이상 안정성시험",
                    "6. (P.8.2) 안정성 시험 계획 및 이행서약",
                    "7. (R.1) 문서 변경 없음 확인서"
                ],
                report_types["Cmaj"]
            )

    if "s3_9" in selections:
        r1 = selections.get("s3_9_req_1")
        r2 = selections.get("s3_9_req_2")
        r3 = selections.get("s3_9_req_3")
        r4 = selections.get("s3_9_req_4")

        # 16a. 공정관리시험 기준 변경 - 1, 2, 4 충족 → AR
        if all(r == "충족" for r in [r1, r2, r4]):
            show_result(
                "3.2.P.3 제조\n16. 공정관리시험 또는 IPC 변경 (16a 조건)",
                [
                    "2. (P.3.3/P.3.4) 공정 중 시험 규격 비교표"
                ],
                report_types["AR"]
            )

        # 16b. 공정관리시험 기준 변경(Cmaj) - 2 충족 → Cmaj
        elif r2 == "충족" and all(selections.get(k) != "충족" for k in ["s3_9_req_1", "s3_9_req_3", "s3_9_req_4"]):
            show_result(
                "3.2.P.3 제조\n16. 공정관리시험 또는 IPC 변경 (16b 조건)",
                [
                    "1. (P.2 또는 R) 동등성시험자료",
                    "2. (P.3.3/P.3.4) 시험 규격 비교표",
                    "3. 새로운 시험방법 자료",
                    "4. 밸리데이션 보고서 또는 요약문",
                    "5. 최소 1배치 시험성적 비교자료",
                    "6. 타당성 입증 자료"
                ],
                report_types["Cmaj"]
            )

        # 16c. 시험 항목 삭제 - 2, 3 충족 → AR
        elif r2 == "충족" and r3 == "충족":
            show_result(
                "3.2.P.3 제조\n16. 시험 항목 삭제 (16c 조건)",
                [
                    "6. 타당성 입증 자료"
                ],
                report_types["AR"]
            )

        # 16d. 시험 기준 추가 - 2 충족 → AR
        elif r2 == "충족" and all(selections.get(k) != "충족" for k in ["s3_9_req_1", "s3_9_req_3", "s3_9_req_4"]):
            show_result(
                "3.2.P.3 제조\n16. 시험 기준 추가 (16d 조건)",
                [
                    "2. (P.3.3/P.3.4) 시험 규격 비교표",
                    "3. 새로운 시험방법 자료",
                    "4. 밸리데이션 보고서 또는 요약문",
                    "5. 최소 1배치 시험성적 비교자료",
                    "6. 타당성 입증 자료"
                ],
                report_types["AR"]
            )
            
    if "s3_10" in selections:
        r1 = selections.get("s3_10_req_1")

        # 17a. 동물성→식물 or 합성 / 1 충족 → AR
        if r1 == "충족":
            show_result(
                "3.2.P.4 첨가제의 관리\n17. 첨가제 기원의 변경 (17a 조건)",
                [
                    "1. 첨가제가 식물 또는 합성 기원임을 입증하는 제조업자의 확인서"
                ],
                report_types["AR"]
            )

        # 17b. 식물 또는 합성 → 동물성 / 모든 요건 미충족 → Cmin
        elif all(v == "미충족" for k, v in selections.items() if k.startswith("s3_10_req_") and k != "s3_10_req_1"):
            show_result(
                "3.2.P.4 첨가제의 관리\n17. 첨가제 기원의 변경 (17b 조건)",
                [
                    "2. (P.4) 첨가제 기준 및 시험방법 자료",
                    "3. (A.2) 외인성 물질에 대한 안전성 평가 자료(필요 시)",
                    "4. 변경 전후 첨가제 규격 및 성적서"
                ],
                report_types["Cmin"]
            )
            
    if "s3_11" in selections:
        r1 = selections.get("s3_11_req_1")

        # 18. 별규 시험방법 변경 / 1 충족 → Cmin
        if r1 == "충족":
            show_result(
                "3.2.P.4 첨가제의 관리\n18. 별규 첨가제 시험방법 변경",
                [
                    "1. 타당성 입증 자료",
                    "2. 변경 전후 규격 비교표, 시험방법 및 밸리데이션 자료"
                ],
                report_types["Cmin"]
            )
            
    if "s3_12" in selections:
        r1 = selections.get("s3_12_req_1")

        # 19. 공정서 규격으로 변경 / 1 충족 → AR
        if r1 == "충족":
            show_result(
                "3.2.P.4 첨가제의 관리\n19. 공정서 규격으로 변경",
                [
                    "1. 첨가제 규격 비교표 등 변경 전후 자료"
                ],
                report_types["AR"]
            )
            
    if "s4_1" in selections:
        cond_met = [v == "충족" for k, v in selections.items() if k.startswith("s4_1_req_")]
        if any(cond_met):
            show_result(
                "3.2.P.7 용기-마개 시스템\n20. 비무균제제 포장재 변경 - 조건 충족",
                [
                    "1. 의약품 성상",
                    "2. 포장 적합성 및 보호성 자료",
                    "3. 제조방법 자료",
                    "4. 포장 구성 정보",
                    "6. 안정성 시험 계획 및 이행서약"
                ],
                report_types["IR"]
            )
        else:
            show_result(
                "3.2.P.7 용기-마개 시스템\n20. 비무균제제 포장재 변경 - 조건 미충족",
                [
                    "1. 의약품 성상",
                    "2. 포장 적합성 및 보호성 자료",
                    "3. 제조방법 자료",
                    "4. 포장 구성 정보",
                    "5. 안정성 시험 자료 (3개월 이상)",
                    "6. 안정성 시험 계획 및 이행서약"
                ],
                report_types["Cmaj"]
            )
            
    if "s4_2" in selections:
        cond_met = [v == "충족" for k, v in selections.items() if k.startswith("s4_2_req_")]
        if any(cond_met):
            show_result(
                "3.2.P.7 용기-마개 시스템\n21. 무균제제 포장재 변경 - 조건 충족",
                [
                    "1. 의약품 성상",
                    "2. 포장 적합성 자료",
                    "3. 제조방법 자료",
                    "4. 포장 구성 정보",
                    "5. 장기보존 및 가속 시험 자료 (3개월 이상)",
                    "7. 안정성 시험 계획 및 이행서약"
                ],
                report_types["Cmin"]
            )
        else:
            show_result(
                "3.2.P.7 용기-마개 시스템\n21. 무균제제 포장재 변경 - 조건 미충족",
                [
                    "1. 의약품 성상",
                    "2. 포장 적합성 자료",
                    "3. 제조방법 자료",
                    "4. 포장 구성 정보",
                    "6. 장기보존 및 가속 시험 자료 (6개월 이상, 파일럿 배치 포함)",
                    "7. 안정성 시험 계획 및 이행서약"
                ],
                report_types["Cmaj"]
            )
            
    if "s4_3" in selections:
        r1 = selections.get("s4_3_req_1")
        r2 = selections.get("s4_3_req_2")

        if r1 == "충족" and r2 == "충족":
            show_result(
                "3.2.P.7 용기-마개 시스템\n22. 직접포장 규격 변경 (기준 강화 및 시험 항목 변경)",
                [
                    "1. 규격 비교표 등 자료",
                    "2. 시험방법 자료"
                ],
                report_types["AR"]
            )
        elif r1 == "충족":
            show_result(
                "3.2.P.7 용기-마개 시스템\n22. 직접포장 규격 변경 (기준 강화)",
                [
                    "1. 규격 비교표 등 자료"
                ],
                report_types["AR"]
            )
        elif r2 == "충족":
            show_result(
                "3.2.P.7 용기-마개 시스템\n22. 직접포장 규격 변경 (시험 항목 변경)",
                [
                    "1. 규격 비교표 등 자료",
                    "2. 시험방법 자료"
                ],
                report_types["AR"]
            )
            
    if "s4_4" in selections:
        r1 = selections.get("s4_4_req_1")
        r2 = selections.get("s4_4_req_2")

        if r1 == "충족" and r2 == "충족":
            show_result(
                "3.2.P.7 용기-마개 시스템\n23. 포장단위 변경",
                [
                    "1. 포장단위 비교표 등 변경 전후 자료"
                ],
                report_types["IR"]
            )
            
    if "s4_5" in selections:
        show_result(
            "3.2.P.7 용기-마개 시스템\n24. 디자인스페이스 도입 또는 확장 (제조공정 변경 포함)",
            [
                "1. 디자인스페이스 타당성 입증자료",
                "2. 디자인스페이스 설명 자료(표 형식)",
                "3. CTD 관련 변경 신청서류"
            ],
            report_types["Cmaj"]
        )

    if "s4_6" in selections:
        show_result(
            "3.2.P.7 용기-마개 시스템\n24. 디자인스페이스 도입 또는 확장 (시험방법 변경 포함)",
            [
                "1. 디자인스페이스 타당성 입증자료",
                "2. 디자인스페이스 설명 자료(표 형식)",
                "3. CTD 관련 변경 신청서류"
            ],
            report_types["Cmaj"]
        )
        
    col1, col2 = st.columns(2)
    with col1:
        st.button("이전단계로", on_click=lambda: st.session_state.update(step=6))
    with col2:
        st.button("신청서 출력", on_click=lambda: st.session_state.update(step=8))

# STEP 8: 신청양식 PDF 출력용 결과 페이지
# Step7의 도출 결과를 기반으로, 각 변경유형에 대해 보고유형 및 필요서류를 종합 정리하여 PDF 생성/출력 기능 제공

import streamlit as st
from fpdf import FPDF
import os
import uuid

if "step" not in st.session_state:
    st.session_state.step = 7

if "step7_results" not in st.session_state:
    st.session_state.step7_results = [
        {
            "title": "3.2.S.1 일반정보\n1. 원료의약품 명칭변경",
            "change_type": "1. 원료의약품 명칭변경",
            "required_docs": [
                "(S.1.1) 공정서 또는 국제 의약품 일반명 리스트〔The International Nonproprietary Name(INN)〕 등 근거서류.",
                "개정된 제품정보."
            ],
            "report_type": "AR, 연차보고\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 제2항 및 제4항에 따른 연차보고(Annual Report, AR) 수준의 변경사항입니다."
        }
    ]

def go_back_to_step7():
    st.session_state.step = 7

def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="의약품 제조방법 변경에 따른 신청양식", ln=True, align='C')
    pdf.ln(10)

    for idx, item in enumerate(data, 1):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt=f"{idx}. 변경유형: {item['change_type']}", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 8, f"1. 필요서류:")
        for doc in item['required_docs']:
            pdf.multi_cell(0, 8, f"  - {doc}")
        pdf.ln(1)
        pdf.multi_cell(0, 8, f"2. 보고유형:\n{item['report_type']}")
        pdf.ln(10)

    # 파일 저장
    filename = f"/mnt/data/신청양식_{uuid.uuid4().hex}.pdf"
    pdf.output(filename)
    return filename

if st.session_state.step == 8:
    st.markdown("## Step 8")
    st.write("Step 8. 제조방법 변경에 따른 신청양식이 아래와 같이 자동으로 생성되었습니다.")

    for idx, result in enumerate(st.session_state.step7_results, 1):
        st.markdown(f"### {idx}. {result['change_type']}")
        st.markdown("**1. 필요서류:**")
        for doc in result['required_docs']:
            st.write(f"- {doc}")
        st.markdown("**2. 보고유형:**")
        st.write(result['report_type'])

    if st.button("PDF로 생성 및 다운로드하기"):
        pdf_path = generate_pdf(st.session_state.step7_results)
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="PDF 파일 다운로드하기",
                data=f,
                file_name=os.path.basename(pdf_path),
                mime="application/pdf"
            )

    st.markdown("---")
    st.button("이전단계로", on_click=go_back_to_step7)

        