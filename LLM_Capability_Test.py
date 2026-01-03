import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

st.set_page_config(page_title="AI Text Generator", page_icon="✨")
st.title("✨ Generative AI Text Generator")

def comp(prompt, max_tokens=50):
    response = client.responses.create(
        model="gpt-4.1-mini",   # safer for deployment
        input=prompt,
        max_output_tokens=max_tokens,
    )
    return response.output_text


# UI
prompt = st.text_area(
    "Enter your prompt:",
    value="Write a success story of a Generative AI Engineer."
)

max_tokens = st.slider("Max tokens", 20, 300, 50)

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating..."):
            try:
                result = comp(prompt, max_tokens)
                st.subheader("Generated Output")
                st.write(result)
            except Exception as e:
                st.error("Something went wrong. Please try again.")
