#!/usr/bin/env python

# basic pdfmerge tool
import sys
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

##
## @brief      Verifies that proper usage is implemented.
##
## @param      args  the command line arguments
##
## @return     nothing - will cause system exit if error encountered.
##
def Verify_proper_usage( args ):
	if (len(args[1:]) < 3):
		print 'PDFMerge requires at least 3 parameters...'
		print 'Usage: ./PDFMerge [buildpath/name.pdf] [merge1.pdf] [merge2.pdf] ... [mergeN.pdf]'
		print 'First parameter is the path and name of the pdf to "build".'
		print 'All of the following parameters should be pdf file names to be merged into the build file.'
		sys.exit(2)

##
## @brief      Removes a build file.
##
## @param      file  the file to be removed.
##
## @return     nothing, on an error a system exit is issued.
##
def remove_build_file( file ):
	try:
		if os.path.exists(file):
			os.remove(file)
	except:
		print "Error attempting to delete " + file + " !"
		sys.exit(1)

##
## @brief      Initializes the build file for merging.  First the file is
##             removed so the pdfs are merged into a empty file.
##
## @param      file_name  the file to initialize
##
## @return     the file name variable
##
def init_build_file( file_name ):
	remove_build_file(file_name)
	return file_name

##
## @brief      Gets the pdf file content.
##
## @param      file_name  The pdf file to be extracting the content of.
##
## @return     The pdf file content.
##
def get_pdf_file_content( file_name ):
	base_file_name = os.path.basename(file_name)
	print("Appending " + base_file_name + "...")
	return PdfFileReader(file(file_name, 'rb'))


def main():

	Verify_proper_usage(sys.argv)

	build_file = init_build_file(sys.argv[1])

	merge_result = PdfFileMerger()

	print("Beginning build of " + build_file + "...")
	# walk through file arguments and append then to the build file
	for f in sys.argv[2:]:
		merge_result.append(get_pdf_file_content(f))
		file(f).close() # Close the file to prevent duplicate pages from being appended

	# Write all the appends to a new file
	merge_result.write(build_file)
	print("Merge Completed, " + build_file + " is ready.")


main()