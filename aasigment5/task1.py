my_dict={"Sam":88,'Roni':97,'Alice':85}
input_value=input("Enter the student's name: ")
if input_value in my_dict:
    mark=my_dict.get(input_value)
    print(input_value,"'s marks: ",mark)
else:
    print("student not found.")