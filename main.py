import requests
import pandas as pd
import json  # for pretty-printing
import streamlit as st

st.title("I'm Only Happy When It X")
user_input = st.text_input("Enter a city (e.g. Haifa,IL")


api_key = "c0405f59ce8122b64146c3258e531ee0"
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": user_input,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    st.write(f"Weather in {data['name']},{data['sys']['country']}: {data['weather'][0]['description']} ({data['main']['temp']}°C)")
else:
    st.write("Error:", response.status_code, response.text)

