import streamlit as st # type: ignore
from refactor import find_issues, fix_code, ai_suggestions

st.title("🧠 AI Code Refactoring Tool")

uploaded_file = st.file_uploader("Upload Python File", type=["py"])

if uploaded_file:
    code = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Original Code")
    st.code(code, language="python")

    if st.button("🔍 Analyze & Refactor"):

        issues = find_issues(code)

        st.subheader("⚠️ Issues Found")
        for i in issues:
            st.write("-", i)

        new_code = fix_code(code)

        st.subheader("✨ Refactored Code")
        st.code(new_code, language="python")

        try:
            exec(new_code)
            st.success("✅ Code runs successfully")
        except:
            st.error("❌ Error detected")

    if st.button("🤖 AI Suggestions"):

        suggestions = ai_suggestions(code)

        st.subheader("🤖 AI Suggestions")
        for s in suggestions:
            st.write("-", s)