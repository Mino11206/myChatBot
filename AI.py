# import google.generativeai as gemini
# import os
# import streamlit as st

# st.title("ChatBot du lịch thông minh:")

# os.environ["GRPC_VERBOSITY"] = "NONE"
# os.environ["GLOG_minloglevel"] = "2"

# gemini.configure(api_key=st.secrets["GEMINI_API_KEY"])
# model = gemini.GenerativeModel("gemini-2.5-flash")

# history =[""]
# context = "Bạn là TravelBot một tư vấn viên du lịch chuyên nghiệp, hãy dùng tiếng việt một cách chuyên nghiệp và cuốn hút ghi nhớ câu trả lời trước và trả lời câu hỏi"
# query = "context: " + context + ", your previous response: " + history[-1]
# query += st.text_input("Nhập vào câu hỏi của bạn: ", key = "query_input")
# if st.button("Gửi"):
#     response = model.generate_content(query)
#     history.append(response.text)
#     st.success(response.text)


        
import streamlit as st
import google.generativeai as gemini
import os

# ===== Cấu hình =====
st.set_page_config(page_title="ChatBot Du Lịch Thông Minh", page_icon="🌏")
st.title("🌴 ChatBot Du Lịch Thông Minh")

# Giảm log
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"

# Kết nối API Gemini
gemini.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = gemini.GenerativeModel("gemini-2.5-flash")

# ===== Khởi tạo lịch sử =====
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ===== Giao diện =====
user_input = st.text_input("✈️ Hãy hỏi TravelBot điều bạn muốn:", key="query_input")

# ===== Khi người dùng gửi =====
if st.button("Gửi") and user_input.strip():
    # Tạo prompt gồm context + lịch sử hội thoại
    context = (
        "Bạn là TravelBot — một tư vấn viên du lịch chuyên nghiệp. "
        "Hãy trả lời bằng tiếng Việt, giọng văn thân thiện, sinh động, gợi mở. "
        "Giữ ngữ cảnh hội thoại trước đó và không lặp lại câu hỏi."
    )

    # Ghép lịch sử trò chuyện vào prompt
    conversation = ""
    for role, text in st.session_state.chat_history[-6:]:  # chỉ lấy 6 lần gần nhất để tránh quá dài
        conversation += f"{role}: {text}\n"

    prompt = f"{context}\n\n{conversation}\nNgười dùng: {user_input}\nTravelBot:"

    # Gọi API
    response = model.generate_content(prompt)
    answer = response.text.strip()

    # Cập nhật lịch sử
    st.session_state.chat_history.append(("Người dùng", user_input))
    st.session_state.chat_history.append(("TravelBot", answer))

# ===== Hiển thị hội thoại =====
for role, text in reversed(st.session_state.chat_history):
    if role == "TravelBot":
        st.markdown(f"🧭 **{role}:** {text}")
    else:
        st.markdown(f"👤 **{role}:** {text}")
