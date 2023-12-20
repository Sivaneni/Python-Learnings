
## Project 1: Read PDF from Folder

### Requirements
- Store a PDF file in the folder `/content/Project1/input_pdfs`
- Read a PDF file from the folder
- Write the content to a text file called `output.txt` under `/content/Project1/output`

### Error Handling
- Handle the case where the folder is not available
- Handle the case where the PDF file is not present in the content folder
- Handle the case where the `output.txt` file is not available



## Project 2: Traverse and Filter PDF Files

### Requirements
- Add sub-folders called `One`, `Two`, `Three` under the folder `/content/Project2`
- Add PDF files under each of the sub-folders
- Load all PDF files under the sub-folders and load the PDF content
- Write the content to a text file called `output.txt` under each sub-folder respectively

### Error Handling
- Handle the case where the folder is not available
- Handle the case where the PDF file is not present in a sub-folder
- Handle the case where the `output.txt` file is not available in a sub-folder



## Project 3: Read Content from a Particular Page

### Requirements
- Update Project 1 and modify the reading of content 
- Take a page number as input from the command prompt
- Read the content of the provided page number and write it to the output file under `/content/Project3/output`

### Error Handling
- Handle the case where the folder is not available
- Handle the case where the PDF file is not present in a sub-folder
- Handle the case where the `output.txt` file is not available in a sub-folder



## Project 4: Read Regular Expression from a Config File and Extract Content

### Requirements
- Update Project 3
- Add support for a configuration file 
- In the configuration file, set a config with key `regex` and value as some regular expression that will match a part of the content in the PDF
- Update the code to extract only the content matching the regular expression 
- Write the content to the output file

### Error Handling
- Handle the case where the folder is not available
- Handle the case where the PDF file is not present in a sub-folder
- Handle the case where the `output.txt` file is not available in a sub-folder
- Handle the case where no configuration file is available
- Handle the case where the configuration file does not have the regular expression



## Project 5: Store Extracted Questions in MySQL

### Requirements
- Update Project 4 and add support for a database
- Create a database to store the following:
  - Subject Name
  - Question Text
  - Answer Options
  - Chapter Name
- Load a PDF containing questions
- Extract each question as per a regular expression
- Store each question in the database

### Error Handling
- Handle the case where the database is not available
- Handle the case where the table is not available
- Handle any error handling in DB operations



## Project 6: Load All Questions from a Chapter

### Requirements
- Update Project 5 and add support for taking a chapter name as input in the command line
- Load all questions from the input chapter
- Print all questions on the console

### Error Handling
- Handle the case where an empty string is provided as input from the command line
- Handle the case where there are no questions corresponding to the provided chapter name

## Project 7: Load RSS Content and Extract Content from Each Link in Multiple Threads

### Requirements
- Load an RSS XML file (Format: [https://www.w3schools.com/xml/xml_rss.asp](https://www.w3schools.com/xml/xml_rss.asp))
- Loop through each link
- Extract content from each link and write it to `output.txt`
- Execute reading from multiple links in parallel

### Error Handling
- Handle the case where no RSS XML file is available
- Handle the case where the XML file is empty

