# 🎨 Text-to-Image Generator

Generate stunning images from text prompts using Stable Diffusion and Streamlit.

## 🔧 Features

- Enter any text prompt and generate an AI image
- Save images to disk with timestamps
- Download generated images directly
- Gallery view of all saved images
- Works locally (no API or HF token needed)
- CPU and GPU compatible

## 🚀 Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
