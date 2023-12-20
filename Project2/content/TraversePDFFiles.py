import os
import pdfplumber

# Path where existing /content folder is present
base_path = r'C:\Users\Welcome\Desktop\Generative AI\learnpython\content'  

# List of sub folders to create
sub_folders = ['One', 'Two', 'Three']

# Create sub folders
for folder in sub_folders:
    path = os.path.join(base_path, folder)  
    os.makedirs(path, exist_ok=True)

# Dictionary to store PDFs for each folder  
pdfs = {f:[] for f in sub_folders}

# Add sample PDFs to each folder (add actual logic)  
for folder in pdfs:
    pdfs[folder].extend(['sample.pdf'])
    
# Function to process PDFs for folder    
def process_pdfs(folder_path):

    output_path = os.path.join(folder_path, 'output.txt')
    
    for pdf_path in pdfs[folder_name]: 
        
        full_path = os.path.join(folder_path, pdf_path)
        
        # Extract text from each page
        content = []
        with pdfplumber.open(full_path) as pdf:
            for page in pdf.pages:
                content.append(page.extract_text())
        
        # Write content to output.txt
        with open(output_path, 'w') as f:
            f.write('\n\n'.join(content))
            
# Process PDFs for each folder
for folder_name in pdfs.keys():
    folder_path = os.path.join(base_path, folder_name)  
    process_pdfs(folder_path)
    
print('PDF content extraction complete!')