import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# Load your template image
TEMPLATE_PATH = "teachers-day-template.png"

# Streamlit app
st.title("🎉 Teacher's Day Card Generator")
st.write("Type the teacher’s name below and generate a personalized greeting card!")

# Input from user
teacher_name = st.text_input("Enter Teacher's Name:")

if st.button("Generate Card") and teacher_name.strip():
    # Load image
    image = Image.open(TEMPLATE_PATH).convert("RGB")
    draw = ImageDraw.Draw(image)

    # Load custom font
    font = ImageFont.truetype("GreatVibes-Regular.ttf", 80)  

    # Get image size and text dimensions
    W, H = image.size
    text_w = draw.textlength(teacher_name, font=font)
    text_h = font.size

    # Position text
    x = (W - text_w) / 2
    y = H - (text_h + 730)  # Adjust this value to move text up/down

    # Draw text
    draw.text((x, y), teacher_name, font=font, fill=(0, 0, 0))

    # Save with unique filename
    safe_name = teacher_name.replace(" ", "_")
    output_path = f"card_{safe_name}.png"
    image.save(output_path)

    # Display success and preview
    st.success(f"Card generated for {teacher_name}!")
    st.image(image, caption=f"Card for {teacher_name}", use_column_width=True)

    # Download button
    with open(output_path, "rb") as f:
        st.download_button(
            label="📥 Download Card",
            data=f,
            file_name=output_path,
            mime="image/png"
        )