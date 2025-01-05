from PIL import Image, ImageDraw, ImageFont
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import piexif

def strip_metadata(image_path):
    try:
        piexif.remove(image_path)
    except Exception as e:
        print(f"Failed to strip metadata: {e}")


def add_watermark(image_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    watermark_text = "CryptImage Secure"

    # Define font and position
    font = ImageFont.load_default()
    text_position = (10, 10)
    text_color = (255, 255, 255)

    draw.text(text_position, watermark_text, fill=text_color, font=font)
    image.save(image_path)


def encrypt_image(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()

    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    encrypted_path = image_path + '.enc'
    with open(encrypted_path, 'wb') as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    os.remove(image_path)
    return encrypted_path


def process_image(image_path):
    strip_metadata(image_path)
    add_watermark(image_path)
    return image_path
