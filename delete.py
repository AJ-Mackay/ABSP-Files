# Module 11 - Files: Deleting Files

### FILES AND DIRECTORIES ARE DELETED ###
### PERMANENTLY ###
### NOT JUST MOVED TO TRASH! ###

# os.unlink('arg') - Deletes the single file provided as arg.
# os.rmdir('arg') - Removes the directory provided. Folder MUST be empty.
# shutil.removetree() - Deletes a folder AND contents.

# WINDOWS Example:
# import os
# os.unlink('bacon.txt')
# os.rmdir('c:\\delicious') # Will error if directory provided is not empty.

# import shutil # SH(ell) UTIL(ities)
# shutil.removetree('c:\\delicious')

### DO A "DRY RUN" FIRST ###
# WINDOWS Example with a typo:

import os

os.chdir('C:\\Users\\Al\\Desktop')

for filename in os.listdir():
    if filename.endswith('.rxt'): # ".rxt" is a typo, meant to be ".txt".
        # os.unlink(filename) # Comment out the delete line first to ensure the code works.
        print(filename) # Will display the files that would have been deleted.

# In this example "IMPORTANT_FILE!!!.rxt" is returned as a string.
# which would have been the file that was deleted forever
# instead of the ".txt" files that were meant to be removed.

# WINDOWS Example without typo:

import os

os.chdir('C:\\Users\\Al\\Desktop')

for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print(filename)

# In this example "Switching to Python.txt" is returned.
# As this is the desired file to be removed, the print() line can be commented.
# The os.unlink(filename) file can be commented back in and the program run.

# WINDOWS Example: send2trash

import send2trash

send2trash.send2trash('C:\\Users\\Al\\Desktop\\IMPORTANT_FILE!!!.rxt')

# This will send the selected files/folders to the recycle bin.
# They are NOT deleted permanently unless the bin is emptied.
# Folders do not need to be emptied first to use send2trash.
