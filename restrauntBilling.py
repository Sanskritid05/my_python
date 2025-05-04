#2
#restraunt billing

bill = float(input("Enter the amount : ")) 
print("\n")

if bill > 5000: 
    print("Amount : " , bill)
    bill = bill - 0.2*bill 
    print("Discount % : 20")
    print("Payable Amount : " , bill) 

elif bill >= 2000 and bill < 5000: 
    print("Amount : " , bill)
    bill = bill - 0.1*bill 
    print("Discount % : 10")
    print("Payable Amount : " , bill) 

else:
    print("Amount : " , bill)
    print("Discount % : 0")
    print("Payable Amount : " , bill) 
    