
import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="이름")
grade = st.radio("학년", ["1", "2", "3"], horizontal=True)
ban = st.number_input("반", min_value=1, max_value=11, value=1)
hard = st.select_slider("난이도",options=["쉬움", "보통", "어려움", "매우 어려움"],value="보통")
score = st.slider("점수", 0, 100, 50)
feel = st.text_area("소감", placeholder="소감합니다.")

if st.button("확인"):
        st.success(f"{user_id} / {grade} / {ban}반 / {hard}")
        st.info(f"소감: {feel}")
