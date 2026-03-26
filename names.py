import name_function
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease enter a first name: ")
    if first == 'q':
        break
    last = input("Please enter a last name: ")
    if last == 'q':
        break
        
    formatted_name = name_function.get_formatted_name(first, last)
    print(f"\tCorrectly formatted name: {formatted_name}.")
