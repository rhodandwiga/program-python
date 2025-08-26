def modify_content(content):
    """
    Modify the file content in some way.
    Example: Convert text to uppercase.
    """
    return content.upper()


def read_and_write_file():
    try:
        # Ask the user for input filename
        input_filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify content
        modified_content = modify_content(content)

        # Create a new file and write modified content
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{output_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
read_and_write_file()
