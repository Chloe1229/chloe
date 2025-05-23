import streamlit as st

# ===== 초기 상태 정의 =====
if "step" not in st.session_state:
    st.session_state.step = 1

if "step1_answer" not in st.session_state:
    st.session_state.step1_answer = None
if "step2_answer" not in st.session_state:
    st.session_state.step2_answer = None
if "step3_answer" not in st.session_state:
    st.session_state.step3_answer = None

if "step4_selections" not in st.session_state:
    st.session_state.step4_selections = {}

if "step5_targets" not in st.session_state:
    st.session_state.step5_targets = []

# ===== Step1 함수 및 화면 =====
def go_to_step2():
    if st.session_state.step1_answer == "예":
        st.session_state.step = 2

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

# ===== Step2 함수 및 화면 =====
def go_to_step3():
    if st.session_state.step2_answer == "예":
        st.session_state.step = 3

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

# ===== Step3 함수 및 화면 =====
def go_to_step4():
    if st.session_state.step3_answer == "예":
        st.session_state.step = 4

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

# Step 4 상태 초기화
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

# ===== Step5 상태 초기화 =====
if "step5_selections" not in st.session_state:
    st.session_state.step5_selections = {}
if "step6_targets" not in st.session_state:
    st.session_state.step6_targets = []

# ===== Step5 항목 정의 (전체 하드코딩) =====
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
            "24": "24. 디자인스페이스(Design Space) 변경"
        }
    }
}

# ===== Step 간 이동 함수 =====
def go_to_step6():
    st.session_state.step6_targets = [
        key for key, val in st.session_state.step5_selections.items() if val == "변경 있음"
    ]
    st.session_state.step = 6

def go_back_to_step4():
    st.session_state.step = 4

# ===== Step5 화면 =====
if st.session_state.step == 5:
    st.markdown("## Step 5")
    st.write("Step 5. 선택한 변경항목 중 변경사항을 선택하세요.")

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

    all_selected = all(
        v in ["변경 있음", "변경 없음"]
        for k, v in st.session_state.step5_selections.items()
        if not k.startswith("ds_")
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button("이전단계로", on_click=go_back_to_step4)
    with col2:
        st.button("다음단계로", on_click=go_to_step6, disabled=not all_selected)

if "step6_selections" not in st.session_state:
    st.session_state.step6_selections = {}

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
    },
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
    },
    "p1_7": {
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
    "p1_8": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n8. 고형제제의 코팅층 무게 변경",
        "subitems": {},
        "requirements": {}
    },
    "p1_9": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n9. 완제의약품(고형제제 제외)의 조성 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 시럽제, 엘릭서제, 틴크제 등 경구용 액제 및 외용액제(유제 및 현탁제 제외)",
            "2": "2. 주사제, 점안제, 점이제로 원료약품의 종류가 이미 허가·신고사항과 동일하거나 다음의 첨가제가 다른 경우 : 「의약품의 품목허가·신고·심사 규정」 제27조제3항제2호에 따라 주사제는 보존제, 완충제, 항산화제, pH조절제(이미 허가·신고된 바있는 주사제에 사용된 pH조절제에 한함), 점안제 및 점이제는 보존제, 완충제, 등장화제, 점도조절제, pH조절제.",
            "3": "3. 흡입 전신마취제",
            "4": "4. 국소적용 외용제제로서 원료약품 종류 동일하고, 첨가제가 다른 경우",
            "5": "5. 유효성분을 기체나 증기 형태로 흡입하는 국소요법 제제",
            "6": "6. 수액제, 혈액증량제 및 인공관류액 제제",
            "7": "7. 폐에 적용하는 흡입제",
            "8": "8. 위 충족조건에 포함되지 않는 경우",
            "9": "9. 첨가제는 새로운 첨가제가 아니다."
        }
    },
    "p1_10": {
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
    "p3_11": {
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
    "p3_12": {
        "title": "3.2.P.3 제조\n12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
        "subitems": {
            "12a": "12a. 이차 포장 제조소",
            "12b1": "12b.1. 일차 포장 제조소 – 고형(정제, 캡슐제), 반고형(연고제, 크림제) 및 액상 제제",
            "12b2": "12b.2. 일차 포장 제조소 – 그 밖의 액상 제제(유제, 현탁제)",
            "12c1": "12c1. 원료칭량 공정 및 완제품 포장공정 제조소를 제외한 그 밖의 모든 제조소",
            "12c2": "12c2. 원료칭량 공정 및 완제품 포장공정 제조소를 제외한 그 밖의 모든 제조소"
        },
        "requirements": {
            "1": "1. 배치 조성, 제조 공정 및 공정 관리의 기록 사항, 장비 등급 및 공정 관리, 주요 공정 및 반제품의 관리 또는 완제의약품 규격에 있어서 변경이 없다.",
            "2": "2. (해당하는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서가 있거나, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서가 있다.",
            "3": "3. 무균제제가 아니다.",
            "4": "4. 포장 재질의 변경이 없다.",
            "5": "5. 액상제제(경구용 액제, 주사제, 점안제, 점이제 등), 폐에 적용하는 흡입제 및 반고형제제에 해당한다. (유제 및 현탁제 제외)"
        }
    },
    "p3_13": {
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
    "p3_14": {
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
    "p3_15": {
        "title": "3.2.P.3 제조\n15. 완제의약품의 제조공정 변경",
        "subitems": {
            "15a": "15a. 완제의약품의 제조공정 변경",
            "15b": "15b. 완제의약품의 제조공정 변경(예 : 용출에 영향을 주는 첨가제 등급 변경, 결합액의 용매 양 변경, 용출에 영향을 주는 첨가제의 투입순서 변경, 코팅액의 용매 변경 등)",
            "15c": "15c. 완제의약품의 제조공정 변경(예 :결합액의 용매 종류 변경 등)"
        },
        "requirements": {
            "1": "1. 불순물 프로파일의 변경이 없고 물리 화학적 성질에 변경이 없다. 용출 프로파일은 대조약 배치의 프로파일과 유사하다.",
            "2": "2. 변경 전·후 제제의 제조공정은 동일한 원리이고 반제품은 동일하며, 공정에 사용되는 제조 용매에는 변경이 없다(습식 조립법에서 건식 조립법으로의 변경, 직접 분말 압축법에서 습식 또는 건식 과립 압축법으로의 변경, 또는 그 반대로의 변경은 제조 원리의 변경으로 간주된다).",
            "3": "3. 변경 전·후 작동원리가 같은 동일 계열의 제조장비를 사용한다.(제조장비의 작동원리 및 디자인의 동일 여부는 [부록 1], [부록 2]를 참고한다.)",
            "4": "4. 완제의약품의 품질에 영향을 미치는 제조공정(주요공정) 조건의 변동이 없다.",
            "5": "5. 반제품 또는 완제의약품의 규격 변경은 없다.",
            "6": "6. 제조 중에 발생하는 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제 때문에 발생한 변경은 아니다.",
            "7": "7. 해당 변경은 계량 및/또는 전달 기능을 제공하는 일차 포장과 관련된 포장이나 라벨링 공정을 포함하지 않는다.",
            "8": "8. 일반제제에 해당한다(장용성 및 방출조절제제, 서방성제제 등 제형의 특수성이 인정되는 제제 제외).",
            "9": "9. 액상제제(경구용 액제, 주사제, 점안제, 점이제 등)에 해당한다."
        }
    },
    "p3_16": {
        "title": "3.2.P.3 제조\n16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
        "subitems": {
            "16a": "16a. 공정관리시험 기준의 변경",
            "16b": "16b. 공정관리시험 기준의 변경",
            "16c": "16c. 공정관리시험 항목의 삭제",
            "16d": "16d. 새로운 공정관리시험 기준의 추가",
            "16e": "16e. 공정관리시험 방법의 변경"
        },
        "requirements": {
            "1": "1. 해당 변경은 공정관리 기준(예, 마손도, 경도, 입도, 밀도, 수분 등) 범위 내에 있다.",
            "2": "2. 해당 변경은 제조 중에 발생하는 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제로 인하여 필요로 하는 것이 아니다.",
            "3": "3. 삭제된 공정관리 항목은 불필요하거나 생략 가능한 것으로 입증되었으며, 제제의 주요 품질 특성(예: 혼합균일성, 질량편차)에 미치는 영향이 없거나 적다.",
            "4": "4. 시험방법에는 변경이 없다."
        }
    },
    "p4_17": {
        "title": "3.2.P.4 첨가제의 관리\n17. 첨가제 기원의 변경",
        "subitems": {
            "17a": "17a. 동물성 기원 → 식물 또는 합성 기원",
            "17b": "17b. 식물 또는 합성 기원 → 동물성 기원 또는 다른 동물성 기원"
        },
        "requirements": {
            "1": "1. 첨가제와 완제의약품의 규격에는 변경이 없다."
        }
    },
    "p4_18": {
        "title": "3.2.P.4 첨가제의 관리\n18. 별규에 해당하는 첨가제의 규격 또는 시험방법 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 해당 변경은 제조 과정 중 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제로 인해 발생한 변경이 아니다."
        }
    },
    "p4_19": {
        "title": "3.2.P.4 첨가제의 관리\n19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 공정서를 준수하기 위해 요구되는 규격 이외에는 변경이 없다. (예: 입자 크기 분포의 변경 없음)"
        }
    },
    "p7_20": {
        "title": "3.2.P.7 용기-마개 시스템\n20. 비무균제제의 직접용기 및 포장 재질, 종류 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 고형제제로서 주성분, 제형, 투여경로가 동일한 기허가 의약품에서 사용례가 확인되는 용기 재질로의 변경 또는 동일한 종류/보호성 동등 이상인 재질로의 변경이며, 사용기간은 기허가의약품 사용기간을 초과하지 않는다."
        }
    },
    "p7_21": {
        "title": "3.2.P.7 용기-마개 시스템\n21. 무균제제의 직접용기 및 포장 재질, 종류 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 변경 후 용기의 보호성 등이 동등 이상이고 상호작용 위험이 없다."
        }
    },
    "p7_22": {
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
    "p7_23": {
        "title": "3.2.P.7 용기-마개 시스템\n23. 포장단위 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 해당 변경은 제조 과정에서 발생하는 예기치 않은 사례로 인한 규격 미충족 혹은 안정성 문제 때문에 발생한 변경이 아니다.",
            "2": "2. 이외 허가사항의 변경은 없다."
        }
    },
    "ds_24": {
        "title": "3.2.P.7 용기-마개 시스템\n24. 새로운 디자인스페이스 도입 또는 허가된 디자인스페이스의 확장",
        "subitems": {},
        "requirements": {}
    }
}

if "step6_selections" not in st.session_state:
    st.session_state.step6_selections = {}

if "step6_page" not in st.session_state:
    st.session_state.step6_page = 0

def go_to_prev_step6_page():
    if st.session_state.step6_page > 0:
        st.session_state.step6_page -= 1

def go_to_next_step6_page():
    if st.session_state.step6_page < len(st.session_state.step6_targets) - 1:
        st.session_state.step6_page += 1

def go_back_to_step5():
    st.session_state.step = 5

def go_to_step7():
    st.session_state.step = 7

if st.session_state.step == 6:
    st.markdown("## Step 6")
    st.write("Step 6. Step5에서 '변경 있음'으로 선택된 항목에 대해 하위항목과 충족요건을 모두 선택하세요.")

    targets = st.session_state.step6_targets
    if not targets:
        st.warning("Step5에서 선택된 항목이 없습니다.")
    else:
        current_key = targets[st.session_state.step6_page]
        block = step6_items.get(current_key)

        if block:
            st.markdown(f"### {block['title']}")

            # 자동 동기화 쌍 정의
            sync_pairs = {
                "12c1": "12c2",
                "12c2": "12c1",
                "16a": "16b",
                "16b": "16a",
            }

            # 하위항목
            for sub_key, sub_text in block.get("subitems", {}).items():
                full_key = f"{current_key}_sub_{sub_key}"

                if current_key == "p3_15":
                    st.session_state.step6_selections[full_key] = "변경 있음"
                    st.radio(sub_text, ["변경 있음"], index=0, key=full_key, disabled=True)

                elif sub_key in sync_pairs:
                    other = sync_pairs[sub_key]
                    other_key = f"{current_key}_sub_{other}"

                    current_value = st.session_state.step6_selections.get(full_key, "변경 없음")
                    current_value = st.radio(
                        sub_text,
                        ["변경 있음", "변경 없음"],
                        key=full_key,
                        index=0 if current_value == "변경 있음" else 1
                    )

                    st.session_state.step6_selections[full_key] = current_value
                    st.session_state.step6_selections[other_key] = current_value

                else:
                    st.session_state.step6_selections[full_key] = st.radio(
                        sub_text,
                        ["변경 있음", "변경 없음"],
                        key=full_key
                    )

            # 충족요건
            for req_key, req_text in block.get("requirements", {}).items():
                full_key = f"{current_key}_req_{req_key}"
                label = f"{req_key}. {req_text}"
                st.session_state.step6_selections[full_key] = st.radio(
                    label,
                    ["충족", "미충족"],
                    key=full_key
                )

        else:
            st.warning("해당 항목 정보를 찾을 수 없습니다.")

        # 하단 버튼 영역
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                "이전단계로",
                on_click=go_back_to_step5 if st.session_state.step6_page == 0 else go_to_prev_step6_page
            )
        with col2:
            if st.session_state.step6_page == len(st.session_state.step6_targets) - 1:
                st.button("결과 확인하기", on_click=go_to_step7)
            else:
                st.button("다음항목 선택하기", on_click=go_to_next_step6_page)

import streamlit as st

# ===== 초기 상태 정의 =====
if "step" not in st.session_state:
    st.session_state.step = 1

if "step1_answer" not in st.session_state:
    st.session_state.step1_answer = None
if "step2_answer" not in st.session_state:
    st.session_state.step2_answer = None
if "step3_answer" not in st.session_state:
    st.session_state.step3_answer = None

if "step4_selections" not in st.session_state:
    st.session_state.step4_selections = {}

if "step5_targets" not in st.session_state:
    st.session_state.step5_targets = []

# ===== Step1 함수 및 화면 =====
def go_to_step2():
    if st.session_state.step1_answer == "예":
        st.session_state.step = 2

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

# ===== Step2 함수 및 화면 =====
def go_to_step3():
    if st.session_state.step2_answer == "예":
        st.session_state.step = 3

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

# ===== Step3 함수 및 화면 =====
def go_to_step4():
    if st.session_state.step3_answer == "예":
        st.session_state.step = 4

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

# Step 4 상태 초기화
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

# ===== Step5 상태 초기화 =====
if "step5_selections" not in st.session_state:
    st.session_state.step5_selections = {}
if "step6_targets" not in st.session_state:
    st.session_state.step6_targets = []

# ===== Step5 항목 정의 (전체 하드코딩) =====
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
            "24": "24. 디자인스페이스(Design Space) 변경"
        }
    }
}

# ===== Step 간 이동 함수 =====
def go_to_step6():
    st.session_state.step6_targets = [
        key for key, val in st.session_state.step5_selections.items() if val == "변경 있음"
    ]
    st.session_state.step = 6

def go_back_to_step4():
    st.session_state.step = 4

# ===== Step5 화면 =====
if st.session_state.step == 5:
    st.markdown("## Step 5")
    st.write("Step 5. 선택한 변경항목 중 변경사항을 선택하세요.")

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

    all_selected = all(
        v in ["변경 있음", "변경 없음"]
        for k, v in st.session_state.step5_selections.items()
        if not k.startswith("ds_")
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button("이전단계로", on_click=go_back_to_step4)
    with col2:
        st.button("다음단계로", on_click=go_to_step6, disabled=not all_selected)

if "step6_selections" not in st.session_state:
    st.session_state.step6_selections = {}

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
    },
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
    },
    "p1_7": {
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
    "p1_8": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n8. 고형제제의 코팅층 무게 변경",
        "subitems": {},
        "requirements": {}
    },
    "p1_9": {
        "title": "3.2.P.1 완제의약품의 성상 및 조성\n9. 완제의약품(고형제제 제외)의 조성 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 시럽제, 엘릭서제, 틴크제 등 경구용 액제 및 외용액제(유제 및 현탁제 제외)",
            "2": "2. 주사제, 점안제, 점이제로 원료약품의 종류가 이미 허가·신고사항과 동일하거나 다음의 첨가제가 다른 경우 : 「의약품의 품목허가·신고·심사 규정」 제27조제3항제2호에 따라 주사제는 보존제, 완충제, 항산화제, pH조절제(이미 허가·신고된 바있는 주사제에 사용된 pH조절제에 한함), 점안제 및 점이제는 보존제, 완충제, 등장화제, 점도조절제, pH조절제.",
            "3": "3. 흡입 전신마취제",
            "4": "4. 국소적용 외용제제로서 원료약품 종류 동일하고, 첨가제가 다른 경우",
            "5": "5. 유효성분을 기체나 증기 형태로 흡입하는 국소요법 제제",
            "6": "6. 수액제, 혈액증량제 및 인공관류액 제제",
            "7": "7. 폐에 적용하는 흡입제",
            "8": "8. 위 충족조건에 포함되지 않는 경우",
            "9": "9. 첨가제는 새로운 첨가제가 아니다."
        }
    },
    "p1_10": {
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
    "p3_11": {
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
    "p3_12": {
        "title": "3.2.P.3 제조\n12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
        "subitems": {
            "12a": "12a. 이차 포장 제조소",
            "12b1": "12b.1. 일차 포장 제조소 – 고형(정제, 캡슐제), 반고형(연고제, 크림제) 및 액상 제제",
            "12b2": "12b.2. 일차 포장 제조소 – 그 밖의 액상 제제(유제, 현탁제)",
            "12c1": "12c1. 원료칭량 공정 및 완제품 포장공정 제조소를 제외한 그 밖의 모든 제조소",
            "12c2": "12c2. 원료칭량 공정 및 완제품 포장공정 제조소를 제외한 그 밖의 모든 제조소"
        },
        "requirements": {
            "1": "1. 배치 조성, 제조 공정 및 공정 관리의 기록 사항, 장비 등급 및 공정 관리, 주요 공정 및 반제품의 관리 또는 완제의약품 규격에 있어서 변경이 없다.",
            "2": "2. (해당하는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서가 있거나, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서가 있다.",
            "3": "3. 무균제제가 아니다.",
            "4": "4. 포장 재질의 변경이 없다.",
            "5": "5. 액상제제(경구용 액제, 주사제, 점안제, 점이제 등), 폐에 적용하는 흡입제 및 반고형제제에 해당한다. (유제 및 현탁제 제외)"
        }
    },
    "p3_13": {
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
    "p3_14": {
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
    "p3_15": {
        "title": "3.2.P.3 제조\n15. 완제의약품의 제조공정 변경",
        "subitems": {
            "15a": "15a. 완제의약품의 제조공정 변경",
            "15b": "15b. 완제의약품의 제조공정 변경(예 : 용출에 영향을 주는 첨가제 등급 변경, 결합액의 용매 양 변경, 용출에 영향을 주는 첨가제의 투입순서 변경, 코팅액의 용매 변경 등)",
            "15c": "15c. 완제의약품의 제조공정 변경(예 :결합액의 용매 종류 변경 등)"
        },
        "requirements": {
            "1": "1. 불순물 프로파일의 변경이 없고 물리 화학적 성질에 변경이 없다. 용출 프로파일은 대조약 배치의 프로파일과 유사하다.",
            "2": "2. 변경 전·후 제제의 제조공정은 동일한 원리이고 반제품은 동일하며, 공정에 사용되는 제조 용매에는 변경이 없다(습식 조립법에서 건식 조립법으로의 변경, 직접 분말 압축법에서 습식 또는 건식 과립 압축법으로의 변경, 또는 그 반대로의 변경은 제조 원리의 변경으로 간주된다).",
            "3": "3. 변경 전·후 작동원리가 같은 동일 계열의 제조장비를 사용한다.(제조장비의 작동원리 및 디자인의 동일 여부는 [부록 1], [부록 2]를 참고한다.)",
            "4": "4. 완제의약품의 품질에 영향을 미치는 제조공정(주요공정) 조건의 변동이 없다.",
            "5": "5. 반제품 또는 완제의약품의 규격 변경은 없다.",
            "6": "6. 제조 중에 발생하는 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제 때문에 발생한 변경은 아니다.",
            "7": "7. 해당 변경은 계량 및/또는 전달 기능을 제공하는 일차 포장과 관련된 포장이나 라벨링 공정을 포함하지 않는다.",
            "8": "8. 일반제제에 해당한다(장용성 및 방출조절제제, 서방성제제 등 제형의 특수성이 인정되는 제제 제외).",
            "9": "9. 액상제제(경구용 액제, 주사제, 점안제, 점이제 등)에 해당한다."
        }
    },
    "p3_16": {
        "title": "3.2.P.3 제조\n16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
        "subitems": {
            "16a": "16a. 공정관리시험 기준의 변경",
            "16b": "16b. 공정관리시험 기준의 변경",
            "16c": "16c. 공정관리시험 항목의 삭제",
            "16d": "16d. 새로운 공정관리시험 기준의 추가",
            "16e": "16e. 공정관리시험 방법의 변경"
        },
        "requirements": {
            "1": "1. 해당 변경은 공정관리 기준(예, 마손도, 경도, 입도, 밀도, 수분 등) 범위 내에 있다.",
            "2": "2. 해당 변경은 제조 중에 발생하는 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제로 인하여 필요로 하는 것이 아니다.",
            "3": "3. 삭제된 공정관리 항목은 불필요하거나 생략 가능한 것으로 입증되었으며, 제제의 주요 품질 특성(예: 혼합균일성, 질량편차)에 미치는 영향이 없거나 적다.",
            "4": "4. 시험방법에는 변경이 없다."
        }
    },
    "p4_17": {
        "title": "3.2.P.4 첨가제의 관리\n17. 첨가제 기원의 변경",
        "subitems": {
            "17a": "17a. 동물성 기원 → 식물 또는 합성 기원",
            "17b": "17b. 식물 또는 합성 기원 → 동물성 기원 또는 다른 동물성 기원"
        },
        "requirements": {
            "1": "1. 첨가제와 완제의약품의 규격에는 변경이 없다."
        }
    },
    "p4_18": {
        "title": "3.2.P.4 첨가제의 관리\n18. 별규에 해당하는 첨가제의 규격 또는 시험방법 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 해당 변경은 제조 과정 중 예기치 않은 사례로 인한 규격 미충족 또는 안정성 문제로 인해 발생한 변경이 아니다."
        }
    },
    "p4_19": {
        "title": "3.2.P.4 첨가제의 관리\n19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 공정서를 준수하기 위해 요구되는 규격 이외에는 변경이 없다. (예: 입자 크기 분포의 변경 없음)"
        }
    },
    "p7_20": {
        "title": "3.2.P.7 용기-마개 시스템\n20. 비무균제제의 직접용기 및 포장 재질, 종류 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 고형제제로서 주성분, 제형, 투여경로가 동일한 기허가 의약품에서 사용례가 확인되는 용기 재질로의 변경 또는 동일한 종류/보호성 동등 이상인 재질로의 변경이며, 사용기간은 기허가의약품 사용기간을 초과하지 않는다."
        }
    },
    "p7_21": {
        "title": "3.2.P.7 용기-마개 시스템\n21. 무균제제의 직접용기 및 포장 재질, 종류 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 변경 후 용기의 보호성 등이 동등 이상이고 상호작용 위험이 없다."
        }
    },
    "p7_22": {
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
    "p7_23": {
        "title": "3.2.P.7 용기-마개 시스템\n23. 포장단위 변경",
        "subitems": {},
        "requirements": {
            "1": "1. 해당 변경은 제조 과정에서 발생하는 예기치 않은 사례로 인한 규격 미충족 혹은 안정성 문제 때문에 발생한 변경이 아니다.",
            "2": "2. 이외 허가사항의 변경은 없다."
        }
    },
    "ds_24": {
        "title": "3.2.P.7 용기-마개 시스템\n24. 새로운 디자인스페이스 도입 또는 허가된 디자인스페이스의 확장",
        "subitems": {},
        "requirements": {}
    }
}

if "step6_selections" not in st.session_state:
    st.session_state.step6_selections = {}

if "step6_page" not in st.session_state:
    st.session_state.step6_page = 0

def go_to_prev_step6_page():
    if st.session_state.step6_page > 0:
        st.session_state.step6_page -= 1

def go_to_next_step6_page():
    if st.session_state.step6_page < len(st.session_state.step6_targets) - 1:
        st.session_state.step6_page += 1

def go_back_to_step5():
    st.session_state.step = 5

def go_to_step7():
    st.session_state.step = 7

if st.session_state.step == 6:
    st.markdown("## Step 6")
    st.write("Step 6. Step5에서 '변경 있음'으로 선택된 항목에 대해 하위항목과 충족요건을 모두 선택하세요.")

    targets = st.session_state.step6_targets
    if not targets:
        st.warning("Step5에서 선택된 항목이 없습니다.")
    else:
        current_key = targets[st.session_state.step6_page]
        block = step6_items.get(current_key)

        if block:
            st.markdown(f"### {block['title']}")

            # 자동 동기화 쌍 정의
            sync_pairs = {
                "12c1": "12c2",
                "12c2": "12c1",
                "16a": "16b",
                "16b": "16a",
            }

            # 하위항목
            for sub_key, sub_text in block.get("subitems", {}).items():
                full_key = f"{current_key}_sub_{sub_key}"

                if current_key == "p3_15":
                    st.session_state.step6_selections[full_key] = "변경 있음"
                    st.radio(sub_text, ["변경 있음"], index=0, key=full_key, disabled=True)

                elif sub_key in sync_pairs:
                    other = sync_pairs[sub_key]
                    other_key = f"{current_key}_sub_{other}"

                    current_value = st.session_state.step6_selections.get(full_key, "변경 없음")
                    current_value = st.radio(
                        sub_text,
                        ["변경 있음", "변경 없음"],
                        key=full_key,
                        index=0 if current_value == "변경 있음" else 1
                    )

                    st.session_state.step6_selections[full_key] = current_value
                    st.session_state.step6_selections[other_key] = current_value

                else:
                    st.session_state.step6_selections[full_key] = st.radio(
                        sub_text,
                        ["변경 있음", "변경 없음"],
                        key=full_key
                    )

            # 충족요건
            for req_key, req_text in block.get("requirements", {}).items():
                full_key = f"{current_key}_req_{req_key}"
                label = f"{req_key}. {req_text}"
                st.session_state.step6_selections[full_key] = st.radio(
                    label,
                    ["충족", "미충족"],
                    key=full_key
                )

        else:
            st.warning("해당 항목 정보를 찾을 수 없습니다.")

        # 하단 버튼 영역
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                "이전단계로",
                on_click=go_back_to_step5 if st.session_state.step6_page == 0 else go_to_prev_step6_page
            )
        with col2:
            if st.session_state.step6_page == len(st.session_state.step6_targets) - 1:
                st.button("결과 확인하기", on_click=go_to_step7)
            else:
                st.button("다음항목 선택하기", on_click=go_to_next_step6_page)
# --- Content from: STEP 7_intro.py ---
# STEP 7 - 제조방법 변경에 따른 필요서류와 보고유형 도출
import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 7

if "step6_selections" not in st.session_state:
    st.session_state.step6_selections = {}

if "step7_page" not in st.session_state:
    st.session_state.step7_page = 0

if "step7_results" not in st.session_state:
    st.session_state.step7_results = []

def go_to_step6():
    st.session_state.step = 6

def go_to_step8():
    st.session_state.step = 8

def go_next_page():
    st.session_state.step7_page += 1

def go_prev_page():
    if st.session_state.step7_page > 0:
        st.session_state.step7_page -= 1

# 보고유형 문구 (하드코딩)
report_types = {
    "AR": "AR, 연차보고\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 제2항 및 제4항에 따른 연차보고(Annual Report, AR) 수준의 변경사항입니다.",
    "IR": "IR, 시판전보고\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2제4항 단서조항에 따른 시판전 보고(Immediate Report, IR) 수준의 변경사항입니다.",
    "Cmaj": "Cmaj, 변경허가(신고)\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 및 제6조에 따라 품질에 중요한 영향을 미치는 변경허가(신고) 신청(Change, C) 대상이며, 중요도 및 제출자료 요건을 고려할 때 Major change(Cmaj) 수준의 변경사항입니다.",
    "Cmin": "Cmin, 변경허가(신고)\n「의약품의 품목허가‧신고‧심사 규정」 제3조의2 및 제6조에 따라 품질에 중요한 영향을 미치는 변경허가(신고) 신청(Change, C) 대상이며, 중요도 및 제출자료 요건을 고려할 때 Minor change(Cmin) 수준의 변경사항입니다."
}

# 도출결과 출력 함수
def show_result(title, required_docs, report_type_key):
    st.markdown(f"### {title}")
    st.markdown("**필요서류는 다음과 같습니다.**")
    for idx, doc in enumerate(required_docs, 1):
        st.markdown(f"{idx}. {doc}")
    st.markdown("**보고유형은 다음과 같습니다.**")
    st.markdown(report_types[report_type_key])

# Step7 도입 화면 표시
if st.session_state.step == 7:
    st.markdown("## Step 7")
    st.markdown("**제조방법 변경에 따른 필요서류와 보고유형을 도출합니다.**")

    selections = st.session_state.step6_selections
    current_page = st.session_state.step7_page

    # Step6에서 선택된 title 순서대로 리스트 구성
    selected_titles = []
    for key in selections:
        if "_sub_" in key:
            title_key = key.split("_sub_")[0]
            if title_key not in selected_titles:
                selected_titles.append(title_key)

    selected_titles = sorted(set(selected_titles))  # 중복 제거 및 정렬

    if not selected_titles:
        st.error("Step6에서 선택된 항목이 없습니다.")
    else:
        current_title = selected_titles[current_page]

        # 이후 여기에 각 title별 도출 로직이 이어짐

        col1, col2 = st.columns(2)

        if len(selected_titles) == 1:
            with col1:
                st.button("이전단계로", on_click=go_to_step6)
            with col2:
                st.button("신청서 출력", on_click=go_to_step8)
        else:
            if current_page < len(selected_titles) - 1:
                with col1:
                    st.button("이전단계로", on_click=go_prev_page)
                with col2:
                    st.button("다음항목 확인하기", on_click=go_next_page)
            else:
                with col1:
                    st.button("이전단계로", on_click=go_prev_page)
                with col2:
                    st.button("신청서 출력", on_click=go_to_step8)


# --- Content from: STEP 7_Title1.py ---
    # Title 1: 원료의약품 명칭변경
    if current_title == "s1_1":
        sub_key = "s1_1_sub_1"
        selected_conditions = selections.get(sub_key, [])

        if "1" in selected_conditions:
            required_docs = [
                "1. (S.1.1) 공정서 또는 국제 의약품 일반명 리스트〔The International Nonproprietary Name(INN)〕 등 근거서류.",
                "2. 개정된 제품정보."
            ]
            show_result("1. 원료의약품 명칭변경", required_docs, "AR")
        else:
            st.markdown("### 1. 원료의약품 명칭변경")
            st.markdown("**필요서류는 다음과 같습니다.**")
            st.markdown("해당 없음")
            st.markdown("**보고유형은 다음과 같습니다.**")
            st.markdown("「의약품 허가 후 제조방법 변경관리 가이드라인(민원인 안내서)」에 포함되지 않은 변경의 경우 위험평가를 수행하여 품질에 영향을 미치지 않거나 경미한 영향을 미치는 변경의 경우 제조사의 문서화된 절차 및 의약품품질시스템에 따라 처리하고 해당 변경이 제제의 품질 및 안전성‧유효성에 영향을 미치지 않도록 관리해야 하며, 그 외의 사항은 기본적으로 품질에 영향을 미치는 중요한 변경사항으로 간주 되어야 합니다.")


# --- Content from: STEP 7_Title2.py ---
# Title 2: 원료의약품의 제조소 또는 제조업자의 변경 또는 추가
if current_title == "s2_2":
    sub_keys = [k for k in selections if k.startswith("s2_2_sub_")]
    for sub_key in sub_keys:
        selected_conditions = selections.get(sub_key, [])

        # 2a. 출발물질 생산 변경 있음
        if sub_key.endswith("2a"):
            if all(c in selected_conditions for c in ["3", "4", "9"]):
                required_docs = [
                    "1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료."
                ]
                show_result("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가", required_docs, "IR")
            else:
                required_docs = [
                    "1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "3. (S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.",
                    "4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "7. (S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.",
                    "10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료.",
                    "11. (S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."
                ]
                show_result("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가", required_docs, "Cmaj")

        # 2b. 중간체 생산 변경 있음
        elif sub_key.endswith("2b"):
            if all(c in selected_conditions for c in ["3", "5"]):
                required_docs = [
                    "1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "8. (S.2) 원료의약품 및 핵심(최종) 중간체(해당되는 경우) 합성 경로, 사용 원료, 품질 관리 절차 및 규격 변경이 없다는 확인서(statement).",
                    "10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료."
                ]
                show_result("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가", required_docs, "IR")
            else:
                required_docs = [
                    "1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "3. (S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.",
                    "4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "7. (S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.",
                    "10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당하는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료.",
                    "11. (S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."
                ]
                show_result("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가", required_docs, "Cmaj")

        # 2c. 생산 변경 있음
        elif sub_key.endswith("2c"):
            if all(c in selected_conditions for c in ["1", "2", "3", "6", "7", "8"]):
                required_docs = [
                    "1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "5. (S.4.4) 변경 전·후 원료의약품 2배치(파일럿 배치 이상)에 대한 배치분석자료.",
                    "8. (S.2) 원료의약품 및 핵심(최종) 중간체(해당되는 경우) 합성 경로, 사용 원료, 품질 관리 절차 및 규격 변경이 없다는 확인서(statement)."
                ]
                show_result("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가", required_docs, "IR")
            elif "10" in selected_conditions:
                required_docs = [
                    "12. 해당국가의 공식기관에서 발급받은 문서(GMP 증명서 등 포함) 또는 인증여부를 확인할 수 있는 자료(제조소의 책임자가 서명하고 공증받은 자료 등)."
                ]
                show_result("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가", required_docs, "Cmin")
            else:
                required_docs = [
                    "1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                    "2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.",
                    "3. (S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.",
                    "4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우) 제조 공정에 관한 자료.",
                    "5. (S.4.4) 변경 전·후 원료의약품 2배치(파일럿 배치 이상)에 대한 배치분석자료.",
                    "6. (P.8.2) 원료의약품의 품질 특성이 완제의약품의 안정성에 영향을 미칠 수 있는 변경의 경우, 완제의약품 1배치(실제 생산 규모의)에 대한 안정성 시험 이행 계획서.",
                    "7. (S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.",
                    "9. 변경 후 원료의약품이 완제의약품의 안전성, 유효성 및 품질에 미치는 영향에 대한 고찰자료.",
                    "11. (S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."
                ]
                show_result("2. 원료의약품의 제조소 또는 제조업자의 변경 또는 추가", required_docs, "Cmaj")


# --- Content from: STEP 7_Title3.py ---
    # Title 3: 원료의약품 제조 공정의 변경
    if current_title == "s2_3":
        sub_keys = [k for k in selections if k.startswith("s2_3_sub_")]
        for sub_key in sub_keys:
            selected_conditions = selections.get(sub_key, [])

            if all(c in selected_conditions for c in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                required_docs = [
                    "2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료",
                    "3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료",
                    "4. (S.2.3) (해당되는 경우) 사용 원료의 규격 및 시험 성적서",
                    "11. (S.4.4) 최소 2배치에 대한 배치분석 자료"
                ]
                show_result("3. 원료의약품 제조 공정의 변경", required_docs, "IR")

            elif all(c in selected_conditions for c in ["1", "2", "3", "5", "7", "8", "9"]):
                required_docs = [
                    "2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료",
                    "3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료",
                    "10. (S.4.1) 변경 후 기준 및 시험방법",
                    "11. (S.4.4) 최소 2배치에 대한 배치분석 자료"
                ]
                show_result("3. 원료의약품 제조 공정의 변경", required_docs, "Cmin")

            elif all(c in selected_conditions for c in ["1", "2", "3", "4", "5", "6"]):
                required_docs = [
                    "2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료",
                    "3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료",
                    "10. (S.4.1) 변경 후 기준 및 시험방법",
                    "11. (S.4.4) 최소 2배치에 대한 배치분석 자료"
                ]
                show_result("3. 원료의약품 제조 공정의 변경", required_docs, "Cmin")

            elif len(selected_conditions) == 0:
                required_docs = [
                    "1. 변경 후 품질에 미치는 영향 고찰자료",
                    "2. 변경 전·후 제조방법 비교표",
                    "3. (S.2.2) 변경 공정 흐름도 및 상세 제조 공정 자료",
                    "4. (S.2.3) 사용 원료의 규격 및 시험 성적서",
                    "5. (S.2.3) 사람/동물 유래물질 BSE/TSE 위해 적합성 평가 자료",
                    "6. (S.2.4) 주요 공정 및 중간체 관리 자료",
                    "7. (S.2.5) 멸균 공정 밸리데이션 또는 평가 자료",
                    "8. (S.3.1) 구조결정 및 물리화학적 성질 자료",
                    "9. (S.3.2) 불순물 고찰 및 근거 자료",
                    "10. (S.4.1) 변경 후 기준 및 시험방법",
                    "11. (S.4.4) 최소 2배치 배치분석 자료",
                    "12. (S.7.1) 3개월 이상 가속 및 장기보존 시험 자료",
                    "13. 결정형 또는 입자도 변경에 따른 품질/생체이용률 영향 입증 자료"
                ]
                show_result("3. 원료의약품 제조 공정의 변경", required_docs, "Cmaj")


# --- Content from: STEP 7_Title4.py ---
    # Title 4: 원료의약품 제조 공정관리 규격의 변경
    if current_title == "s2_4":
        sub_keys = [k for k in selections if k.startswith("s2_4_sub_")]
        for sub_key in sub_keys:
            selected_conditions = selections.get(sub_key, [])

            if all(c in selected_conditions for c in ["4a_1", "4a_2", "4a_3"]):
                required_docs = [
                    "1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료"
                ]
                show_result("4. 원료의약품 제조 공정관리 규격의 변경", required_docs, "AR")

            elif "4b_1" in selected_conditions:
                required_docs = [
                    "1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "4. 해당되는 경우, 분석 방법 상세 자료",
                    "5. 공정관리 시험 규격에 대한 타당성 입증 자료 또는 설명자료"
                ]
                show_result("4. 원료의약품 제조 공정관리 규격의 변경", required_docs, "AR")

            elif sub_key.endswith("4c") and len(selected_conditions) == 0:
                required_docs = [
                    "1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "4. 해당되는 경우, 분석 방법 상세 자료",
                    "5. 공정관리 시험 규격에 대한 타당성 입증 자료 또는 설명자료",
                    "7. (S.2.5) 무균 관련 공정 밸리데이션 자료",
                    "8. (S.3.2) 불순물에 대한 고찰 및 근거자료",
                    "9. (S.4.1) 변경 후 규격에 관한 자료",
                    "10. (S.4.4) 최소 1배치의 배치분석자료"
                ]
                show_result("4. 원료의약품 제조 공정관리 규격의 변경", required_docs, "Cmin")

            elif all(c in selected_conditions for c in ["4d_1", "4d_4", "4d_5"]):
                required_docs = [
                    "1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "6. 품질에 영향 없음 입증자료 또는 위험 평가 자료"
                ]
                show_result("4. 원료의약품 제조 공정관리 규격의 변경", required_docs, "AR")

            elif "4d_1" in selected_conditions:
                required_docs = [
                    "1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "5. 공정관리 시험 규격에 대한 타당성 입증 자료 또는 설명자료",
                    "7. (S.2.5) 무균 관련 공정 밸리데이션 자료",
                    "8. (S.3.2) 불순물에 대한 고찰 및 근거자료",
                    "9. (S.4.1) 변경 후 규격에 관한 자료",
                    "10. (S.4.4) 최소 1배치의 배치분석자료"
                ]
                show_result("4. 원료의약품 제조 공정관리 규격의 변경", required_docs, "Cmaj")

            elif "4e_1" in selected_conditions:
                required_docs = [
                    "1. 변경 전·후 공정관리 시험 비교표 등 변경 전·후에 관한 자료",
                    "2. (S.2.2) 변경 후 합성 공정 흐름도 및 제조 공정에 대한 서술 자료",
                    "3. (S.2.4) 변경 후 공정관리 시험 규격에 관한 자료",
                    "5. 공정관리 시험 규격에 대한 타당성 입증 자료 또는 설명자료",
                    "7. (S.2.5) 무균 관련 공정 밸리데이션 자료",
                    "8. (S.3.2) 불순물에 대한 고찰 및 근거자료",
                    "9. (S.4.1) 변경 후 규격에 관한 자료",
                    "10. (S.4.4) 최소 1배치의 배치분석자료"
                ]
                show_result("4. 원료의약품 제조 공정관리 규격의 변경", required_docs, "Cmaj")


# --- Content from: STEP 7_Title5.py ---
    elif current_title == "s2_5":
        sub_5a = selections.get("s2_5_sub_5a", [])
        sub_5b = selections.get("s2_5_sub_5b", [])
        sub_5c = selections.get("s2_5_sub_5c", [])

        if all(x in sub_5a for x in ["1", "2", "3"]):
            show_result(
                "5. 원료의약품 또는 중간체의 제조 규모 변경 - 제조 규모의 10배 이하 확대",
                [
                    "1. (S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.",
                    "2. (S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "3. (S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).",
                    "4. (S.4.4) 변경 전·후 제조 규모에서 각 최소 1배치에 대한 배치 분석 자료."
                ],
                "AR"
            )

        elif all(x in sub_5b for x in ["1", "2", "3"]):
            show_result(
                "5. 원료의약품 또는 중간체의 제조 규모 변경 - 제조 규모의 축소",
                [
                    "1. (S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.",
                    "2. (S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "3. (S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).",
                    "4. (S.4.4) 변경 전·후 제조 규모에서 각 최소 1배치에 대한 배치 분석 자료."
                ],
                "AR"
            )

        elif all(x in sub_5c for x in ["1", "2"]):
            show_result(
                "5. 원료의약품 또는 중간체의 제조 규모 변경 - 제조 규모의 10배 초과 확대",
                [
                    "1. (S.2.2) 변경 전·후 제조공정 비교표 및 변경 후 상세 제조 공정에 관한 자료.",
                    "2. (S.2.5) (해당되는 경우, 위험도 평가에 따른) 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "3. (S.4.1) 원료의약품의 규격에 관한 자료(해당되는 경우 중간체 규격에 관한 자료).",
                    "5. (S.4.4) 변경 전·후 제조 규모에서 각 최소 2배치에 대한 배치 분석 자료."
                ],
                "Cmin"
            )


# --- Content from: STEP 7_Title6.py ---
    elif current_title == "s2_6":
        sub_6a = selections.get("s2_6_sub_6a", [])
        sub_6b = selections.get("s2_6_sub_6b", [])
        sub_6c = selections.get("s2_6_sub_6c", [])
        sub_6d = selections.get("s2_6_sub_6d", [])
        sub_6e = selections.get("s2_6_sub_6e", [])
        sub_6f = selections.get("s2_6_sub_6f", [])
        sub_6g = selections.get("s2_6_sub_6g", [])

        if all(x in sub_6a for x in ["1", "2", "3"]):
            show_result(
                "6. 원료의약품의 제조에 사용되는 원료(출발물질, 중간체, 용매, 시약 등)의 규격변경 - 규격 기준의 강화",
                [
                    "1. 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "2. (S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "3. (S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서)."
                ],
                "AR"
            )

        elif all(x in sub_6b for x in ["4", "5", "6"]):
            show_result(
                "6. 원료의약품의 제조에 사용되는 원료 - 시험방법의 변경",
                [
                    "2. (S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "3. (S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서)."
                ],
                "AR"
            )

        elif all(x in sub_6c for x in ["1", "5", "6", "7"]):
            show_result(
                "6. 원료의약품의 제조에 사용되는 원료 - 기준 및 시험방법 추가",
                [
                    "1. 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "2. (S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "3. (S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서)."
                ],
                "AR"
            )

        elif all(x in sub_6d for x in ["1", "8", "9"]):
            show_result(
                "6. 원료의약품의 제조에 사용되는 원료 - 기준 또는 시험방법의 삭제",
                [
                    "1. 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "2. (S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "3. (S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서).",
                    "4. 해당 변경이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료)."
                ],
                "AR"
            )

        elif sub_6e == []:
            show_result(
                "6. 원료의약품의 제조에 사용되는 원료 - 안전성/품질관리 문제로 기준의 추가 또는 교체 (요건 미충족)",
                [
                    "1. 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "2. (S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "3. (S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서).",
                    "4. 해당 변경이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료).",
                    "5. (S.3.2) (해당하는 경우) 불순물에 대한 고찰 및 근거자료."
                ],
                "Cmaj"
            )

        elif all(x in sub_6f for x in ["3", "6", "7", "9"]):
            show_result(
                "6. 원료약품(용매, 시약, 촉매 등)에 대한 기준 완화",
                [
                    "1. 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "2. (S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서)."
                ],
                "AR"
            )

        elif sub_6g == []:
            show_result(
                "6. 출발물질/핵심중간체 기준 완화 (요건 미충족)",
                [
                    "1. 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료.",
                    "2. (S.2.3) 원료의약품의 제조에 사용하는 변경된 원료의 정보(규격 또는 공급처 성적서).",
                    "3. (S.2.4) (해당하는 경우) 변경된 중간체에 대한 정보(규격 또는 공급처 성적서).",
                    "4. 해당 변경이 품질에 영향을 미치지 않음을 입증하는 자료(또는 위험 평가 자료).",
                    "5. (S.3.2) (해당하는 경우) 불순물에 대한 고찰 및 근거자료."
                ],
                "Cmaj"
            )


# --- Content from: STEP 7_Title7.py ---
    elif current_title == "p1_7":
        sub_7a = selections.get("p1_7_sub_7a", [])
        sub_7b = selections.get("p1_7_sub_7b", [])
        sub_7c = selections.get("p1_7_sub_7c", [])

        if all(x in sub_7a for x in ["1", "4"]):
            show_result(
                "7. 완제의약품 중 고형 제제의 조성 변경 - 타르색소(황색4호 제외)의 종류 변경",
                [
                    "2. (P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "3. (P.2) 변경하고자 하는 제제의 성분에 대한 검토 자료(예: 첨가제의 선택, 원료의약품과 첨가제의 배합 적합성).",
                    "5. (P.4) 첨가제 종류를 변경/추가하는 경우, 첨가제의 규격에 관한 자료.",
                    "7. (P.5) 완제의약품의 기준 및 시험방법, 최소 1배치(파일럿 배치 이상)에 대한 시험 성적서.",
                    "10. (P.8.2) 변경하고자 하는 제제의 생산 규모 배치에 대한 안정성 시험 계획서 및 이행서약."
                ],
                "AR"
            )

        elif all(x in sub_7b for x in ["1", "2", "3", "4", "5"]):
            show_result(
                "7. 완제의약품 중 고형 제제의 조성 변경 - 착색제 또는 착향제의 종류 및 분량 변경 (충족조건 1,2,3,4,5)",
                [
                    "2. (P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "5. (P.4) 첨가제 종류를 변경/추가하는 경우, 첨가제의 규격에 관한 자료.",
                    "7. (P.5) 완제의약품의 기준 및 시험방법, 최소 1배치(파일럿 배치 이상)에 대한 시험 성적서.",
                    "8. (P.5.3) 해당되는 경우, 변경된 첨가제가 완제의약품의 분석 절차를 방해하지 않는다는 것을 입증하는 자료.",
                    "10. (P.8.2) 변경하고자 하는 제제의 생산 규모 배치에 대한 안정성 시험 계획서 및 이행서약."
                ],
                "IR"
            )

        elif all(x in sub_7b for x in ["1", "2", "3", "4"]):
            show_result(
                "7. 완제의약품 중 고형 제제의 조성 변경 - 착색제 또는 착향제의 종류 및 분량 변경 (충족조건 1,2,3,4)",
                [
                    "2. (P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "5. (P.4) 첨가제 종류를 변경/추가하는 경우, 첨가제의 규격에 관한 자료.",
                    "7. (P.5) 완제의약품의 기준 및 시험방법, 최소 1배치(파일럿 배치 이상)에 대한 시험 성적서.",
                    "8. (P.5.3) 해당되는 경우, 변경된 첨가제가 완제의약품의 분석 절차를 방해하지 않는다는 것을 입증하는 자료."
                ],
                "Cmin"
            )

        elif all(x in sub_7c for x in ["1", "4"]):
            show_result(
                "7. 완제의약품 중 고형 제제의 조성 변경 - 첨가제의 종류 및 분량 변경",
                [
                    "1. (P.2 또는 R) 「의약품동등성시험기준」 [별표2] 원료약품 및 그 분량 변경수준 및 제출자료 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.",
                    "2. (P.1) 완제의약품의 성상 및 원료약품 분량.",
                    "3. (P.2) 변경하고자 하는 제제의 성분에 대한 검토 자료(예: 첨가제의 선택, 원료의약품과 첨가제의 배합 적합성).",
                    "4. (P.3) 배치 조성에 대한 자료.",
                    "5. (P.4) 첨가제 종류를 변경/추가하는 경우, 첨가제의 규격에 관한 자료.",
                    "6. (P.4.5) 사람 또는 동물 유래 물질이 사용되는 경우, 출처가 새로운 원료약품에 대한 BSE/TSE 위해 적합성 평가 자료.",
                    "7. (P.5) 완제의약품의 기준 및 시험방법, 최소 1배치(파일럿 배치 이상)에 대한 시험 성적서.",
                    "8. (P.5.3) 해당되는 경우, 변경된 첨가제가 완제의약품의 분석 절차를 방해하지 않는다는 것을 입증하는 자료.",
                    "9. (P.8.1) 변경 후 완제의약품 최소 2배치(파일럿 배치 이상)에 대한 장기 및 가속 안정성 시험 최소 3개월 자료. 생물학적동등성시험을 제출하는 경우, 장기 및 가속 최소 6개월 자료.",
                    "10. (P.8.2) 변경하고자 하는 제제의 생산 규모 배치에 대한 안정성 시험 계획서 및 이행서약."
                ],
                "Cmaj"
            )


# --- Content from: STEP 7_Title8.py ---
    elif current_title == "p1_8":
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


# --- Content from: STEP 7_Title9.py ---
    elif current_title == "p1_9":
        show_result(
            "9. 완제의약품(고형제제 제외)의 조성 변경",
            [
                "1. (P.2 또는 R) 「의약품동등성시험기준」 [별표2] 원료약품 및 그 분량 변경수준 및 제출자료 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료로서, 완제의약품의 물리화학적 특성에 변화가 없음을 입증할 수 있는 이화학적동등성시험자료(예: 점도, 삼투압, pH 등).",
                "3. (P.1) 완제의약품의 성상 및 조성.",
                "4. (P.2) 변경하고자 하는 제제의 구성 성분에 대한 검토 자료(예: 첨가제의 선택, 원료약품과 첨가제 간의 배합성, 변경된 제제의 포장 시스템 적합성 시험).",
                "5. (P.3) 배치 조성, 제조공정 및 공정 관리의 설명 자료, 중요 공정 및 중간체의 관리, (위험도 평가에 따른) 공정 밸리데이션 계획서 및/또는 평가 자료.",
                "6. (P.4) 첨가제 종류를 변경/추가하는 경우, 해당 첨가제의 규격에 관한 자료.",
                "7. (P.4.5) 사람 또는 동물 유래 물질이 사용되는 경우, 출처가 새로운 원료약품에 대한 BSE/TSE(소해면상뇌증/전염성해면상뇌증) 위해 적합성 평가 자료.",
                "8. (P.5) 완제의약품의 기준 및 시험방법, 최소 1배치(파일럿 배치 이상) 시험 성적서.",
                "9. (P.5.3) 해당되는 경우, 변경된 첨가제가 완제의약품의 분석 절차를 방해하지 않는다는 것을 입증하는 자료.",
                "10. (P.8.1) 변경 후 완제의약품 최소 2배치(파일럿 배치 이상)에 대한 장기 및 가속 안정성 시험 최소 3개월 자료. 생물학적동등성시험을 제출하는 경우, 장기 및 가속 최소 6개월 자료.",
                "11. (P.8.2) 변경하고자 하는 제제의 생산규모 배치에 대한 안정성 시험 계획서 및 이행서약."
            ],
            "Cmaj"
        )


# --- Content from: STEP 7_Title10.py ---
    elif current_title == "p1_10":
        show_result(
            "10. 완제의약품(고형제제 제외)에 쓰이는 착색제 또는 착향제의 종류와 분량의 변경",
            [
                "1. (P.1) 완제의약품의 원료약품 분량.",
                "2. (P.3) 배치 조성에 대한 자료.",
                "5. (P.5) 완제의약품 기준 및 시험방법 및 최소 1배치(파일럿 배치 이상) 이상의 시험 성적서.",
                "7. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                "8. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
            ],
            "AR"
        )


# --- Content from: STEP 7_Title11.py ---
    elif current_title == "p3_11":
        show_result(
            "11. 정성적 또는 정량적인 조성과 평균 질량의 변경이 없는 성상의 변경",
            [
                "2. 완제의약품의 성상.",
                "3. (P.3) 배치 조성에 대한 자료, 제조공정 및 공정관리의 설명자료, 해당되는 경우, 제조공정 파라미터 변경을 확인할 수 있는 자료.",
                "4. (P.5) 변경된 기준 및 시험방법.",
                "5. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
            ],
            "Cmin"
        )


# --- Content from: STEP 7_Title12.py ---
    elif current_title == "p3_12":
        keys = [k for k in selections if k.startswith("p3_12_sub_")]
        values = [selections[k] for k in keys]

        if "12a" in values and "2" in values:
            show_result("12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
                        [
                            "1. (해당하는 경우) 해당 제조소의 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서 또는 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                            "2. (P.3.1) 수탁업소를 포함한 각 제조원, 주소, 책임소재 등의 자료."
                        ], "Cmin")

        elif "12b.1" in values and all(c in values for c in ["2", "3", "4"]):
            show_result("12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
                        [
                            "1. (해당하는 경우) 해당 제조소의 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서 또는 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                            "2. (P.3.1) 수탁업소를 포함한 각 제조원, 주소, 책임소재 등의 자료.",
                            "8. (P.8.2) 변경 후 생산규모 배치에 대한 안정성 시험 계획 및 이행서약. 단, 생물학적동등성시험을 제출하는 경우, 최소 2배치(파일럿 배치 이상)의 장기 및 가속 최소 6개월 자료."
                        ], "Cmin")

        elif "12b.2" in values and all(c in values for c in ["2", "3", "4"]):
            show_result("12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
                        [
                            "1. (해당하는 경우) 해당 제조소의 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서 또는 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                            "2. (P.3.1) 수탁업소를 포함한 각 제조원, 주소, 책임소재 등의 자료.",
                            "5. (P.3.5) 변경 후 (위험도 평가에 따른) 실생산 규모의 3배치에 대한 공정 밸리데이션 보고서 또는 밸리데이션 실시 계획서.",
                            "8. (P.8.2) 변경 후 생산규모 배치에 대한 안정성 시험 계획 및 이행서약. 단, 생물학적동등성시험을 제출하는 경우, 최소 2배치(파일럿 배치 이상)의 장기 및 가속 최소 6개월 자료."
                        ], "Cmaj")

        elif "12c1" in values and all(c in values for c in ["1", "2"]):
            show_result("12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
                        [
                            "1. (해당하는 경우) 해당 제조소의 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서 또는 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                            "2. (P.3.1) 수탁업소를 포함한 각 제조원, 주소, 책임소재 등의 자료.",
                            "3. (P.2) 원료의약품이 녹지 않은 상태로 존재하는 반고형 제제와 액상 제제일 때는 입도시험 또는 입자도 시험에 대한 적절한 밸리데이션 자료.",
                            "4. (P.2 또는 R) 「의약품동등성시험기준」 [별표4] 제조소의 변경수준 및 제출자료 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.",
                            "5. (P.3.5) 변경 후 (위험도 평가에 따른) 실생산 규모의 3배치에 대한 공정 밸리데이션 보고서 또는 밸리데이션 실시 계획서.",
                            "6. (P.5.1) 변경 후 완제의약품 규격에 관한 자료.",
                            "7. (P.5.4) 변경 전·후 최소 생산규모 1배치에 대한 배치분석 자료.",
                            "9. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
                        ], "Cmin")

        elif "12c1" in values and all(c in values for c in ["1", "2", "5"]):
            show_result("12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
                        [
                            "1. (해당하는 경우) 해당 제조소의 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서 또는 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                            "2. (P.3.1) 수탁업소를 포함한 각 제조원, 주소, 책임소재 등의 자료.",
                            "3. (P.2) 원료의약품이 녹지 않은 상태로 존재하는 반고형 제제와 액상 제제일 때는 입도시험 또는 입자도 시험에 대한 적절한 밸리데이션 자료.",
                            "5. (P.3.5) 변경 후 (위험도 평가에 따른) 실생산 규모의 3배치에 대한 공정 밸리데이션 보고서 또는 밸리데이션 실시 계획서.",
                            "6. (P.5.1) 변경 후 완제의약품 규격에 관한 자료.",
                            "7. (P.5.4) 변경 전·후 최소 생산규모 1배치에 대한 배치분석 자료.",
                            "9. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
                        ], "Cmin")

        elif "12c2" in values and "2" in values:
            show_result("12. 완제의약품 제조공정의 일부 또는 전부에 대한 제조소 추가 또는 변경",
                        [
                            "1. (해당하는 경우) 해당 제조소의 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서 또는 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.",
                            "2. (P.3.1) 수탁업소를 포함한 각 제조원, 주소, 책임소재 등의 자료.",
                            "3. (P.2) 원료의약품이 녹지 않은 상태로 존재하는 반고형 제제와 액상 제제일 때는 입도시험 또는 입자도 시험에 대한 적절한 밸리데이션 자료.",
                            "4. (P.2 또는 R) 「의약품동등성시험기준」 [별표4] 제조소의 변경수준 및 제출자료 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.",
                            "5. (P.3.5) 변경 후 (위험도 평가에 따른) 실생산 규모의 3배치에 대한 공정 밸리데이션 보고서 또는 밸리데이션 실시 계획서.",
                            "6. (P.5.1) 변경 후 완제의약품 규격에 관한 자료.",
                            "7. (P.5.4) 변경 전·후 최소 생산규모 1배치에 대한 배치분석 자료.",
                            "8. (P.8.2) 변경 후 생산규모 배치에 대한 안정성 시험 계획 및 이행서약. 단, 생물학적동등성시험을 제출하는 경우, 최소 2배치(파일럿 배치 이상)의 장기 및 가속 최소 6개월 자료.",
                            "9. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
                        ], "Cmaj")


# --- Content from: STEP 7_Title13.py ---
    elif current_title == "p3_13":
        conditions = selections.get("p3_13_conditions", [])
        
        if set(["13a", "cond1", "cond2", "cond3", "cond4"]).issubset(conditions):
            required_docs = [
                "2. (P.3.5) (위험도 평가에 따른) 변경하고자 하는 제조 규모의 3배치에 대한 공정 밸리데이션 실시 보고서 또는 밸리데이션 실시 계획서.",
                "4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치분석 자료(변경사항 13a는 연차보고시점 변경된 제조규모의 생산실적이 있는 경우 구비).",
                "5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                "6. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
            ]
            show_result("13. 비무균제제의 제조 규모 변경", required_docs, "AR")

        elif set(["13b", "cond1", "cond2", "cond3", "cond4", "cond5"]).issubset(conditions):
            required_docs = [
                "1. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료의 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.",
                "2. (P.3.5) (위험도 평가에 따른) 변경하고자 하는 제조 규모의 3배치에 대한 공정 밸리데이션 실시 보고서 또는 밸리데이션 실시 계획서.",
                "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                "4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치분석 자료(변경사항 13a는 연차보고시점 변경된 제조규모의 생산실적이 있는 경우 구비).",
                "5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                "6. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
            ]
            show_result("13. 비무균제제의 제조 규모 변경", required_docs, "IR")

        elif set(["13b", "cond1", "cond2", "cond3", "cond4", "cond6"]).issubset(conditions):
            required_docs = [
                "2. (P.3.5) (위험도 평가에 따른) 변경하고자 하는 제조 규모의 3배치에 대한 공정 밸리데이션 실시 보고서 또는 밸리데이션 실시 계획서.",
                "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                "4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치분석 자료(변경사항 13a는 연차보고시점 변경된 제조규모의 생산실적이 있는 경우 구비).",
                "5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                "6. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
            ]
            show_result("13. 비무균제제의 제조 규모 변경", required_docs, "IR")

        elif set(["13c", "cond1", "cond2", "cond3", "cond4"]).issubset(conditions):
            required_docs = [
                "1. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료의 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.",
                "2. (P.3.5) (위험도 평가에 따른) 변경하고자 하는 제조 규모의 3배치에 대한 공정 밸리데이션 실시 보고서 또는 밸리데이션 실시 계획서.",
                "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                "4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치분석 자료(변경사항 13a는 연차보고시점 변경된 제조규모의 생산실적이 있는 경우 구비).",
                "5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                "6. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
            ]
            show_result("13. 비무균제제의 제조 규모 변경", required_docs, "Cmaj")


# --- Content from: STEP 7_Title14.py ---
    elif current_title == "p3_14":
        if set(selections.get("p3_14_conditions", [])) == {"1", "2", "3", "4"}:
            show_result(
                "14. 무균제제의 제조 규모 변경",
                [
                    "1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.",
                    "2. (P.3.5) (위험도 평가에 따른) 공정밸리데이션 자료 또는 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                    "4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치 분석 자료(비교표 형식).",
                    "5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약."
                ],
                "AR"
            )
        elif set(selections.get("p3_14_conditions", [])) == {"1", "2", "3", "4", "5"}:
            show_result(
                "14. 무균제제의 제조 규모 변경",
                [
                    "1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.",
                    "2. (P.3.5) (위험도 평가에 따른) 공정밸리데이션 자료 또는 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                    "4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치 분석 자료(비교표 형식).",
                    "5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약."
                ],
                "IR"
            )
        elif set(selections.get("p3_14_conditions", [])) == {"1", "2", "3", "4", "6"}:
            show_result(
                "14. 무균제제의 제조 규모 변경",
                [
                    "1. 현재 승인 및 신청한 배치 조성에 대한 비교표 등 변경 전·후에 관한 자료.",
                    "2. (P.3.5) (위험도 평가에 따른) 공정밸리데이션 자료 또는 무균공정과 멸균 공정 밸리데이션 또는 평가결과에 관한 자료.",
                    "3. (P.5.1) 완제의약품의 기준 및 시험방법.",
                    "4. (P.5.4) 변경 전·후 생산 규모 완제의약품의 최소 1배치에 대한 배치 분석 자료(비교표 형식).",
                    "5. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "6. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료."
                ],
                "Cmaj"
            )


# --- Content from: STEP 7_Title15.py ---
    elif current_title == "p3_15":
        if set(selections.get("p3_15_conditions", [])) == {"1", "2", "3", "4", "5", "6", "7"}:
            show_result(
                "15. 완제의약품의 제조공정 변경",
                [
                    "2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(In-Vitro 비교시험 자료, 고형 제제 단위의 기준 및 시험방법에서의 용출 프로파일, 원료의약품을 용해/비용해 상태로 함유하는 비무균 반고형 제형의 In-Vitro 멤브레인 확산시험, 비용해 액상제제의 형상 가시적 변화 확인 자료와 입자 크기 분포 비교자료 등).",
                    "3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.",
                    "6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
                ],
                "AR"
            )
        elif set(selections.get("p3_15_conditions", [])) == {"1", "2", "3", "5", "6", "7", "8"}:
            show_result(
                "15. 완제의약품의 제조공정 변경",
                [
                    "1. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료의 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.",
                    "2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(In-Vitro 비교시험 자료, 고형 제제 단위의 기준 및 시험방법에서의 용출 프로파일, 원료의약품을 용해/비용해 상태로 함유하는 비무균 반고형 제형의 In-Vitro 멤브레인 확산시험, 비용해 액상제제의 형상 가시적 변화 확인 자료와 입자 크기 분포 비교자료 등).",
                    "3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.",
                    "4. (P.5) 변경 전·후 생산 규모 1배치에 대한 규격 및 시험성적서.",
                    "5. (P.8.1) 최소 2배치(파일럿배치이상)에 대한 3개월 가속 및 장기안정성 시험결과, 생물학적동등성시험 제출 시 최소 6개월 자료.",
                    "6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
                ],
                "IR"
            )
        elif set(selections.get("p3_15_conditions", [])) == {"1", "2", "3", "5", "6", "7", "8", "9"}:
            show_result(
                "15. 완제의약품의 제조공정 변경",
                [
                    "2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(In-Vitro 비교시험 자료, 고형 제제 단위의 기준 및 시험방법에서의 용출 프로파일, 원료의약품을 용해/비용해 상태로 함유하는 비무균 반고형 제형의 In-Vitro 멤브레인 확산시험, 비용해 액상제제의 형상 가시적 변화 확인 자료와 입자 크기 분포 비교자료 등).",
                    "3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.",
                    "4. (P.5) 변경 전·후 생산 규모 1배치에 대한 규격 및 시험성적서.",
                    "5. (P.8.1) 최소 2배치(파일럿배치이상)에 대한 3개월 가속 및 장기안정성 시험결과, 생물학적동등성시험 제출 시 최소 6개월 자료.",
                    "6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
                ],
                "IR"
            )
        elif selections.get("p3_15_conditions") == []:
            show_result(
                "15. 완제의약품의 제조공정 변경",
                [
                    "2. (P.2) 해당되는 경우, 제조 공정의 개발에 관한 검토 자료(In-Vitro 비교시험 자료, 고형 제제 단위의 기준 및 시험방법에서의 용출 프로파일, 원료의약품을 용해/비용해 상태로 함유하는 비무균 반고형 제형의 In-Vitro 멤브레인 확산시험, 비용해 액상제제의 형상 가시적 변화 확인 자료와 입자 크기 분포 비교자료 등).",
                    "3. (P.3) 배치 조성, 제조공정과 공정관리의 설명 자료, 주요 단계와 중간체의 관리, 공정 밸리데이션 계획서 및/또는 평가 자료.",
                    "4. (P.5) 변경 전·후 생산 규모 1배치에 대한 규격 및 시험성적서.",
                    "5. (P.8.1) 최소 2배치(파일럿배치이상)에 대한 3개월 가속 및 장기안정성 시험결과, 생물학적동등성시험 제출 시 최소 6개월 자료.",
                    "6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약.",
                    "7. (R.1) 해당 변경 사항 외에 제조 관련 문서에 일체의 변경이 없다는 내용의 확인서(statement)."
                ],
                "Cmaj"
            )


# --- Content from: STEP 7_Title16.py ---
    elif current_title == "p3_16":
        if set(selections.get("p3_16_conditions", [])) == {"1", "2", "4"}:
            show_result(
                "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
                [
                    "2. (P.3.3/P.3.4) 공정 중 시험의 규격 비교표 등 변경 전·후에 관한 자료."
                ],
                "AR"
            )
        elif set(selections.get("p3_16_conditions", [])) == {"2"}:
            show_result(
                "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
                [
                    "1. (P.2 또는 R) 「의약품동등성시험기준」 [별표3] 제조방법의 변경수준 및 제출자료의 범위에 따른 의약품동등성시험자료 및 실시한 의약품동등성시험이 동 규정에 적합함을 입증하는 자료.",
                    "2. (P.3.3/P.3.4) 공정 중 시험의 규격 비교표 등 변경 전·후에 관한 자료.",
                    "3. (P.3.3/P.3.4) 새로운 공정관리 시험방법을 사용하는 경우, 시험방법에 관한 자료.",
                    "4. 새로운 시험방법을 사용하는 경우, 필요 시 밸리데이션 실시 보고서 또는 요약문.",
                    "5. (P.5.4) 변경 전후 최소 1배치(파일럿 배치 이상)에 대한 시험성적 비교자료.",
                    "6. 공정관리시험 및 기준의 추가, 삭제, 변경에 대한 타당성 입증 자료."
                ],
                "Cmaj"
            )
        elif set(selections.get("p3_16_conditions", [])) == {"2", "3"}:
            show_result(
                "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
                [
                    "6. 공정관리시험 및 기준의 추가, 삭제, 변경에 대한 타당성 입증 자료."
                ],
                "AR"
            )
        elif selections.get("p3_16_conditions", []) == ["2"]:
            show_result(
                "16. 완제의약품 또는 반제품의 제조에 적용되는 공정관리시험 또는 공정관리시험 기준(IPC)의 변경",
                [
                    "2. (P.3.3/P.3.4) 공정 중 시험의 규격 비교표 등 변경 전·후에 관한 자료.",
                    "3. (P.3.3/P.3.4) 새로운 공정관리 시험방법을 사용하는 경우, 시험방법에 관한 자료.",
                    "4. 새로운 시험방법을 사용하는 경우, 필요 시 밸리데이션 실시 보고서 또는 요약문.",
                    "5. (P.5.4) 변경 전후 최소 1배치(파일럿 배치 이상)에 대한 시험성적 비교자료.",
                    "6. 공정관리시험 및 기준의 추가, 삭제, 변경에 대한 타당성 입증 자료."
                ],
                "AR"
            )


# --- Content from: STEP 7_Title17.py ---
    elif current_title == "p4_17":
        satisfied = set(selections.get("p4_17_satisfied", []))

        # 판단조건 : 17a
        if satisfied == {"1"}:
            required_docs = [
                "1. 첨가제가 식물 또는 합성 기원임을 입증하는 제조업자의 확인서(statement)."
            ]
            show_result("17. 첨가제 기원의 변경", required_docs, "AR")

        # 판단조건 : 17b (모두 미충족)
        elif not satisfied:
            required_docs = [
                "2. (P.4) 첨가제의 관리에 관한 자료(기준 및 시험방법 등, 기 사용 예가 있는 경우 관련 자료 포함).",
                "3. (A.2) 외인성 물질에 대한 안전성 평가 자료(필요 시).",
                "4. 변경 전·후 첨가제의 규격(비교표 등 변경 전·후에 관한 자료) 및 성적서."
            ]
            show_result("17. 첨가제 기원의 변경", required_docs, "Cmin")


# --- Content from: STEP 7_Title18.py ---
    elif current_title == "p4_18":
        satisfied = set(selections.get("p4_18_satisfied", []))

        # 판단조건 : 충족조건 1을 충족한 경우
        if satisfied == {"1"}:
            required_docs = [
                "1. 해당 변경에 대한 타당성 입증 자료.",
                "2. (P.4) 변경 전·후 규격 비교표 등 변경 전·후에 관한 자료, 변경하고자 하는 규격의 기준설정 근거자료, 시험방법에 관한 자료 및 밸리데이션 자료, 성적서."
            ]
            show_result("18. 별규에 해당하는 첨가제의 규격 또는 시험방법 변경", required_docs, "Cmin")


# --- Content from: STEP 7_Title19.py ---
    elif current_title == "p4_19":
        satisfied = set(selections.get("p4_19_satisfied", []))

        # 판단조건 : 충족조건 1을 충족한 경우
        if satisfied == {"1"}:
            required_docs = [
                "1. 첨가제의 규격 비교표 등 변경 전·후에 관한 자료."
            ]
            show_result("19. 식약처장이 인정하는 공정서 규격으로 첨가제 규격의 변경", required_docs, "AR")


# --- Content from: STEP 7_Title20.py ---
    elif current_title == "p7_20":
        conditions = selections.get("p7_20_conditions", [])
        if set(conditions) == {"1"}:
            required_docs = [
                "1. 용기·포장 재질 변경이 반영된 의약품의 성상.",
                "2. (P.2) (해당하는 경우) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료, 기허가 의약품에서 변경하고자 하는 용기·포장 재질의 사용례 등.",
                "3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.",
                "4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).",
                "6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약."
            ]
            show_result("비무균제제의 직접용기 및 포장 재질, 종류 변경", required_docs, "IR")
        else:
            required_docs = [
                "1. 용기·포장 재질 변경이 반영된 의약품의 성상.",
                "2. (P.2) (해당하는 경우) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료, 기허가 의약품에서 변경하고자 하는 용기·포장 재질의 사용례 등.",
                "3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.",
                "4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).",
                "5. (P.8.1) 안정성 요약문과 결론, 2배치(파일럿배치 이상) 이상에 대한 3개월 이상의 장기보존 및 가속 시험. 해당되는 경우, 광 가혹 시험 결과.",
                "6. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약."
            ]
            show_result("비무균제제의 직접용기 및 포장 재질, 종류 변경", required_docs, "Cmaj")


# --- Content from: STEP 7_Title21.py ---
    elif current_title == "p7_21":
        conditions = selections.get("p7_21_conditions", [])
        if set(conditions) == {"1"}:
            required_docs = [
                "1. 용기·포장 재질 변경이 반영된 의약품의 성상.",
                "2. (P.2) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료.",
                "3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.",
                "4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).",
                "5. (P.8.1) 안정성 요약문과 결론, 2배치(파일럿배치 이상)에 대한 3개월 이상의 장기보존 및 가속 시험.",
                "7. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약."
            ]
            show_result("무균제제의 직접용기 및 포장 재질, 종류 변경", required_docs, "Cmin")
        else:
            required_docs = [
                "1. 용기·포장 재질 변경이 반영된 의약품의 성상.",
                "2. (P.2) 현재의 포장 시스템에 비해 동등하거나 우수한 보호성을 입증하는 용기 마개 시스템의 적합성에 대한 자료. 기능성 포장을 변경하는 경우, 새로운 포장의 기능성을 입증하는 자료.",
                "3. (P.3) 직접 용기·포장의 재질 및 종류 변경이 반영된 제조방법 자료.",
                "4. (P.7) 변경하고자 하는 일차 포장 유형에 대한 정보(예: 성상, 일차 포장 구성 성분들의 구성 재료, 규격, 성적서 등).",
                "6. (P.8.1) 안정성 요약문과 결론, 생산 규모 3배치(최소 2배치 파일럿배치 이상)에 대한 6개월 이상의 장기보존 및 가속 시험. 해당되는 경우, 광 가혹 시험 결과.",
                "7. (P.8.2) 변경 후 제제의 생산규모 배치에 대한 안정성 시험 계획 및 이행서약."
            ]
            show_result("무균제제의 직접용기 및 포장 재질, 종류 변경", required_docs, "Cmaj")


# --- Content from: STEP 7_Title22.py ---
    elif current_title == "p7_22":
        selected_conditions = selections.get("p7_22_conditions", [])

        if set(["1", "2"]).issubset(selected_conditions):
            required_docs = [
                "1. (P.7) 규격 비교표 등 변경 전·후에 관한 자료, 변경하고자 하는 규격의 타당성 입증 자료."
            ]
            report_type = "AR"

        elif "2" in selected_conditions:
            required_docs = [
                "1. (P.7) 규격 비교표 등 변경 전·후에 관한 자료, 변경하고자 하는 규격의 타당성 입증 자료.",
                "2. (P.7) 추가 또는 삭제된 시험방법에 관한 자료."
            ]
            report_type = "AR"

        else:
            required_docs = []
            report_type = None

        if required_docs and report_type:
            show_result("22. 직접 포장의 규격 변경", required_docs, report_type)


# --- Content from: STEP 7_Title23.py ---
    # Title: 3.2.P.7 용기-마개 시스템 > 23. 포장단위 변경
    if current_title == "p7_23":
        satisfied = all(
            st.session_state.step6_selections.get("p7_23_req_1") == "충족" and
            st.session_state.step6_selections.get("p7_23_req_2") == "충족"
        )

        if satisfied:
            docs = [
                "1. (R.1) 포장단위 비교표 등 변경 전·후에 관한 자료"
            ]
            show_result("23. 포장단위 변경", docs, "IR")


# --- Content from: STEP 7_Title24.py ---
    # Title: 24. 새로운 디자인스페이스 도입 또는 허가된 디자인스페이스의 확장
    if current_title == "da_24":
        satisfied_a = st.session_state.step6_selections.get("da_24_case") == "24a"
        satisfied_b = st.session_state.step6_selections.get("da_24_case") == "24b"

        if satisfied_a or satisfied_b:
            docs = [
                "1. 변경에 따른 디자인 스페이스가 타당함을 입증하는 자료(위해평가 및 다변량 연구를 포함하여 디자인 스페이스를 구성하는 다양한 파라미터들의 상호작용에 대한 연구결과를 통해 도출되었음을 입증하는 자료)",
                "2. 표 형식으로 디자인 스페이스를 설명한 자료.",
                "3. 신청 서류의 변경과 관련된 CTD 자료."
            ]
            show_result("24. 새로운 디자인스페이스 도입 또는 허가된 디자인스페이스의 확장", docs, "Cmaj")

