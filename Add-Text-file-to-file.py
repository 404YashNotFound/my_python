file_name = "user_data.txt"  # Define the text file to store data
input_file = "/content/Text.txt"  # Input file containing user data

# Step 1: Read the data from input file
with open(input_file, "r") as file:
    user_list = [line.strip() for line in file if line.strip()]  # Read and clean lines

# Step 2: Write data into the file in the required format
data = []  # List to store user input

with open(file_name, "a") as file:  # Append mode to avoid overwriting
    for user_name in user_list:
        if user_name.lower() == "stop":
            break
        else:
            text = f"summary ~ '{user_name}' OR "
            file.write(text)  # Write to file
            data.append(text)  # Store input in the list

# Step 3: Convert List to Tuple
data1 = tuple(data)
print("Stored Data:", data1)
