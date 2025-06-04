Step6에서 질문내용B의 내용 1을 ‘충족’으로 선택하였다.

if "s1_1" in step6_targets:
    if step6_selections.get("s1_1_req_1") == "충족":
        step7_outputs["s1_1"] = """보고유형은 다음과 같습니다.
 
AR, 연차보고
「의약품의 품목허가‧신고‧심사 규정」 제3조의2 제2항 및 제4항에 따른 연차보고(Annual Report, AR) 수준의 변경사항입니다.

필요서류는 다음과 같습니다.

1. (S.1.1) 공정서 또는 국제 의약품 일반명 리스트(INN, The International Nonproprietary Name) 등 근거서류.
2. 개정된 제품정보"""

Step6에서 질문내용A의 내용이 2a.에서 ‘변경 있음’으로 선택하고, Step6에서 질문내용B의 내용 3, 4, 9를 ‘충족’으로 선택하고, 동시에 1, 2, 5, 6, 7, 8, 10을 ‘미충족’으로 선택하였다.

if "s2_2" in step6_targets:
    if (
        step6_selections.get("s2_2_sub_2a") == "변경 있음" and
        step6_selections.get("s2_2_req_3") == "충족" and
        step6_selections.get("s2_2_req_4") == "충족" and
        step6_selections.get("s2_2_req_9") == "충족" and
        step6_selections.get("s2_2_req_1") == "미충족" and
        step6_selections.get("s2_2_req_2") == "미충족" and
        step6_selections.get("s2_2_req_5") == "미충족" and
        step6_selections.get("s2_2_req_6") == "미충족" and
        step6_selections.get("s2_2_req_7") == "미충족" and
        step6_selections.get("s2_2_req_8") == "미충족" and
        step6_selections.get("s2_2_req_10") == "미충족"
    ):
        step7_outputs["s2_2"] = """보고유형은 다음과 같습니다.

IR, 시판전보고
「의약품의 품목허가‧신고‧심사 규정」 제3조의2제4항 단서조항에 따른 시판전 보고(Immediate Report, IR) 수준의 변경사항입니다.

필요서류는 다음과 같습니다.

1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.
2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.
4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우)제조 공정에 관한 자료.
10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당되는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료."""

Step6에서 질문내용A의 내용이 2a.에서 ‘변경 있음’으로 선택하고, Step6에서 질문내용B의 내용 1, 2, 3, 4, 5, 6, 7, 8, 9, 10을 ‘미충족’으로 선택하였다.

if "s2_2" in step6_targets:
    if (
        step6_selections.get("s2_2_sub_2a") == "변경 있음" and
        step6_selections.get("s2_2_req_1") == "미충족" and
        step6_selections.get("s2_2_req_2") == "미충족" and
        step6_selections.get("s2_2_req_3") == "미충족" and
        step6_selections.get("s2_2_req_4") == "미충족" and
        step6_selections.get("s2_2_req_5") == "미충족" and
        step6_selections.get("s2_2_req_6") == "미충족" and
        step6_selections.get("s2_2_req_7") == "미충족" and
        step6_selections.get("s2_2_req_8") == "미충족" and
        step6_selections.get("s2_2_req_9") == "미충족" and
        step6_selections.get("s2_2_req_10") == "미충족"
    ):
        step7_outputs["s2_2"] = """보고유형은 다음과 같습니다.

Cmaj, 변경허가(신고)
「의약품의 품목허가‧신고‧심사 규정」 제3조의2(의약품의 허가‧신고의 변경 처리) 및 제6조(국제공통기술문서 작성)에 따라 원료의약품과 완제의약품의 제조원 또는 제조방법 중 품질에 중요한 영향을 미치는 변경허가(신고) 신청(Change, C) 대상에 해당하며, 변경사항의 중요도, 충족조건 및 제출자료 요건의 난이도 등을 고려하였을 때 Major change(Cmaj)수준의 변경사항입니다.

필요서류는 다음과 같습니다.

1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.
2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.
3. (S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.
4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우)제조 공정에 관한 자료.
7. (S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.
10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당되는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료.
11. (S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."""

Step6에서 질문내용A의 내용이 2b.에서 ‘변경 있음’으로 선택하고, Step6에서 질문내용B의 내용 3, 5를 ‘충족’으로 선택하고, 동시에 1, 2, 4, 6, 7, 8, 9, 10을 ‘미충족’으로 선택하였다.

if "s2_2" in step6_targets:
    if (
        step6_selections.get("s2_2_sub_2b") == "변경 있음" and
        step6_selections.get("s2_2_req_3") == "충족" and
        step6_selections.get("s2_2_req_5") == "충족" and
        step6_selections.get("s2_2_req_1") == "미충족" and
        step6_selections.get("s2_2_req_2") == "미충족" and
        step6_selections.get("s2_2_req_4") == "미충족" and
        step6_selections.get("s2_2_req_6") == "미충족" and
        step6_selections.get("s2_2_req_7") == "미충족" and
        step6_selections.get("s2_2_req_8") == "미충족" and
        step6_selections.get("s2_2_req_9") == "미충족" and
        step6_selections.get("s2_2_req_10") == "미충족"
    ):
        step7_outputs["s2_2"] = """보고유형은 다음과 같습니다.

IR, 시판전보고
「의약품의 품목허가‧신고‧심사 규정」 제3조의2제4항 단서조항에 따른 시판전 보고(Immediate Report, IR) 수준의 변경사항입니다.

필요서류는 다음과 같습니다.

1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.
2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.
4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우)제조 공정에 관한 자료.
8. (S.2) 원료의약품 및 핵심(최종) 중간체(해당되는 경우) 합성 경로, 사용 원료, 품질 관리 절차 및 규격 변경이 없다는 확인서(statement).
10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당되는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료."""

Step6에서 질문내용A의 내용이 2c.에서 ‘변경 있음’으로 선택하고, Step6에서 질문내용B의 내용 1, 2, 3, 6, 7, 8을 ‘충족’으로 선택하고, 동시에 4, 5, 9, 10을 ‘미충족’으로 선택하였다.

if "s2_2" in step6_targets:
    if (
        step6_selections.get("s2_2_sub_2c") == "변경 있음" and
        step6_selections.get("s2_2_req_1") == "충족" and
        step6_selections.get("s2_2_req_2") == "충족" and
        step6_selections.get("s2_2_req_3") == "충족" and
        step6_selections.get("s2_2_req_6") == "충족" and
        step6_selections.get("s2_2_req_7") == "충족" and
        step6_selections.get("s2_2_req_8") == "충족" and
        step6_selections.get("s2_2_req_4") == "미충족" and
        step6_selections.get("s2_2_req_5") == "미충족" and
        step6_selections.get("s2_2_req_9") == "미충족" and
        step6_selections.get("s2_2_req_10") == "미충족"
    ):
        step7_outputs["s2_2"] = """보고유형은 다음과 같습니다.

IR, 시판전보고
「의약품의 품목허가‧신고‧심사 규정」 제3조의2제4항 단서조항에 따른 시판전 보고(Immediate Report, IR) 수준의 변경사항입니다.

필요서류는 다음과 같습니다.

1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.
2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.
4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우)제조 공정에 관한 자료.
5. (S.4.4) 변경 전·후 원료의약품 2배치(파일럿 배치 이상)에 대한 배치분석자료 .
8. (S.2) 원료의약품 및 핵심(최종) 중간체(해당되는 경우) 합성 경로, 사용 원료, 품질 관리 절차 및 규격 변경이 없다는 확인서(statement)."""

Step6에서 질문내용A의 내용이 2c.에서 ‘변경 있음’으로 선택하고, Step6에서 질문내용B의 내용 1, 2, 3, 4, 5, 6, 7, 8, 9, 10을 ‘미충족’으로 선택하였다.

if "s2_2" in step6_targets:
    if (
        step6_selections.get("s2_2_sub_2c") == "변경 있음" and
        step6_selections.get("s2_2_req_1") == "미충족" and
        step6_selections.get("s2_2_req_2") == "미충족" and
        step6_selections.get("s2_2_req_3") == "미충족" and
        step6_selections.get("s2_2_req_4") == "미충족" and
        step6_selections.get("s2_2_req_5") == "미충족" and
        step6_selections.get("s2_2_req_6") == "미충족" and
        step6_selections.get("s2_2_req_7") == "미충족" and
        step6_selections.get("s2_2_req_8") == "미충족" and
        step6_selections.get("s2_2_req_9") == "미충족" and
        step6_selections.get("s2_2_req_10") == "미충족"
    ):
        step7_outputs["s2_2"] = """보고유형은 다음과 같습니다.

Cmaj, 변경허가(신고)
「의약품의 품목허가‧신고‧심사 규정」 제3조의2(의약품의 허가‧신고의 변경 처리) 및 제6조(국제공통기술문서 작성)에 따라 원료의약품과 완제의약품의 제조원 또는 제조방법 중 품질에 중요한 영향을 미치는 변경허가(신고) 신청(Change, C) 대상에 해당하며, 변경사항의 중요도, 충족조건 및 제출자료 요건의 난이도 등을 고려하였을 때 Major change(Cmaj)수준의 변경사항입니다.

필요서류는 다음과 같습니다.

1. (해당되는 경우) 해당 품목을 제조하는 제조소에 ‘의약품 등의 안전에 관한 규칙’ 제48조의2에 따른 제조 및 품질관리기준 적합판정서, 해외 제조원인 경우 제4조제1항제4호에 따른 유효기간 내의 제조증명서.
2. (S.2.1) 제조소명, 주소, 책임부과범위 및 해당하는 경우 수탁업소에 관한 자료.
3. (S.2.5) 무균원료의약품 생산의 경우 (위험도 평가 결과에 따른) 무균공정에 대한 공정밸리데이션 자료 및 평가 자료.
4. 변경 전·후 제조소의 원료의약품, 중간체 또는 원료의약품 출발 물질 (해당되는 경우)제조 공정에 관한 자료.
5. (S.4.4) 변경 전·후 원료의약품 2배치(파일럿 배치 이상)에 대한 배치분석자료 .
6. (P.8.2) 원료의약품의 품질 특성이 완제의약품의 안정성에 영향을 미칠 수 있는 변경의 경우, 완제의약품 1배치(실제 생산 규모의)에 대한 안정성 시험 이행 계획서.
7. (S.4.1) 원료의약품 기준 및 시험방법에 관한 자료.
9. 변경 후 원료의약품이 완제의약품의 안전성, 유효성 및 품질에 미치는 영향에 대한 고찰자료.
10. 변경 전·후 출발 물질 또는 중간체의 최소 1배치에 대한 시험 성적서(해당되는 경우), 출발물질 또는 중간체 변경 전·후 최종 원료의약품 2배치에 대한 배치분석 자료.
11. (S.7.2) 변경 후 원료의약품의 안정성 시험 필요성 고찰 및 필요한 경우 안정성 시험 이행 계획서."""

Step6에서 질문내용B의 내용 1, 2, 3, 4, 5, 6, 7, 8을 ‘충족’으로 선택하고, 동시에 9를 ‘미충족’으로 선택하였다.

if "s2_3" in step6_targets:
    if (
        step6_selections.get("s2_3_req_1") == "충족" and
        step6_selections.get("s2_3_req_2") == "충족" and
        step6_selections.get("s2_3_req_3") == "충족" and
        step6_selections.get("s2_3_req_4") == "충족" and
        step6_selections.get("s2_3_req_5") == "충족" and
        step6_selections.get("s2_3_req_6") == "충족" and
        step6_selections.get("s2_3_req_7") == "충족" and
        step6_selections.get("s2_3_req_8") == "충족" and
        step6_selections.get("s2_3_req_9") == "미충족"
    ):
        step7_outputs["s2_3"] = """보고유형은 다음과 같습니다.

IR, 시판전보고
「의약품의 품목허가‧신고‧심사 규정」 제3조의2제4항 단서조항에 따른 시판전 보고(Immediate Report, IR) 수준의 변경사항입니다.

필요서류는 다음과 같습니다.

2. 변경 전·후 제조방법 비교표 등 변경 전·후에 관한 자료
3. (S.2.2) 변경하고자 하는 합성 공정 흐름도 및 상세 제조 공정에 관한 자료.
4. (S.2.3)(해당되는 경우) 변경하고자 하는 원료의약품 제조에 사용된 원료(예 : 원료약품, 출발 물질, 용매, 시약, 촉매)의 규격 및 시험 성적서.
11. (S.4.4) 변경 전·후 원료의약품 최소 2배치(파일럿 배치 이상)에 대한 배치분석 자료."""






















































































