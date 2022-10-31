import streamlit as st 

st.write('Hello Junggoo')

'I love you!'

['I', 'love', 'you!']

st.title('Junggoo is good') 
st.subheader('Junggoo is the best!') 
st.write(('I think junggoo should be the king of the world! Racoon will well support her!')) 

st.markdown(
    """
# Cute
## Brave
### Racoon!
    """
)

st.markdown(
            """
            <p>헤이리틀몽몽</p>
            <img src="https://i.pinimg.com/564x/d0/c2/fc/d0c2fcd393d19a1b88504e5d85314672.jpg" width=50% hieght=50%">
            <p>스노우볼 홈페이지</p>
            <iframe src="https://m.blog.naver.com/studygir/221585622789" width="600" height="600"></iframe>
            """,
            unsafe_allow_html=True
        )