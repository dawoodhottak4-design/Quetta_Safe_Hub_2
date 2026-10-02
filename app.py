import streamlit as st
from crew import run_safe_hub_pipeline

# Page Configuration
st.set_page_config(
    page_title="Quetta Safe Hub 2.0",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Quetta Safe Hub 2.0")
st.caption("Autonomous Civic Safety & Intelligence Network (Powered by Groq & CrewAI)")

st.markdown("""
Welcome to **Quetta Safe Hub**. Enter a specific civic issue, area name (e.g., *Spini Road traffic*, *Sariab Road infrastructure*), or general safety topic below to generate a real-time risk assessment report.
""")

st.divider()

# Input area
user_input = st.text_input(
    "Enter location or safety issue to analyze:",
    placeholder="e.g., Traffic hazards and road conditions on Airport Road Quetta"
)

if st.button("Generate Safety Report", type="primary"):
    if not user_input.strip():
        st.warning("Please enter a valid topic or area name.")
    else:
        # Line 30 updated according to openai/gpt-oss-120b model
        with st.spinner("Analyzing safety data with Groq GPT-OSS-120B..."):
            try:
                final_report = run_safe_hub_pipeline(user_input)
                
                st.success("Analysis Complete!")
                st.divider()
                
                st.markdown("### 📋 Civic Safety Intelligence Report")
                st.markdown(str(final_report))
                
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")
                st.info("Tip: Ensure GROQ_API_KEY is saved in Streamlit Secrets.")
