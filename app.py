import streamlit as st
import pandas as pd

# Cấu hình trang
st.set_page_config(page_title="Ôn tập Dẫn luận Ngôn ngữ học", page_icon="🎓", layout="wide")

# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/vi/thumb/a/a2/Logo_Tr%C6%B0%E1%BB%9Dng_%C4%90%E1%BA%A1i_h%E1%BB%8Dc_M%E1%BB%9F_H%C3%A0_N%E1%BB%99i.png/150px-Logo_Tr%C6%B0%E1%BB%9Dng_%C4%90%E1%BA%A1i_h%E1%BB%8Dc_M%E1%BB%9F_H%C3%A0_N%E1%BB%99i.png", width=100)
st.sidebar.title("📚 Mục lục bài giảng")
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

if choice == "Giới thiệu chung":
    st.title("🎓 Dẫn luận Ngôn ngữ học (ENO3)")
    st.markdown("---")
    st.info("**Giảng viên:** PGS.TS. Phạm Tất Thắng\n\n**Đơn vị:** Chương trình Đào tạo Trực tuyến - Trường Đại học Mở Hà Nội")
    st.write("Ứng dụng tổng hợp chi tiết toàn bộ kiến thức môn Dẫn luận Ngôn ngữ học (ENO3).")
    st.write("Bản cập nhật này bổ sung đầy đủ các ví dụ minh họa, quy tắc chính tả, tác giả các học thuyết và các khái niệm chuyên sâu nhằm hỗ trợ tối đa cho việc ôn thi và nghiên cứu ngôn ngữ.")
    
elif choice == "Bài 1: Bản chất & Chức năng":
    st.title("Bài 1: Bản chất và Chức năng của Ngôn ngữ")
    tab1, tab2 = st.tabs(["Bản chất của Ngôn ngữ", "Chức năng của Ngôn ngữ"])
    
    with tab1:
        st.subheader("1. Quan niệm duy tâm")
        st.markdown('''
        * Cho rằng ngôn ngữ giống các hiện tượng tự nhiên (sấm, sét, mưa, gió, hạn hán...).
        * Coi ngôn ngữ giống tiếng kêu của động vật.
        * Cho rằng ngôn ngữ có tính di truyền.
        * Ngôn ngữ là hiện tượng cá nhân hay của một giai cấp nhất định.
        ''')
        
        st.subheader("2. Quan niệm duy vật")
        st.success("**Ngôn ngữ là hiện tượng xã hội:**\n* Được sinh ra trong xã hội do con người sáng tạo ra.\n* Là tài sản chung cho cả cộng đồng chứ không thuộc về cá nhân.\n* Sự tồn tại và phát triển của ngôn ngữ gắn liền với sự tồn tại và phát triển của xã hội.")
        st.info("**Ngôn ngữ là hiện tượng xã hội đặc biệt:**\n* Không thuộc cơ sở hạ tầng và kiến trúc thượng tầng.\n* Không có tính giai cấp.\n* Có mối liên hệ trực tiếp với hoạt động sản xuất.")
        
    with tab2:
        st.subheader("1. Chức năng giao tiếp")
        st.write("Giao tiếp là hoạt động trao đổi thông tin. So với các phương tiện khác (cử chỉ, tín hiệu giao thông, morse...), ngôn ngữ là công cụ quan trọng nhất vì:")
        st.markdown('''
        * Nội dung biểu đạt phong phú, đa dạng và chi tiết hơn.
        * Gần gũi và quen thuộc với đời sống con người.
        * Có khả năng biểu thị mọi trạng thái cảm xúc của con người.
        ''')
        
        st.subheader("2. Chức năng thể hiện tư duy")
        st.write("Tư duy là quá trình nhận thức thế giới từ trực quan sinh động (cảm tính) đến trừu tượng (lí tính).")
        st.markdown('''
        * **Hiện thực trực tiếp của tư tưởng:** Bất kì đơn vị có nghĩa nào (từ, cụm từ, câu) cũng chứa đựng ý nghĩ. *(Ví dụ: từ "mưa", câu "Trời mưa")*.
        * **Tham gia hình thành tư tưởng:** Ý nghĩ được định hình dưới dạng ngôn ngữ. Nếu không diễn đạt được bằng ngôn ngữ, tư tưởng đó sẽ trở nên mơ hồ, trừu tượng và rất khó hiểu.
        ''')

elif choice == "Bài 2: Nguồn gốc & Phát triển":
    st.title("Bài 2: Nguồn gốc và Sự phát triển của Ngôn ngữ")
    
    with st.expander("🌟 Nguồn gốc của Ngôn ngữ", expanded=True):
        st.markdown('''
        **A. Các quan niệm trước chủ nghĩa Mác:** 
        * **Thuyết Tượng thanh:** Do bắt chước âm thanh tự nhiên. *(Đại biểu: Platon, Augustin)*. Tuy có các từ tượng thanh (chim chích chòe, rì rào...) nhưng số lượng rất ít.
        * **Thuyết Cảm thán:** Bắt nguồn từ âm thanh cảm xúc (vui, buồn, đau đớn). *(Đại biểu: Rút-sô, Stăng-đan)*. Số lượng thán từ (ối, á, a ha...) cũng không đủ làm nguồn gốc toàn bộ ngôn ngữ.
        * **Thuyết Khế ước xã hội:** Do con người thỏa thuận với nhau. *(Đại biểu: Adam Smít, Rút-sô)*. Nhược điểm: Muốn thỏa thuận thì phải có ngôn ngữ từ trước.
        * **Thuyết Ngôn ngữ Cử chỉ:** Dùng tư thế cơ thể và tay. *(Đại biểu: Vunter, Mac)*. Thực tế cử chỉ chỉ đi kèm phụ trợ, không thể đẻ ra tiếng nói.
        
        **B. Quan niệm của chủ nghĩa Mác (Thuyết Lao động):**
        * Do **C. Mác** và **Ph. Ăng-ghen** đề xướng. 
        * Lao động giúp con người hoàn thiện về tư tưởng, có khả năng tư duy trừu tượng. Lao động quyết định sự ra đời của ngôn ngữ (vừa tạo nhu cầu giao tiếp, vừa thúc đẩy tư duy). **Đây là quan niệm duy nhất đúng.**
        ''')
        
    with st.expander("📈 Quá trình phát triển", expanded=True):
        st.markdown('''
        1. **Ngôn ngữ bộ lạc:** Cộng đồng thị tộc (cùng huyết thống) kết hợp thành bộ lạc, có chung 1 ngôn ngữ trên 1 lãnh thổ.
        2. **Ngôn ngữ khu vực:** Bước quá độ khi bộ lạc tan rã, dùng làm tiếng nói chung cho mọi người trong một vùng không phân biệt thị tộc.
        3. **Ngôn ngữ dân tộc:** Đòi hỏi của nhà nước/dân tộc. Dựa trên sự thống nhất có chọn lọc từ các phương ngữ. *(Ví dụ: VN có 3 vùng phương ngữ Bắc, Trung, Nam).*
        4. **Ngôn ngữ văn hóa:** Biến thể được trau chuốt, chuẩn mực hóa, dùng trong văn học, hành chính, khoa học. Tồn tại ở dạng Nói và Viết.
        5. **Ngôn ngữ cộng đồng tương lai:** Thứ ngôn ngữ quốc tế dùng chung cho nhân loại. 
        ''')
        st.write("*Ví dụ về Quốc tế ngữ Esperanto (L.L. Zamenhof sáng lập 1887):*")
        df = pd.DataFrame({
            "Tiếng Việt": ["Xin chào", "Cảm ơn", "Tôi yêu bạn"],
            "Tiếng Anh": ["Hello", "Thank you", "I love you"],
            "Esperanto": ["Saluton", "Dankon", "Mi amas vin"]
        })
        st.table(df)
        
    with st.expander("⚙️ Cách thức & Nhân tố phát triển"):
        st.markdown('''
        * **Cách thức:** Phát triển kế thừa (từ từ, liên tục), không nhảy vọt. Tốc độ thay đổi không đồng đều:
          * *Từ vựng:* Thay đổi nhanh nhất, tức thời phản ánh xã hội.
          * *Ngữ âm:* Biến đổi chậm.
          * *Ngữ pháp:* Biến đổi chậm nhất vì là kết cấu lõi.
        * **Nhân tố khách quan:** Kinh tế, chính trị, văn hóa, giáo dục.
        * **Nhân tố chủ quan:** Quan điểm, thái độ của con người, chính sách pháp luật về ngôn ngữ quốc gia/ngoại ngữ.
        ''')

elif choice == "Bài 3: Hệ thống kí hiệu":
    st.title("Bài 3: Ngôn ngữ là Hệ thống Kí hiệu Đặc biệt")
    
    st.markdown('''
    * **Hệ thống:** Một thể thống nhất gồm các yếu tố và mối liên hệ giữa chúng. *(Ví dụ: "Gia đình" là hệ thống gồm các thành viên và quan hệ giữa họ).*
    * **Kí hiệu:** Dạng vật chất mang thông tin. Có tính vật chất, gồm Hình thức & Nội dung, mang tính quy ước và nằm trong hệ thống.
    * **Ngôn ngữ:** Gồm các đơn vị (Âm vị, hình vị, từ, cụm từ, câu) liên kết qua các quan hệ: **Tuyến tính** (ngang), **Liên tưởng** (dọc), và **Cấp độ** (bao thuộc).
    ''')
    
    st.subheader("5 Đặc trưng của Kí hiệu ngôn ngữ")
    st.info("**1. Tính võ đoán (Arbitrariness):**\nMối quan hệ giữa Cái biểu đạt (vỏ âm thanh) và Cái được biểu đạt (ý nghĩa) không có lí do tự nhiên. \n*Ví dụ: Từ "cà cuống" gọi tên 1 loài côn trùng lưỡng cư, không liên quan gì đến nghĩa gốc của từ "cà" và "cuống".*")
    st.info("**2. Tính đa trị (Multi-values):**\nSự đa dạng giữa hình thức - nội dung. Thể hiện qua từ đa nghĩa, đồng nghĩa, trái nghĩa, đồng âm; hoặc các hiện tượng nghĩa đen, nghĩa bóng, ẩn dụ, hoán dụ.")
    st.info("**3. Tính xuất hiện theo trật tự tuyến tính (Linear):**\nCác kí hiệu phải xuất hiện kế tiếp nhau liên tục trên trục thời gian. \n*Ví dụ thay đổi trật tự làm đổi nghĩa:*\n- Sao bảo nó không đến.\n- Bảo sao nó không đến.\n- Nó bảo sao không đến.")
    st.info("**4. Vừa đồng loại, vừa không đồng loại:**\nCó nhiều loại hình thức (âm vị, thanh điệu, hình vị...). Quan hệ giữa chúng theo nhiều cấp độ tôn ti (Âm vị < Hình vị < Từ < Cụm từ < Câu).")
    st.info("**5. Vừa có tính đồng đại, vừa có tính lịch đại:**\nLà sản phẩm của quá khứ để lại (lịch đại) nhưng lại đang được con người sử dụng làm công cụ tư duy, giao tiếp hàng ngày (đồng đại).")

elif choice == "Bài 4: Ngữ âm":
    st.title("Bài 4: Ngữ âm")
    st.markdown("Ngữ âm là vỏ vật chất âm thanh của ngôn ngữ. Có 2 phân ngành: **Ngữ âm học** (Phonetics - nghiên cứu bản chất chung) và **Âm vị học** (Phonology - nghiên cứu hệ thống âm thanh của 1 ngôn ngữ cụ thể).")
    
    tab1, tab2, tab3 = st.tabs(["Bản chất & Đơn vị", "Hệ thống Âm vị Tiếng Việt", "Cấu tạo Âm tiết"])
    
    with tab1:
        st.subheader("1. Bản chất")
        st.markdown('''
        * **Cơ sở vật lí:** Sóng âm dao động, đo bằng biên độ, cao độ, trường độ, cường độ, âm sắc.
        * **Cơ sở sinh lí (Bộ máy phát âm):**
          * *Phổi:* Khởi phát nguồn hơi.
          * *Dây thanh:* Nằm trong thanh hầu, tạo tiếng thanh.
          * *Khoang cộng hưởng:* 
            * **Khoang họng:** Tạo âm họng/tắc họng (h, l).
            * **Khoang mũi:** Tạo âm mũi (m, n, ng, p, t, k).
            * **Khoang miệng:** Lớn nhất và quan trọng nhất (răng, lợi, lưỡi, ngạc...), phát ra hầu hết nguyên âm và phụ âm.
        ''')
        st.subheader("2. Các đơn vị")
        st.markdown('''
        * **Âm tố [a]:** Đơn vị ngữ âm nhỏ nhất về mặt cấu âm - thính giác.
        * **Âm vị /a/:** Đơn vị ngữ âm nhỏ nhất có chức năng khu biệt vỏ âm thanh. *(Vd: "tan" có 3 âm vị /t/, /a/, /n/).*
        * **Âm tiết:** Khúc đoạn âm thanh nhỏ nhất trong chuỗi lời nói. *(Vd: "hôm nay trời mưa" có 4 âm tiết).*
        ''')
        
    with tab2:
        st.subheader("Hệ thống Âm vị Tiếng Việt")
        st.markdown('''
        * **Nguyên âm:** 
          * 11 nguyên âm đơn (trong đó /â/ và /ă/ là âm ngắn).
          * 2 bán nguyên âm (/u/ và /i/).
          * 3 nguyên âm đôi: **/iê/, /uô/, /ươ/** (Có quy tắc viết chính tả đa dạng, vd: uô $\rightarrow$ ua; iê $\rightarrow$ ia, yê, ya; ươ $\rightarrow$ ưa).
        * **Phụ âm:** 17 phụ âm đơn, 10 phụ âm ghép.
        ''')
        with st.expander("📌 Quy tắc chính tả phụ âm quan trọng:"):
            st.markdown('''
            * **Phụ âm /k/:** 
              * Viết là **K** trước e, ê, i, iê, y.
              * Viết là **Q** trước bán nguyên âm u (quê, qua).
              * Viết là **C** trước các nguyên âm còn lại (cá, con).
            * **Phụ âm /g/:**
              * Viết là **Gh** trước e, ê, i, iê.
              * Viết là **G** trước các nguyên âm còn lại.
            * **Phụ âm /ng/:**
              * Viết là **Ngh** trước i, iê, ê, e.
              * Viết là **Ng** trước các nguyên âm còn lại.
            ''')
            
    with tab3:
        st.subheader("Cấu tạo Âm tiết")
        colA, colB = st.columns(2)
        with colA:
            st.success('''
            **Tiếng Anh**
            * `Khởi âm` (1) + `Đỉnh âm` (2) + `Kết âm` (3).
            * **Đỉnh âm:** Luôn luôn nằm ở trung tâm và không bao giờ vắng mặt. Luôn do 1 nguyên âm đảm nhận.
            * *Quy tắc:* Từ có bao nhiêu nguyên âm (đỉnh âm) thì có bấy nhiêu âm tiết. 
            * *(Vd: car = 1; table = 2; bicycle = 3).*
            ''')
        with colB:
            st.info('''
            **Tiếng Việt**
            * Gồm 5 phần: `Âm đầu` + `Âm đệm (u,o)` + `Âm chính` + `Âm cuối (p, t, c, m, n, nh, ch, i/y, u/o)` + `Thanh điệu`.
            * `Âm đệm + Âm chính + Âm cuối` gọi chung là **Phần vần**.
            * Tiếng Việt có 6 thanh điệu (không, huyền, ngã, hỏi, sắc, nặng).
            * *(Vd: "tan" - vắng âm đệm; "toàn" - đủ 5 thành phần).*
            ''')

elif choice == "Bài 5: Từ vựng":
    st.title("Bài 5: Từ vựng")
    
    st.markdown("Từ vựng (Lexicon) là tập hợp các đơn vị có nghĩa nhỏ nhất. Ngành nghiên cứu về nó gọi là **Từ vựng học (Lexicology)**.")
    st.write("**Các đơn vị từ vựng:**")
    st.markdown('''
    1. **Từ:** Đơn vị cơ bản nhất, độc lập, có chức năng định danh.
    2. **Cụm từ cố định:** Thành ngữ *(mẹ tròn con vuông)*, Quán ngữ *(của đáng tội)*.
    3. **Tên riêng:** Gọi tên đối tượng cá biệt, đơn nhất (nhân danh, địa danh, tên cơ quan...).
    ''')
    
    tab1, tab2, tab3 = st.tabs(["Hình vị & Cấu tạo từ", "Phân loại từ", "Ý nghĩa của Từ"])
    with tab1:
        st.subheader("1. Đơn vị cấu tạo từ (Hình vị - Morpheme)")
        st.markdown('''
        * **Trong tiếng Anh:** 
          * *Hình vị căn tố (Root):* Mang nghĩa từ vựng cốt lõi. (Vd: `teach`).
          * *Hình vị phụ tố (Affix):* Mang nghĩa ngữ pháp (Tiền tố `un-`, Hậu tố `-er`, Trung tố).
        * **Trong tiếng Việt (Tiếng / Từ tố):**
          * *Tiếng độc lập (Tự do):* Đứng một mình có nghĩa (Vd: `sạch`).
          * *Tiếng không độc lập:* Phải ghép mới có nghĩa (Vd: `sẽ` trong `sạch sẽ`).
        ''')
        st.subheader("2. Phương thức cấu tạo từ")
        st.write("* **Tiếng Anh:** Phụ gia (teach+er = teacher), Ghép (class+room = classroom), Láy (chit-chat, zigzag).*")
        st.write("* **Tiếng Việt:** Ghép (nhà cửa, máy bay), Láy (sạch sẽ, lủng cà lủng củng).*")
        
    with tab2:
        st.subheader("Phân loại từ theo hình thức cấu tạo")
        st.markdown('''
        * **Từ đơn:** nhà, cửa, trời, đất...
        * **Từ ghép:**
          * *Đẳng lập:* nhà cửa, bàn ghế, xe cộ.
          * *Chính phụ:* tàu hỏa, đường sắt, sân bay.
          * *Ngẫu hợp:* mì chính, bồ hóng, ễnh ương.
        * **Từ láy:**
          * *Láy đôi:* sạch sẽ, bóng bảy.
          * *Láy ba:* sạch sành sanh, sát sàn sạt.
          * *Láy tư:* khúc kha khúc khuỷu.
        ''')
        
    with tab3:
        st.subheader("Các thành tố nghĩa của từ (Ngữ nghĩa học - Semantics)")
        st.markdown('''
        * **Nghĩa biểu vật (Denotative):** Liên hệ giữa vỏ ngữ âm với sự vật hiện tượng thực tế (nhà, cửa, nóng, lạnh).
        * **Nghĩa biểu niệm (Significative):** Liên hệ giữa từ với ý niệm, thuộc tính khái quát. *(Vd: "Gà" = động vật nuôi, họ chim, sống trên cạn, lấy thịt/trứng).*
        * **Nghĩa biểu thái/Ngữ dụng (Pragmatical):** Thái độ, cảm xúc người nói. *(Vd: "mắt trắng dã" biểu thị sự chê bai/coi thường; "Ôi Tổ quốc..." biểu thị cảm xúc).*
        * **Nghĩa ngữ pháp (Grammar meaning):** Ý nghĩa nối kết giữa các từ trong lời nói.
        ''')

elif choice == "Bài 6: Ngữ pháp":
    st.title("Bài 6: Ngữ pháp")
    
    st.markdown('''
    Ngữ pháp là tổng thể các quy tắc kết hợp các đơn vị có nghĩa bậc thấp thành bậc cao.
    * **Hình thái học (Morphology):** Nghiên cứu cấu trúc bên trong của từ (cấu tạo từ, biến hình từ, đặc tính ngữ pháp).
    * **Cú pháp học (Syntactics):** Nghiên cứu quy tắc ghép từ thành cụm từ và câu.
    ''')
    st.info("**Hệ thống đơn vị:** `Hình vị (Morpheme)` $\rightarrow$ `Từ (Words)` $\rightarrow$ `Cụm từ (Phrase)` $\rightarrow$ `Câu (Sentence)`")
    
    tab1, tab2 = st.tabs(["Ý nghĩa & Phương thức Ngữ pháp", "Phạm trù & Quan hệ Ngữ pháp"])
    with tab1:
        st.subheader("1. Ý nghĩa ngữ pháp vs Ý nghĩa từ vựng")
        st.markdown('''
        * **Ý nghĩa từ vựng:** Nghĩa cụ thể của riêng một từ. *(Vd: "bàn" = đồ dùng bằng gỗ, mặt phẳng, có chân để bày đồ...).*
        * **Ý nghĩa ngữ pháp:** Nghĩa chung bao trùm lên 1 nhóm từ. *(Vd: các từ nhà, cửa, chó, mèo... đều mang ý nghĩa ngữ pháp chỉ "sự vật" nói chung $\rightarrow$ Danh từ).*
        ''')
        st.subheader("2. Phương thức ngữ pháp")
        st.markdown('''
        * **Phương thức phụ gia:** Dùng phụ tố kết hợp căn tố để tạo Từ phái sinh (Dùng nhiều ở Anh, Pháp, Đức... Vd: `teach` + `er` = `teacher`).
        * **Phương thức biến đổi căn tố:** Thay đổi cấu tạo bên trong căn tố. *(Vd: `take` $\rightarrow$ `took`; `foot` $\rightarrow$ `feet`; `good` $\rightarrow$ `better`).*
        * **Phương thức ngữ điệu:** Thay đổi đường nét giọng nói (Áp dụng cho mọi ngôn ngữ. Vd: *Give it to me!*).
        ''')
    with tab2:
        st.subheader("1. Phạm trù ngữ pháp (Grammatical categories)")
        st.markdown('''
        Những ý nghĩa đối lập tạo thành từng nhóm (2 loại trở lên):
        * **Giống (Gender):** Thuộc danh từ. *(Vd Tiếng Nga: cтoл - giống đực; книга - giống cái).*
        * **Số (Number):** Thuộc danh từ. Ít/nhiều *(Vd: book - books).*
        * **Ngôi (Person):** Thuộc động từ, biểu thị vai giao tiếp. *(Vd: I shall speak / Tôi sẽ nói).*
        ''')
        st.subheader("2. Quan hệ ngữ pháp (Grammatical relation)")
        st.markdown('''
        * **Quan hệ Đẳng lập:** Bình đẳng, tạo từ/cụm từ/câu. *(Vd: bàn ghế, tuy thông minh nhưng lười học).*
        * **Quan hệ Chính - phụ:** Phụ thuộc 1 chiều, tạo từ/cụm từ/câu. *(Vd: tàu thủy, thích vẽ).*
        * **Quan hệ Chủ - vị:** Phụ thuộc qua lại, **chỉ tham gia tạo câu**. *(Vd: Chim hót hay).*
        ''')
