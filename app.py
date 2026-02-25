import streamlit as st

st.set_page_config(page_title="Script Note Starter", page_icon="📝", layout="centered")

st.title("📝 Script Note Starter")
st.caption("가볍게 시작하는 Streamlit 템플릿")

st.subheader("오늘의 체크리스트")
items = [
    "README 작성/수정",
    "앱 실행 확인",
    "GitHub 업로드",
]

checked_count = 0
for idx, item in enumerate(items):
    done = st.checkbox(item, key=f"todo_{idx}")
    if done:
        checked_count += 1

progress = checked_count / len(items)
st.progress(progress)
st.write(f"진행률: **{int(progress * 100)}%**")

st.subheader("메모")
note = st.text_area("아이디어나 TODO를 자유롭게 입력하세요", height=140)

if st.button("미리보기"):
    if note.strip():
        st.success("입력한 메모")
        st.write(note)
    else:
        st.warning("메모가 비어 있어요. 내용을 입력해 주세요.")
