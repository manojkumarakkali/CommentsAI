import streamlit as st
import openai

# Set your API key
openai.api_key = "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"

st.title("AI-Powered PL/SQL Comment Generator")

code_input = st.text_area("Paste your PL/SQL code here:", height=300)

if st.button("Generate Comments"):
    if code_input.strip():
        prompt = f"Add clear and meaningful comments to the following PL/SQL code:\n\n{code_input}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert Oracle PL/SQL developer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        commented_code = response['choices'][0]['message']['content']
        st.subheader("Code with AI-Generated Comments:")
        st.code(commented_code, language="sql")
    else:
        st.warning("Please paste some PL/SQL code.")
