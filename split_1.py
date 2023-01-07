# import sys to access command line arguments
import sys
import os

"""
Create a new file from a compound string
compound: a string representing a compound
"""
def create_compound_file(dirName, compound):
    # split the compound string into lines, with the 'MODEL' line removed
        lines = compound.split('\n')[1:]
        # get the file name from the 'REMARK Name' line
        file_name = lines[0].split()[-1]
        file_name = file_name + ".pdbqt"
        # open a file with the returned file name
        with open(os.path.join(dirName, file_name), 'w') as new_file:
            # write all lines onto the new file
            new_file.write('\n'.join(lines))


"""
Create a new file for each compound in a source file
file: path to source file
"""
def create_new_files(dirName, file):
    # open file and create a new file for each compound
    with open(os.path.join(dirName, file), 'r') as source_file:
        # read and store lines into a list
        text = source_file.read()
        # split text into each compound
        compounds = text.split('\nENDMDL\n')[0:-1]
        # iterate over each compound and create a new file
        for compound in compounds:
            create_compound_file(dirName, compound)

"""
Main program
"""
# specify the directory from which to begin traversing
rootDir = '.'
# traverse all directories
for dirName, subdir_list, file_list in os.walk(rootDir):
    # if current directory is not rootDir...
    if dirName != '.':
        # if there is any file in the current directory...
        if len(file_list) != 0:
            # iterate over all the files in the current directory
            for file in file_list:
                # check if the file is an unziped file
                if file.endswith('pdbqt'):
                    # produce a new file for each compound
                    create_new_files(dirName, file)
                    # rename the source file
                    print(dirName)
                    os.rename(os.path.join(dirName, file), os.path.join(dirName, file + 'COMBINED'))
