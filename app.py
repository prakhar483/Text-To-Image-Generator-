# app.py

import streamlit as st
from model import load_model
from utils import save_image, list_saved_images, get_image_bytes
from PIL import Image

# Page setup
st.set_page_config(
    page_title="🎨 Text-to-Image Generator",
    layout="wide",
    page_icon="🖌️"
)

# Title & Description
st.title("🎨 Text-to-Image Generator")
st.markdown("""
Welcome to the **AI Image Generator** app! 🧠🖼️  
Type any creative prompt and watch as **Stable Diffusion** brings it to life in seconds.

---

### 👉 How to use:
1. ✏️ Type a creative prompt (e.g., *A dragon flying over a futuristic city at night*)
2. ⚙️ Adjust settings from the sidebar: guidance, steps, save options
3. 🚀 Click **Generate Image**
4. 📥 Download your image or browse the gallery

> Powered by `Stable Diffusion v1.5`, built with ❤️ using Streamlit and Hugging Face 🤗

---
""")

# Load model once
@st.cache_resource
def get_model():
    return load_model()

pipe = get_model()

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Generation Settings")
    guidance = st.slider("🎚️ Guidance Scale", 1.0, 20.0, 7.5, help="Higher = more creative, lower = more literal")
    steps = st.slider("🔁 Inference Steps", 10, 50, 25, help="More steps = better quality (but slower)")
    image_width = st.selectbox("🖼️ Display Width", [256, 512, 768], index=1)
    save_output = st.checkbox("💾 Save Generated Images", value=True)
    show_gallery = st.checkbox("🖼️ Show Gallery of Saved Images", value=True)

# Prompt input
prompt = st.text_input("📝 Enter your image prompt:", "A fantasy castle in the clouds")

if st.button("🚀 Generate Image"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("🎨 Creating your masterpiece..."):
            result = pipe(prompt, guidance_scale=guidance, num_inference_steps=steps)
            image = result.images[0]

            # Display generated image with selected width
            st.image(image, caption="✅ Your Generated Image", width=image_width)

            # Save image
            if save_output:
                path = save_image(image)
                st.success(f"📁 Image saved to `{path}`")

            # Download button
            img_bytes = get_image_bytes(image)
            st.download_button("📥 Download Image", data=img_bytes, file_name="generated_image.png", mime="image/png")

# Show gallery if enabled
if show_gallery:
    st.markdown("---")
    st.subheader("🖼️ Gallery: Previously Generated Images")

    images = list_saved_images()
    if images:
        cols = st.columns(3)
        for i, img_path in enumerate(images):
            with cols[i % 3]:
                st.image(Image.open(img_path), use_container_width=True, caption=img_path.name)
    else:
        st.info("No images found in gallery yet. Try generating one!")

# Footer / Branding
st.markdown("""
---
<center>
    💡 Made with ❤️ by **Prakhar Dwivedi**  
    Built using [Streamlit](https://streamlit.io/) ⚡ & [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index) 🤗  
    Connect on [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com)  
</center>
""", unsafe_allow_html=True)

