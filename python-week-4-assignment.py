def read_and_modify_file():
    filename = input("Enter the filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nOriginal file content successfully read. \n")

            # Modify the content - let's get a little fancy
            modified_content = content.upper()  # We'll turn everything into CAPITAL LETTERS for drama
            
    except FileNotFoundError:
        print(f"\n🚨 Error: The file '{filename}' was not found. Check your spelling or if the file even exists.")
        return
    except PermissionError:
        print(f"\n🚨 Error: Permission denied. I can't read '{filename}'. Try another file or fix permissions.")
        return
    except Exception as e:
        print(f"\n🚨 An unexpected error occurred: {e}")
        return

    # Write to a new file
    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"\n Modified content successfully written to '{new_filename}'. Go check it out!")
    except Exception as e:
        print(f"\n🚨 Failed to write the modified file: {e}")


if __name__ == "__main__":
    print("Welcome to the File Read & Write Challenge 🖋️ + Error Handling Lab 🧪!")
    read_and_modify_file()
