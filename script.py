# Python v3.11.4

import os
from PIL import Image

def convert_cr2_to_png(input_path: any, output_path: any) -> any:
    try:
        # Open the .CR2 file
        image = Image.open(input_path)

        # Convert to RGB mode (CR2 typically contains RAW data)
        image_rgb = image.convert('RGB')

        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        # Extract the filename from the input path
        filename = os.path.splitext(os.path.basename(input_path))[0]

        # Save the image as .PNG format in the output directory
        output_file = os.path.join(output_path, f"{filename}.png")
        image_rgb.save(output_file, format='PNG')

        print(f"Conversion successful. Image saved as {output_file}")
    except Exception as e:
        print(f"Error converting the file: {e}")

if __name__ == "__main__":

    try:
        #input_directory = "path/to/your/input_directory"
        input_directory
    except NameError:
        #var_exists = False
        input_directory = input("Enter the input directory:")

    print("Input Folder is: " + input_directory)

    try:
        #output_directory = "path/to/your/output_directory"
        output_directory
    except NameError:
        #var_exists = False
        output_directory = input("Enter the output directory:")

    print("Output Folder is: " + output_directory)

    # Get a list of all files in the input directory
    input_files = [
                os.path.join(root, name)
                for root, dirs, files in os.walk(input_directory)
                    for name in files
                        if name.lower().endswith((".cr2"))
                ]

    for input_file in input_files:
        input_file_path = os.path.join(input_directory, input_file)
        convert_cr2_to_png(input_file_path, output_directory)
