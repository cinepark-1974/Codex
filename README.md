👖 BLUE JEANS REWRITE ENGINE v1.0

간단한 **스크립트/아이디어 노트 앱** 시작 템플릿입니다.

- `README.md`: 프로젝트 설명
- `app.py`: 실행 가능한 Streamlit 앱
- `requirements.txt`: 필요한 패키지
- `.env.example`: 환경변수 샘플
- `.gitignore`: 불필요 파일 제외

---

## 1) 프로젝트 목적

빠르게 실행 가능한 Python 웹앱(Streamlit) 기본 구조를 제공해,
GitHub에 올리자마자 바로 개발을 시작할 수 있도록 돕습니다.

---

## 2) 실행 방법

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

브라우저에서 안내된 주소(보통 `http://localhost:8501`)로 접속하세요.

---

## 3) 주요 기능

- 프로젝트 제목 표시
- 오늘 할 일(To-Do) 체크박스
- 간단한 메모 입력 및 미리보기
- 진행도(Progress bar) 표시

---

## 4) GitHub에 직접 파일 만들 때 체크리스트

아래 파일까지 같이 만들면 초기에 훨씬 편합니다.

1. `README.md`  
2. `app.py`  
3. `requirements.txt`  
4. `.gitignore`  
5. `.env.example`  

선택(권장):
- `LICENSE` (배포/공유 예정이면)
- `tests/` (기능이 늘어나면)

---

## 5) 다음 확장 아이디어

- 로그인 기능 추가
- 파일 업로드 기능 추가
- 메모를 로컬 파일 또는 DB에 저장
- 배포(Streamlit Community Cloud / Render / Railway)
