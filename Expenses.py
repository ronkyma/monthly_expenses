total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent €", total, sep='')

num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent €", total, sep='')