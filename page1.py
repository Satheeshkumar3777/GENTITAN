import streamlit as st

introduction = """
Welcome to GenTitan, your ultimate destination for AI-generated jewelry designs! With the power of cutting-edge technologies like Stable Diffusion, OpenAI's DALL-E 3, and Mid-Journey exploration, we bring you a unique and mesmerizing collection of jewelry pieces crafted by artificial intelligence.

Step into the world of innovation and creativity, where every piece tells a story of its own. From elegant necklaces to exquisite earrings, our AI-driven designs are meticulously crafted to captivate your imagination and elevate your style.

Discover the magic of Generative Jewelry at GenTitan, where creativity knows no bounds. Whether you're seeking timeless classics or avant-garde creations, our AI designers are here to transform your vision into reality.

Indulge in the fusion of art and technology, explore our diverse range of AI-generated jewelry, and let your unique style shine with GenTitan. 
Experience the future of jewelry design today!
"""

# Define the pages
def page1():
    st.title("OpenAI DALL·E")
    st.markdown(introduction)