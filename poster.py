import qrcode
import streamlit as st
import graphviz as graphviz


page_title = '如何透過參與黑客松，與學生們一同協作設計出能解決教學問題的方案'
st.set_page_config(page_title=page_title, layout='wide')
st.title(page_title)
st.success('蘇羿豪(Astrohackers in Taiwan社群)@2022 K-12天文教育論壇')

qr = qrcode.QRCode()
qr.add_data(
    data='https://yihaosu-2022k-12astroeduforumposter-poster-99k4yn.streamlitapp.com/'
)
qr_img = qr.make_image(fill='black', back_color='white')
qr_img.save('./qrcode.png')
st.subheader('請掃QR Code進入互動式海報')
st.image('./qrcode.png')


with st.expander('什麼是黑客松？'):
    st.info('[黑客松(hackathon)](https://zh.wikipedia.org/zh-tw/%E9%BB%91%E5%AE%A2%E6%9D%BE)為一種集思廣益解決問題的活動，參與者在短而密集的時間內(通常為一、兩天)，專注於某個問題，協作產出可以解決該問題的軟體、產品、教案...。若是與天文教育和研究相關的問題，產出可能是一個教材或是資料分析的工具。')
    graph = graphviz.Digraph()
    graph.edge('遇到問題', '初步解法')
    graph.edge('初步解法', '提出構想')
    graph.edge('提出構想', '討論與實做')
    st.graphviz_chart(graph)
    st.markdown('以上步驟取自主軸為公民科技的[g0v黑客松網頁](https://jothon.g0v.tw/)，參與者曾在該黑客松協作出[口罩地圖](https://g0v.hackmd.io/@kiang/mask-info)、[Cofacts 真的假的](https://cofacts.tw/)、[阿美族萌典](https://amis.moedict.tw/)等專案。')
