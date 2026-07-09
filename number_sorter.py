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
        print("Or type 'done' to finish")
# Cheak if user entered at least one number
if len(numbers)==0:
    print("\n No numbers were entered.")
else:
    # count total numbers
    total_count=len(numbers)

    # Sort numbers from least to greatest 
    sorted_numbers=sorted(numbers)

    # Count Occurance of each unique number
    unique_counts={}
    for num in sorted_numbers:
        if num in unique_counts:
            unique_counts[num]=1
        else:
            unique_counts[num]=1
    
    # Display Results
    print(f"\n Total numbers entered: {total_count}")
    print(f"Unique Numbers:{len(unique_counts)}\n")

    print("Sorted List (Least to Greatest):")
    print(sorted_numbers)

    print("\n--- Number Frequency Table ---")
    print(f"{'Number':<10}{'Count': <10}")
    print("-"*20)
    for num in sorted(unique_counts):
        print(f"{num:10}{unique_counts[num]:<10}")