import matplotlib.pyplot as plt
import tkinter
import tkinter.scrolledtext as tkst
import pydicom              # pydicom
import pydicom_Tkinter
import numpy
import PIL
from tkinter import *
import Image, ImageTk
import xml.etree.ElementTree as ET
from pydicom_PIL import show_PIL
from pydicom.data import get_testdata_files
import AnnPaint


def rightClickOnQuickComment (event):
    tree = ET.parse('C:/Users/veeti/Desktop/inno/xml/annotationOptions.xml')
    EtRoot = tree.getroot()
    print("Right")
    master = Tk()

    listbox = Listbox(master)

    listbox.pack()

    #listbox.insert(END, "a list entry")

    for child in EtRoot:
        listbox.insert(END, child.attrib['category'])
    listbox.bind('<<ListboxSelect>>', onselect)

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    quickAnnotations.insert('insert', value + '\n')
    print ('You selected item %d: "%s"' % (index, value))


def annotate(evt):
    master = Tk()
    master.attributes('-alpha', 0.3)
    w = Canvas(master, width=500, height=500)

    w.pack()

    last_x = 0
    last_y = 0
    first_x = 0
    first_y = 0
    def mark(event):
        nonlocal last_x
        nonlocal last_y
        nonlocal first_x
        nonlocal first_y
        if  last_x == 0:
            last_x=event.x
            last_y=event.y
            first_x = event.x
            first_y = event.y
            print("first click")
        else:
            w.create_line(last_x,last_y,event.x,event.y,fill="red",width=5)
            last_x = event.x
            last_y = event.y

    def closeMark(event):
        nonlocal last_x
        nonlocal last_y
        nonlocal first_x
        nonlocal first_y
        if  last_x == 0:
            print("Start marking with left button")
        else:
            w.create_line(last_x, last_y, first_x,first_y, fill="red", width=5)


    master.bind("<Button-1>", mark)
    master.bind("<Button-2>",closeMark)


filename = get_testdata_files('brain.dcm')[0]


df = pydicom.read_file(filename)



root = Tk()
root.geometry('1000x1000')
root.bind('<Control-a>', annotate)
frame = tkinter.Frame(root, bg='white')
imageFrame = tkinter.Frame(root, bg='white')


canvas = Canvas(imageFrame ,width=500,height=500)





pilImage = show_PIL(df)
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(image.height()/2,image.width()/2,image=image)



'textbox'
edit_space = tkst.ScrolledText(
    master = frame,
    wrap   = 'word',  # wrap text at full words only

    width  = 60,      # characters
    height = 10,      # text lines
    bg='beige'        # background color of edit area
)


'textbox'
quickAnnotations = tkst.ScrolledText(
    master = frame,
    wrap   = 'word',  # wrap text at full words only

    width  = 60,      # characters
    height = 10,      # text lines
    bg='beige'        # background color of edit area
)

quickAnnotations.bind("<Button-3>",rightClickOnQuickComment)

edit_space.insert('insert', "Free text")
quickAnnotations.insert('insert',"")

imageLabel = Label(imageFrame, text="image name")
freeTextLabel = Label(frame, text="free text")
quickAnnotationLabel=Label(frame, text="quickAnnotations")

imageFrame.grid(row=0)
canvas.grid(row=1,column=0)

imageLabel.grid(row=0,column=0)

quickAnnotationLabel.grid(row=1,column=1,padx=10, pady=10,sticky=W)
quickAnnotations.grid(row=2,column=1,sticky=E)
freeTextLabel.grid(row=3,column=1, rowspan=1,padx=10, pady=10,sticky=W)
edit_space.grid(row=4,column=1, rowspan=1,sticky=E)
frame.grid(column=1,row=0,sticky=E+N)

root.mainloop()