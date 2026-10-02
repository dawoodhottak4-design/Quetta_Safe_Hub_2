import streamlit as st
from crew import run_safe_hub_pipeline

# Page Configuration
st.set_page_config(
    page_title="Quetta Safe Hub 2.0",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Quetta Safe Hub 2.0")
st.subtitle("Autonomous Civic Safety & Intelligence Network")

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
        with st.spinner("Analyzing safety data and generating response..."):
            try:
                # Execution
                final_report = run_safe_hub_pipeline(user_input)
                
                st.success("Analysis Complete!")
                st.divider()
                
                # Output display
                st.markdown("### 📋 Civic Safety Intelligence Report")
                st.markdown(str(final_report))
                
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")
                st.info("Tip: Ensure your Gemini API key is valid and has active quota.")
