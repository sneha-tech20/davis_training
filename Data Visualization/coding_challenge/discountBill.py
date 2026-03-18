current_bill=int(input("Enter the amount of your bill : ")) 
discount=int(input("Enter discount in percentage : "))  #discount in %


#LOGIC
disc_amount=(discount/100)*current_bill  

paid_bill=current_bill-disc_amount
print(paid_bill)  