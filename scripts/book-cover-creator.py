from PIL import Image, ImageDraw, ImageFont

def create_book_cover(title, subtitle, image_path, author_img_path, output_path="book_cover.png"):
    # Define sizes and positions
    cover_width, cover_height = 800, 1200
    title_font_size = 60
    subtitle_font_size = 40
    margin = 50
    font_color = "white"
    bg_color = "black"

    # Create a new image with black background
    cover = Image.new('RGB', (cover_width, cover_height), bg_color)
    draw = ImageDraw.Draw(cover)

    # Load fonts (Make sure the fonts are available in your system)
    title_font = ImageFont.truetype("arial.ttf", title_font_size)
    subtitle_font = ImageFont.truetype("arial.ttf", subtitle_font_size)

    # Draw the title at the top, centered horizontally
    title_width, title_height = draw.textsize(title, font=title_font)
    draw.text(((cover_width - title_width) / 2, margin), title, fill=font_color, font=title_font)

    # Load and resize the center image
    center_image = Image.open(image_path)
    center_image = center_image.resize((600, 600))  # Adjust the size as needed
    center_image_position = ((cover_width - center_image.width) // 2, (cover_height - center_image.height) // 2)
    cover.paste(center_image, center_image_position)

    # Draw the subtitle below the center image
    subtitle_width, subtitle_height = draw.textsize(subtitle, font=subtitle_font)
    draw.text(((cover_width - subtitle_width) / 2, center_image_position[1] + center_image.height + margin // 2), 
              subtitle, fill=font_color, font=subtitle_font)

    # Load and resize the author logo
    author_logo = Image.open(author_img_path)
    author_logo = author_logo.resize((100, 100))  # Adjust the size as needed
    author_logo_position = ((cover_width - author_logo.width) // 2, cover_height - 200)
    cover.paste(author_logo, author_logo_position, author_logo)  # Use the third parameter for transparency if needed

    # Save the cover image
    cover.save(output_path)
    cover.show()

# Example usage:
create_book_cover(
    title="Your Book Title",
    subtitle="Your Subtitle",
    image_path="assets/llama.jpg",
    author_img_path="assets/logo.jpg,
    output_path="output_book_cover.png"
)