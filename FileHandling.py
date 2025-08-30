import os

def process_file(input_filename, output_filename):
    """
    Reads content from an input file, modifies it, and writes the result to an output file.
    Includes error handling for non-existent input files.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the new file to write to.
    """
    try:
        # Step 1: Read the content from the input file
        # The 'with' statement ensures the file is automatically closed
        with open(input_filename, 'r') as infile:
            original_content = infile.read()
        
        # Step 2: Perform a simple modification (e.g., convert to uppercase)
        modified_content = original_content.upper()
        
        # Step 3: Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            
        # Success message
        print(f"Success! The content from '{input_filename}' has been converted to uppercase and written to '{output_filename}'.")
        
    except FileNotFoundError:
        # Error Handling: Catch this specific error if the input file doesn't exist
        print(f"Error: The file named '{input_filename}' was not found. Please check the filename and try again.")
    except Exception as e:
        # General error handling for other unexpected issues
        print(f"An unexpected error occurred: {e}")

# --- Main Program Execution ---
# Prompt the user to enter the filenames
input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the new file to write to: ")

# Call the function to run the file processing logic
process_file(input_file, output_file)

# Example usage without user input (uncomment to test):
# process_file('input.txt', 'output.txt') # This will work if input.txt exists
# process_file('nonexistent_file.txt', 'new_file.txt') # This will trigger the error handling