from PIL import Image

def invert_colors(image_path, output_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Invert pixel colors
        inverted_img = Image.eval(img, lambda x: 255 - x)

        # Save the result
        inverted_img.save(output_path)

if __name__ == "__main__":
    input_image_path =  "share.png"  # Replace with the path to your input image
    output_image_path = "output_image.png"  # Replace with the desired output path

    invert_colors(input_image_path, output_image_path)
