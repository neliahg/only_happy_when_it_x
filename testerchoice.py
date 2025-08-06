import requests
import pandas as pd
import streamlit as st
import datetime
import pytz
import time

#page configuration

st.set_page_config(
    page_title = "Weather X",
    page_icon="✨",
    layout="centered"
)

st.image('https://raw.githubusercontent.com/neliahg/only_happy_when_it_x/2c6a999d73f5a0db8556d4f32684ec516ac792d1/assets/backgrounds/weatherx.png')


df_cities = pd.read_csv('https://raw.githubusercontent.com/neliahg/only_happy_when_it_x/main/assets/backgrounds/cities_list.csv')
random_row = df_cities.sample(1)
lat,lon= random_row['lat'],random_row['lon']



def weather(data): #get weather details across all
    with st.container():
        st.markdown(f"📍 **{data['name']}, {data['sys']['country']}**")
        st.write(data["weather"][0]["description"].capitalize())
        st.write(f"🌡 Temperature: {data['main']['temp']}°C (feels like {data['main']['feels_like']}°C)")
        st.write(f"💨 Wind: {data['wind']['speed']} m/s")

        city_name = data["name"]
        country = data["sys"]["country"]
        weather_description = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        wind_speed = data["wind"]["speed"]
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        with st.container(border=True):
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(icon_url, width=80)

            with col2:
                st.markdown(f"### 📍 {city_name}, {country}")
                st.markdown(f"**{weather_description}**")
                st.markdown(f"🌡️ **{temp}°C** *(feels like {feels_like}°C)*")
                st.markdown(f"💨 Wind: {wind_speed} m/s")

        # Optional: show map below
        loc_df = pd.DataFrame({
            "lat": [data['coord']['lat']],
            "lon": [data['coord']['lon']]
        })
        st.map(loc_df, zoom=8)
def cityweather(city):
    api_key = st.secrets["openweather"]["api_key"]
    url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather(data)
        return data
    else:
        st.error(f"{response.status_code}: {response.json().get('message')}")
        return None


def rand_weather():
    df_cities = pd.read_csv('https://raw.githubusercontent.com/neliahg/only_happy_when_it_x/main/assets/backgrounds/cities_list.csv')
    random_row = df_cities.sample(1)
    lat = random_row['lat'].iloc[0]
    lon = random_row['lon'].iloc[0]


    api_key = st.secrets["openweather"]["api_key"]
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather(data)
        return data

    else:
        st.error(f"{response.status_code}: {response.json().get('message')}")
        return None


def ipweather():  #based on ip address
    ip_info = requests.get("https://ipinfo.io/json").json()
    city = ip_info.get("city")
    country = ip_info.get("country")
    loc = ip_info.get("loc")
    lat, lon = loc.split(',')

    api_key = st.secrets["openweather"]["api_key"]
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather(data)
        return data
    else:
        st.error(f"{response.status_code}: {response.json().get('message')}")
        return None



col1, col2, col3 = st.columns([0.1, 0.8, 0.1])

with col1:
    st.write("")#spaaaaaaace

with col2:
    city = st.text_input("Search city or town:", placeholder="",help="For best results, specify the country code (i.e. Paris,FR)")
    with st.container():
        button_col1, button_col2, button_col3 = st.columns([1,1,1])
        with button_col1:
            get_weather = st.button("Get Weather!", use_container_width=True)
        with button_col2:
            feeling_lucky = st.button("I'm feeling lucky...", use_container_width=True)
        with button_col3:
            go_home = st.button("Go Home", use_container_width=True)
with col3:
    st.write("")#spaaaaaaace




if get_weather and city.strip():
    with st.spinner(f"Searching Weather X for **{city.upper()}**..."):
        time.sleep(3)
    cityweather(city)
elif feeling_lucky:
    with st.spinner(f"Searching Weather X for a **RANDOM** location..."):
        time.sleep(3)
    rand_weather()

elif go_home:
    with st.spinner(f"Searching Weather X for a **YOUR** IP location..."):
        time.sleep(3)
    ipweather()