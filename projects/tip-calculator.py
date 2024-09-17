
print("welcome to the tip calculator")
bill=float(input("what was the total bill $"))
tip=int(input("what percentage tip would you liek to give 10,12,15%"))
people=int(input("how many people are to split the bill"))
percent=tip/100
tip1=bill*percent
total=bill+tip1
split=total/people
print(f"eachh person should pay{round(split,2)}")