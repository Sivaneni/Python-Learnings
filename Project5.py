import os
import pdfplumber

import re
import cx_Oracle  # Make sure you have installed the cx_Oracle package
   # this returns 1.2.15 for me

def create_database_connection():
    # Replace with your actual database credentials
    username = "system"
    password = "system"
    dsn = "localhost:1521/xe"  # e.g., localhost:1521/xe
    cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\Welcome\Downloads\instantclient-basic-windows.x64-11.2.0.4.0\instantclient_11_2")
    try:
        conn = cx_Oracle.connect(username, password, dsn)
        return conn
    except cx_Oracle.DatabaseError as e:
        print(f"Error connecting to the database: {e}")
        return None

def extract_and_store_questions(pdf_path, page_number, regex_pattern=None):
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
            chapter = f'Chapter {page.page_number}'
            extracted_text = page.extract_text()
            print(extracted_text)

            # Apply regex pattern if provided
            if regex_pattern:
                #print('in true case')
                matched_content = re.findall(regex_pattern, extracted_text)
                #print(matched_content)
                #extracted_text = "\n".join(matched_content)
                extracted_text=matched_content
            print(extracted_text)
        
        conn = create_database_connection()
        for text in extracted_text:
            print('text is',text)
            
            if conn:
                cursor = conn.cursor()
                print('execute time')
                cursor.execute("""
                INSERT INTO questions (subject_name, question_text, answer_options, chapter_name)
                VALUES (:subject, :question, :options, :chapter)
                """, {
                'subject': 'GK',
                'question': text[0],
                'options': '(A)'+text[1]+'\n'+'(B)'+text[2]+'\n'+'(C)'+text[3]+'\n'+'(D)'+text[4]+'\n',
                'chapter': chapter
                })
        conn.commit()
        conn.close()

        print(f"Extracted text from page {page_number} has been stored in the database.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    pdf_path = r'C:\Users\Welcome\Desktop\Generative AI\learnpython\content\sample2.pdf'

    # Example: Extract questions from page 1 with a regex pattern
    page_number = 4
    regex_pattern = r'(\d+.\s[\s\S]+?)\s?\(A\)\s(.*?)\s?\(B\)\s(.*?)\s?\(C\)\s(.*?)\s?\(D\)\s(.*)'  # Replace with your actual regex
    extract_and_store_questions(pdf_path, page_number, regex_pattern)
