import requests
import pandas as pd
import streamlit as st

st.title("I'm Only Happy When It X")
st.subheader("Weather Dashboard")

user_input = st.text_input("Enter ")

api_key = "c0405f59ce8122b64146c3258e531ee0"
url = "http://api.openweathermap.org/data/2.5/weather"

if user_input:
    params = {
        "q": user_input,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        condition = data["weather"][0]["description"].title()
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        # --- Display Weather Info ---
        st.markdown(f"### 📍 {city}, {country}")
        st.image(icon_url)
        st.metric("🌡 Temperature", f"{temp}°C", f"Feels like {feels_like}°C")
        st.markdown(f"**Conditions:** {condition}")

    else:
        st.error(f"Error {response.status_code}: Could not retrieve weather for '{user_input}'")