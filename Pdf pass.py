# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:55:27 2020

@author: Shivam
"""
import PyPDF2 as p
import os
import pandas as pd
df=pd.read_csv(r"C:\Users\Shivam\Desktop\Python Codes\pass.csv")
folder_path = r"C:\Users\Shivam\Desktop\New folder (3)"



for i in os.walk(folder_path):
    for j in i[2]:
        if i.endswith(".pdf"):
            y=j
            
    #print(x)
            output=p.PdfFileWriter()
            input_stream=p.PdfFileReader(open(x,"rb"))
            for k in range(0,input_stream.getNumPages()):
                output.addPage(input_stream.getPage(k))
    
    
    if os.path.isfile(y):
        os.remove(y)
    outputstream=open(y,"wb")
    
    output.encrypt(j["Pass"],use_128bit=True)
    
    output.write(outputstream)
    outputstream.close()

# Specify the output jpg/png folder path


