import argparse
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


def pdf_split(path, start, end):
    input_file = open(path, 'rb')
    pdf = PdfReader(input_file)
    fname = Path(path).stem
    if end == -1:
        end = len(pdf.pages)
    pdf_writer = PdfWriter()

    for pagenum in range(start-1, end):
        pdf_writer.add_page(pdf.pages[pagenum])

    output_filename = '{}_{:02d}-{:02d}.pdf'.format(
        fname, start, end
    )

    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)

    input_file.close()
    print('Created: {}'.format(output_filename))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    parser.add_argument('--start', '-s', type=int, default=1, required=False)
    parser.add_argument('--end', '-e', type=int, default=-1, required=False)
    args = parser.parse_args()

    pdf_split(args.file, args.start, args.end)
