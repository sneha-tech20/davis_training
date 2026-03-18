# function to find simple interest

def findSI(p,r,t):
    si=(p*r*t)/100 # calculate si
    return si

p=int(input("Enter the principal amount: ")) #principal
r=int(input("Enter the rate (in %): "))  #rate in percentage
t=int(input("Enter the time interval: ")) #time interval

#to display
print(findSI(p,r,t))  # function call