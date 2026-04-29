import streamlit as st
import random
from datetime import datetime
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Smart Paddy AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for "farmer-friendly green theme"
st.markdown("""
    <style>
    :root {
        --primary-green: #2ecc71;
        --dark-green: #27ae60;
    }
    .stApp {
        background-color: #f4f6f8;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 10px rgba(46, 204, 113, 0.3);
    }
    .stButton>button:hover {
        background-color: #27ae60;
    }
    .status-safe { color: #2ecc71; font-weight: bold; }
    .status-warning { color: #f1c40f; font-weight: bold; }
    .status-danger { color: #e74c3c; font-weight: bold; }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Mock Data
if 'alerts' not in st.session_state:
    st.session_state.alerts = [
        {"id": 1, "type": "Stem Borer Worm", "severity": "High", "time": "10 Mins Ago", "status": "Infected"},
        {"id": 2, "type": "Leaf Folder", "severity": "Medium", "time": "2 Hours Ago", "status": "Risk"},
    ]

# Navigation Sidebar
st.sidebar.title("🌾 Smart Paddy AI")
page = st.sidebar.radio("Navigation", ["Home", "Monitoring", "Alerts", "Suggestions", "Manual", "Helpline", "History", "Settings"])

def home_page():
    st.title("Welcome to Smart Paddy AI")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    health_status = "Infected" if any(a['status'] == 'Infected' for a in st.session_state.alerts) else "Healthy"
    status_class = "status-danger" if health_status == "Infected" else "status-safe"
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Current Field Status")
        st.markdown(f'<h2 class="{status_class}">{health_status}</h2>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("Latest Detection")
        latest = random.choice(["No pests detected.", "Warning: Stem borer activity possible.", "All clear."])
        st.info(latest)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("Recent Alerts")
    if st.session_state.alerts:
        df = pd.DataFrame(st.session_state.alerts)
        st.dataframe(df, use_container_width=True)
    else:
        st.success("No recent alerts.")

def monitoring_page():
    st.title("📷 Live Field Monitoring")
    st.markdown("### Camera 1 - Main Paddy Field")
    # Placeholder for live camera feed
    st.image("https://images.unsplash.com/photo-1590682680695-43b964a3ae17?q=80&w=1000&auto=format&fit=crop", 
             caption="Live Feed", use_container_width=True)
    st.button("Capture Snapshot")

def alerts_page():
    st.title("🔔 Alerts")
    df = pd.DataFrame(st.session_state.alerts)
    st.table(df)

def suggestions_page():
    st.title("💡 AI Suggestions")
    st.info("Based on recent activity, we recommend applying organic pesticide for Stem Borer.")
    st.warning("Increase water level by 2 inches for optimal growth this week.")

def manual_page():
    st.title("📖 Farming Manual")
    st.write("Welcome to the comprehensive guide for paddy farming.")
    with st.expander("Pest Control Guide"):
        st.write("Detailed instructions on handling common pests like Stem Borer and Leaf Folder.")
    with st.expander("Water Management"):
        st.write("Best practices for maintaining water levels during different growth stages.")

def helpline_page():
    st.title("📞 Farmer Helpline")
    farmers = [
        {"Name": "Ravi Kumar", "Crop Type": "Basmati", "Phone": "+91 9876543210"},
        {"Name": "Suresh Singh", "Crop Type": "Sona Masuri", "Phone": "+91 8765432109"}
    ]
    st.table(pd.DataFrame(farmers))
    st.button("Call Support Expert")

def history_page():
    st.title("📜 Alert History")
    st.dataframe(pd.DataFrame(st.session_state.alerts), use_container_width=True)

def settings_page():
    st.title("⚙️ Settings")
    st.text_input("Farm Name", value="My Main Farm")
    st.selectbox("Notification Frequency", ["Immediate", "Hourly", "Daily summary"])
    st.checkbox("Enable SMS Alerts", value=True)
    st.button("Save Settings")

# Router
if page == "Home":
    home_page()
elif page == "Monitoring":
    monitoring_page()
elif page == "Alerts":
    alerts_page()
elif page == "Suggestions":
    suggestions_page()
elif page == "Manual":
    manual_page()
elif page == "Helpline":
    helpline_page()
elif page == "History":
    history_page()
elif page == "Settings":
    settings_page()
elif page == "Home":
    # This reads the file from your 'templates' folder
    with open("templates/base.html", "r", encoding='utf-8') as f:
        html_content = f.read()
    
    # This 'injects' the HTML into your Streamlit app
    components.html(html_content, height=1000, scrolling=True)

elif page == "Monitoring":
    with open("templates/monitoring.html", "r", encoding='utf-8') as f:
        monitor_html = f.read()
    components.html(monitor_html, height=1000)
    