import streamlit as st
import random
import pandas as pd
<<<<<<< HEAD
import streamlit.components.v1 as components
import os
=======
from datetime import datetime
>>>>>>> 2fe242d (Initial commit)

st.set_page_config(
    page_title="Smart Paddy AI",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Minimal custom CSS for things Streamlit doesn't natively support (like gradient headers and status badges)
st.markdown("""
    <style>
    .gradient-header {
        background: linear-gradient(135deg, #2ecc71, #27ae60);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(46, 204, 113, 0.3);
    }
    .badge-safe { background-color: #2ecc71; color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 14px;}
    .badge-warning { background-color: #f1c40f; color: #333; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 14px;}
    .badge-danger { background-color: #e74c3c; color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 14px;}
    .live-feed { border-radius: 10px; overflow: hidden; position: relative; border: 2px solid #2ecc71;}
    </style>
""", unsafe_allow_html=True)

# Mock Data (Backend State)
if 'alerts' not in st.session_state:
    st.session_state.alerts = [
        {"id": 1, "type": "Stem Borer Worm", "severity": "High", "time": "10 Mins Ago", "status": "Infected"},
        {"id": 2, "type": "Leaf Folder", "severity": "Medium", "time": "2 Hours Ago", "status": "Risk"},
    ]

# Navigation Sidebar
st.sidebar.title("🌾 Smart Paddy AI")
page = st.sidebar.radio("Navigation", ["Home", "Monitoring", "Alerts", "Suggestions", "Manual", "Helpline"])

st.sidebar.divider()
st.sidebar.info("System is Online 🟢")

def home_page():
    st.markdown('<div class="gradient-header"><h1>🌾 Smart Paddy Dashboard</h1></div>', unsafe_allow_html=True)

    health_status = "Infected" if any(a['status'] == 'Infected' for a in st.session_state.alerts) else "Healthy"
    status_badge = "badge-danger" if health_status == "Infected" else "badge-safe"
    latest_msg = random.choice(["No pests detected.", "Warning: Stem borer activity possible.", "All clear."])

    # Top metrics using native columns
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Field Status")
            st.markdown(f'<span class="{status_badge}">STATUS: {health_status.upper()}</span>', unsafe_allow_html=True)
            st.caption("Updated just now")
    with col2:
        with st.container(border=True):
            st.subheader("Latest Detection")
            st.write(latest_msg)
            st.caption("AI Vision Sensor 1")
    
    st.write("### Recent Alerts")
    if not st.session_state.alerts:
        st.success("No active alerts! Your field is safe.")
    else:
        for alert in st.session_state.alerts:
            with st.container(border=True):
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.write(f"**{alert['type']}**")
                    st.caption(f"{alert['time']} • {alert['status']}")
                with col_b:
                    b_class = "badge-danger" if alert['severity'] == "High" else "badge-warning"
                    st.markdown(f'<div style="text-align: right;"><span class="{b_class}">{alert["severity"]}</span></div>', unsafe_allow_html=True)

def monitoring_page():
    st.markdown('<div class="gradient-header"><h2>📷 Live Field Monitoring</h2></div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        st.write("### Camera 1 - Main Paddy Field")
        st.markdown('<span class="badge-danger">🔴 LIVE</span>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        # Display image nicely using streamlit
        st.image("https://images.unsplash.com/photo-1590682680695-43b964a3ae17?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "28°C", "+1°C")
        col2.metric("Humidity", "65%", "-2%")
        col3.metric("Soil Moisture", "45%", "Optimal")
        
        if st.button("Capture High-Res Snapshot", use_container_width=True):
            st.success("Snapshot saved to gallery!")

def alerts_page():
    st.markdown('<div class="gradient-header"><h2>🔔 All Alerts</h2></div>', unsafe_allow_html=True)
    df = pd.DataFrame(st.session_state.alerts)
    st.dataframe(df, use_container_width=True, hide_index=True)

def suggestions_page():
    st.markdown('<div class="gradient-header"><h2>💡 AI Suggestions</h2></div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        st.subheader("🐛 Pest Control")
        st.warning("Based on recent activity, apply organic pesticide for Stem Borer immediately.")
    
    with st.container(border=True):
        st.subheader("💧 Irrigation")
        st.info("Increase water level by 2 inches for optimal growth this week.")

def manual_page():
    st.markdown('<div class="gradient-header"><h2>📖 Farming Manual</h2></div>', unsafe_allow_html=True)
    with st.expander("🐛 Pest Control Guide", expanded=True):
        st.write("Detailed instructions on handling common pests like Stem Borer and Leaf Folder. Use neem-based organic sprays as first line of defense.")
    with st.expander("💧 Water Management"):
        st.write("Maintain 2-3 inches of standing water during the vegetative stage to prevent weed growth.")

def helpline_page():
    st.markdown('<div class="gradient-header"><h2>📞 Farmer Helpline</h2></div>', unsafe_allow_html=True)
    farmers = [
        {"Name": "Ravi Kumar", "Crop": "Basmati", "Phone": "+91 9876543210", "Status": "Available"},
        {"Name": "Suresh Singh", "Crop": "Sona Masuri", "Phone": "+91 8765432109", "Status": "Busy"}
    ]
    st.dataframe(pd.DataFrame(farmers), use_container_width=True, hide_index=True)
    st.button("Contact Support Team", use_container_width=True)

# Route to the selected page
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
<<<<<<< HEAD
elif page == "History":
    history_page()
elif page == "Settings":
    settings_page()
elif page == "Home":
    # This reads the file from your 'templates' folder
    with open("templates/base.html", "r", encoding='utf-8') as f:
        html_content = f.read()
    
    # This 'injects' the HTML into your Streamlit app
    components.html(html_content, height=500)

elif page == "Monitoring":
    with open("templates/monitoring.html", "r", encoding='utf-8') as f:
        monitor_html = f.read()
    components.html(monitor_html, height=1000)
# Get the folder where app.py lives
current_dir = os.path.dirname(__file__)
if page == "Home":
    # 1. First, show the Dashboard (The Face)
    with open("templates/base.html", "r", encoding='utf-8') as f:
        html_content = f.read()
    components.html(html_content, height=500) # Reduced height so table fits below

    # 2. Then, show the alerts and table below it
    st.info("All clear.")
   
    # Your table data code goes here
    # st.table(df) or st.dataframe(df)
=======

>>>>>>> 2fe242d (Initial commit)
