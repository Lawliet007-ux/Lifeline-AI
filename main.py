import streamlit as st
import random
import time
import base64

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="LifeLine AI",
    page_icon="🚑",
    layout="wide"
)

# ---------------- LOAD LOGO (FROM FILE) ----------------
def get_base64_logo(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 👉 PUT YOUR LOGO FILE NAME HERE
LOGO_PATH = "logo.png"   # same folder

try:
    logo_base64 = get_base64_logo(LOGO_PATH)
    logo_html = f"<img src='data:image/png;base64,{logo_base64}' width='60'>"
except:
    logo_html = ""

# ---------------- CUSTOM CSS (🔥 UI MAGIC) ----------------
st.markdown(f"""
<style>
/* Background */
.stApp {{
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}}

/* Glass cards */
.glass {{
    background: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
}}

/* Title */
.title {{
    font-size: 40px;
    font-weight: bold;
}}

/* Status colors */
.safe {{
    color: #22c55e;
    font-size: 22px;
}}
.warning {{
    color: #facc15;
    font-size: 22px;
}}
.danger {{
    color: #ef4444;
    font-size: 24px;
    font-weight: bold;
}}

/* Button */
.stButton>button {{
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 8])

with col1:
    st.markdown(logo_html, unsafe_allow_html=True)

with col2:
    st.markdown("<div class='title'>🚑 LifeLine AI</div>", unsafe_allow_html=True)
    st.caption("Smart Accident Detection System")

st.markdown("---")

# ---------------- HERO ----------------
st.markdown("""
### 🚨 Every 4 minutes, someone dies in a road accident

Not always because of the crash...  
**But because help didn’t arrive on time**

## 💡 LifeLine AI solves delay — instantly.
""")

st.markdown("---")

# ---------------- FEATURES ----------------
col1, col2, col3 = st.columns(3)

col1.markdown("<div class='glass'>📱 Sensors<br>Accelerometer + Gyroscope</div>", unsafe_allow_html=True)
col2.markdown("<div class='glass'>📍 GPS Tracking<br>Real-time location</div>", unsafe_allow_html=True)
col3.markdown("<div class='glass'>🤖 AI Engine<br>False alert reduction</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIMULATION ----------------
st.subheader("🧠 AI Detection System")

simulate = st.button("🚨 Start Live Simulation")

status = st.empty()
metrics = st.empty()
alert = st.empty()
map_box = st.empty()

def generate_data():
    return {
        "speed": random.randint(10, 120),
        "impact": random.uniform(0, 10),
        "rotation": random.uniform(0, 180),
        "lat": random.uniform(28.5, 28.8),
        "lon": random.uniform(77.1, 77.4)
    }

def predict(data):
    score = data["impact"]*2 + data["rotation"]*0.05 + data["speed"]*0.1
    if score > 20:
        return "danger"
    elif score > 10:
        return "warning"
    return "safe"

if simulate:
    for _ in range(12):
        d = generate_data()
        state = predict(d)

        # STATUS
        if state == "danger":
            status.markdown("<div class='danger'>🚨 SEVERE ACCIDENT DETECTED</div>", unsafe_allow_html=True)
        elif state == "warning":
            status.markdown("<div class='warning'>⚠️ IMPACT DETECTED</div>", unsafe_allow_html=True)
        else:
            status.markdown("<div class='safe'>✅ ALL SAFE</div>", unsafe_allow_html=True)

        # METRICS
        metrics.markdown(f"""
        <div class='glass'>
        🚗 Speed: {d['speed']} km/h<br>
        💥 Impact: {round(d['impact'],2)}<br>
        🔄 Rotation: {round(d['rotation'],2)}°<br>
        </div>
        """, unsafe_allow_html=True)

        # MAP
        map_box.map({"lat":[d["lat"]], "lon":[d["lon"]]})

        # ALERT
        if state == "danger":
            alert.error("📡 Ambulance + Emergency Contacts Alerted!")
        elif state == "warning":
            alert.warning("📡 Monitoring situation...")

        time.sleep(1)

else:
    status.info("Click 'Start Live Simulation' to activate system")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
### ⚙️ How It Works
- Sensors detect motion  
- AI analyzes crash patterns  
- GPS identifies location  
- Alerts sent instantly  

**No delay. No panic. Just action.**
""")
