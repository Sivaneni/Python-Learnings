import os
import pdfplumber
import re
import configparser

def extract_page_content(pdf_path):
    try:
        # Check if the folder exists
        if not os.path.exists(os.path.dirname(pdf_path)):
            raise FileNotFoundError(f"Folder does not exist: {os.path.dirname(pdf_path)}")

        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            
            extracted_text=''
            for page in pdf.pages:

            
                extracted_text+=page.extract_text()

           


        # Write the extracted text to a text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

        print(f"Extracted text  has been written to {output_file_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    pdf_path = r'C:\Users\Welcome\Desktop\Generative AI\learnpython\projects\Project1\content\input_pdf.pdf'
    output_file_path = r'C:\Users\Welcome\Desktop\Generative AI\learnpython\projects\Project1\extracted_text.txt'

    

    try:
        
        extract_page_content(pdf_path)
    except ValueError:
        print("Invalid input. Please provide a valid integer page number.")
