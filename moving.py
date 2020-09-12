# Module 11 - Files: Copying and Moving Files and Folders

# shutil.copy('arg1', 'arg2') - Copies the file provided as arg1 to the destination provided as arg2.
# shutil.copytree('arg1', 'arg2') - Copies the directory provided as arg1 into the new destination (arg2).
# shutil.move('arg1', 'arg2') - Moves the file provided as arg1 to the destination provided as arg2. Can be used to rename files.

# WINDOWS Example:
# import shutil

# shutil.copy('c:\\spam.txt', 'c:\\delicious') # Returns the string of the copied file's new location - 'c:\\delicious\\spam.txt'.
# shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt') # Renames the copied file to the name given in arg2, then returns the string 'c:\\delicious\\spamspamspam.txt'.

# shutil.copytree('c:\\delicious', 'c:\\delicious_backup') # Copies directory into new directory, creates if the directory (arg2) does not already exist, then returns the string 'c:\\delicious_backup'.

# shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut') # Moves the "spam.txt" file to the "walnut" folder inside the "delicious" folding, creating them if they do not already exist, then returns the string 'c:\\delicious\\walnut\\spam.txt'.
# shutil.move('c:\\delicious\\walnut\\spam.txt', 'c:\\delicious\\walnut\\eggs.txt') # Renames "spam.txt" to "eggs.txt", then returns the string 'c:\\delicious\\walnut\\eggs.txt'.
