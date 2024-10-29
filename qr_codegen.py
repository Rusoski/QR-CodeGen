import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import qrcode as qrc

# To build the ejecutable (Windows), run these 2 commands: (reuires to have pyinstaller to be installed)
#
# cd "<path to this file>"
# pyinstaller --onefile --noconsole qr_codegen.py

# Generate and store QR code
def genqrcode(text:str, filename:str):
    img = qrc.make(text)
    type(img)
    img.save(filename)

# Load QR code image
def load_and_resize_image(panel, filename:str):
    path = filename
    img = Image.open(path)
    resized_image = img.resize((380, 380), Image.Resampling.LANCZOS)
    new_image = ImageTk.PhotoImage(resized_image)
    panel.configure(image = new_image)
    panel.image = new_image

# Generate and load the QR code
def domagic(panel, text:str, filename:str):
    genqrcode(text, filename)
    load_and_resize_image(panel, filename)

# Create an instance of tkinter frame
root = tk.Tk()

# Set title for the tkinter frame
root.title('QR Code Generator')

# Set the geometry of tkinter frame
root.geometry("400x600")

# Limit size of tkinter frame
root.minsize(400, 600)
root.maxsize(400, 600)

# Create a text with a scroll
text_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 52, height = 10, font = ('calibre', 10 ,'normal'))

# Pack the text with a scroll
text_area.pack(pady = 10, side = tk.TOP)

# Create a button
button = tk.Button(root, text = 'Generate QR Code', command = lambda: domagic(panel, text_area.get("1.0",'end-1c'), 'qr_code.png'))

# Pack the button
button.pack(side = tk.TOP)

# Generate blank image
img = ImageTk.PhotoImage(Image.new('RGB', (512, 512), 'white'))

# Create a panel
panel = tk.Label(root, width = 380, height = 380, image = img)

# Keep the image reference
panel.image = img

# Pack the panel
panel.pack(pady = 10, side = tk.BOTTOM)

# Run the loop
root.mainloop()