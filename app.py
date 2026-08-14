import os
import pandas as pd
import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Ôn tập Dẫn luận Ngôn ngữ học", page_icon="🎓", layout="wide"
)

# Sidebar - Hiển thị Logo an toàn
logo_path = "logo.png"
if os.path.exists(logo_path):
  st.sidebar.image(logo_path, width=150)
else:
  # Nếu không có file logo nội bộ, sử dụng biểu tượng Emoji lớn và đẹp
  st.sidebar.markdown(
      "<h1 style='text-align: center; margin-bottom: 0;'>🎓</h1>",
      unsafe_allow_html=True,
  )
  st.sidebar.markdown(
      "<p style='text-align: center; font-weight: bold; color:"
      " #1E88E5;'>ĐẠI HỌC MỞ HÀ NỘI</p>",
      unsafe_allow_html=True,
  )

st.sidebar.title("📚 Mục lục bài giảng")
menu = [
    "Giới thiệu chung",
    "Bài 1: Bản chất & Chức năng",
    "Bài 2: Nguồn gốc & Phát triển",
    "Bài 3: Hệ thống kí hiệu",
    "Bài 4: Ngữ âm",
    "Bài 5: Từ vựng",
    "Bài 6: Ngữ pháp",
]
choice = st.sidebar.radio("Điều hướng:", menu)

if choice == "Giới thiệu chung":
  st.title("🎓 Dẫn luận Ngôn ngữ học (ENO3)")
  st.markdown("---")
  st.info(
      "**Giảng viên:** PGS.TS. Phạm Tất Thắng\n\n**Đơn vị:** Chương trình Đào"
      " tạo Trực tuyến - Trường Đại học Mở Hà Nội"
  )
  st.write(
      "Ứng dụng tổng hợp chi tiết toàn bộ kiến thức môn Dẫn luận Ngôn ngữ học"
      " (ENO3)."
  )
  st.write(
      "Bản cập nhật này đã **SỬA HOÀN TOÀN LỖI MẤT ICON / LỖI ẢNH LOGO VỠ**,"
      " đồng thời giữ nguyên toàn bộ nội dung chi tiết và ví dụ minh họa."
  )

elif choice == "Bài 1: Bản chất & Chức năng":
  st.title("Bài 1: Bản chất và Chức năng của Ngôn ngữ")
  tab1, tab2 = st.tabs(["Bản chất của Ngôn ngữ", "Chức năng của Ngôn ngữ"])

  with tab1:
    st.subheader("1. Quan niệm duy tâm (Đã lỗi thời)")
    st.markdown("""
        * Cho rằng ngôn ngữ giống các hiện tượng tự nhiên (như sấm, sét, mưa, gió...).
        * Coi ngôn ngữ giống tiếng kêu của động vật (bản năng).
        * Cho rằng ngôn ngữ có tính di truyền (cha sinh con ra tự nhiên biết nói).
        * Ngôn ngữ là hiện tượng cá nhân hay của một giai cấp nhất định.
        """)

    st.subheader("2. Quan niệm duy vật (Chính xác)")
    st.success("""
        **A. Ngôn ngữ là hiện tượng xã hội:**
        * Được sinh ra trong xã hội do con người sáng tạo ra. Trẻ em nếu bị cô lập khỏi xã hội loài người (như bé gái người sói) sẽ không có ngôn ngữ.
        * Là tài sản chung cho cả cộng đồng, không ai có đặc quyền sở hữu.
        * Phát triển gắn liền cùng xã hội. **Ví dụ:** Khi xã hội xuất hiện Internet, các từ vựng mới như *livestream, netizen, AI, app* lập tức ra đời để đáp ứng nhu cầu giao tiếp.
        """)
    st.info("""
        **B. Ngôn ngữ là hiện tượng xã hội ĐẶC BIỆT:**
        * **Không thuộc cơ sở hạ tầng hay kiến trúc thượng tầng:** Khi chế độ phong kiến sụp đổ, hệ tư tưởng phong kiến mất đi, nhưng tiếng Việt không hề bị diệt vong, nó vẫn tiếp tục phục vụ xã hội mới.
        * **Không có tính giai cấp:** Cả người giàu và người nghèo, giai cấp thống trị hay bị trị đều dùng chung một bộ quy tắc ngữ pháp và từ vựng. Không có "ngôn ngữ của người giàu" theo định nghĩa hệ thống.
        * **Có mối liên hệ trực tiếp với sản xuất:** Ngôn ngữ hỗ trợ con người hiệp đồng lao động.
        """)

  with tab2:
    st.subheader("1. Chức năng giao tiếp")
    st.write(
        "Giao tiếp là hoạt động truyền đạt và trao đổi thông tin. Ngôn ngữ là"
        " công cụ vạn năng và quan trọng nhất vì:"
    )
    st.markdown("""
        * **Vượt qua không gian và thời gian:** Ta có thể đọc được suy nghĩ của người xưa qua các văn bản lịch sử.
        * **Đa dạng và chi tiết:** Có thể diễn tả từ những khái niệm cụ thể (cái bàn, cái ghế) đến trừu tượng (hạnh phúc, triết học, hạt quark).
        * **Biểu thị cảm xúc:** Kết hợp với ngữ điệu để truyền tải sự phẫn nộ, vui mừng, mỉa mai...
        """)

    st.subheader("2. Chức năng thể hiện tư duy")
    st.markdown("""
        Tư duy và ngôn ngữ như hai mặt của một tờ giấy, không thể tách rời.
        * **Ngôn ngữ là hiện thực trực tiếp của tư tưởng:** Mọi đơn vị có nghĩa đều chứa đựng ý nghĩ. Bạn không thể "nghĩ" ra một khái niệm nếu không có "từ" để khoác lên nó.
        * **Quá trình hình thành tư tưởng:** Khi bạn giải toán hay lập luận, bạn thực chất đang "nói thầm" trong đầu bằng ngôn ngữ. Nếu diễn đạt bằng ngôn ngữ không rõ ràng (mơ hồ), điều đó chứng tỏ tư duy của bạn về vấn đề đó cũng đang bị rối.
        """)

elif choice == "Bài 2: Nguồn gốc & Phát triển":
  st.title("Bài 2: Nguồn gốc và Sự phát triển của Ngôn ngữ")

  with st.expander("🌟 Nguồn gốc của Ngôn ngữ", expanded=True):
    st.markdown("""
        **A. Các quan niệm trước chủ nghĩa Mác (Chủ quan, chưa hoàn thiện):** 
        * **Thuyết Tượng thanh (Platon, Augustin):** Bắt chước âm thanh tự nhiên. 
          * *Ví dụ:* chim chích chòe, tu hú, rào rào, đùng đoàng. -> Hạn chế: Những từ trừu tượng như "hòa bình", "tình yêu" thì bắt chước âm thanh gì?
        * **Thuyết Cảm thán (Rút-sô):** Bắt nguồn từ tiếng kêu cảm xúc.
          * *Ví dụ:* ối, á, ôi chao. -> Hạn chế: Thán từ quá ít, không thể tạo nên hàng vạn từ vựng.
        * **Thuyết Khế ước (Adam Smít):** Do con người ngồi lại thỏa thuận. -> Hạn chế: Chưa có tiếng nói thì dùng gì để thỏa thuận?
        
        **B. Quan niệm của chủ nghĩa Mác (Thuyết Lao động - Duy nhất đúng):**
        * Bắt nguồn từ C. Mác và Ph. Ăng-ghen.
        * **Cơ chế:** Quá trình lao động chung (săn bắt, hái lượm) buộc con người *phải* giao tiếp để phối hợp. Đồng thời, lao động làm biến đổi bộ máy phát âm và hoàn thiện vỏ não, giúp con người có khả năng tư duy trừu tượng -> Ngôn ngữ ra đời.
        """)

  with st.expander("📈 Quá trình phát triển", expanded=True):
    st.markdown("""
        1. **Ngôn ngữ bộ lạc:** Quy mô nhỏ, dùng nội bộ trong thị tộc cùng huyết thống.
        2. **Ngôn ngữ khu vực:** Khi bộ lạc sáp nhập, hình thành phương ngữ vùng.
        3. **Ngôn ngữ dân tộc:** Khi hình thành nhà nước, cần một ngôn ngữ chung. 
          * *Ví dụ thực tế:* Tiếng Việt dân tộc được xây dựng dựa trên sự hòa trộn của 3 phương ngữ Bắc - Trung - Nam, nhưng lấy âm sắc Hà Nội làm chuẩn mực để giao tiếp chung.
        4. **Ngôn ngữ văn hóa:** Là ngôn ngữ đã được chuẩn hóa (có từ điển, có luật chính tả), dùng trong giáo dục, báo chí, văn học nghệ thuật. 
          * *Ví dụ:* Ngôn ngữ trong các bản tin thời sự VTV là ngôn ngữ văn hóa.
        5. **Ngôn ngữ cộng đồng tương lai:** Ước mơ về ngôn ngữ chung cho toàn cầu (ví dụ: quốc tế ngữ Esperanto).
        """)

  with st.expander("⚙️ Cách thức & Nhân tố phát triển"):
    st.markdown("""
        **1. Phát triển không đồng đều (Rất quan trọng):**
        * **Từ vựng (Nhanh nhất):** Mỗi năm tiếng Việt bổ sung hàng trăm từ mới (gen Z, flex, thả thính, trí tuệ nhân tạo).
        * **Ngữ âm (Chậm hơn):** Phải qua hàng trăm năm người ta mới đổi cách phát âm (như tiếng Việt cổ rụng bớt các tổ hợp phụ âm kép: *blời* -> *trời*, *mlời* -> *lời*).
        * **Ngữ pháp (Chậm nhất):** Quy tắc S-V-O (Chủ-Động-Tân) của tiếng Việt, Anh... duy trì hàng ngàn năm không đổi.
        
        **2. Nhân tố tác động:**
        * *Khách quan:* Giao lưu kinh tế, xâm lược (Vd: Tiếng Việt mượn rất nhiều từ Hán-Việt do 1000 năm Bắc thuộc, mượn từ tiếng Pháp như: *xà phòng, gác-đờ-măng, phanh, lốp*).
        * *Chủ quan:* Các chính sách giáo dục ngôn ngữ của nhà nước.
        """)

elif choice == "Bài 3: Hệ thống kí hiệu":
  st.title("Bài 3: Ngôn ngữ là Hệ thống Kí hiệu Đặc biệt")

  st.markdown("""
    * **Hệ thống:** Một thể thống nhất gồm các phần tử và mối quan hệ giữa chúng.
    * **Kí hiệu:** Dạng vật chất mang thông tin. Một kí hiệu phải có vỏ hình thức (Cái biểu đạt) và nội dung ý nghĩa (Cái được biểu đạt).
    """)

  st.subheader("5 Đặc trưng của Kí hiệu ngôn ngữ (Giải thích chi tiết & Ví dụ)")

  st.error("""
    **1. Tính võ đoán (Arbitrariness):**
    Không có lý do logic nào bắt buộc một âm thanh phải gắn với một ý nghĩa. Do cộng đồng tự quy ước.
    * *Ví dụ 1:* Con vật hay sủa để giữ nhà, người Việt gọi là "chó", người Anh gọi là "dog", người Pháp gọi là "chien". Bản thân con vật không quy định cái tên của nó.
    * *Ví dụ 2:* Từ "cà cuống" chỉ một loài côn trùng, nhưng hoàn toàn không liên quan gì đến nghĩa của chữ "cà" (quả cà) và "cuống" (cuống lá).
    """)

  st.warning("""
    **2. Tính đa trị (Multi-values):**
    Một hình thức âm thanh có thể gánh nhiều ý nghĩa, hoặc nhiều hình thức cùng chỉ một ý nghĩa.
    * *Hiện tượng Đa nghĩa:* Từ "Chân" (chân người, chân bàn, chân núi). Từ "Đầu" (đầu người, đầu giường, đầu sông).
    * *Hiện tượng Đồng âm:* "Đường" (con đường) và "Đường" (đường ăn).
    * *Hiện tượng Đồng nghĩa:* Chết, hi sinh, qua đời, tỏi, ngoẻo.
    """)

  st.info("""
    **3. Tính tuyến tính (Linear) - TRỤC NGANG:**
    Khi nói hay viết, các từ phải nối đuôi nhau lần lượt trên trục thời gian. Không thể phát âm 2 từ cùng một lúc. Trật tự sắp xếp tạo ra nghĩa khác nhau.
    * *Ví dụ đảo trật tự:* 
      * "Chó cắn mèo" (Mèo bị thương) KHÁC VỚI "Mèo cắn chó" (Chó bị thương).
      * "Sao bảo nó không đến" KHÁC "Bảo sao nó không đến".
    """)

  st.success("""
    **4. Vừa đồng loại, vừa không đồng loại & TRỤC LIÊN TƯỞNG (TRỤC DỌC):**
    * *Tôn ti cấp độ:* Âm vị (cấp thấp) ghép thành Hình vị $\\rightarrow$ Hình vị tạo thành Từ $\\rightarrow$ Từ ghép thành Câu.
    * *Trục liên tưởng:* Tại một vị trí trong câu, ta có thể thay thế bằng các từ đồng loại. 
      * Vd câu: "Tôi **ăn** cơm". Ta có thể liên tưởng thay chữ **ăn** bằng: *nhai, xơi, đớp, hốc* để tạo sắc thái khác nhau.
    """)

  st.primary("""
    **5. Vừa đồng đại, vừa lịch đại:**
    * *Lịch đại (Quá khứ):* Từ "Thái thú", "Quan huyện" là sản phẩm lịch đại.
    * *Đồng đại (Hiện tại):* Hệ thống đang được sử dụng ngay lúc này.
    """)

elif choice == "Bài 4: Ngữ âm":
  st.title("Bài 4: Ngữ âm")

  tab1, tab2, tab3 = st.tabs([
      "Cơ sở & Đơn vị",
      "Hệ thống Tiếng Việt",
      "Âm tiết (Rất quan trọng)",
  ])

  with tab1:
    st.subheader("1. Cơ sở sinh lí (Bộ máy phát âm)")
    st.write("Bộ máy phát âm con người giống như một chiếc đàn:")
    st.markdown("""
        * **Phổi:** Cung cấp luồng hơi (như động cơ).
        * **Dây thanh (trong thanh quản):** Khi luồng hơi đi qua làm rung dây thanh tạo ra tiếng thanh. (Bạn thử đặt tay lên cổ họng và phát âm "z", sẽ thấy rung).
        * **Khoang cộng hưởng (Họng, Mũi, Miệng):**
          * *Khoang mũi:* Nếu luồng hơi đi qua mũi, ta có **âm mũi** (m, n, ng). Khi bạn bị cảm nghẹt mũi, bạn không thể nói chuẩn âm "m" (mẹ -> bẹ).
          * *Khoang miệng:* Bộ phận quan trọng nhất (răng, môi, lưỡi). Lưỡi linh hoạt nhất tạo ra vô vàn âm. (Âm môi: p, b. Âm đầu lưỡi răng: t, th).
        """)

    st.subheader("2. Âm tố vs Âm vị")
    st.markdown("""
        * **Âm tố (Ký hiệu `[ ]`):** Âm thanh thực tế phát ra (vật lí).
        * **Âm vị (Ký hiệu `/ /`):** Khái niệm trừu tượng trong đầu, có chức năng **khu biệt nghĩa**.
          * *Ví dụ:* Thay âm vị `/b/` bằng `/đ/` trong từ "bàn", ta có từ "đàn" -> Nghĩa thay đổi hoàn toàn. Vậy `/b/` và `/đ/` là hai âm vị khác nhau trong tiếng Việt.
        """)

  with tab2:
    st.subheader("Hệ thống Âm vị Tiếng Việt")
    st.markdown("""
        * **Nguyên âm:** 
          * 11 nguyên âm đơn (có /â/, /ă/ là âm ngắn. Vd phân biệt: "tai" (âm dài a) vs "tay" (âm ngắn ă)).
          * 3 nguyên âm đôi: **/iê/, /uô/, /ươ/**.
        * **Phụ âm:** Tiếng việt có 17 phụ âm đơn (b, m, v, d, t, n...) và 10 phụ âm ghép (ch, tr, nh, ng, ngh, th, kh, ph, gh, gi).
        * **Thanh điệu:** 6 thanh (ngang, huyền, ngã, hỏi, sắc, nặng). Thanh điệu là yếu tố quan trọng nhất khu biệt nghĩa ở cấp độ âm tiết (ma, mà, má, mạ...).
        """)

    st.warning("""
        **QUY TẮC CHÍNH TẢ BẮT BUỘC NHỚ:**
        * **Bộ ba c/k/q:** 
          * Đi với (i, e, ê) -> Viết là **k** (kí, kệ, kén).
          * Đi với âm đệm (u) -> Viết là **q** (quốc, quả).
          * Còn lại -> Viết là **c** (cá, cơm, cúc).
        * **Bộ ba ng/ngh và g/gh:**
          * Đi với (i, e, ê) -> Viết là **ngh, gh** (nghỉ ngơi, ghế gỗ).
          * Còn lại -> Viết là **ng, g** (ngủ, gà).
        """)

  with tab3:
    st.subheader("Cấu tạo Âm tiết (Syllable)")
    st.write(
        "Âm tiết là khúc đoạn âm thanh nhỏ nhất ta phát ra. Cách tính số lượng"
        " âm tiết:"
    )

    col1, col2 = st.columns(2)
    with col1:
      st.success("""
            **TIẾNG ANH**
            * Cấu trúc: `Khởi âm` + `ĐỈNH ÂM` + `Kết âm`.
            * **ĐỈNH ÂM (Nguyên âm):** Yếu tố cốt lõi, không bao giờ vắng mặt.
            * **Cách đếm âm tiết:** Một từ có bao nhiêu nguyên âm đọc lên (đỉnh âm) thì có bấy nhiêu âm tiết.
            * *Ví dụ:* 
              * `Cat` (1 nguyên âm /æ/) -> 1 âm tiết.
              * `Table` (2 nguyên âm /eɪ/ và /ə/) -> 2 âm tiết.
              * `Beautiful` (/bjuːtɪfʊl/ - 3 nguyên âm) -> 3 âm tiết.
            """)
    with col2:
      st.info("""
            **TIẾNG VIỆT**
            * Cấu trúc tối đa 5 phần: `Âm đầu` + `Âm đệm` + `ÂM CHÍNH` + `Âm cuối` + `Thanh điệu`.
            * *Phần Vần:* Gồm Âm đệm + Âm chính + Âm cuối.
            * *Ví dụ phân tích từ "Toàn":*
              * Âm đầu: t
              * Âm đệm: o
              * Âm chính (Đỉnh âm): a
              * Âm cuối: n
              * Thanh điệu: huyền
            * Từ "Ta": Chỉ có Âm đầu (t) + Âm chính (a) + Thanh ngang. Vắng đệm và vắng cuối.
            """)

elif choice == "Bài 5: Từ vựng":
  st.title("Bài 5: Từ vựng")

  st.markdown(
      "Từ vựng học (Lexicology) nghiên cứu về: **Từ** (hoạt động độc lập),"
      " **Cụm từ cố định** (Thành ngữ: *Chó ngáp phải ruồi*, Quán ngữ: *Nói"
      " tóm lại*, *Của đáng tội*), và **Tên riêng**."
  )

  tab1, tab2, tab3 = st.tabs(["Cấu tạo từ", "Phân loại từ", "Ý nghĩa của Từ"])
  with tab1:
    st.subheader("1. Đơn vị cấu tạo từ: HÌNH VỊ (Morpheme)")
    st.markdown("""
        Hình vị là đơn vị nhỏ nhất CÓ NGHĨA.
        * **Trong tiếng Anh:** 
          * Căn tố (Root): Nghĩa cốt lõi. VD: `happy` (hạnh phúc).
          * Phụ tố (Affix): Thêm nghĩa ngữ pháp hoặc trái nghĩa. VD: `un-` (tiền tố chỉ sự phủ định), `-ness` (hậu tố biến thành danh từ). -> `unhappiness` có 3 hình vị.
        * **Trong tiếng Việt:** Hình vị đồng nhất với "Tiếng".
          * *Tiếng tự do:* Đứng 1 mình có nghĩa (VD: `nhà`, `xe`, `đẹp`).
          * *Tiếng không tự do:* Phải đi kèm từ khác mới rõ nghĩa (VD: chữ `sẽ` trong `sạch sẽ`, chữ `rào` trong `rì rào`, chữ `quốc` trong `quốc gia`).
        """)

  with tab2:
    st.subheader("2. Phương thức cấu tạo từ")
    colA, colB = st.columns(2)
    with colA:
      st.markdown("""
            **TIẾNG ANH**
            * **Phụ gia:** Thêm phụ tố vào căn tố. VD: `teach` + `er` = `teacher` (người dạy).
            * **Ghép:** Nối 2 căn tố độc lập. VD: `black` (đen) + `board` (bảng) = `blackboard` (bảng đen).
            * **Láy:** Lặp lại vỏ ngữ âm. VD: `zigzag` (ngoằn ngoèo), `chit-chat` (tán gẫu).
            """)
    with colB:
      st.markdown("""
            **TIẾNG VIỆT**
            * **Từ Ghép:** Phối hợp các tiếng có nghĩa.
              * *Đẳng lập:* 2 tiếng bình đẳng (quần áo, bàn ghế, ăn uống).
              * *Chính phụ:* 1 chính 1 phụ (xe đạp, tàu hỏa, hoa hồng - hoa là chính, hồng là phụ chỉ màu sắc).
            * **Từ Láy:** Phối hợp âm thanh. (sạch sẽ, đo đỏ, rập rờn, lúng ta lúng túng).
            """)

  with tab3:
    st.subheader("3. Các thành tố nghĩa của từ")
    st.markdown("""
        Lấy từ **"Cáo"** làm ví dụ phân tích:
        * **Nghĩa biểu vật (Denotative):** Gọi tên đúng con vật có 4 chân, mõm dài, lông hung, sống trong rừng.
        * **Nghĩa biểu niệm (Significative):** Tập hợp các đặc trưng, thuộc tính (động vật ăn thịt, họ chó, tinh ranh).
        * **Nghĩa biểu thái (Pragmatical):** Thái độ đánh giá. Khi nói "Thằng đó là một con cáo", ta dùng nghĩa biểu thái để chỉ sự xảo quyệt, gian ngoan (có ý chê bai, cảnh giác).
        * **Nghĩa ngữ pháp:** Sự liên kết của từ "Cáo" (Danh từ) với các từ khác trong câu.
        """)

elif choice == "Bài 6: Ngữ pháp":
  st.title("Bài 6: Ngữ pháp")

  st.markdown("""
    Ngữ pháp gồm 2 mảng: **Hình thái học** (biến đổi từ) và **Cú pháp học** (ghép từ thành câu).
    *Trình tự phân tích:* `Hình vị` -> `Từ` -> `Cụm từ` -> `Câu`.
    """)

  tab1, tab2 = st.tabs(["Ý nghĩa & Phương thức", "Phạm trù & Quan hệ"])
  with tab1:
    st.subheader("1. Ý nghĩa ngữ pháp")
    st.write(
        "Khác với ý nghĩa từ vựng (chỉ một sự vật cụ thể), ý nghĩa ngữ pháp"
        " mang tính khái quát cho cả một nhóm."
    )
    st.markdown("""
        * *Ví dụ:* "Đang", "Đã", "Sẽ" đều có ý nghĩa ngữ pháp chung là **chỉ thời gian của hành động** (Thì/Thể). 
        * Các từ "Cây", "Sông", "Nhà", "Xe" đều có ý nghĩa ngữ pháp chung là **Danh từ chỉ sự vật**.
        """)

    st.subheader("2. Phương thức ngữ pháp")
    st.markdown("""
        Cách các ngôn ngữ tạo ra ý nghĩa ngữ pháp:
        * **Phương thức phụ gia:** Dùng phổ biến ở ngôn ngữ biến hình (Anh, Nga). Vd thêm `-ed` để chỉ quá khứ: `play` -> `played`. Thêm `-s` để chỉ số nhiều: `cat` -> `cats`.
        * **Phương thức biến đổi căn tố:** Tự đổi ruột bên trong. Vd: `man` -> `men` (đàn ông số nhiều), `go` -> `went` (đi - quá khứ).
        * **Phương thức hư từ (Đặc trưng Tiếng Việt):** Tiếng Việt không biến đổi từ, mà dùng từ đi kèm (hư từ). Vd: Thêm "những/các" để chỉ số nhiều (*những con mèo*), thêm "đã/sẽ" chỉ thời gian (*đã đi*).
        """)

  with tab2:
    st.subheader("1. Phạm trù ngữ pháp")
    st.markdown("""
        Những ý nghĩa đối lập kết hợp thành một phạm trù:
        * **Phạm trù Số:** Đối lập Số ít vs Số nhiều.
        * **Phạm trù Giống:** Đối lập Giống Đực vs Giống Cái (Rất rõ trong tiếng Pháp: *le* (đực), *la* (cái). Tiếng Nga: *cтoл* (đực) vs *книга* (cái)).
        * **Phạm trù Thời / Thì:** Đối lập Quá khứ, Hiện tại, Tương lai.
        * **Phạm trù Ngôi:** Ngôi 1 (người nói), Ngôi 2 (người nghe), Ngôi 3 (người được nhắc đến).
        """)

    st.subheader("2. Quan hệ ngữ pháp")
    st.markdown("""
        Cách các từ liên kết với nhau trên trục tuyến tính:
        * **Quan hệ Đẳng lập:** Hai bên bình đẳng, không ai làm chủ. Có thể đảo vị trí. *(Vd: "gió và mưa", có thể đổi thành "mưa và gió" mà kết cấu không bị phá vỡ).*
        * **Quan hệ Chính - phụ:** Một từ quyết định, một từ phụ họa. Không thể đảo lộn. *(Vd: "áo đỏ" -> "áo" là chính, "đỏ" bổ nghĩa. Đổi thành "đỏ áo" là vô nghĩa).*
        * **Quan hệ Chủ - vị:** Quan hệ bắt buộc để tạo thành CÂU. Chủ ngữ chỉ đối tượng, Vị ngữ chỉ đặc điểm/hành động. *(Vd: "Mặt trời (C) / đang lặn (V)").*
        """)
