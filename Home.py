import streamlit as st
st.markdown("<h1 style='text-align: center; color: Red;'>Pubs Near me to Redefine the Music Vibe </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Pub culture is an integral part of British life, especially student life. Pubs are a place to go to socialise, relax and have a drink.</h3>", unsafe_allow_html=True)

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://thumbs.dreamstime.com/z/people-party-celebration-drinks-cheers-happiness-concept-drinking-wine-80928369.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

url = "https://www.linkedin.com/in/kavyaarao/"
              
git = "https://github.com/Kavyarao01"


btn_click = st.button("Contact US !")

if btn_click == True:

 st.markdown(":handshake: [Kavya Rao](%s)" % url)
 st.markdown(":computer: [Kavya Rao](%s)" % git)
