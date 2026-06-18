
import streamlit as st
st.image("banner.jpg")
st.title("💰 App tính Thuế Thu Nhập Cá Nhân")

thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (VNĐ)",
    min_value=0.0
)

nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0
)

if st.button("Tính thuế"):
    giam_tru = 11000000 + nguoi_phu_thuoc * 4400000
    thu_nhap_tinh_thue = max(0, thu_nhap - giam_tru)

    thue = thu_nhap_tinh_thue * 0.1

    st.success(f"Thuế phải nộp: {thue:,.0f} VNĐ")
