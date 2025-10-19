import google.generativeai as gemini
import os
import streamlit as st

st.title("ChatBot du lịch thông minh:")

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"

gemini.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = gemini.GenerativeModel("gemini-2.5-flash")

history =[""]
context = "Bạn là TravelBot một tư vấn viên du lịch chuyên nghiệp, hãy dùng tiếng việt một cách chuyên nghiệp và cuốn hút ghi nhớ câu trả lời trước và trả lời câu hỏi"
query = "context: " + context + ", your previous response: " + history[-1]
query += st.text_input("Nhập vào câu hỏi của bạn: ", key = "query_input")
if st.button("Gửi"):
    response = model.generate_content(query)
    history.append(response.text)
    st.success(response.text)


        
