# Step 1: Take user input and write to output.txt (overwrites if file exists)
user_input = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')  # Write initial input
print("Data successfully written to output.txt.\n")    
    
# Step 2: Append additional data
append_input = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(append_input + '\n')  # Append new input
print("Data successfully appended\n")   

# Step 3: Read and display the final content
print("Final content of output.txt:\n")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)