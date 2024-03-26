from PIL import Image, ImageDraw, ImageFont

def create_slide_image(title, bullet_points, image_width=720, image_height=405):
    # Create a blank image
    image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(image)

    # Set font properties
    title_font = ImageFont.load_default()
    bullet_font = ImageFont.load_default()

    # Draw title
    title_width, title_height = draw.textsize(title, font=title_font)
    draw.text(((image_width - title_width) / 2, 20), title, font=title_font, fill="black")

    # Calculate available width for bullet points
    available_width = image_width - 120  # Subtracting left margin of 100 and right margin of 20
    # Draw bullet points
    y = 80
    bullet_point_image = create_bullet_point_image(size=10, color="black")
    bullet_point_width, bullet_point_height = bullet_point_image.size
    for bullet_point in bullet_points:
        # Calculate text wrap width based on available width
        text_wrap_width = available_width - bullet_point_width - 20  # Subtracting bullet point width and some padding
        lines = wrap_text(draw, bullet_point, bullet_font, text_wrap_width)
        # Draw bullet point image
        image.paste(bullet_point_image, (100, y + bullet_point_height // 2), mask=bullet_point_image)
        # Draw wrapped text
        draw.text((120 + bullet_point_width, y), "\n".join(lines), font=bullet_font, fill="black")
        # Update y coordinate for next bullet point
        y += (len(lines) * bullet_point_height) + 20  # Adding extra space between bullet points

    # Add border
    border_color = "black"
    border_width = 5
    draw.rectangle([(border_width, border_width), (image_width - border_width, image_height - border_width)], outline=border_color, width=border_width)

    return image

def create_bullet_point_image(size=20, color="black"):
    # Create a blank image for bullet point
    bullet_image = Image.new("RGBA", (size, size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(bullet_image)

    # Draw bullet point
    draw.ellipse([(0, 0), (size-1, size-1)], fill=color)

    return bullet_image

def wrap_text(draw, text, font, max_width):
    lines = []
    words = text.split()
    while words:
        line = ""
        while words and draw.textsize(line + words[0], font=font)[0] <= max_width:
            line += (words.pop(0) + " ")
        lines.append(line)
    return lines

def save_image(image, filename):
    image.save(filename)

# Example usage
title = "Sample Slide"
bullet_points = ["This is a sample bullet point that stretches to a line instead of being limited to three words.",
                 "Another sample bullet point that demonstrates the text wrapping feature.",
                 "You can add as many bullet points as you need and they will automatically wrap to fit the available width."]

# Create and save the image
slide_image = create_slide_image(title, bullet_points)
slide_image.show()  # Display the image
