print("Welcome to my TIP Calculator PROGRAM")
print("///////////////////////////////////")
total = int(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = input("How many people to split the bill? ")
print(".......BILL CALCULATED.......")
tip_percent = total * (tip / 100)
sum_total = tip_percent + total
each_split = sum_total / float(people)
print(f"Each person should pay: ${each_split}")

