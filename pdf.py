import pandas as pd 
import PyPDF2 as p
import os
import glob

#path=r"C:\Users\Shivam\Desktop\New folder (3)"
df=pd.read_csv(r"C:\Users\Shivam\Desktop\New folder (3)/pass.csv")
for i,j in df.iterrows():
    x=j["filename"]
    y=j["filename"]
    output=p.PdfFileWriter()
    input_stream=p.PdfFileReader(open(x,"rb"))
    if input_stream.isEncrypted:
        input_stream.decrypt(j["Pass"])
    else:
        continue
    for k in range(0,input_stream.getNumPages()):
        output.addPage(input_stream.getPage(k))
    
    outputstream=open(y,"wb")
    
    output.encrypt(j["Pass"],use_128bit=True)
    
    output.write(outputstream)
    outputstream.close()
    \