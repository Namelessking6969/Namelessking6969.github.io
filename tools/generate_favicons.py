#!/usr/bin/env python3
"""
Generate favicon files from SVG avatar.
Requires: pip install Pillow cairosvg
"""
import os
import struct
import zlib
from PIL import Image, ImageDraw, ImageFont

def create_favicon_png(size):
    """Create a PNG favicon with NK initials."""
    # Create image with navy background
    img = Image.new('RGBA', (size, size), (44, 62, 80, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw circle background
    draw.ellipse([0, 0, size-1, size-1], fill=(44, 62, 80, 255))
    
    # Draw text
    try:
        # Try to use a font
        font_size = int(size * 0.4)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "NK"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - bbox[1]
    
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    return img

def save_favicon_ico(images, filepath):
    """Save multiple PNG images as ICO file."""
    with open(filepath, 'wb') as f:
        # ICO header
        f.write(struct.pack('HHH', 0, 1, len(images)))  # Reserved, Type, Count
        
        # Image directory
        image_data = []
        offset = 6 + 16 * len(images)
        
        for img in images:
            # Convert to RGBA then to BGRA for ICO
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Create PNG data
            import io
            png_io = io.BytesIO()
            img.save(png_io, 'PNG')
            png_data = png_io.getvalue()
            
            width = img.width
            height = img.height
            
            # ICO directory entry
            f.write(struct.pack('BBBB', width if width < 256 else 0, 
                               height if height < 256 else 0, 
                               0, 0))  # width, height, palette, reserved
            f.write(struct.pack('H', 1))  # color planes
            f.write(struct.pack('H', 32))  # bits per pixel
            f.write(struct.pack('I', len(png_data)))  # size of image data
            f.write(struct.pack('I', offset))  # offset
            
            image_data.append(png_data)
            offset += len(png_data)
        
        # Write image data
        for data in image_data:
            f.write(data)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_img = os.path.join(base_dir, 'assets', 'img')
    
    # Generate PNGs in different sizes
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    for size in sizes:
        print(f"Generating {size}x{size} favicon...")
        img = create_favicon_png(size)
        png_path = os.path.join(assets_img, f'favicon-{size}x{size}.png')
        img.save(png_path, 'PNG')
        images.append(img)
    
    # Generate favicon.ico with multiple sizes
    ico_path = os.path.join(assets_img, 'favicon.ico')
    print(f"Generating favicon.ico...")
    save_favicon_ico(images[:4], ico_path)  # ICO works best with smaller sizes
    
    # Generate apple-touch-icon.png (180x180)
    apple_icon = create_favicon_png(180)
    apple_path = os.path.join(assets_img, 'apple-touch-icon.png')
    print(f"Generating apple-touch-icon.png...")
    apple_icon.save(apple_path, 'PNG')
    
    # Generate favicon.png (32x32)
    favicon_png = create_favicon_png(32)
    favicon_png_path = os.path.join(assets_img, 'favicon.png')
    print(f"Generating favicon.png...")
    favicon_png.save(favicon_png_path, 'PNG')
    
    print("Favicon generation complete!")

if __name__ == '__main__':
    main()
