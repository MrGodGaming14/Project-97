yr_val=int(input("Please type a Year, to check if it is a Leap year: "))

if(yr_val%4 == 0 and yr_val %100 != 0 or yr_val%400==0):
    print("This is a leap year")
else:
    print("This is not a leap year")

height=int(input("Please Type your Height in cm: "))

inches=height*0.394
feet=round(inches%12)

print("Your Height in inches is ",feet,"foot")
