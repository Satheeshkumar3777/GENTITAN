import streamlit as st
from PIL import Image
import requests
import json
import io

# Function to make API request and generate image
def generate_image(prompt, image_bytes):
    # API endpoint URL
    url = "https://api.wizmodel.com/v1/predictions"
    
    # JSON payload containing input data
    payload = json.dumps({
        "input": {
            "prompt": prompt
        },
        "version": "fbe05661e1ab10b6e4c13908a3e55381e950b2904582cd55240b7733d59b14e6"
    })
    
    # Request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTA3MzIxMTEsInVzZXJfaWQiOiI2NWY3YWQyZGI2ZDJjN2E0NDZiMDBjNjAifQ.gEixP2_RPoKcWa3T_igmQeA4i7cDRPs_i6gKPRHYhpc'
    }
    
    # Send POST request to the API endpoint
    response = requests.post(url, headers=headers, data=payload)
    
    # Decode the response content (image bytes)
    image_bytes = response.content
    
    # Convert image bytes to PIL Image
    generated_image = Image.open(io.BytesIO(image_bytes))
    
    return generated_image

# Streamlit app
def img2img():
    st.title("Image Generation App")

    # Image upload box
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    # Text prompt box
    prompt = st.text_input("Enter Prompt")

    # Submit button
    if st.button("Generate Image"):
        if uploaded_image is not None and prompt:
            # Read the uploaded image
            image = Image.open(uploaded_image)
            # Display the uploaded image
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Generate image using API request
            generated_image = generate_image(prompt, uploaded_image.read())
            # Display the generated image
            st.image(generated_image, caption="Generated Image", use_column_width=True)
        else:
            st.error("Please upload an image and enter a prompt.")

if __name__ == "__main__":
    img2img()
