#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import tkinter

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import numpy
import keras
import dlib
import cv2
import os

import argparse
import time
from parameters import NETWORK, DATASET, VIDEO_PREDICTOR
from model import build_model
from predict import load_model, predict

top = Tk()
top.title('Facial Expression Recognition')
top.geometry('500x270')
canvas = Canvas(top, width=200,height=200, bd=0,bg='white')
canvas.grid(row=1, column=0)
model = load_model();
image = None
shape_predictor = None
image = None

def showImg():
    File = askopenfilename(title='Open Image') 
    e.set(File)
    print (e.get())    
    image = Image.open(e.get())
    w, h = image.size
    image = image.resize((200, 200))
    imgfile = ImageTk.PhotoImage(image)
    
    canvas.image = imgfile  # <--- keep reference of your image
    canvas.create_image(2,2,anchor='nw',image=imgfile)

e = StringVar()

submit_button = Button(top, text ='Open', command = showImg)
submit_button.grid(row=0, column=0)

def Predict():
    # global image
    path = e.get()
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    shape_predictor = dlib.shape_predictor(DATASET.shape_predictor_path)
    image = cv2.imread(path, 0)
    # img = cv2.resize(image, (NETWORK.input_size, NETWORK.input_size))
    image.resize([NETWORK.input_size, NETWORK.input_size], refcheck=False)
    start_time = time.time()
    emotions, confidences = predict(image, model, shape_predictor)
    total_time = time.time() - start_time
    text = ""
    for i in range(4):
        text += "{0} : {1:.1f}%".format(emotions[i], confidences[i]*100) + "\n\r"
    t1.delete(0.0, tkinter.END)
    t1.insert('insert', text+'\n')
    t1.update()
submit_button = Button(top, text ='Predict', command = Predict)
submit_button.grid(row=0, column=1)

l1=Label(top,text="Please <Open> an image, then <Predict>")
l1.grid(row=2)

t1=Text(top,bd=0, width=22,height=13,font='Fixdsys -14')
t1.grid(row=1, column=1)
top.mainloop()