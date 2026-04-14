import streamlit as st
import random
import time
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(page_title="LifeLine AI", layout="wide")

# ---------------- LOGO ----------------
LOGO_URL = "https://raw.githubusercontent.com/Lawliet007-ux/Lifeline-AI/main/image_t2.png"

logo_html = f"""
<img src="{LOGO_URL}" width="70"
style="border-radius:12px; box-shadow: 0 0 15px rgba(59,130,246,0.6);">
"""

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}
.glass {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}
.title { font-size: 40px; font-weight: bold; }
.safe { color: #22c55e; font-size: 22px; }
.warning { color: #facc15; font-size: 22px; }
.danger { color: #ef4444; font-size: 26px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 8])
with col1:
    st.markdown(logo_html, unsafe_allow_html=True)
with col2:
    st.markdown("<div class='title'>🚑 LifeLine AI</div>", unsafe_allow_html=True)
    st.caption("AI-powered accident detection system")

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Controls")
mode = st.sidebar.radio("Mode", ["Manual", "Auto"])
run_time = st.sidebar.slider("Simulation Duration (sec)", 5, 30, 10)

st.sidebar.markdown("### 📞 Emergency Contacts")
contacts = st.sidebar.text_area("Enter contacts (comma separated)", "Mom, Dad, Ambulance")

# ---------------- DATA ----------------
history = []

def generate_data():
    return {
        "speed": random.randint(10, 120),
        "impact": random.uniform(0, 10),
        "rotation": random.uniform(0, 180),
        "lat": random.uniform(28.5, 28.8),
        "lon": random.uniform(77.1, 77.4)
    }

def predict_score(d):
    return d["impact"]*2 + d["rotation"]*0.05 + d["speed"]*0.1

# ---------------- UI ----------------
st.subheader("🧠 Live AI Dashboard")

start = st.button("🚨 Start System")

status = st.empty()
metrics = st.empty()
chart = st.empty()
alert = st.empty()
map_box = st.empty()

impact_list = []
speed_list = []

# ---------------- LOOP ----------------
if start or mode == "Auto":
    for i in range(run_time):

        d = generate_data()
        score = predict_score(d)

        impact_list.append(d["impact"])
        speed_list.append(d["speed"])

        # CLASSIFY
        if score > 20:
            state = "danger"
        elif score > 10:
            state = "warning"
        else:
            state = "safe"

        # STATUS
        if state == "danger":
            status.markdown("<div class='danger'>🚨 SEVERE ACCIDENT DETECTED</div>", unsafe_allow_html=True)
            alert.error(f"📡 Alert sent to: {contacts}")
            st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
        elif state == "warning":
            status.markdown("<div class='warning'>⚠️ IMPACT DETECTED</div>", unsafe_allow_html=True)
        else:
            status.markdown("<div class='safe'>✅ SAFE</div>", unsafe_allow_html=True)

        # METRICS
        metrics.markdown(f"""
        <div class='glass'>
        🚗 Speed: {d['speed']} km/h<br>
        💥 Impact: {round(d['impact'],2)}<br>
        🔄 Rotation: {round(d['rotation'],2)}°<br>
        🧠 AI Score: {round(score,2)}<br>
        </div>
        """, unsafe_allow_html=True)

        # MAP
        map_box.map({"lat":[d["lat"]], "lon":[d["lon"]]})

        # CHART
        df = pd.DataFrame({
            "Impact": impact_list,
            "Speed": speed_list
        })
        chart.line_chart(df)

        # HISTORY
        history.append({"score": score, "state": state})

        time.sleep(1)

# ---------------- HISTORY ----------------
st.markdown("---")
st.subheader("📜 Accident History")

if history:
    st.dataframe(pd.DataFrame(history))
else:
    st.info("No events recorded yet")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
### ⚙️ System Logic

- Uses motion + rotation + speed  
- AI computes severity score  
- Detects crash vs normal events  
- Sends alerts instantly  

**Built for zero delay emergency response**
""")
