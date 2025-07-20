def read():
     dictiona={}
     with open("input.txt","r") as file:
          for line in file:
               line=line.strip().split(",")
               kitta=int(line[0].strip())
               dictiona[kitta]=line[0:]
     file.close()
     return dictiona
