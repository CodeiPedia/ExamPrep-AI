import streamlit as st
import google.generativeai as genai
from supabase import create_client, Client
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- CONFIG ---
st.set_page_config(page_title="ExamPrep AI - Student Portal", layout="wide")

# --- DB & AI SETUP (Secrets से कनेक्ट करें) ---
# SUPABASE_URL = st.secrets["SUPABASE_URL"]
# SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- SIDEBAR: NAVIGATION ---
st.sidebar.title("🚀 ExamPrep AI")
menu = st.sidebar.radio("Go to", ["Dashboard", "Practice Test", "Weakness Analysis", "Study Plan"])

# --- 1. DASHBOARD (Growth Tracking) ---
if menu == "Dashboard":
    st.header(f"Welcome back, Student!") # यहाँ बाद में नाम जोड़ेंगे
    
    # Growth Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Tests Taken", "15", "+2")
    col2.metric("Avg Score", "72%", "+5%")
    col3.metric("Rank", "142", "-10")

    # Growth Chart (Sample Data)
    st.subheader("📈 Your Growth Over Time")
    df = pd.DataFrame({
        'Date': pd.date_range(start='2026-03-01', periods=10),
        'Score': [60, 62, 65, 63, 68, 70, 75, 72, 78, 80]
    })
    fig = px.line(df, x='Date', y='Score', title="Mock Test Performance")
    st.plotly_chart(fig, use_container_width=True)

# --- 2. PRACTICE TEST ---
elif menu == "Practice Test":
    st.header("📝 Personalized Practice Set")
    
    with st.expander("Configure Your Test", expanded=True):
        subject = st.selectbox("Select Subject", ["Electrical Engineering", "General Awareness", "Reasoning"])
        level = st.select_slider("Difficulty", options=["Easy", "Medium", "Hard"])
        num_q = st.number_input("Number of Questions", 5, 20, 10)
        
    if st.button("Start AI-Customized Test"):
        st.session_state.test_active = True
        st.info("AI is fetching questions based on your previous weak areas...")

# --- 3. WEAKNESS ANALYSIS ---
elif menu == "Weakness Analysis":
    st.header("🔍 AI Weakness Tracker")
    st.write("AI ने आपकी पिछली गलतियों के आधार पर ये पॉइंट्स पहचाने हैं:")
    
    weaknesses = {
        "Subject": ["Electrical", "Maths", "GK"],
        "Topic": ["Transformers", "Percentage", "Current Affairs"],
        "Error Pattern": ["Calculation Error", "Conceptual Gap", "Lack of Revision"]
    }
    st.table(pd.DataFrame(weaknesses))
    
    if st.button("Generate Remedial Quiz for Weak Topics"):
        st.write("Generating questions only from 'Transformers' and 'Percentage'...")

# --- 4. STUDY PLAN ---
elif menu == "Study Plan":
    st.header("📅 Your Adaptive Time-Table")
    st.info("यह शेड्यूल आपकी तैयारी की गति के हिसाब से हर रोज बदलता है।")
    
    st.checkbox("08:00 AM - 10:00 AM: Focus on Transformers (Weak Area)", value=False)
    st.checkbox("11:00 AM - 01:00 PM: General Awareness Quiz", value=True)
    st.checkbox("03:00 PM - 05:00 PM: PYQ Practice (SSC CGL)", value=False)
