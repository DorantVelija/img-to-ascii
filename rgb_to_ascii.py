import cv2 as cv

def color(i, j):
    (B, G, R) = image[i, j]

    # White and Black
    if B < 50 and G < 50 and R < 50:
        return ">>>>>>>>>"
    if B > 230 and G > 230 and R > 230 and B > 230:
        return "<</<</<</"

    # Dominant Blue
    if B > G and B > R:
        # Under Half
        if G < 255/2:
            return "¥¥¥¥¥¥"
        if G < 255 / 3:
            return ";;;;;;"
        if G < ((255/3)*2):
            return "nnnnnn"
        if G < 255 / 4:
            return "''''''"

        # Under Half
        if R < 255/2:
            return "??????"
        if R < 255/3:
            return "llllll"
        if R < ((255 / 3) * 2):
            return "gggggg"
        if R < 255/4:
            return "jjjjjj"

        return "######"

    # Dominant Red
    if R > G and R > B:
        # Over Half
        if G > 255/2:
            return "oooooo"
        if G > 170:
            return "bbbbbb"
        if G > 220:
            return "fdsgfs"

        # Under Half
        if G < 255/2:
            return "//////"
        if G < 255/3:
            return "ssssss"
        if G < ((255 / 3) * 2):
            return "wwwwww"
        if G < 255/4:
            return "dddddd"

        # Over Half
        if B > 255 / 2:
            return "tyuacv"
        if B > 170:
            return "ghyulk"
        if B > 220:
            return "poulkm"

        # Under Half
        if B < 255/2:
            return "{{{{{{"
        if B < 255/3:
            return "||||||"
        if B < ((255 / 3) * 2):
            return "cccccc"
        if B < 255/4:
            return "::::::"

        return "!!!!!!"

    # Dominant Green
    if G > R and G > B:
        # Over Half
        if B > 255 / 2:
            return "yupsl;"
        elif B > 170:
            return "quisol"
        elif B > 220:
            return "qtysio"

        # Under Half
        if B < 255/2:
            return "xxxxxx"
        if B < 255/3:
            return "rrrrrr"
        if B < ((255 / 3) * 2):
            return "zzzzzz"
        if B < 255/4:
            return "vvvvvv"

        # Over Half
        if R > 255 / 2:
            return "oooooo"
        if R > 170:
            return "bbbbbb"
        if R > 220:
            return "fdsgfs"
        # Under Half
        if R < 255/2:
            return "++++++"
        if R < 255/3:
            return "aaaaaa"
        if R < ((255 / 3) * 2):
            return "oooooo"
        if R < 255/4:
            return "qqqqqq"
        return "@@@@@@"
    return "......"


path = "images/olli.jpg"

# Open the file
dot_position = path.rfind('.')
filename = path[:dot_position]
file = open(f'{filename}.txt', 'w')


# Open the image
image1 = cv.imread(path)

# For resizing
h, w = image1.shape[:2]
print("//////////////////////////////")
print(f"Original \nHeight: {h}px Width: {w}px")
new_width = 220
new_height = 760

# Resize the image
image = cv.resize(image1, (new_width, new_height))

# Extracting the height and width of an image
h, w = image.shape[:2]

# Writing to the document
for i in range(h):
    for j in range(w):
        file.write(color(i, j))
    file.write('\n')

# Displaying the height and width
print("//////////////////////////////")
print(f"New \nHeight: {h}px Width: {w}px")
print("//////////////////////////////")

file.close()