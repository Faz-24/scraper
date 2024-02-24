import os 
import requests
from bs4 import BeautifulSoup
from docx import Document
import time 

Chap_No = list(range(1,5)) 
base_url = ["https://dulcet-scone-301d4e.netlify.app/chapter_"]
doc = Document()
counter = 0 

for i in Chap_No:
    counter += 1
    time.sleep(5)
    base_url.append(f"https://dulcet-scone-301d4e.netlify.app/chapter_{i}")
    response = requests.get(base_url[0])

    #if response.status_code == 200:        
    soup = BeautifulSoup(response.text, 'html.parser')
    contents = soup.find('p')
        
    if contents:
        chapter = contents.get_text(separator="\n \n")
        doc.add_paragraph(chapter)    
        
    if counter == Chap_No: 
        break
    else:
        print(f"{counter}/{Chap_No[-1]}")
        print(f"{base_url}")
        base_url.pop()
    #else:
         #print("Failed to retrieve the webpage. Status code:", response.status_code)   
destination_folder = "/Users/f.shahriyar/Documents"
output_file = os.path.join(destination_folder, f"chapter-{counter}.docx")
doc.save(output_file)
print(f"Word document saved in chapter'{output_file}'")
