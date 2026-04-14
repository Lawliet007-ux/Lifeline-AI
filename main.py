import streamlit as st
import random
import time

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="LifeLine AI",
    page_icon="🚑",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")

logo = st.sidebar.file_uploader("Upload your logo", type=["png", "jpg"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Simulation Controls")
simulate = st.sidebar.button("🚨 Simulate Accident")

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 6])

with col1:
    if logo:
        st.image(logo, width=80)

with col2:
    st.title("🚑 LifeLine AI")
    st.markdown("### Smart Accident Detection System")

st.markdown("---")

# ---------------- HERO SECTION ----------------
st.markdown("""
### 🚨 Every 4 minutes, someone dies in a road accident.

Not always because of the crash…  
But because help didn’t arrive on time.

**The problem is delay.**

## 💡 Introducing: LifeLine AI
An intelligent system that detects accidents instantly and alerts help.
""")

st.markdown("---")

# ---------------- FEATURES ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📱 Sensors", "Accelerometer + Gyroscope")
col2.metric("📍 Tracking", "Real-time GPS")
col3.metric("🤖 AI Model", "False Alert Reduction")

st.markdown("---")

# ---------------- DASHBOARD ----------------
st.subheader("📊 Live Detection Dashboard")

status_box = st.empty()
data_box = st.empty()
alert_box = st.empty()

def generate_data():
    return {
        "speed": random.randint(0, 120),
        "impact": random.uniform(0, 10),
        "rotation": random.uniform(0, 180),
        "gps": f"{round(random.uniform(28.4,28.9),5)}, {round(random.uniform(77.0,77.5),5)}"
    }

def predict_severity(data):
    score = data["impact"] * 2 + data["rotation"] * 0.05 + data["speed"] * 0.1
    
    if score > 20:
        return "🚨 Severe Crash"
    elif score > 10:
        return "⚠️ Moderate Impact"
    else:
        return "✅ Safe"

# ---------------- LIVE LOOP ----------------
if simulate:
    for i in range(10):
        data = generate_data()
        severity = predict_severity(data)

        # STATUS
        if "Severe" in severity:
            status_box.error(f"🚨 ACCIDENT DETECTED: {severity}")
        elif "Moderate" in severity:
            status_box.warning(f"⚠️ IMPACT DETECTED: {severity}")
        else:
            status_box.success("✅ STATUS: SAFE")

        # DATA DISPLAY
        data_box.markdown(f"""
        **Speed:** {data['speed']} km/h  
        **Impact Force:** {round(data['impact'],2)}  
        **Rotation Angle:** {round(data['rotation'],2)}°  
        **GPS Location:** {data['gps']}
        """)

        # ALERT SYSTEM
        if "Severe" in severity:
            alert_box.error("📡 Alert sent to Ambulance + Emergency Contacts!")
        elif "Moderate" in severity:
            alert_box.warning("📡 Monitoring situation...")

        time.sleep(1)

else:
    status_box.info("Click 'Simulate Accident' to start system")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("### 🔧 How It Works")

st.markdown("""
- 📱 Collects motion data from sensors  
- 🤖 AI analyzes impact patterns  
- 📍 Detects location instantly  
- 🚑 Sends alerts automatically  

**No manual call. No delay. Just action.**
""")
