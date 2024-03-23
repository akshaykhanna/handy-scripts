from PIL import Image, ImageDraw

def create_bullet_point_image(size=20, color="black"):
    # Create a blank image for bullet point
    bullet_image = Image.new("RGBA", (size, size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(bullet_image)

    # Draw bullet point
    draw.ellipse([(0, 0), (size-1, size-1)], fill=color)

    return bullet_image

# Example usage
bullet_point_image = create_bullet_point_image(size=20, color="black")
bullet_point_image.save("bullet_point.png")
