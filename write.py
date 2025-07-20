# Function to write in a file
import read 
from datetime import date
def  write(dic):
     with open('input.txt' ,'w' ) as file:
          for value in dic.values():
               file.write(str(str(value[0])+','+str(value[1])+','+str(value[2])+','+str(value[3])+' ,' +str(value[4])+',' +str(value[-1])))
               file.write("\n")
          file.close()
def rent_bill(kitta,duration):
    dictiona=read.read()
    total_cost=duration*int(dictiona[kitta][4])
    with open('input.txt','r') as file:
        for line in file:
            if str(kitta) in line:
                with open('rent.txt','a') as data:
                    for value in dictiona.values():
                         if str(kitta)==value[0]:
                              data.write(f"{value[0]} \t\t")
                              data.write(f"{value[1]} \t\t")
                              data.write(f"{value[2]} \t\t")
                              data.write(f"{duration} \t\t")
                              data.write(f"{value[4]} \t\t")
                              data.write(f"{total_cost} \t\t")
