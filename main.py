import streamlit as st
from utils import generate_script
st.title("应付评价辅助器")

subject = st.text_input("请输入餐厅名称：")
length = st.number_input("请输入字数要求:")
submit = st.button("生成文字内容")
if submit and not subject:
    st.info("你忘记输入餐厅名称了")
    st.stop()
if submit and not length:
    st.info("你忘记输入字数要求了")
    st.stop()
if submit:
    with st.spinner("AI正在思考"):
        title, script = generate_script(subject, length)
    st.success('生成成功')
    st.write(title)
    st.write(script)