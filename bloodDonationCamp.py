#5
#Blood Donation Camp

age = int(input("Please Enter your Age : "))
weight = int(input("Please Enter your Weight(kgs): "))

if age >= 18:
    if weight > 50 :
        print("Donor Status : Eligible")
    else :
        print("Donor Status : Under Weight")
        print("Required Weight Gain : " , 50 - weight, "Kgs")
else:
    print("Not Eligible")

