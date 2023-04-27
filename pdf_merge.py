# pdf_merge.py

import glob
from PyPDF2 import PdfWriter, PdfReader


def pdf_merge(output_path, input_paths):
    pdf_writer = PdfWriter()

    for path in input_paths:
        with open(path, 'rb') as f:
            pdf_reader = PdfReader(f)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    paths = glob.glob('*.pdf')
    paths.sort()
    pdf_merge('merged.pdf', paths)
