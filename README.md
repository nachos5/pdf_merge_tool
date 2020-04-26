# PDF Merge Tool

Made by Guðmundur Óli Norland (Github: nachos5)

This simple tools sole purpose is to merge multiple PDF files into one.
Arguments are parsed using argparse. The --help command gives the following output:

usage: pdfmerge.py [-h] (-l LIST [LIST ...] | -d DIRECTORY) [-o OUTPUTFOLDER]

PDF Merge Tool

optional arguments:

* -h, --help            show this help message and exit

* -l LIST [LIST ...], --list LIST [LIST ...]
                        A list of PDF file paths

* -d DIRECTORY, --directory DIRECTORY
                        A directory path containing PDF files

* -o OUTPUTFOLDER, --outputfolder OUTPUTFOLDER
                        If provided, the output PDF file will be saved in this
                        directory, else it will be stored in the projects
                        output directory

Examples:

* python pdfmerge.py -d _your_pdf_directory_path
* python pdfmerge.py -l file1.pdf file2.pdf file3.pdf -o _your_output_folder_