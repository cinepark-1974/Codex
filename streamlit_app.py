 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/streamlit_app.py b/streamlit_app.py
new file mode 100644
index 0000000000000000000000000000000000000000..8596f7f3033a6a210af3394380464f792ed4e1ec
--- /dev/null
+++ b/streamlit_app.py
@@ -0,0 +1,107 @@
+import json
+import os
+from pathlib import Path
+
+import streamlit as st
+
+from core.pdf_extract import extract_pdf_text
+from core.analyze import analyze_script
+
+OUTPUT_DIR = os.getenv("OUTPUT_DIR", "outputs")
+os.makedirs(OUTPUT_DIR, exist_ok=True)
+
+st.set_page_config(page_title="Blue Jeans Script Doctor", layout="wide")
+
+
+def load_runs():
+    runs = []
+    for meta_path in Path(OUTPUT_DIR).glob("*/meta.json"):
+        try:
+            with open(meta_path, encoding="utf-8") as f:
+                m = json.load(f)
+            m["run_dir"] = str(meta_path.parent)
+            runs.append(m)
+        except Exception:
+            continue
+    return sorted(runs, key=lambda x: x.get("updated_at", ""), reverse=True)
+
+
+st.title("Blue Jeans Script Doctor v1.2")
+page = st.radio("화면", ["홈/목차", "상세 리포트"], horizontal=True)
+
+if page == "홈/목차":
+    up = st.file_uploader("PDF 시나리오 업로드", type=["pdf"])
+    col1, col2, col3 = st.columns(3)
+    q = col1.text_input("검색(제목)")
+    sort_by = col2.selectbox("정렬", ["Updated", "Final"])
+    genre_filter = col3.text_input("필터(장르)")
+
+    if up and st.button("분석 실행"):
+        with st.spinner("분석 중"):
+            text, pages = extract_pdf_text(up)
+            if not text.strip():
+                st.error("PDF 텍스트 추출이 원활하지 않았다. 다른 PDF로 재시도하는 편이 좋다.")
+            else:
+                result = analyze_script(text, pages, up.name, OUTPUT_DIR)
+                st.success("분석이 완료되었다.")
+                st.session_state["last_run_dir"] = result["run_dir"]
+
+    runs = load_runs()
+    if q:
+        runs = [r for r in runs if q.lower() in r.get("title", "").lower()]
+    if genre_filter:
+        runs = [r for r in runs if genre_filter.lower() in r.get("genre", "드라마").lower()]
+    if sort_by == "Final":
+        runs = sorted(runs, key=lambda x: x["scores"]["final"], reverse=True)
+
+    for r in runs:
+        with st.container(border=True):
+            st.subheader(r.get("title", "Untitled"))
+            st.write(f"Updated: {r.get('updated_at','-')}")
+            st.write(f"Final: {r['scores']['final']:.1f}")
+            st.write(f"4축: S {r['scores']['structure']}, H {r['scores']['hero']}, C {r['scores']['concept']}, G {r['scores']['genre']}")
+            if st.button(f"상세 보기 {r['run_id']}"):
+                st.session_state["selected_run_dir"] = r["run_dir"]
+                st.rerun()
+
+else:
+    run_dir = st.session_state.get("selected_run_dir") or st.session_state.get("last_run_dir")
+    if not run_dir:
+        st.info("먼저 홈에서 분석을 실행하는 편이 좋다.")
+    else:
+        try:
+            with open(Path(run_dir)/"meta.json", encoding="utf-8") as f:
+                meta = json.load(f)
+            coverage = Path(run_dir, "coverage.md").read_text(encoding="utf-8")
+            rewrite = Path(run_dir, "rewrite.md").read_text(encoding="utf-8")
+        except Exception:
+            st.error("리포트 로딩이 원활하지 않았다. 다시 선택하는 편이 좋다.")
+            st.stop()
+
+        left, right = st.columns([2, 3])
+        with left:
+            docx_path = next(Path(run_dir).glob("시나리오검토보고서_*_Blue.docx"), None)
+            if docx_path and docx_path.exists():
+                st.download_button("보고서 다운로드", data=docx_path.read_bytes(), file_name=docx_path.name)
+        with right:
+            st.write(f"제목: {meta['title']} | 장르: {meta.get('genre','드라마')} | 버전: {meta['prompt_version']} | 작성일: {meta['updated_at']}")
+            zpath = Path(run_dir)/"results.zip"
+            if zpath.exists():
+                st.download_button("results.zip 다운로드", data=zpath.read_bytes(), file_name="results.zip")
+
+        if not meta.get("llm_success", True):
+            st.warning("분석이 완료되지 않았다. 재시도 버튼을 사용하는 편이 좋다.")
+            if st.button("재시도"):
+                st.rerun()
+
+        st.markdown(coverage)
+        # 차트 재생성 표시
+        from core.viz import create_charts
+        fig1, fig2, _, _, ok = create_charts(run_dir)
+        if ok:
+            st.plotly_chart(fig1, use_container_width=True)
+            st.plotly_chart(fig2, use_container_width=True)
+        else:
+            st.warning("차트 렌더링이 원활하지 않았다. 결과 파일은 계속 확인 가능하다.")
+
+        st.markdown(rewrite)
 
EOF
)
