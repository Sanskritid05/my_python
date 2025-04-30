#4
# Gym membership

print("\nAvailable Membership Plan:")
plans = [
    {"Duration": "6 months", "Fees": 3000},
    {"Duration": "12 months", "Fees": 5000}
]

for plan in plans:
    print(f"Duration: {plan['Duration']}, Fees: {plan['Fees']}")

print("\n")
plan = int(input("Enter 1 or 2 : "))


if plan == 1 :
    print("Plan A : Successfully Availed")
    print("Duration : 6 months")
    print("Fees : 3000")

elif plan == 2 :
    print("Plan B : Successfully Availed")
    print("Duration : 12 months")
    print("Fees : 5000") 
else:
    print("Plan Currently Unavailable")
