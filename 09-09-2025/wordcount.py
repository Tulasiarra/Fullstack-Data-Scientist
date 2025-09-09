with open("file.txt","w")as f:
    f.write("HELLO CVR")
def wordcount(file):
    f=open(file,"r")
    txt=f.read()
    f.close()
    return len(txt.split())
print(wordcount("file.txt"))
  