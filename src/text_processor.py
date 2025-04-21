def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
    uppercase_text = text.upper()
    
    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
        return False
    
    try:
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def main(input_file="input.txt", output_file="output.txt"):
    """Main function to process a text file."""
    text = read_file(input_file)
    print(text)
    edit = input("Do you want to edit the input file? (Y/N)    ")
    if edit == 'y':
        overwrite = input("Do you want to overwrite the file? (Y/N) -- \"No\" will append to end of file  ")
        if overwrite == 'n':
            try:
                with open(input_file, 'a') as file:
                    addText = input("Type your additional text: \n")
                    file.write("\n" + addText)
                with open(input_file, 'r') as file:
                    fileText = file.read()
                results = process_text(fileText)
                if results:
                    success = write_results(results, output_file)
                    if success:
                        print(f"Processing complete. Results written to {output_file}")
                        return True
                else:
                    print("Processing failed.")
                    return False
            except Exception as e:
                print(f"Error reading file: {e}")
                return None
        else:
            try:
                with open(input_file, 'w') as file:
                    newText = input("Type your additional text: \n")
                    file.write("\n" + newText)
                with open(input_file, 'r') as file:
                    fileText = file.read()
                results = process_text(fileText)
                if results:
                    success = write_results(results, output_file)
                    if success:
                        print(f"Processing complete. Results written to {output_file}")
                        return True
                else:
                    print("Processing failed.")
                    return False
            except Exception as e:
                print(f"Error reading file: {e}")
                return None
    else:
        if text:
            results = process_text(text)
            if results:
                success = write_results(results, output_file)
                if success:
                    print(f"Processing complete. Results written to {output_file}")
                    return True
        
        print("Processing failed.")
        return False

if __name__ == "__main__":
    main()
