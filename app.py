import streamlit as st
from crew import run_safe_hub_pipeline

# Page Configuration
st.set_page_config(
    page_title="Quetta Safe Hub 2.0 | Civic Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Executive CSS
st.markdown("""
<style>
    /* Global Container Padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    
    /* Header Container Styling */
    .header-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        border: 1px solid #334155;
        margin-bottom: 24px;
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        color: #f8fafc;
    }
    .header-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-top: 6px;
        margin-bottom: 0;
    }
    
    /* Metric Card Styling */
    .metric-card {
        background-color: #1e293b;
        border-left: 4px solid #0284c7;
        padding: 16px;
        border-radius: 8px;
        color: #f8fafc;
        margin-bottom: 15px;
    }

    /* Primary Action Button */
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
        border: none;
    }
</style>
""", unsafe_allow_textarea=True)

# -------------------------------------------------------------
# SIDEBAR CONTROLS & METRICS
# -------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/isometric-headers/100/shield.png", width=70)
    st.title("Control Panel")
    st.caption("Quetta Safe Hub 2.0 Engine")
    
    st.divider()
    
    st.markdown("### 📊 System Status")
    st.success("🟢 Core Framework: CrewAI Multi-Agent")
    st.info("⚡ Inference: Groq GPT-OSS-120B")
    
    st.divider()
    
    st.markdown("### 📍 Quick Hotspot Presets")
    st.caption("Click to copy common areas:")
    quick_areas = [
        "Sariab Road Drainage & Traffic",
        "Airport Road Peak Hour Hazards",
        "Spini Road Street Lighting & Roads",
        "Serena Chowk & Cantt Area Safety"
    ]
    for area in quick_areas:
        st.code(area, language="text")
        
    st.divider()
    st.caption("Built for Balochistan Civic Risk Intelligence")

# -------------------------------------------------------------
# MAIN DASHBOARD HEADER
# -------------------------------------------------------------
st.markdown("""
<div class="header-box">
    <h1 class="header-title">🛡️ Quetta Safe Hub 2.0</h1>
    <p class="header-subtitle">Autonomous Civic Safety & Risk Intelligence Network for Quetta City</p>
</div>
""", unsafe_allow_html=True)

# Top Status Indicators
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Active Agents", value="3 Agents", delta="Researcher, Analyst, Advisor")
with col2:
    st.metric(label="Inference Provider", value="Groq Cloud", delta="Ultra Low Latency")
with col3:
    st.metric(label="Target Region", value="Quetta, Pakistan", delta="Provincial Capital")

st.divider()

# Input Form Area
st.markdown("### 🔍 Initiate Civic Risk Analysis")

# Pre-populating query from selection if needed
user_input = st.text_input(
    "Enter location, intersection, or specific civic concern:",
    placeholder="e.g., Traffic hazards, pothole issues, and drainage near Spini Road Quetta",
    help="Enter any road, chowk, or infrastructure problem in Quetta for real-time multi-agent evaluation."
)

col_btn, col_blank = st.columns([1, 2])
with col_btn:
    submit_btn = st.button("🚀 Generate Safety Report", type="primary")

# -------------------------------------------------------------
# EXECUTION & OUTPUT
# -------------------------------------------------------------
if submit_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter a valid location or civic topic before starting analysis.")
    else:
        st.markdown("---")
        st.markdown("#### 🔄 Agent Workflow Progress")
        
        # Status Box for Execution Steps
        with st.status("Executing Multi-Agent Assessment...", expanded=True) as status:
            st.write("🕵️ **Researcher Agent:** Scanning location context and incident history...")
            st.write("📈 **Analyst Agent:** Categorizing risk severity and impact zones...")
            st.write("📋 **Advisor Agent:** Formulating public safety advisories and municipal actions...")
            
            try:
                final_report = run_safe_hub_pipeline(user_input)
                status.update(label="✅ Safety Analysis Completed Successfully!", state="complete", expanded=False)
                
                st.success("Analysis Complete!")
                
                # Render Report
                st.markdown("### 📋 Executive Civic Safety Report")
                
                report_str = str(final_report)
                
                # Display in formatted Container
                st.markdown(f"""
                <div style="background-color: #0f172a; padding: 24px; border-radius: 10px; border: 1px solid #334155;">
                    {report_str}
                </div>
                """, unsafe_allow_html=True)
                
                st.divider()
                
                # Action Buttons
                st.download_button(
                    label="📥 Download Report (.md)",
                    data=report_str,
                    file_name=f"Quetta_Safety_Report_{user_input.replace(' ', '_')}.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                status.update(label="❌ Execution Failed", state="error", expanded=True)
                st.error(f"Execution Error: {str(e)}")
                st.info("Tip: Verify your GROQ_API_KEY configuration in Streamlit Secrets.")
