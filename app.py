import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key="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")
# Streamlit page settings
st.set_page_config(page_title="AI-Powered PL/SQL Comment Generator", layout="centered")
st.title("AI-Powered PL/SQL Comment Generator")
st.write("Paste your PL/SQL code below and generate meaningful comments using AI.")

# Text area for PL/SQL input
plsql_code = st.text_area("Paste your PL/SQL code here:", height=300)

# Button to generate comments
if st.button("Generate Comments"):
    if not plsql_code.strip():
        st.error("Please enter some PL/SQL code.")
    else:
        with st.spinner("Generating comments..."):
            try:
                # Call OpenAI API with new syntax
                response = client.chat.completions.create(
                    model="gpt-4o",  # Use gpt-4o or gpt-4-turbo for best performance
                    messages=[
                        {"role": "system", "content": "You are an expert PL/SQL developer."},
                        {"role": "user", "content": f"Add detailed comments to the following PL/SQL code:\n{plsql_code}"}
                    ],
                    temperature=0.3
                )

                # Extract AI-generated comments
                comments = response.choices[0].message.content

                # Display results
                st.subheader("Generated Comments:")
                st.code(comments, language="sql")

                # Option to download commented code
                st.download_button(
                    label="Download Commented Code",
                    data=comments,
                    file_name="commented_plsql.sql",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")

