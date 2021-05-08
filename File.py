f=open("Country.txt","a")
f.write("New Content\n")
f.close()

f=open("Country.txt","r")
print(f.read())
f.close()

