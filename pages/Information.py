import streamlit as st

st.set_page_config(
    page_title="Info",
)

st.write(":blue[Project was made by Blake Almon for i2]")

url = "https://github.com/blakealmon"
st.write("Github : [link](%s)" % url)