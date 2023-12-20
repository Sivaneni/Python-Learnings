import os
import pdfplumber
import re
import configparser

def extract_page_content(pdf_path, page_number, regex_pattern=None):
    try:
        # Check if the folder exists
        if not os.path.exists(os.path.dirname(pdf_path)):
            raise FileNotFoundError(f"Folder does not exist: {os.path.dirname(pdf_path)}")

        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Validate page number
            if page_number < 1 or page_number > len(pdf.pages):
                raise ValueError(f"Invalid page number. Please provide a valid page number (1-{len(pdf.pages)})")

            # Extract text from the specified page
            page = pdf.pages[page_number - 1]
            extracted_text = page.extract_text()

           


        # Write the extracted text to a text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

        print(f"Extracted text from page {page_number} has been written to {output_file_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    pdf_path = r'C:\Users\Welcome\Desktop\Generative AI\learnpython\projects\Project3\content\sample.pdf'
    output_file_path = r'C:\Users\Welcome\Desktop\Generative AI\learnpython\projects\Project3\extracted_text.txt'

    

    try:
        page_number = int(input("Enter the page number: "))
        extract_page_content(pdf_path, page_number)
    except ValueError:
        print("Invalid input. Please provide a valid integer page number.")
