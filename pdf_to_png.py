
import os
import fitz  # PyMuPDF

def pdf_to_png(input_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = fitz.open(input_path)
    total_pages = len(doc)
    
    print(f"Total pages: {total_pages}")

    for i in range(total_pages):
        page = doc.load_page(i)  # number of page
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # render page to an image, zoom x2 for better quality
        output_filename = f"page_{i + 1:02d}.png"
        output_path = os.path.join(output_dir, output_filename)
        pix.save(output_path)
        print(f"Created: {output_filename}")

if __name__ == "__main__":
    input_pdf = "/Users/levon/Code/docs/full-repatriation-guide-enpdf_2.pdf"
    output_directory = "pdf_images"
    pdf_to_png(input_pdf, output_directory)
