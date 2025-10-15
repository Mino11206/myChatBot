import google.generativeai as gemini
import os
import streamlit as st

st.title("ChatBot du lịch thông minh:")

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"

gemini.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = gemini.GenerativeModel("gemini-2.5-flash")

query = st.text_input("Nhập vào câu hỏi của bạn: ", key = "query_input")
if st.button("Gửi"):
    response = model.generate_content(query)
    st.success(response.text)


        
