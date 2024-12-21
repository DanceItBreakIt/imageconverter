import PySimpleGUI as sg
from PIL import Image
import os

sg.set_options(font=('Comic Sans MS', 20))
sg.theme('Dark Green 6')

# display ↓↓↓
layout = [  [sg.Push(), sg.Text(f"Convert Images To Different File Formats", pad=(0,10), font=('Comic Sans MS',18), colors=('white on darkred')), sg.Push()],
            [sg.FileBrowse(pad=((50,5),5), key=('-INPUT 1-')), sg.Text(f"Select file: ", pad=((30,5),5), font=('Comic Sans MS',8))],
            [sg.Push(), sg.Text("Accepted file formats: JPEG, PNG, BMP, DDS, EPS, GIF, ICNS,\nICO, PCX, PPM, SGI, TGA, TIFF, and WebP", font=('Comic Sans MS',10)), sg.Push()],
            [sg.Push(), sg.Combo(['.jpeg', '.png', '.bmp', '.dds', '.eps', '.gif', '.icns', '.ico', '.pcx', '.ppm', '.sgi', '.tga', '.tiff', '.webp'], default_value='.jpeg', pad=(0,10), key=('filex')), sg.Button('  Convert  ', pad=((50,0),10)), sg.Push()]]

            # online it said PIL could support JPEG, PNG, BMP, BLP, DDS, EPS, GIF, ICNS, ICO, MSP, PCX, PNG, PPM, SGI, TGA, TIFF, WebP, and XBM, but it actually wont do all of them

window = sg.Window('Image Converter', layout, titlebar_icon="icon.ico") # sets up window

while True: # runtime
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '  Convert  ': # when convert button pressed
        img = Image.open(values['-INPUT 1-'])
        imgpath = os.path.dirname(values['-INPUT 1-'])
        if os.path.exists(f"{imgpath}\\convertedimage{values['filex']}"): # checks if file exists
            i = 1
            while os.path.exists(f"{imgpath}\\convertedimage{i}{values['filex']}"): # adds up variable to eventually create image
                i += 1
            img = img.save(f"{imgpath}\\convertedimage{i}{values['filex']}")
        else:
            img = img.save(f"{imgpath}\\convertedimage{values['filex']}")
        sg.popup("Image saved successfully\n", font=('Comic Sans MS', 15), title=('Image Saved Successfully')) # popup

window.close() # ends program