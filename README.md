+# 👖 BLUE JEANS SCRIPT DOCTOR v1.2
+
+제품 매뉴얼 (실사용/개발 공용) — 풀버전
+Korean Terms First (English in parentheses) / 용어 유선(영문 병기)
+
+---
+
+## PART 1) 매뉴얼
+
+### 0. 한 줄 정의 (One-liner)
+
+Raw(작가의 젊은 감각) + Vintage(시간이 지나도 남는 깊이)를 보존하면서,
+헐리우드 스튜디오 커버리지(Studio Coverage) 수준으로 진단(커버리지, Coverage)하고,
+실제 작업에 바로 붙여 넣을 수 있는 개선안(리라이트/리라이팅, Rewrite)을 제공하는 Script Doctoring SaaS.
+
+#### 핵심 원칙
+- 원고의 결(Voice)을 훼손하지 않는다.
+- 억지 리라이팅 금지: 문제가 없으면 KEEP이 정답이다.
+- 모든 판단은 “근거(페이지/시퀀스)”와 연결한다.
+
+### A. 용어 유선(Glossary) — 문서/코드 공용
+- 커버리지(Coverage): 분석/평가/진단 리포트 본문(결론+근거 포함)
+- 닥터링(Doctoring): 문제-진단-처방(위험 포함) 설계
+- 워싱(Washing): 불순물 제거(인과/욕망/대가/장면 기능) 중심의 정제 작업
+- 시퀀스(Sequence): 시간/공간 변화 중심의 이야기 덩어리(최대 12개)
+- 리라이트(Rewrite): 실제 각본 형식으로 제공되는 개선본(개선본만)
+- 리포트(Report): 최종 사용자 다운로드 파일(기본: Word .docx 1개)
+
+### I. 브랜드 철학: Indigo Spirit
+1. **New & Classic**
+   - 원고의 에너지(New)를 훼손하지 않는다.
+   - 시간이 지나도 남는 클래식한 깊이(Classic)를 덧입힌다.
+2. **Freedom Fit**
+   - 정답 강요보다 작품이 가장 숨 쉬는 방향(Fit)을 제안한다.
+   - 문제가 없으면 KEEP이 답이다(억지 리라이팅 금지).
+3. **Innovative Washing**
+   - 표면(문장)보다 서사의 불순물(인과, 욕망, 대가, 장면 기능)을 먼저 걷어낸다.
+   - 분석 결과는 페이지/시퀀스 근거로 연결한다.
+
+### II. 사용자 플로우(SaaS User Flow)
+1. PDF 업로드(Upload)
+2. 분석 실행(멀티패스 파이프라인, Multi-pass Pipeline)
+3. 홈(카드형 목차, Index) 생성
+4. 상세 리포트(단일 스크롤, Detail) 확인
+5. 보고서 다운로드(Word .docx)
+
+#### 노출 원칙
+- 사용자에게는 기본적으로 “DOCX 보고서 1개”만 다운로드로 노출한다.
+- 내부적으로는 품질/재현성을 위해 run_id 기반 아카이브(내부 산출물)를 유지한다(운영/개발용).
+
+### III. 화면/리포트 구성(2페이지 UI)
+
+#### 1장: 홈(목차, Index) — 카드형 갤러리
+**카드 필수 요소**
+- 작품 제목(타이틀 디스커버리, Title Discovery: 본문에서 추출된 제목 우선)
+- Updated(최근 분석 시각)
+- Final Fit 점수(0.0~10.0, 소수점 1자리)
+
+**카드 옵션 요소**
+- 4축 점수: STRUCTURE/HERO/CONCEPT/GENRE
+
+#### 2장: 상세 리포트(Detail) — 단일 스크롤(섹션 고정)
+**상단 좌측 고정 버튼**
+- [보고서 다운로드] → `시나리오검토보고서_[작품제목]_Blue.docx`
+
+**섹션 순서(고정)**
+1. 로그라인 패키지(Logline Pack)
+2. 장점/보완점(Pros & Cons)
+3. 시놉시스 워싱(Synopsis Washing)
+4. 서사 동력(Narrative Drive)
+5. 캐릭터 배치(Hero/Villain/Protagonist)
+6. 대사 워싱(Dialogue Washing: 대사/서브텍스트)
+7. 3막 진단(3-Act Diagnosis: 전환점 페이지 근거)
+8. 15비트 시트(15-Beat Sheet)
+9. 비주얼 진단(Visual Diagnosis: 2종 고정)
+10. 워싱 테이블(Washing Table: Doctoring)
+11. 리라이트(Rewrite: Fitting Room)
+12. 샘플 리라이트(Sample Rewrite: 개선본만)
+
+### IV. 분석 메트릭(4축) & Final
+
+**4축 점수: 0.0~10.0, 소수점 1자리**
+- STRUCTURE(구성/플롯): 30%
+- HERO(캐릭터): 30%
+- CONCEPT(소재/컨셉): 20%
+- GENRE(장르 적합성): 20%
+
+**Final 공식**
+- `Final = 0.3S + 0.3H + 0.2C + 0.2G`
+- 소수점 1자리 반올림
+
+**판정(Verdict) — 점수 컷라인 금지**
+- 텍스트 판정 1줄 + 근거 3줄
+  1) 판단 핵심
+  2) 가장 큰 리스크 1개
+  3) 가장 큰 매력 1개
+
+### V. 로그라인 패키지(Logline Pack) 규칙 — 강제 삽입
+
+섹션 맨 위 고정 문장:
+
+> “Somebody wants something badly and is having difficulty getting it.”
+
+출력 구성:
+- Original Logline(원고에서 추출)
+- Washed Logline(시장 소구 강화 버전)
+- 체크리스트(최소 5요소)
+  - Somebody(주인공)
+  - Wants(욕망/목표)
+  - Difficulty(난관)
+  - Stakes(대가/리스크)
+  - Hook(차별점)
+
+### VI. 분석 파이프라인(Pipeline Engine) — 품질 고정 핵심
+1. 구조/사실 파싱(Structure & Fact Parsing)
+2. 시놉시스 워싱(Synopsis Washing)
+3. 커버리지 분석(Coverage Analysis)
+4. 닥터링 설계(Doctoring Design)
+5. 리라이트 생성(Rewrite Generation)
+
+### VII. 서사 동력(Narrative Drive) 규칙
+반드시 한눈에 제시:
+- 목적/욕망(Goal)
+- 상실/결핍(Loss/Need)
+- 해결 전략(Strategy)
+- 엔딩 회수(Ending Payoff): 1~2문장
+
+### VIII. 3막 & 15비트(헐리우드 표준)
+- 전환점은 사건 촉발/선택/대가/회수 흐름으로 설명한다.
+- 15비트는 상태(있음/약함/없음) + 근거 1~2줄로 출력한다.
+
+### IX. 비주얼 진단(Visual Diagnosis) — 2종 고정
+1. 긴장도 아크(Tension Arc: 12구간)
+2. 서사 점유율(Narrative Share: Donut)
+
+### X. 문제유형(고정 10개) & 라벨 규칙
+문제유형 10개:
+1) 목표 불명확
+2) 대가 약함
+3) 대립·압박 약함
+4) 인과 붕괴
+5) 리듬 늘어짐
+6) 정보 타이밍 문제
+7) 톤 흔들림
+8) 캐릭터 불일치
+9) 회수 부족
+10) 장면 기능 불명확
+
+라벨 규칙:
+- 시퀀스당 최대 2개
+- 3개 이상이면: “추가 이슈 존재: 구조적 수정이 필요할 수 있다.”
+
+### XI. 워싱 테이블(Washing Table: Doctoring) — 핵심
+- 시퀀스는 시간/공간 변화 중심, 최대 12개
+- 라벨 형식: 동사➡️동사 (예: 잠복➡️발각)
+- 표 필수 컬럼: 시퀀스/페이지 | 문제유형 | 진단 | 처방 | Risk
+- 처방 문장은 권고형 어미를 사용한다.
+
+### XII. 리라이트(Rewrite: Fitting Room) — 실사용 규격
+- 대상은 오프닝 훅 또는 치명상 구간 중 1개만 선택
+- 억지 리라이팅 금지 게이트 적용
+- 문제 없으면 고정 문구:
+  - “문제 구간 없음. 리라이팅 불필요.”
+  - “오프닝: KEEP”
+
+### XIII. 출력물(Export) — 사용자 노출/내부 아카이브 분리
+**사용자 노출**
+- `시나리오검토보고서_[작품제목]_Blue.docx`
+
+**내부 아카이브**
+- `coverage.md`, `rewrite.md`, `meta.json`, `charts/*.png`, `raw_analysis.json`
+- run_id 폴더 구조 저장
+
+### XIV. 디자인 시스템(The Denim Look)
+- Raw Ivory `#FFF9E5`
+- Midnight Blue `#191970`
+- Stitch Yellow `#FFCB05`
+- UI 폰트: Paperlogy, 본문: Pretendard, 각본: Courier New
+
+---
+
+## PART 2) 코딩용 프롬프트 엔진 설계 (Prompt Engine Spec)
+
+### 0) 목표
+- 멀티패스 5단계로 품질을 고정한다.
+- 최종 사용자 산출물은 DOCX 1개로 단순화한다.
+- 내부적으로 `meta.json` / `raw_analysis.json`으로 재현성을 확보한다.
+- 출력 언어는 한국어, 명령형 금지(권고형 종결 혼합).
+- 플랫폼(극장/OTT) 관련 필드는 v1.2에서 금지한다.
+
+### 1) 아키텍처 개요
+레이어:
+- UI(streamlit)
+- Core(파이프라인)
+- LLM Provider(OpenAI/Gemini)
+- Export(DOCX/chart/meta)
+
+환경변수:
+- `LLM_PROVIDER=openai|gemini`
+- `OPENAI_API_KEY`
+- `GEMINI_API_KEY`
+- `MODEL_NAME`
+- `OUTPUT_DIR` (기본 `./outputs`)
+- `PROMPT_VERSION`
+- `MAX_PAGES`, `MAX_TOKENS`, `RETRY_LIMIT`
+
+### 2) 입력 전처리 규격
+- PDF 텍스트 추출은 `pypdf` 사용
+- 빈 텍스트면 추출 실패 안내 + `meta.json`에 `extraction_status="empty"`
+- Scene/Character 후보는 휴리스틱으로 추출
+- 페이지 모드는 `script_page` 우선, 실패 시 `pdf_fallback`
+
+### 3) 파이프라인 PASS별 출력 스키마(엄격)
+모든 PASS는 JSON ONLY:
+- PASS1: `parse.json`
+- PASS2: `synopsis.json`
+- PASS3: `coverage.json`
+- PASS4: `doctoring.json`
+- PASS5: `rewrite.json`
+
+### 4) 프롬프트 템플릿 공통 규칙
+- 출력 언어 한국어
+- 명령형 금지
+- 근거는 1~2문장, 가능하면 페이지/시퀀스 참조
+- 사실/추측 분리
+- 플랫폼(극장/OTT) 언급 금지
+
+### 5) 품질 게이트(Quality Gates)
+- **G1 억지 리라이팅 금지:** 치명상 없으면 KEEP 고정 문구
+- **G2 리라이트 자동 검수:** 톤/인과/호칭 정합 검사
+- **G3 비용/속도 가드레일:** 토큰/리트라이/출력 길이 제한
+
+### 6) DOCX 렌더링 규격
+- `python-docx`로 Page 1~7 와이어프레임 고정
+- 차트 PNG 삽입
+- 판정/리스크/매력은 Stitch Yellow 콜아웃
+- 각본 블록은 Courier New
+
+### 7) 저장/보안/운영 최소 규칙
+- 원본 PDF는 결과 생성 후 기본 삭제
+- `meta.json`에 `model`, `prompt_version`, `run_id` 필수
+- 로그에 API 키/원문 전체 미기록(요약/해시만 허용)
+
+---
+
+## 부록 A) DOCX 레이아웃 와이어프레임
+- Page 1 COVER
+- Page 2 EXECUTIVE SUMMARY
+- Page 3 STORY CORE
+- Page 4 STRUCTURE
+- Page 5 VISUAL DIAGNOSIS
+- Page 6 WASHING TABLE
+- Page 7 REWRITE
+
+## 부록 B) 리포트 QA 체크
+- 첫 30초 결론 노출
+- Verdict 한 문장 강조
+- 리스크/매력 콜아웃 분리
+- 차트 2종 삽입
+- 장문 블록 최소화
 
EOF
)
