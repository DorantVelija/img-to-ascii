# ASCII Art Generator

This Python application converts images to ASCII art and saves the output in a text file.

## Features

- Open and display images.
- Resize images to predefined or custom resolutions.
- Convert images to grayscale.
- Save ASCII art to a `.txt` file.
- Automatically open the generated ASCII art file.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

## Installation

1. Install OpenCV:
   ```bash
   pip install opencv-python

## Usage

1.	Place your images in the images folder.
2.  Run the script:
    ```bash
    python ascii_art_generator.py
    
Script Functions

    open_file(file_path): Opens a file using the default application on the current operating system.
	printDir(): Lists files in the images folder.
    get_resolution(): Prompts the user to select or input a resolution for resizing the image.
	color(i, j): Maps a grayscale value to an ASCII character.
