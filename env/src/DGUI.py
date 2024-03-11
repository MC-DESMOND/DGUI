from tkinter import *

"""

                                         
 ___  ___  _ __ ___   ___    ___ ___ ___ 
/ __|/ _ \| '_ ` _ \ / _ \  / __/ __/ __|
\__ \ (_) | | | | | |  __/ | (__\__ \__ \
|___/\___/|_| |_| |_|\___|  \___|___/___/
                                         
       _   _        _ _           _            
  __ _| |_| |_ _ __(_) |__  _   _| |_ ___  ___ 
 / _` | __| __| '__| | '_ \| | | | __/ _ \/ __|
| (_| | |_| |_| |  | | |_) | |_| | ||  __/\__ \    
 \__,_|\__|\__|_|  |_|_.__/ \__,_|\__\___||___/   

 ___ _   _       ______   _______ _   _  ___  _   _ 
|_ _| \ | |     |  _ \ \ / /_   _| | | |/ _ \| \ | |
 | ||  \| |     | |_) \ V /  | | | |_| | | | |  \| |
 | || |\  |     |  __/ | |   | | |  _  | |_| | |\  |
|___|_| \_|     |_|    |_|   |_| |_| |_|\___/|_| \_|
                                                    


 ____  _____ ____  ____  ____   ___ ___ ____    ___            
|  _ \| ____/ ___||  _ \|  _ \ / _ \_ _|  _ \  |_ _|_ __   ___ 
| | | |  _| \___ \| | | | |_) | | | | || | | |  | || '_ \ / __|
| |_| | |___ ___) | |_| |  _ <| |_| | || |_| |  | || | | | (__ 
|____/|_____|____/|____/|_| \_\\___/___|____/  |___|_| |_|\___|
                                                               



"""


class Gui(Tk):
    def __init__(self,master=None,width=None ,height = None):
        if master:
            root = master
        else:
            root =  super()
        self.body = Canvas(root)
        if width and height:
            self.body.config(width = width,height=height)
            self.width = width 
            self.height =  height
            self.linear_list = []
            self.bg:str

    def set_bg(self, color = '#00aaaa'):
        ''' color in hashes e.g #00aaaa'''
        self.body.config(bg = color)
        self.bg = color
    
    def linear_gradient(self,x,y,width:int,color):
        """ x,y middle point of gradient
        color in `hashes` e.g #00ff00"""
        color_letters = [i for i in color]
        color_letters.remove('#')
