# Mini Project : Number Counter and Sorter Table(User Input)
numbers=[]
print("Enter number one at a time.")
print("Type 'done' when you are finished. \n")

while True:
    user_input= input("Enter the number")
    
    if user_input.lower()=='done':
        break
    if user_input.isdigit():
        numbers.append(int(user_input))
    else:
        print("Please enter a valid whole number")