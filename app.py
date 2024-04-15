import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")

import requests

def load_lottieurl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        if r.text:  # Check if response is not empty
            return r.json()
        else:
            print("Empty response received.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage
lottie_data = load_lottieurl("https://app.lottiefiles.com/animation/93fa2d15-3bc5-45cc-9a22-77d0961bcedb.json")
img_contact_form=Image.open("images/ks.png")
img_lottie_animation=Image.open("images/sha.png")


# -----Header Section-----
with st.container():
    st.subheader("Hi, my name is Prachi Agrawal")
    st.title("A college student")
    st.write("I am a student passionate about learning python")
    st.write("[Learn More>)(https://pythonandvda.com)")
    st.write("[Learn More>](https://mail.google.com")
# ---what i do---

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write("""If You are a passionate learner diving into the exciting world
         of machine learning (ML). With a curious mind and a thirst for knowledge,
          you are exploring the intricacies of algorithms, data analysis, and pattern 
          recognition. As you delve deeper into ML concepts, you are discovering the
           power of data-driven decision-making and its applications across various domains. 
           then you can check""")
        st.write("[github channel>] https://github.com/Prachi194agrawal")

        with right_column:
            if lottie_data:
                # Process the JSON data here
                st.write(lottie_data)
            else:
                st.write("Failed to fetch Lottie data.")




#---- projects-----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
         st.image(img_lottie_animation)
    with text_column:
        st.subheader("Hoe to add a contact from to your streamlit app")
        st.write("""    
        Want to add a contact from to your streamlit app?
        In this video i am going to show you how to add a contact to your streamlit 
        using pycharm""")
    st.markdown("watch video....](https://www.youtube.com/watch?v=VqgUkExPvLY&t=369s)")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
         st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animation Inside your Streamlite")
        st.write("""Streamlit Lottie enables you to import and display Lottie 
        animations within your Streamlit app, enhancing the overall user experience
         by adding dynamic visual elements.""")
    st.markdown("watch video....](https://www.youtube.com/watch?v=VqgUkExPvLY&t=369s)")







