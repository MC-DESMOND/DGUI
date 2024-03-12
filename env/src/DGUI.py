from tkinter import *
import math
"""

                                         
 ___  ___  _ __ ___   ___    ___ ___ ___ 
/ __|/ _ \| '_ ` _ \ / _ \  / __/ __/ __|
\__ \ (_) | | | | | |  __/ | (__\__ \__ \.
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
    def __init__(self,master=None,width=300 ,height = 300):
        if master:
            self.root = master
        else:
            self.root =  super()
        self.body = Canvas(self.root)
        if width and height:
            self.body.config(width = width,height=height)
            self.width = width 
            self.height =  height
            self.linear_list = []
            self.bg:str
            self.colorAz = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            self.colorAz = [i.upper() for i in self.colorAz]
            self.pack = self.body.pack
            self.set_bg()

    def set_bg(self, color = '#ffacaa'):
        ''' color in hashes e.g #00aaaa'''
        self.body.config(bg = color)
        self.bg = color

    def linear_blured_color(self,x,angle,width:int,color):
        """ x,y middle point of gradient
        color in `hashes` e.g #00ff00"""
        width = width*2
        color_letters = [i.upper() for i in color]
        color_letters.remove('#')
        bg_letters = [i.upper() for i in self.bg]
        bg_letters.remove('#')
        epochs = 0
        cindex = 0
        bindex = 0
        each_color = []
        cindexlist = []
        bindexlist = []
        widthXcolorsIndex = []
        widthXcolors = []
        result =[]
        for i in range(0,len("000000")):
            cindex = self.colorAz.index(color_letters[i])
            bindex = self.colorAz.index(bg_letters[i])
            
            cindexlist.append(cindex)
            bindexlist.append(bindex)
        
        while cindexlist != bindexlist:
            cheak = 0
            for j in range(0,len("000000")):
                if cindexlist[j] > bindexlist[j]:
                    cindexlist[j] = cindexlist[j] -1
                    each_color.append([e for e in cindexlist])
                    each_color.append([e for e in cindexlist])
                elif cindexlist[j] < bindexlist[j]:
                    cindexlist[j] = cindexlist[j] +1
                    each_color.append([e for e in cindexlist])
                    each_color.append([e for e in cindexlist])
                if cindexlist[j] == bindexlist[j]:
                    cheak = cheak + 1
                    each_color.append([e for e in cindexlist])
                
            # each_color.append([e for e in cindexlist])
                
            if cheak == len("000000"):
                break
        insertIndex = 0
        k = 0
        ite=1
        while epochs < width:
            if k < len(each_color):
                widthXcolorsIndex.append(each_color[k])
                k = k+1
                epochs = k
            elif k == len(each_color):
                k = k+1
                widthXcolorsIndex.reverse()
            else:
                try:
                    insertIndex = insertIndex+ite
                    widthXcolorsIndex.insert(insertIndex+insertIndex,widthXcolorsIndex[insertIndex+insertIndex])
                    epochs = len(widthXcolorsIndex)
                except:
                    ite = 2
                    insertIndex = 0
        widthXcolorsIndex.reverse()    

        for i in widthXcolorsIndex:
            widthXcolors.append([self.colorAz[index] for index in i])

        for i in widthXcolors:
            colorResult = '#'
            for letter in i:
                colorResult += letter
            result.append(colorResult)

        for i in result:
            print(i)
        print(len(result))
        linelist = []
        colorList = []
        result.reverse()
        for Iter,i in enumerate(result):
            
            xer = (x-len(result))+Iter
            colorList.append(i)
            linelist.append(self.body.create_line(xer,0,xer,self.height,fill=i,width=1))
        result.reverse()
        for Iter,i in enumerate(result):
            xer = x+Iter
            colorList.append(i)
            linelist.append(self.body.create_line(xer,0,xer,self.height,fill=i,width=1))
            # self.root.update()
        self.root.update()


            


def test():
    root = Tk()
    gui = Gui(root,width=500,height=int(root.winfo_screenheight()))
    gui.pack(fill=BOTH,expand=True)
    gui.set_bg(color='#000000')
    gui.linear_blured_color(250,0,100,'#00ff00')
    gui.linear_blured_color(500+150,0,100,'#ff0000')
    gui.linear_blured_color(500+550,0,100,'#0000ff')
    root.mainloop()



if __name__ == '__main__':
    test()