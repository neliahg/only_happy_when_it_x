import requests
import pandas as pd
import streamlit as st

#style
st.set_page_config(layout="centered")
st.title("I'm Only Happy When It X")

#state
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "city" not in st.session_state:
    st.session_state.city = ""

#function reset
def reset():
    st.session_state.submitted = False
    st.session_state.city = ""

# --- Input Screen ---
if not st.session_state.submitted:
    st.subheader("Enter a city to get the weather forecast")
    city_input = st.text_input("City (e.g. Paris or Paris,FR)", key="city_input")
    if st.button("Get Weather") and city_input.strip():
        st.session_state.city = city_input.strip()
        st.session_state.submitted = True

# --- Result Screen ---

else:
    api_key = "c0405f59ce8122b64146c3258e531ee0"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": st.session_state.city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        st.markdown(f"### 📍 {data['name']}, {data['sys']['country']}")
        st.image(icon_url)
        st.metric("🌡 Temperature", f"{data['main']['temp']}°C", f"Feels like {data['main']['feels_like']}°C")
        st.markdown(f"**Conditions:** {data['weather'][0]['description'].title()}")
        st.markdown(f"💧 Humidity: {data['main']['humidity']}%")
        st.markdown(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        st.error(f"Could not fetch weather for '{st.session_state.city}'. Try a different city.")

    st.markdown("---")
    st.button("🔁 Try Again", on_click=reset)