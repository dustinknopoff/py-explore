#!/usr/bin/env python2.7
import os
import PyPDF2


class pdfSplitter():
    def __init__(self, original_pdf, out_name, splits):
        """
        Creates new instance of pdfSplitter class
        :param original_pdf: String for path to pdf file to split from
        :param out_name: prefix for output files
        :param splits: Array of intervals to split on
        """
        self.original_pdf = original_pdf
        self.original = open(self.original_pdf, 'rb')
        self.original_reader = PyPDF2.PdfFileReader(self.original)
        self.out_name = out_name
        self.path = self.__make_path()
        self.max_pages = self.__get_max()
        self.splits = self.__valid_splits(splits)

    def __valid_splits(self, splits):
        """
        Checks to see that intervals is equal to the maximum number of pages in the PDF
        :param splits: Array of integers
        :return: Array of integers if sum of array is equal to number of pages in PDF
        """
        if sum(splits) == self.max_pages:
            return splits
        else:
            raise Exception

    def __make_path(self):
        """
        Gets directory path of original PDF
        :return:
        """
        return os.path.dirname(self.original_pdf)

    def __get_max(self):
        """
        Get's number of pages in original PDF
        :return:
        """
        return self.original_reader.getNumPages()

    def split(self):
        """
        Splits a PDF by the requested intervals
        """
        # For every split option
        for index, split in enumerate(splits):
            new_file = PyPDF2.PdfFileWriter()
            # For every page that adds to
            for count in range(int(split)):
                page = self.original_reader.getPage(count)
                new_file.addPage(page)
            file = open(self.path + '/' + self.out_name +
                        '-page' + str(index) + '.pdf', 'wb')
            new_file.write(file)
            print self.out_name + '-page' + \
                str(index) + '.pdf' + ' has been made.'
            file.close()


if __name__ == '__main__':
    # Get path
    path = raw_input("Which PDF would you like to split? (full path)")
    # Example /Users/Home/Desktop/sample.pdf
    # Get name of output files
    name = raw_input('What would you like the output files to start with?')
    # Example "activity"
    # Get split of pages
    # NOTE: Must add up to number of pages in PDF or script will crash.
    splits = raw_input('Tell me how to split it up! i.e. (1, 3, 7)')
    # Generate list of ints from split
    splits = list(splits)
    # Convert to list of numbers
    numbers = []
    for split in splits:
        if str(split).isdigit():
            numbers.append(int(split))
    splitter = pdfSplitter(path, name, numbers)
    splitter.split()
