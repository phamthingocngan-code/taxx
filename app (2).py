
import streamlit as st
st.image("banner.jpg")
st.title("💰 App tính Thuế Thu Nhập Cá Nhân")

thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (VNĐ)",
    min_value=0.0
)

nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0,
    step=1
)

if st.button("Tính thuế"):

    # Giảm trừ gia cảnh
    giam_tru_ban_than = 11_000_000
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 4_400_000

    # Bảo hiểm bắt buộc 10.5%
    bao_hiem = thu_nhap * 0.105

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = max(
        0,
        thu_nhap
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
        - bao_hiem
    )

    # Thuế TNCN (ví dụ 5%)
    thue = thu_nhap_tinh_thue * 0.05

    # Thu nhập sau thuế
    thu_nhap_sau_thue = thu_nhap - bao_hiem - thue

    st.success("Kết quả tính toán")

    st.write(f"📌 Thu nhập trước thuế: {thu_nhap:,.0f} VNĐ")
    st.write(f"📌 Giảm trừ bản thân: {giam_tru_ban_than:,.0f} VNĐ")
    st.write(f"📌 Giảm trừ người phụ thuộc: {giam_tru_phu_thuoc:,.0f} VNĐ")
    st.write(f"📌 Bảo hiểm bắt buộc (10.5%): {bao_hiem:,.0f} VNĐ")
    st.write(f"📌 Thu nhập tính thuế: {thu_nhap_tinh_thue:,.0f} VNĐ")
    st.write(f"📌 Thuế TNCN phải nộp: {thue:,.0f} VNĐ")
    st.write(f"📌 Thu nhập sau thuế: {thu_nhap_sau_thue:,.0f} VNĐ")
