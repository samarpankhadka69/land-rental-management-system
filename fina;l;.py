# Importing Libraries
from datetime import datetime,timedelta
import sys
def lining():
     print("*******************************************************************************************************************************************************")
def read():
     dictiona={}
     with open("input.txt","r") as file:
          for line in file:
               line=line.strip().split(",")
               kitta=int(line[0].strip())
               dictiona[kitta]=line[0:]
     file.close()
     return dictiona
# Function to write in a file
def  write(dic):
     with open('input.txt' ,'w' ) as file:
          for value in dic.values():
               file.write(str(str(value[0])+','+str(value[1])+','+str(value[2])+','+str(value[3])+' ,' +str(value[4])+',' +str(value[-1])))
               file.write("\n")
          file.close()

def calculate_fine(expected_return_date,return_date,cost,duration):
     price = duration * cost
     if return_date > expected_return_date:
        delayed_days = (return_date - expected_return_date).days
        fine = 0.10 * (delayed_days * cost)
        total_cost = price + fine
        return total_cost

     else:
          return price

def invoice(name,phone,rented_date,expected_return_date,return_date,cost,duration):
     total_cost=calculate_fine(expected_return_date,return_date,cost,duration)
     bill =f"Returned by : {name} \n"
     bill +=f"Contact number: {phone} \n"
     bill += f"Rent Date: {rented_date.strftime('%Y-%m-%d')}\n"
     bill += f"Return Date: {return_date.strftime('%Y-%m-%d')}\n"
     bill += f"Duration of Rent: {duration} months\n"
     bill += f"Cost per Month: Rs. {cost}\n"
     bill += f"Total Rental Cost: Rs. {total_cost}\n"
     return bill

def display_invoice():
     print("Invoice Detail")
     with open('invoice.txt','r') as file:
          for line in file:
               print(line.strip())
def rent_bill(name,phone,kitta,duration,cost):
    dictiona=read()
    total_cost=duration*cost
    with open('input.txt','r') as file:
        for line in file:
            if str(kitta) in line:
                with open('rent.txt','w') as data:
                    for value in dictiona.values():
                         if str(kitta)==value[0]:
                              data.write("---------------------------------Invoice (Rent Bill)--------------------------------------\n\n")
                              data.write(f'Customer name: {name} \n')
                              data.write(f'Contact Details: {phone} \n')
                              data.write("------------------------------------------------------------------------------------------\n\n")
                              data.write(f"Kitta Number: {value[0]} \n")
                              data.write(f"City: {value[1]} \n")
                              data.write(f"Direction: {value[2]} \n")
                              data.write(f"Rented Duration: {duration} \n")
                              data.write(f"Land Price: {value[4]} \n")
                              data.write("------------------------------------------------------------------------------------------\n")
                              data.write(f"Total Cost: {total_cost} \n")
                              data.write("------------------------------------------------------------------------------------------")

def display_rent_bill():
     with open('rent.txt','r') as file:
          for line in file:
               print(line.strip())

def rent():
     print(" Rent")
     try: 
          dictiona=read()
          
          name=input("Enter the name of the customer: ")
          phone=input("Enter the contact number: ")
          print("Kitta\t\t City\t\t\t Direction \t Anna \t\t Cost (Rs) \t  Status")
          file=open("input.txt","r")
          for line in file:
               data=line.replace(",","\t\t")
               print(data)
          kitta=int(input(("Enter the kitta number to rent:")))
          if kitta in dictiona:
               # If status of kitta  number is available then you can take the rent
               if(dictiona[kitta][5]=="Available"):
                    dictiona[kitta][5]="Not Available"
                    times=int(input(" Enter the duration of time in month(): "))                       
                    write(dictiona)
                    print(" The land is available for rent\n")
                    rent_bill(name,phone,kitta,times,int(dictiona[kitta][4]))
                    display_rent_bill()
               else:
                    print(" The land is not available")

          else:
               print("Please Enter the valid Kitta number")
     except Exception as e:
          print(f"An error occurred: {str(e)}")



     



def return_rent(): 
     try:
          name = input("Enter the name of the customer: ")
          phone = input("Enter the contact number: ")
          kitta = int(input("Enter the kitta number to return: "))

          
          dictiona = read()
          if kitta in dictiona:

               times = int(input("Enter the duration of time in months: "))
               return_date = int(input("Enter the time you rented for (in months): "))
               if dictiona[kitta][5] == 'Not Available':
                    dictiona[kitta][5] = "Available"
                    print("Land returned successfully")
                    print("Kitta Number\tCity\tDirection\tAnna\tCost (Rs)\tAvailability")
                    for values in dictiona.values():
                         print(f"{values[0]}\t{values[1]}\t{values[2]}\t{values[3]}\t{values[4]}\t{values[5]}")
                    # Taking today's date
                    rented_date = datetime.now()
                    expected_return_date = rented_date.replace(month=rented_date.month + times)
                    return_date = rented_date.replace(month=rented_date.month + return_date)
                    bill = invoice(name, phone, rented_date, expected_return_date, return_date, int(dictiona[kitta][4]), times)
                    with open("invoice.txt",'w') as file:
                         file.write("-------------------------------------------Total Bill--------------------------------------------------------------\n")
                         file.write(bill+'\n')
                    print(bill)
                    write(dictiona)
               else:
                    print("The land is not available")
          else:
               print("Please enter a valid Kitta number!")
     except ValueError:
          print("Enter the valid input")


  
          
def main():
     lining()
     print("\n")
     print("\t\t\t\t\t\t\t\tWelcome to Techno Property Nepal \n")
     print("\t\t\t\t\t\t\t We are located at Kamalpokhari , Kathmandu    |      Contact us: 9852678924\n\n\n")
     lining()
     print(" \t\t\t\tSearching For A Property? \n\n\t\t\t\t\t Find it on Techno Property Nepal...")
     lining()
     print("\t\tClick  here  to find the suitable options")
     while(True):
          lining()
          print("Press 1 to rend land")
          print("Press 2  to return land")
          print("Press 3 to exit the interface")
          lining()
          choice=int(input("Enter your choice: "))
          if choice==1:
               rent()
          elif choice==2:
               return_rent()
          elif choice==3:
               print("Thank You for using our services!!!!!")
               exit()
          else:
               print("Enter the valid option from (1,2 and 3)")
          lining()
          continue_using=input("Do you want to continue using this platform for rent and returning the land?(y/n):")
          if(continue_using.lower()=='n'):
               print("Thanks for using our service!!!")
               break

if __name__=='__main__':
     main()
     
                
     
