import streamlit as st
import pandas as pd
import os
from groq import Groq

# -------------------------------------------------------------
# CẤU HÌNH TRANG
# -------------------------------------------------------------
st.set_page_config(page_title="Ôn tập Dẫn luận Ngôn ngữ học & Trợ lý AI", page_icon="🎓", layout="wide")

# -------------------------------------------------------------
# KHỞI TẠO GROQ CLIENT
# -------------------------------------------------------------
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "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")
try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception:
    client = None

# -------------------------------------------------------------
# SYSTEM PROMPT CHO AI (GIỚI HẠN NGHIÊM NGẶT CHỦ ĐỀ)
# -------------------------------------------------------------
SYSTEM_PROMPT = """Bạn là một Chuyên gia và Giảng viên Ngôn ngữ học kiêm Gia sư AI cho sinh viên ngành Ngôn ngữ Anh (Đại học Mở Hà Nội).
Nhiệm vụ của bạn là giải đáp chi tiết, ngắn gọn, dễ hiểu và chuẩn xác các thắc mắc về môn Dẫn luận Ngôn ngữ học (ENO3) gồm 6 chuyên đề:
1. Bản chất & Chức năng của ngôn ngữ.
2. Nguồn gốc & Phát triển.
3. Hệ thống kí hiệu.
4. Ngữ âm.
5. Từ vựng.
6. Ngữ pháp.

QUY TẮC TỐI THƯỢNG: TUYỆT ĐỐI KHÔNG trả lời bất kỳ câu hỏi nào nằm ngoài phạm vi môn Dẫn luận Ngôn ngữ học (như toán học, lập trình, kĩ thuật mạng, y tế, đời sống...). Nếu người dùng hỏi sai chủ đề, hãy từ chối lịch sự, nói rõ bạn chỉ hỗ trợ ôn tập môn Dẫn luận Ngôn ngữ học và nhắc họ quay lại bài học.

Hãy luôn đưa ra ví dụ trực quan (tiếng Việt hoặc tiếng Anh) và giải thích từng bước cho các câu hỏi đúng chuyên môn."""

# -------------------------------------------------------------
# HÀM NHÚNG TRỢ LÝ AI VÀO CUỐI BÀI HỌC
# -------------------------------------------------------------
def render_ai_tutor(lesson_name):
    st.markdown("---")
    st.subheader(f"🤖 Hỏi đáp AI - {lesson_name}")
    st.caption("Trợ lý sẽ chỉ trả lời các câu hỏi liên quan đến môn Dẫn luận Ngôn ngữ học.")

    if not client:
        st.error("Chưa cấu hình API Key cho Groq hoặc API Key không hợp lệ.")
        return

    # Khởi tạo lịch sử chat trong Session State nếu chưa có
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Chào bạn! Tôi là Trợ lý AI môn Dẫn luận Ngôn ngữ học. Bạn có phần nào chưa hiểu ở bài này hay cần tôi cho ví dụ bài tập không?"}
        ]

    # Hiển thị lịch sử tin nhắn
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Xử lý input từ người dùng
    user_input = st.chat_input(f"Nhập câu hỏi về {lesson_name} tại đây...")

    if user_input:
        # Thêm tin nhắn của user
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Gọi Groq API
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            try:
                # Gửi bối cảnh cho AI
                groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                for m in st.session_state.messages:
                    groq_messages.append({"role": m["role"], "content": m["content"]})

                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=groq_messages,
                    temperature=0.3,
                    max_tokens=1000,
                    stream=True,
                )

                for chunk in completion:
                    content = chunk.choices[0].delta.content or ""
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                error_msg = f"⚠️ Đã có lỗi xảy ra khi kết nối tới Groq AI: {str(e)}"
                message_placeholder.error(error_msg)


# -------------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------------
logo_path = "logo.png"
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=150)
else:
    st.sidebar.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🎓</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center; font-weight: bold; color: #1E88E5;'>ĐẠI HỌC MỞ HÀ NỘI</p>", unsafe_allow_html=True)

st.sidebar.title("📚 Mục lục bài giảng")
# Loại bỏ mục Trợ lý AI riêng biệt, trả về danh sách thuần túy
menu = [
    "Giới thiệu chung", 
    "Bài 1: Bản chất & Chức năng", 
    "Bài 2: Nguồn gốc & Phát triển", 
    "Bài 3: Hệ thống kí hiệu", 
    "Bài 4: Ngữ âm", 
    "Bài 5: Từ vựng", 
    "Bài 6: Ngữ pháp"
]
choice = st.sidebar.radio("Điều hướng:", menu)

# Thêm nút Clear Chat ở Sidebar
st.sidebar.markdown("---")
if st.sidebar.button("🗑️ Xóa đoạn chat AI"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Chào bạn! Tôi là Trợ lý AI môn Dẫn luận Ngôn ngữ học. Bạn có phần nào chưa hiểu ở bài này hay cần tôi cho ví dụ bài tập không?"}
    ]
    st.rerun()

# -------------------------------------------------------------
# NỘI DUNG CHÍNH
# -------------------------------------------------------------
if choice == "Giới thiệu chung":
    st.title("🎓 Dẫn luận Ngôn ngữ học (ENO3)")
    st.markdown("---")
    st.info("**Giảng viên:** PGS.TS. Phạm Tất Thắng\n\n**Đơn vị:** Chương trình Đào tạo Trực tuyến - Trường Đại học Mở Hà Nội")
    st.write("Ứng dụng tổng hợp chi tiết toàn bộ kiến thức môn Dẫn luận Ngôn ngữ học (ENO3) kèm **Trợ lý Gia sư AI**.")
    st.write("👉 **Lưu ý mới:** Trợ lý AI hiện đã được nhúng trực tiếp vào cuối mỗi bài học. AI được lập trình chuyên biệt để **từ chối mọi câu hỏi ngoài luồng** và chỉ tập trung hỗ trợ bạn ôn luyện ngôn ngữ học.")

elif choice == "Bài 1: Bản chất & Chức năng":
    st.title("Bài 1: Bản chất và Chức năng của Ngôn ngữ")
    tab1, tab2 = st.tabs(["Bản chất của Ngôn ngữ", "Chức năng của Ngôn ngữ"])
    with tab1:
        st.subheader("1. Quan niệm duy tâm (Đã lỗi thời)")
        st.markdown("* Cho rằng ngôn ngữ giống các hiện tượng tự nhiên.\n* Coi ngôn ngữ giống tiếng kêu của động vật.\n* Có tính di truyền.\n* Là hiện tượng cá nhân hay giai cấp.")
        st.subheader("2. Quan niệm duy vật (Chính xác)")
        st.success("**Ngôn ngữ là hiện tượng xã hội:** Được sinh ra do con người sáng tạo, là tài sản chung cộng đồng.")
        st.info("**Ngôn ngữ là hiện tượng xã hội ĐẶC BIỆT:** Không thuộc kiến trúc thượng tầng/hạ tầng, không có tính giai cấp, liên hệ trực tiếp với sản xuất.")
    with tab2:
        st.subheader("1. Chức năng giao tiếp")
        st.write("Là phương tiện truyền đạt thông tin quan trọng nhất, vượt thời gian, không gian, biểu đạt chi tiết từ khái niệm đến cảm xúc.")
        st.subheader("2. Chức năng thể hiện tư duy")
        st.write("Ngôn ngữ là hiện thực trực tiếp của tư tưởng, trực tiếp tham gia quá trình hình thành tư tưởng.")
    
    # Gọi hàm nhúng AI
    render_ai_tutor("Bài 1")

elif choice == "Bài 2: Nguồn gốc & Phát triển":
    st.title("Bài 2: Nguồn gốc và Sự phát triển của Ngôn ngữ")
    with st.expander("🌟 Nguồn gốc của Ngôn ngữ", expanded=True):
        st.markdown("**A. Trước Mác:** Tượng thanh, Cảm thán, Khế ước, Cử chỉ (Chưa hoàn thiện).\n\n**B. Thuyết Lao động (Mác-Ăngghen):** Quá trình lao động buộc con người phải giao tiếp và giúp hoàn thiện bộ não -> Ngôn ngữ ra đời (Đúng đắn).")
    with st.expander("📈 Quá trình phát triển", expanded=True):
        st.markdown("Ngôn ngữ bộ lạc -> Khu vực -> Dân tộc -> Văn hóa -> Cộng đồng tương lai (Quốc tế ngữ).")
    with st.expander("⚙️ Cách thức & Nhân tố phát triển"):
        st.markdown("Phát triển không đồng đều: Từ vựng (Nhanh) -> Ngữ âm (Chậm) -> Ngữ pháp (Rất chậm). Chịu tác động khách quan (Kinh tế, giao lưu) và chủ quan (Chính sách).")
    
    # Gọi hàm nhúng AI
    render_ai_tutor("Bài 2")

elif choice == "Bài 3: Hệ thống kí hiệu":
    st.title("Bài 3: Ngôn ngữ là Hệ thống Kí hiệu Đặc biệt")
    st.markdown("* **Hệ thống:** Một thể thống nhất gồm các phần tử và mối quan hệ giữa chúng.\n* **Kí hiệu:** Gồm Cái biểu đạt (âm thanh) và Cái được biểu đạt (ý nghĩa).")
    st.subheader("5 Đặc trưng của Kí hiệu ngôn ngữ")
    st.error("**1. Tính võ đoán:** Không có lý do logic bắt buộc âm thanh phải gắn với ý nghĩa (vd: chó, dog, chien).")
    st.warning("**2. Tính đa trị:** Từ đa nghĩa, đồng âm, đồng nghĩa.")
    st.info("**3. Tính tuyến tính:** Từ xuất hiện nối tiếp trên trục thời gian.")
    st.success("**4. Vừa đồng loại, không đồng loại & TRỤC LIÊN TƯỞNG:** Phân cấp Âm vị -> Hình vị -> Từ -> Câu. Có thể thay thế các từ cùng loại tại một vị trí.")
    st.primary("**5. Vừa đồng đại, vừa lịch đại:** Kế thừa quá khứ và sử dụng ở hiện tại.")
    
    # Gọi hàm nhúng AI
    render_ai_tutor("Bài 3")

elif choice == "Bài 4: Ngữ âm":
    st.title("Bài 4: Ngữ âm")
    tab1, tab2, tab3 = st.tabs(["Cơ sở & Đơn vị", "Hệ thống Tiếng Việt", "Âm tiết"])
    with tab1:
        st.markdown("**Cơ sở sinh lí:** Phổi, Dây thanh, Khoang cộng hưởng (Họng, Mũi, Miệng).\n\n**Âm tố:** Âm thanh thực tế `[ ]`. **Âm vị:** Đơn vị khu biệt nghĩa `/ /`.")
    with tab2:
        st.markdown("**Tiếng Việt:** 11 nguyên âm đơn, 3 nguyên âm đôi (iê, uô, ươ), 17 phụ âm đơn, 10 phụ âm ghép, 6 thanh điệu.")
        st.warning("**Chính tả:** k/gh/ngh đi với i, e, ê. Còn c/g/ng đi với các âm khác. q đi với âm đệm u.")
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.success("**Tiếng Anh:** Khởi âm + ĐỈNH ÂM (Nguyên âm) + Kết âm. *Quy tắc đếm:* Bao nhiêu nguyên âm đọc lên -> bấy nhiêu âm tiết.")
        with col2:
            st.info("**Tiếng Việt:** Âm đầu + Âm đệm + ÂM CHÍNH + Âm cuối + Thanh điệu.")
    
    # Gọi hàm nhúng AI
    render_ai_tutor("Bài 4")

elif choice == "Bài 5: Từ vựng":
    st.title("Bài 5: Từ vựng")
    tab1, tab2, tab3 = st.tabs(["Cấu tạo từ", "Phân loại từ", "Ý nghĩa của Từ"])
    with tab1:
        st.markdown("**Hình vị (Morpheme):** Đơn vị nhỏ nhất có nghĩa.\n* *Anh:* Căn tố (Root), Phụ tố (Affix).\n* *Việt:* Tiếng tự do, Tiếng không tự do.")
    with tab2:
        st.markdown("* **Anh:** Phụ gia, Ghép, Láy.\n* **Việt:** Từ ghép (Đẳng lập, Chính phụ), Từ láy (Láy đôi, ba, tư).")
    with tab3:
        st.markdown("**Các thành tố nghĩa:**\n* Nghĩa biểu vật (Sự vật hiện thực).\n* Nghĩa biểu niệm (Thuộc tính khái quát).\n* Nghĩa biểu thái (Thái độ, cảm xúc).\n* Nghĩa ngữ pháp (Vai trò trong câu).")
    
    # Gọi hàm nhúng AI
    render_ai_tutor("Bài 5")

elif choice == "Bài 6: Ngữ pháp":
    st.title("Bài 6: Ngữ pháp")
    tab1, tab2 = st.tabs(["Ý nghĩa & Phương thức", "Phạm trù & Quan hệ"])
    with tab1:
        st.markdown("**Ý nghĩa ngữ pháp:** Nghĩa khái quát cho một nhóm (vd: thời gian hành động, sự vật).\n\n**Phương thức:**\n* Phụ gia (Anh, Nga).\n* Biến đổi căn tố (man->men).\n* Hư từ (đặc trưng Tiếng Việt: đã, đang, sẽ).")
    with tab2:
        st.markdown("**Phạm trù:** Số, Giống, Thời/Thì, Ngôi.\n\n**Quan hệ:**\n* Đẳng lập (gió và mưa).\n* Chính - phụ (áo đỏ).\n* Chủ - vị (Mặt trời lặn).")
    
    # Gọi hàm nhúng AI
    render_ai_tutor("Bài 6")
