import requests
import json  # for pretty-printing
import streamlit as st

st.title("I'm Only Happy When It X")


api_key = "c0405f59ce8122b64146c3258e531ee0"
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "London",
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))  # pretty-print the full JSON
else:
    print("Error:", response.status_code, response.text)
