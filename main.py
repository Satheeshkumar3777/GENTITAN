import streamlit as st
from src.page1 import page1
from src.page2 import page2
from src.page3 import page3
from src.page4 import page4
from src.page5 import page5
from src.img2img import img2img
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

pages = {
    "HOME": page1,
    "OPEN AI-Text to image": page2,
    "OPEN AI-Image variation": page3, # Pass HD function reference here
    "STABLE-DIFUSSION TEXT2IMAGE":page4,
    "SD":page5,
    "page5":img2img,
}

# Create the selectbox in the sidebar
page = st.sidebar.selectbox("Select a page", list(pages.keys()))
pages[page]()  # Call other pages as before
