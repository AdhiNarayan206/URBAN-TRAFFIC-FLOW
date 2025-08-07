import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import random

# Initialize session state for form data and prediction
if 'form_data' not in st.session_state:
    st.session_state.form_data = {
        'start_location': '',
        'end_location': '',
        'departure_time': None,
        'weather_condition': 'Clear'
    }
if 'prediction' not in st.session_state:
    st.session_state.prediction = None
if 'loading' not in st.session_state:
    st.session_state.loading = False

# Mock historical data
historical_data = [
    {"time": "06:00", "volume": 120, "speed": 45, "congestion": "Low"},
    {"time": "07:00", "volume": 280, "speed": 35, "congestion": "Medium"},
    {"time": "08:00", "volume": 420, "speed": 25, "congestion": "High"},
    {"time": "09:00", "volume": 380, "speed": 30, "congestion": "High"},
    {"time": "10:00", "volume": 250, "speed": 40, "congestion": "Medium"},
    {"time": "11:00", "volume": 200, "speed": 45, "congestion": "Low"},
    {"time": "12:00", "volume": 220, "speed": 42, "congestion": "Medium"},
    {"time": "13:00", "volume": 240, "speed": 38, "congestion": "Medium"},
    {"time": "14:00", "volume": 260, "speed": 36, "congestion": "Medium"},
    {"time": "15:00", "volume": 320, "speed": 32, "congestion": "High"},
    {"time": "16:00", "volume": 380, "speed": 28, "congestion": "High"},
    {"time": "17:00", "volume": 450, "speed": 22, "congestion": "High"},
    {"time": "18:00", "volume": 480, "speed": 20, "congestion": "High"},
    {"time": "19:00", "volume": 350, "speed": 30, "congestion": "High"},
    {"time": "20:00", "volume": 280, "speed": 35, "congestion": "Medium"},
    {"time": "21:00", "volume": 200, "speed": 42, "congestion": "Low"}
]

# Mock route data
route_data = [
    {"route": "Route A (Highway)", "distance": "15.2 km", "time": "22 min", "traffic": "Medium", "fuel": "1.2L"},
    {"route": "Route B (City Roads)", "distance": "12.8 km", "time": "28 min", "traffic": "High", "fuel": "1.4L"},
    {"route": "Route C (Mixed)", "distance": "14.1 km", "time": "25 min", "traffic": "Low", "fuel": "1.1L"}
]

# Mock current stats
current_stats = {
    "average_speed": 32,
    "congestion_level": 75,
    "active_vehicles": 15420,
    "weather_impact": 15
}

# Helper functions
def get_traffic_color(level):
    return {
        "High": "background-color: #fee2e2; color: #dc2626;",
        "Medium": "background-color: #fef9c3; color: #d97706;",
        "Low": "background-color: #dcfce7; color: #15803d;"
    }.get(level, "background-color: #f3f4f6; color: #4b5563;")

def generate_prediction():
    st.session_state.loading = True
    time.sleep(2)  # Simulate API call delay
    form_data = st.session_state.form_data
    hour = datetime.strptime(form_data['departure_time'], '%Y-%m-%dT%H:%M').hour if form_data['departure_time'] else 12
    base_traffic = next((d for d in historical_data if int(d['time'].split(':')[0]) == hour), historical_data[8])

    weather_multiplier = {"Clear": 1.0, "Rain": 1.3, "Snow": 1.6, "Fog": 1.4}[form_data['weather_condition']]
    predicted_volume = round(base_traffic['volume'] * weather_multiplier)
    predicted_speed = round(base_traffic['speed'] / weather_multiplier)
    estimated_time = round((15.2 / predicted_speed) * 60)  # Assuming 15.2km route

    st.session_state.prediction = {
        "predicted_volume": predicted_volume,
        "predicted_speed": predicted_speed,
        "estimated_time": estimated_time,
        "congestion_level": "High" if predicted_volume > 350 else "Medium" if predicted_volume > 250 else "Low",
        "confidence": round(85 + random.random() * 10),
        "weather_factor": round((weather_multiplier - 1) * 100),
        "recommendations": [
            "Consider alternative routes" if predicted_volume > 350 else "Primary route looks good",
            "Allow extra time due to weather" if weather_multiplier > 1.2 else "Normal travel time expected",
            "Peak morning hours - expect delays" if 7 <= hour <= 9 else "Off-peak travel time"
        ]
    }
    st.session_state.loading = False

# Streamlit app
st.set_page_config(page_title="Urban Traffic Flow Predictor", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main { background: linear-gradient(to bottom right, #eff6ff, #ffffff, #f5f3ff); }
        .header { background: #ffffff; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border-bottom: 4px solid #3b82f6; padding: 1.5rem; }
        .tab-button { margin-right: 0.5rem; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 500; }
        .tab-button:hover { background: #e5e7eb; }
        .active-tab { background: #ffffff; color: #3b82f6; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }
        .card { background: #ffffff; border-radius: 0.75rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border: 1px solid #e5e7eb; padding: 1.5rem; }
        .metric-card { border-radius: 0.5rem; padding: 1rem; border: 1px solid #e5e7eb; }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">', unsafe_allow_html=True)
st.markdown("<h1 style='font-size: 1.875rem; font-weight: bold; color: #111827;'>🚗 Urban Traffic Flow Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #6b7280;'>AI-powered traffic forecasting and route optimization</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div style='text-align: center;'><div style='font-size: 1.5rem; font-weight: bold; color: #3b82f6;'>{current_stats['average_speed']}</div><div style='color: #6b7280;'>Avg Speed (km/h)</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div style='text-align: center;'><div style='font-size: 1.5rem; font-weight: bold; color: #7c3aed;'>{current_stats['congestion_level']}%</div><div style='color: #6b7280;'>Congestion</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div style='text-align: center;'><div style='font-size: 1.5rem; font-weight: bold; color: #10b981;'>{current_stats['active_vehicles']:,}</div><div style='color: #6b7280;'>Active Vehicles</div></div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Navigation Tabs
tabs = ["Traffic Prediction", "Route Optimization", "Traffic Analytics"]
active_tab = st.radio("Select Tab", tabs, index=0, horizontal=True, key="active_tab")

# Traffic Prediction Tab
if active_tab == "Traffic Prediction":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 1.25rem; font-weight: bold; color: #111827;'>📍 Trip Details</h2>", unsafe_allow_html=True)
        
        st.session_state.form_data['start_location'] = st.text_input("From", value=st.session_state.form_data['start_location'], placeholder="Enter starting location")
        st.session_state.form_data['end_location'] = st.text_input("To", value=st.session_state.form_data['end_location'], placeholder="Enter destination")
        st.session_state.form_data['departure_time'] = st.text_input("Departure Time", value=st.session_state.form_data['departure_time'], type="datetime-local")
        st.session_state.form_data['weather_condition'] = st.selectbox("Weather Condition", ["Clear", "Rain", "Snow", "Fog"], index=["Clear", "Rain", "Snow", "Fog"].index(st.session_state.form_data['weather_condition']))
        
        is_form_valid = st.session_state.form_data['start_location'] and st.session_state.form_data['end_location'] and st.session_state.form_data['departure_time']
        if st.button("Predict Traffic", disabled=st.session_state.loading or not is_form_valid):
            generate_prediction()
        if st.session_state.loading:
            st.markdown("<div style='text-align: center;'>⏳ Analyzing Traffic...</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 1.25rem; font-weight: bold; color: #111827;'>📈 Traffic Prediction</h2>", unsafe_allow_html=True)
        
        if st.session_state.prediction:
            prediction = st.session_state.prediction
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"<div class='metric-card' style='background: #eff6ff; border-color: #bfdbfe;'><div style='font-size: 1.875rem; font-weight: bold; color: #3b82f6;'>{prediction['predicted_volume']}</div><div style='color: #1e40af;'>Vehicles/Hour</div></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='metric-card' style='background: #f3e8ff; border-color: #d8b4fe;'><div style='font-size: 1.875rem; font-weight: bold; color: #7c3aed;'>{prediction['estimated_time']}</div><div style='color: #6d28d9;'>Minutes ETA</div></div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<div class='metric-card' style='background: #d1fae5; border-color: #6ee7b7;'><div style='font-size: 1.875rem; font-weight: bold; color: #10b981;'>{prediction['predicted_speed']}</div><div style='color: #047857;'>km/h Avg Speed</div></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='metric-card' style='background: #f3f4f6; border-color: #d1d5db;'><div style='font-size: 1.875rem; font-weight: bold; color: #4b5563;'>{prediction['confidence']}%</div><div style='color: #6b7280;'>Confidence</div></div>", unsafe_allow_html=True)
            
            st.markdown(f"<div style='display: flex; justify-content: space-between; padding: 0.75rem; background: #f3f4f6; border-radius: 0.5rem;'><span style='font-weight: 500; color: #4b5563;'>Congestion Level:</span><span style='{get_traffic_color(prediction['congestion_level'])} padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;'>{prediction['congestion_level']}</span></div>", unsafe_allow_html=True)
            
            if prediction['weather_factor'] > 0:
                st.markdown(f"<div style='display: flex; justify-content: space-between; padding: 0.75rem; background: #ffedd5; border-radius: 0.5rem; border: 1px solid #fed7aa;'><span style='font-weight: 500; color: #c2410c;'>☁ Weather Impact:</span><span style='color: #c2410c; font-weight: 600;'>+{prediction['weather_factor']}% delay</span></div>", unsafe_allow_html=True)
            
            st.markdown("<div style='background: #fef9c3; border: 1px solid #fde68a; border-radius: 0.5rem; padding: 1rem;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-weight: 600; color: #713f12; margin-bottom: 0.75rem;'>⚠ AI Recommendations</h3>", unsafe_allow_html=True)
            for rec in prediction['recommendations']:
                st.markdown(f"<div style='display: flex; align-items: start; color: #713f12; font-size: 0.875rem;'><span style='width: 0.5rem; height: 0.5rem; background: #facc15; border-radius: 9999px; margin-top: 0.5rem; margin-right: 0.75rem; flex-shrink: 0;'></span>{rec}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align: center; padding: 3rem; color: #6b7280;'>", unsafe_allow_html=True)
            st.markdown("🚗 <p style='font-size: 1.125rem;'>Enter trip details to get traffic prediction</p>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 0.875rem; margin-top: 0.5rem;'>Our AI model analyzes historical patterns, weather, and real-time data</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Route Optimization Tab
elif active_tab == "Route Optimization":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 1.25rem; font-weight: bold; color: #111827;'>🛣 Optimal Route Suggestions</h2>", unsafe_allow_html=True)
    
    for route in route_data:
        st.markdown('<div style="border: 1px solid #e5e7eb; border-radius: 0.5rem; padding: 1rem; margin-bottom: 1rem;">', unsafe_allow_html=True)
        st.markdown(f"<div style='display: flex; justify-content: space-between; margin-bottom: 0.75rem;'><h3 style='font-weight: 600; font-size: 1.125rem; color: #111827;'>{route['route']}</h3><span style='{get_traffic_color(route['traffic'])} padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem; font-weight: 500;'>{route['traffic']} Traffic</span></div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<div style='text-align: center;'><div style='font-weight: 600; color: #3b82f6;'>{route['distance']}</div><div style='color: #6b7280;'>Distance</div></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div style='text-align: center;'><div style='font-weight: 600; color: #7c3aed;'>{route['time']}</div><div style='color: #6b7280;'>Est. Time</div></div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div style='text-align: center;'><div style='font-weight: 600; color: #10b981;'>{route['fuel']}</div><div style='color: #6b7280;'>Fuel Est.</div></div>", unsafe_allow_html=True)
        
        st.button("Select Route", key=f"select_route_{route['route']}")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Traffic Analytics Tab
elif active_tab == "Traffic Analytics":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 1.125rem; font-weight: 600; color: #111827; margin-bottom: 1rem;'>Traffic Volume Throughout Day</h3>", unsafe_allow_html=True)
    df = pd.DataFrame(historical_data)
    fig = px.line(df, x="time", y="volume", title="Traffic Volume", labels={"volume": "Vehicles/Hour", "time": "Time of Day"})
    fig.update_traces(line=dict(color="#3b82f6", width=3))
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 1.125rem; font-weight: 600; color: #111827; margin-bottom: 1rem;'>Average Speed Analysis</h3>", unsafe_allow_html=True)
    fig = px.bar(df, x="time", y="speed", title="Average Speed", labels={"speed": "km/h", "time": "Time of Day"})
    fig.update_traces(marker_color="#10b981")
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 1.125rem; font-weight: 600; color: #111827; margin-bottom: 1rem;'>Congestion Patterns</h3>", unsafe_allow_html=True)
    cols = st.columns(8)
    for i, data in enumerate(historical_data):
        with cols[i % 8]:
            height = (data['volume'] / 500) * 100
            color = {"High": "#ef4444", "Medium": "#facc15", "Low": "#22c55e"}[data['congestion']]
            st.markdown(f"<div style='text-align: center;'><div style='font-size: 0.75rem; color: #6b7280; margin-bottom: 0.5rem;'>{data['time']}</div><div style='height: {height}px; background: {color}; border-radius: 0.5rem; display: flex; align-items: end; justify-content: center; color: white; font-weight: bold; font-size: 0.75rem;'>{data['volume']}</div></div>", unsafe_allow_html=True)
    
    st.markdown("<div style='display: flex; justify-content: center; margin-top: 1rem; gap: 1.5rem; font-size: 0.875rem;'>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; align-items: center;'><div style='width: 1rem; height: 1rem; background: #22c55e; border-radius: 0.25rem; margin-right: 0.5rem;'></div>Low Traffic</div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; align-items: center;'><div style='width: 1rem; height: 1rem; background: #facc15; border-radius: 0.25rem; margin-right: 0.5rem;'></div>Medium Traffic</div>", unsafe_allow_html=True)
    st.markdown("<div style='display: flex; align-items: center;'><div style='width: 1rem; height: 1rem; background: #ef4444; border-radius: 0.25rem; margin-right: 0.5rem;'></div>High Traffic</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<footer style="background: #111827; color: white; padding: 2rem; margin-top: 4rem; text-align: center;">', unsafe_allow_html=True)
st.markdown("<p style='color: #d1d5db;'>Urban Traffic Flow Predictor - Powered by Machine Learning & Real-time Data</p>", unsafe_allow_html=True)
st.markdown("<p style='color: #6b7280; font-size: 0.875rem; margin-top: 0.5rem;'>Built with Streamlit, Plotly, and modern Python technologies</p>", unsafe_allow_html=True)
st.markdown('</footer>', unsafe_allow_html=True)
