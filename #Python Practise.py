#Python Practise
print("Welcome to Shrek's cafe!")
name = input("May I know your name?\n:")
continue_program= True
if name == "Mayank":
    print("You are not allowed in our cafe! Get Out!!")
    continue_program = False


if continue_program == True:
 
 order = input("Okay, "+ name +". What would you like to order?\n1.Coffee\n2.Tea\n3.Caffe Americano\n4.Cappccino")

 if order == "1" or order == "Coffee":
    quant = int(input("Great way to start your day!\nHow many coffee would you like to have?"))  
    bill = quant*3
    print("Your total bill would be $"+ str(bill))
 elif  order == "2" or order == "Tea":
    quant = int(input("Great way to start your day!\nHow many Tea would you like to have?"))
    bill = quant*3
    print("Your total bill would be: $"+ str(bill))
 elif order == "3" or order == "Caffe Americano":
    quant = int(input("Great way to start your day!\nHow many Caffe Americanos would you like to have?"))
    bill = quant*5
    print("Your total bill would be: $"+ str(bill)  )