import cv2
import os
import subprocess
import platform


def open_file(file_path):
    current_os = platform.system()
    if current_os == 'Windows':
        os.startfile(file_path)
    elif current_os == 'Darwin':  # macOS
        subprocess.run(['open', file_path])
    elif current_os == 'Linux':
        subprocess.run(['xdg-open', file_path])
    else:
        raise OSError('Unsupported operating system')


def printDir():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the folder name within the script directory
    folder_name = 'images'

    # Create the full path to the target folder
    folder_path = os.path.join(script_dir, folder_name)

    # List all files and directories in the specified folder
    files = os.listdir(folder_path)

    # Print the list of files and directories
    for file in files:
        print(file)

def get_resolution():
    print("\033[92m1. 44x44\n2. 90x90\n3. 120x120\n4. 240x240 \n5. 500x500\n6. Other")
    resolution = int(input(f"\033[36mPick a resolution: "))
    if resolution == 1:
        return 44, 44
    elif resolution == 2:
        return 90, 90
    elif resolution == 3:
        return 120, 120
    elif resolution == 4:
        return 240, 240
    elif resolution == 5:
        return 500, 500
    elif resolution == 6:
        height = int(input("Height: "))
        width = int(input("Width: "))
        return height, width
    else:
        print("Invalid option, defaulting to 44x44")
        return 44, 44


def color(i,j):
    # Get the value from 0-255 and return a corresponding value
    gray_value = gray_img[i, j]
    if 0 < gray_value <= 60:
        return "@"
    elif 60 < gray_value <= 100:
        return "!"
    elif 100 < gray_value <= 140:
        return "+"
    elif 140 < gray_value <= 160:
        return "%"
    elif 160 < gray_value <= 190:
        return "*"
    elif 190 < gray_value <= 220:
        return "^"
    elif 220 < gray_value <= 255:
        return "."
    return ";"


# Path to the image, the .txt file will be generated in the same directory as the original image
print(f"\033[92m")
printDir()
imgName = input(f"\033[93mSelect image (name.extension): ")
path = "images/" + imgName

# Open the image
h, w = get_resolution()
img = cv2.imread(path)

# Resize the image
img = cv2.resize(img, (w, h))

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Uncomment to open the resized image with grayscale applied
cv2.imshow("Press any key to continue",gray_img)
cv2.waitKey(0)

# Open the output file
dot_position = path.rfind('.')
filename = path[:dot_position]
file = open(f'{filename}.txt', 'w')

# Print the output
for i in range(h):
    for j in range(w):
        # Check what colour that specific pixel is
        file.write(color(i, j))
    file.write('\n')
file.close()
print(f"\033[96m////////////////////////////////////////////////////////////")
print(f"\033[95mGenerated output at \033[93m{filename}.txt")
print(f"\033[96m////////////////////////////////////////////////////////////")
open_file(f"{filename}.txt")