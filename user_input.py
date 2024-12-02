def file_read_write():
    try:
        # Prompt user for the input file
        input_file = input("Enter the filename to read: ")

        # Attempt to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        #To modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # To write to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read. Please check the file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# To run the program
if __name__ == "__main__":
    file_read_write()
