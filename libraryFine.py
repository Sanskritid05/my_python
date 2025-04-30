#3
# library fine system 

days = int(input("Enter no. of days took to return : ")) 
fine = 0 

print("\n") 

if days < 7 :
    print("No Fine")     
elif days > 7 and days < 30 :
    fine = (days - 7)*5 
    print("Fine to pay : Rs." , fine)
else :
    fine = (days - 7)*5 
    print("Fine to pay : Rs." , fine)
    print("Membership Cancelled") 
    
    