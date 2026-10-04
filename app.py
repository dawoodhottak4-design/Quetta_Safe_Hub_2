import streamlit as st
from crew import run_safe_hub_pipeline

# -------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -------------------------------------------------------------
st.set_page_config(
    page_title="Quetta Safe Hub 2.0 | Civic Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------
# 2. CUSTOM EXECUTIVE CSS
# -------------------------------------------------------------
CUSTOM_CSS = """
<style>
    /* Main Layout Padding */
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
    
    /* Executive Header Card */
    .header-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }
    .header-title {
        font-size: 2.1rem;
        font-weight: 700;
        margin: 0;
        color: #f8fafc;
    }
    .header-subtitle {
        font-size: 1rem;
        color: #94a3b8;
        margin-top: 6px;
        margin-bottom: 0;
    }
    
    /* Primary Submit Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-weight: 600;
        background-color: #0284c7;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0369a1;
        color: white;
        border: none;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -------------------------------------------------------------
# 3. SIDEBAR CONTROLS & STATUS
# -------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/isometric-headers/100/shield.png", width=65)
    st.title("Control Panel")
    st.caption("Quetta Safe Hub 2.0 Engine")
    
    st.divider()
    st.markdown("### 📊 System Health")
    st.success("🟢 Framework: CrewAI Multi-Agent")
    st.info("⚡ Model: Groq GPT-OSS-120B")
    
    st.divider()
    st.markdown("### 📍 Hotspot Presets")
    st.caption("Common assessment areas in Quetta:")
    
    quick_areas = [
        "Sariab Road Drainage & Traffic",
        "Airport Road Peak Hour Hazards",
        "Spini Road Street Lighting & Roads",
        "Serena Chowk & Cantt Area Safety"
    ]
    for area in quick_areas:
        st.code(area, language="text")
        
    st.divider()
    st.caption("Balochistan Civic Intelligence Network")

# -------------------------------------------------------------
# 4. DASHBOARD HEADER & METRICS
# -------------------------------------------------------------
HEADER_HTML = """
<div class="header-box">
    <h1 class="header-title">🛡️ Quetta Safe Hub 2.0</h1>
    <p class="header-subtitle">Autonomous Civic Safety & Risk Intelligence Network for Quetta City</p>
</div>
"""
st.markdown(HEADER_HTML, unsafe_allow_html=True)

# Executive Metric Cards
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.metric(label="Active Agents", value="3 Agents", delta="Researcher, Analyst, Advisor")
with m_col2:
    st.metric(label="Inference Provider", value="Groq Cloud", delta="Ultra-Low Latency")
with m_col3:
    st.metric(label="Target Region", value="Quetta, PK", delta="Provincial Capital")

st.divider()

# -------------------------------------------------------------
# 5. INPUT SECTION
# -------------------------------------------------------------
st.markdown("### 🔍 Initiate Civic Risk Assessment")

user_input = st.text_input(
    label="Enter location, intersection, or specific civic issue:",
    placeholder="e.g., Traffic hazards, sewerage blockage, and road damage on Spini Road Quetta",
    help="Type any location or hazard in Quetta to trigger automated multi-agent risk assessment."
)

btn_col, _ = st.columns([1, 2])
with btn_col:
    submit_btn = st.button("🚀 Generate Safety Report", type="primary")

# -------------------------------------------------------------
# 6. PIPELINE EXECUTION & REPORT DISPLAY
# -------------------------------------------------------------
if submit_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter a location or civic concern before generating the report.")
    else:
        st.markdown("---")
        st.markdown("#### 🔄 Agent Workflow Progress")
        
        # Real-time Status Tracker
        with st.status("Executing Multi-Agent Assessment...", expanded=True) as status:
            st.write("🕵️ **Researcher Agent:** Gathering area context and local incident patterns...")
            st.write("📈 **Analyst Agent:** Evaluating threat severity, impact zones, and risk levels...")
            st.write("📋 **Advisor Agent:** Synthesizing public safety advisories and municipal action plans...")
            
            try:
                # Call CrewAI Orchestration
                final_report = run_safe_hub_pipeline(user_input)
                status.update(label="✅ Assessment Completed Successfully!", state="complete", expanded=False)
                
                st.success("Analysis Complete!")
                
                # Render Report Output
                st.markdown("### 📋 Executive Civic Safety Briefing")
                report_str = str(final_report)
                
                # Display output cleanly
                st.markdown(report_str)
                
                st.divider()
                
                # Download Button for Executive Markdown Report
                st.download_button(
                    label="📥 Download Executive Report (.md)",
                    data=report_str,
                    file_name=f"Quetta_Safety_Report_{user_input.replace(' ', '_')}.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                status.update(label="❌ Execution Failed", state="error", expanded=True)
                st.error(f"Execution Error: {str(e)}")
                st.info("Tip: Ensure GROQ_API_KEY is properly saved in Streamlit Secrets.")
