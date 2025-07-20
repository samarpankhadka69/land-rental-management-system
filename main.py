import operation
def lining():
     print("*******************************************************************************************************************************************************************************************************************************************************************************************************")
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
          print("Press 1 to rent land")
          print("Press 2  to return land")
          print("Press 3 to exit the interface")
          lining()
          try:
               choice=int(input("Enter your choice: "))
               if choice==1:
                    operation.rent()
               elif choice==2:
                    operation.return_rent()
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
          except:
               print("Values cant be set empty")
               main()

if __name__=='__main__':
     main()
     
