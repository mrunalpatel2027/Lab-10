"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import image_lib
import ctypes
import inspect

# Get the script and images directory
script_name = inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
  os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry("600x600")
root.minsize(500,600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TODO: Set the icon
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap(os.path.join(script_dir, 'poke_ball.ico'))


# TODO: Create frames
frm = ttk.Frame(root)
frm.root.columnconfigure(0, weight=1)
frm.root.rowconfigure(0, weight=1)
frm.grid(stic=NSEW)

#create the button to set desktop bg
def handle_set_desktop():
    """
    Event handler called when user clecks the "Set as Desktop Image" Button.
    Sets the desktop bg image to the current Poekman dispplay image

    """
    image_lib.set_desktop_background_image(image_path)

btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command=handle_set_desktop)
btn_set_desktop.state('disabled')
btn_set_desktop.grid(row=1,column=0,padx=0,pady=(10,20))

#create list of pull down pokemon names
pokemon_list = poke_api.get_pokemon_names()
pokemon_list.sort()
cbox_poke_sel = ttk.Combobox(frm, value=pokemon_list, state = 'readonly')
cbox_poke_sel.set("Select a pokemon")

def handle_poke_sel(event):
   global image_path

   current_sel = cbox_poke_sel.get()
   image_path = poke_api.download_pokemon_artwork(current_sel, images_dir)
   if image_path:
      
      lbl_image['text'] = None
      photo['file'] = image_path

# TODO: Populate frames with widgets and define event handler functions


root.mainloop()