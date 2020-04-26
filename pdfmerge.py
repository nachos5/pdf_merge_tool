import argparse
import datetime
import os
import sys
import uuid

from PyPDF2 import PdfFileMerger


def pdf_file_type(filepath):
    """
    Checks if the input string is a PDF file
    """
    if not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(f"{filepath} is not a file")
    if not os.path.splitext(filepath)[1] == ".pdf":
        raise argparse.ArgumentTypeError(f"{filepath} is not a PDF file")
    return filepath


def pdf_directory_type(dir_path):
    """
    Checks if the input string is a directory and whether is contains PDF files
    """
    if not os.path.isdir(dir_path):
        raise argparse.ArgumentTypeError(f"{dir_path} is not a directory")
    pdf_filelist = []
    for f in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, f)):
            if os.path.splitext(f)[1] == ".pdf":
                pdf_filelist.append(os.path.join(dir_path, f))
    if not pdf_filelist:
        raise argparse.ArgumentTypeError(f"{dir_path} contains no PDF files")

    return pdf_filelist


def output_type(output_path):
    """
    Checks if the input string is a directory
    """
    if not os.path.isdir(output_path):
        raise argparse.ArgumentTypeError(f"{output_path} is not a directory")
    return output_path


def parse_args(args):
    """
    Takes arguments as input and tries to parse them according to the following rules
    """
    parser = argparse.ArgumentParser(description="PDF Merge Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-l", "--list", nargs="+", help="A list of PDF file paths", type=pdf_file_type,
    )
    group.add_argument(
        "-d",
        "--directory",
        help="A directory path containing PDF files",
        type=pdf_directory_type,
    )
    parser.add_argument(
        "-o",
        "--outputfolder",
        help="If provided, the output PDF file will be saved in this directory, else it will be stored in the projects output directory",
        type=output_type,
    )

    return parser.parse_args(args)


def run(args):
    """
    Runs the program, tries to parse the input arguments at first, if they are valid the PDF files are merged
    """
    parsed_args = parse_args(args)
    pdf_list = parsed_args.directory if parsed_args.directory else parsed_args.list
    output_dir = (
        parsed_args.outputfolder
        if parsed_args.outputfolder
        else os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    )
    merger = PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    output_filepath = os.path.join(output_dir, f"output_{uuid.uuid4()}.pdf")
    merger.write(output_filepath)
    merger.close()


if __name__ == "__main__":
    run(sys.argv[1:])
