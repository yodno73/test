import streamlit as st

st.title("약수 계산기")

num = st.number_input("숫자를 입력하세요", min_value=1, step=1)

if st.button("약수 구하기"):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    st.write(f"**{num}의 약수:** {divisors}")
