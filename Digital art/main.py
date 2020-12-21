import pywhatkit

# variables
image = input("Enter the name of Image file (with extension): ")
text = input("Enter the name for Art file (recommended in txt extension): ")

# main code
pywhatkit.image_to_ascii_art(image,text)