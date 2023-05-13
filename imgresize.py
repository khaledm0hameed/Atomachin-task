from PIL import Image
import os

def resize_image(image_path, new_size):
    image = Image.open(image_path)
    resized_image = image.resize(new_size)

    # Get the path and filename of the original image
    path, filename = os.path.split(image_path)

    # Split the filename and extension
    name, extension = os.path.splitext(filename)

    # Create a new filename with the resized dimensions
    resized_filename = f"{name}_{new_size[0]}x{new_size[1]}{extension}"

    # Save the resized image in the same folder
    resized_image.save(os.path.join(path, resized_filename))
    print(f"Image resized and saved as: {resized_filename}")


