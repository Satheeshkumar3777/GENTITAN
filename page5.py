import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline
from diffusers import StableDiffusionImg2ImgPipeline

def load_diffusion_model():
    # Load diffusion model
    pipeline = StableDiffusionImg2ImgPipeline.from_pretrained("stabilityai/stable-diffusion-xl-refiner-1.0")
    return pipeline

def generate_image(uploaded_image, prompt):
    # Load diffusion model
    pipeline = load_diffusion_model()

    # Generate image
    image = Image.open(uploaded_image)
    generated_image = pipeline(prompt=prompt, image=image)

    return generated_image

def page5():
    st.title("Generate Images using Diffusion Model")
    
    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Input prompt
        prompt = st.text_input("Enter your prompt")

        # Generate image button
        if st.button("Generate Image"):
            if prompt:
                with st.spinner("Generating image..."):
                    # Generate the image
                    generated_image = generate_image(uploaded_image, prompt)

                # Display the generated image
                st.image(generated_image, caption="Generated Image", use_column_width=True)
            else:
                st.warning("Please enter a prompt.")

if __name__ == "__main__":
    page5()
