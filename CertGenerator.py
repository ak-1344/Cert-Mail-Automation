import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError as e:
        print(f"⚠️ Could not load font '{path}', using default. Error: {e}")
        return ImageFont.load_default()

def fit_text(draw, text, font_path, max_width, start_size):
    """Reduce font size until text fits max_width"""
    size = start_size
    while size > 10:
        font = ImageFont.truetype(font_path, size)
        # Use textbbox instead of textsize (Pillow >= 10)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        if text_width <= max_width:
            return font
        size -= 5
    return ImageFont.truetype(font_path, 20)


def generate_certificate(name, reg_number, position, template_path, output_path,
                         story_font_path, reg_font_path, merri_font_path):
    template = Image.open(template_path).convert("RGB")
    draw = ImageDraw.Draw(template)
    cert_width, cert_height = template.size

    # Fit fonts dynamically
    name_font = ImageFont.truetype(story_font_path, 60)
    reg_font = fit_text(draw, reg_number, reg_font_path, cert_width - 850, 300)
    position_font = ImageFont.truetype(merri_font_path, 80)

    # Positions
    name_y = cert_height * 0.40
    reg_y = cert_height * 0.46

    position_y = cert_height * 0.58

    # Draw
    draw.text((cert_width/2, name_y), name, fill="white", font=name_font, anchor="mm")
    draw.text((cert_width/2, reg_y), reg_number, fill="white", font=reg_font, anchor="mm")
    draw.text((cert_width/2, position_y), f"{position} Department", fill="white", font=position_font, anchor="mm")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    template.save(output_path)
    print(f"✅ Generated: {output_path}")

def main():
    df = pd.read_csv("certificate_data.csv")
    template_path = "<-- Path to template -->"
    story_font_path = "<-- Path to font -->"
    reg_font_path = '<-- Path to font -->'
    merri_font_path = "<-- Path to font -->"

    output_dir = "GeneratedCertificates"
    os.makedirs(output_dir, exist_ok=True)

    for _, row in df.iterrows():
        name = str(row['Name']).strip()
        reg_number = str(row['Registration']).strip()
        position = str(row['Position']).strip()
        output_path = os.path.join(output_dir, f"{reg_number}.png")

        generate_certificate(name, reg_number, position,
                             template_path, output_path,
                             story_font_path, reg_font_path, merri_font_path)

if __name__ == "__main__":
    main()