
import os
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, output_dir, chunk_size=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    
    print(f"Total pages: {total_pages}")

    for start_page in range(0, total_pages, chunk_size):
        end_page = min(start_page + chunk_size, total_pages)
        writer = PdfWriter()
        
        for i in range(start_page, end_page):
            writer.add_page(reader.pages[i])
            
        output_filename = f"chunk_{start_page // chunk_size + 1:02d}_pages_{start_page + 1}-{end_page}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
            
        print(f"Created: {output_filename}")

if __name__ == "__main__":
    input_pdf = "/Users/levon/Code/docs/full-repatriation-guide-enpdf_2.pdf"
    output_directory = "pdf_chunks"
    split_pdf(input_pdf, output_directory)
