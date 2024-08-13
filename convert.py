import os
import sys
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def convert_to_jpg(input_file, output_file):
    try:
        img = Image.open(input_file)
        img = img.convert("RGB")
        img.save(output_file, "JPEG", quality=95)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def main():
    # Set input and output directories
    desktop_directory = os.path.join(os.path.expanduser("~"),"Desktop")
    folder = input("Enter the name of your folder in Desktop: ")
    input_directory = os.path.join(desktop_directory, folder)
    output_directory = os.path.join(desktop_directory, "jpg")
    print(f"Input directory: {input_directory}")
    print(f"Output directory: {output_directory}")
    
    if not os.path.exists(input_directory):
        print(f"Input directory {input_directory} does not exist. Please create it and add .heic files.")
        return
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for root, _, files in os.walk(input_directory):
        for file in files:
            file_ext = os.path.splitext(file.lower())[1]
            if file_ext == '.heic':
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_directory, os.path.splitext(file)[0] + ".jpg")
                print(f"Converting {input_file} to {output_file}")
                convert_to_jpg(input_file, output_file)
            else:
                print(f"Skipping file {file}, not a .heic file.")

if __name__ == "__main__":
    main()
