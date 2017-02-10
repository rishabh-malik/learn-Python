#for reading and appending the file
file1=open("text.txt","a+")
file1.read()
file1.write(". haha!")
file1.close()

#for copying the file
file= open("text.txt","r")
f2=open("text2.txt","w")
f2.write(file.read())
f2.close()
file.close()