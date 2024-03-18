import streamlit as st
import requests
import io
from PIL import Image

# Define function to query Hugging Face model
def query_huggingface(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Main Streamlit app
def page4():
    st.title("Hugging Face Text-to-Image Generation")
    
    # Text input for user prompt
    prompt = st.text_input("Enter your prompt:")
    
    # Button to generate image
    if st.button("Generate Image"):
        # Check if prompt is provided
        if prompt:
            # Query Hugging Face model
            image_bytes = query_huggingface(prompt)
            # Display generated image
            if image_bytes:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption="Generated Image", use_column_width=True)
            else:
                st.error("Failed to generate image. Please try again later.")
        else:
            st.warning("Please enter a prompt before generating the image.")

if __name__ == "__main__":
    page4()
