#6
#Gym goals


plans = [
    {"Goals": "Weight Loss" , "Suggested" : "Cardio + Diet"},
    {"Goals": "Muscle Gain" , "Suggested" : "Strength Training + Protein Diet"},
    {"Goals": "Flexibility" , "Suggested" : "Yoga + Streaching"}
    
    ]

for plan in plans : 
    print(f"Goals : {plan['Goals']} , Suggested :{plan['Suggested']} ")
    
ch = int(input("\nMake a Choice of 1 , 2 or 3 : "))

print("\n")
if ch == 1  :
    print("Plan-A successfully Availed ")
    print("Goals : Weight Loss\nSuggested : Cardio + Diet")

elif ch == 2  :
    print("Plan-B successfully Availed")
    print("Goals : Muscle Gain\nSuggested : Strength Training + Protein Diet")

elif ch == 3  :
    print("Plan-C successfully Availed")
    print("Goals : Flexibility\nSuggested : Yoga + Streaching")

else:
    print("Suggested : Personalized Consultation")






























