from datetime import datetime,timedelta
import write
import read
from write import rent_bill
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



def display_rent_bill():
     with open('rent.txt','r') as file:
          for line in file:
               print(line.strip())
def rent():
     print(" Rent")
     try: 
          dictiona=read.read()
          rented_kittas=[]
          duration=0
          name=input("Enter the name of the customer: ")
          phone=input("Enter the contact number: ")
          c='y'
          while(c=='y'):
               print("Kitta\t\t City\t\t Direction \t Anna \t\t Cost (Rs) \t  Status")
               file=open("input.txt","r")
               for line in file:
                    data=line.replace(",","\t\t")
                    print(data)
               kitta=int(input(("Enter the kitta number to rent:")))
               if kitta in dictiona:
                    # If status of kitta  number is available then you can take the rent
                    if(dictiona[kitta][5]=="Available"):
                         dictiona[kitta][5]="Not Available"
                         duration=int(input(" Enter the duration of time in month(): "))                       
                         write.write(dictiona)
                         print(" The land is available for rent\n")
                         rented_kittas.append(kitta)
                    else:
                         print(" The land is not available")
               else:
                    print("Please Enter the valid Kitta number")
               
               c=input("DO you want to continue?:")
               if(c.lower()=='n'):
                    break
          for kittas in rented_kittas:
               rent_bill(kittas, duration)
               display_rent_bill()
     except Exception as e:
          print(f"An error occurred: {str(e)}")


def return_rent(): 
     try:
          name = input("Enter the name of the customer: ")
          phone = input("Enter the contact number: ")
          kitta = int(input("Enter the kitta number to return: "))

          
          dictiona = read.read()
          if kitta in dictiona:

               times = int(input("Enter the duration of time in months: "))
               return_date = int(input("Enter the time you rented for (in months): "))
               if dictiona[kitta][5] == 'Not Available':
                    dictiona[kitta][5] = "Available"
                    print("Land returned successfully")
                    print("Kitta \tCity\t\tDirection\tAnna\tCost (Rs)\tAvailability")
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
                    write. write(dictiona)
               else:
                    print("The land is not available")
          else:
               print("Please enter a valid Kitta number!")
     except ValueError:
          print("Enter the valid input")
