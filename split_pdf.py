
import os
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, output_dir, chunk_size=1):
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
            
        # 1-based indexing for filename
        output_filename = f"page_{start_page + 1:02d}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
            
        print(f"Created: {output_filename}")

if __name__ == "__main__":
    input_pdf = "/Users/levon/Code/docs/full-repatriation-guide-enpdf_2.pdf"
    output_directory = "pdf_pages"
    split_pdf(input_pdf, output_directory, chunk_size=1)
