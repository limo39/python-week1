def create_file():
    try:
        # Create a new text file in write mode
        with open("my_file.txt", 'w') as file:
            # Write three lines of text to the file
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line, containing a number: 42.\n")
            file.write("Finally, the third line of text.\n")
        print("File created and written successfully.")

    except (PermissionError, FileNotFoundError) as e:
        print(f"Error occurred while creating the file: {e}")

    finally:
        print("Create file operation completed.")


def read_file():
    try:
        # Read the contents of the file
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    finally:
        print("Read file operation completed.")


def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", 'a') as file:
            # Append three additional lines of text
            file.write("Appending a new line to the file.\n")
            file.write("This is the second appended line: 3.14.\n")
            file.write("And here is the third appended line.\n")
        print("File updated successfully.")

    except (PermissionError, FileNotFoundError) as e:
        print(f"Error occurred while appending to the file: {e}")

    finally:
        print("Append file operation completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read the file again to display the updated contents
