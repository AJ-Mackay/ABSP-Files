# Module 11 - Files: Filenames and Absolute/Relative File Paths

# ONLY FOR WINDOWS - 
# Use r to create raw strings or \ as the escape character.
# Example:
# 'c:\\spam\\eggs.png' - uses \ to escape.
# r'c:\spam\eggs.png' - uses raw strings.
# Both are the same.

# Mac and Linux use "/" instead of "\" for directories.

import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
print(os.sep) # States which value the join function will use.
print(os.getcwd()) # Returns Current Working Directory as a string.
print(os.chdir(r'/')) # Changes cwd to the argument provided, returns 'None'.
print(os.getcwd()) # Returns the new directory given in the previous command.

# 'spam.png' = Relative File Path - Assumes you are in the current folder.
# 'c:\\folder1\\folder2\\spam.png' = Absolute File Path.

# . = This directory/folder (relative file path)
# .. = The parent folder (relative file path)

print(os.path.abspath('spam.png')) # Returns the absolute path of the argument passed.
# WINDOWS - print(os.path.abspath('..\\..\\spam.png')) # Returns the absolute path of the file in the parent folder's parent folder.
print(os.path.isabs('/')) # Returns 'True' if the provided path is absolute.

# os.path.relpath('arg1', 'arg2') - Returns the relative path between the given arguments. arg2 = current working directory.
# os.path.dirname('arg') - Returns the directory of the file.
# os.path.basename('arg') - Returns the base name (the part after the last "\\").
# os.path.exists('arg') - Returns 'True' if the given route exists.
# os.path.isfile('arg') - Returns 'True' if the given argument is a file.
# os.path.isdir('arg') - Returns 'True' if the given argument is a directory.
# os.path.getsize('arg') - Returns the size of the given file in bytes.
# os.listdir('arg') - Return a list of strings of the contents of the given folder.
# os.makedirs('arg') - Will create the given directory.

# WINDOWS Examples:
# print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1') - Returns 'folder2\\spam.png'
# print(os.path.dirname('c:\\folder1\\folder2\\spam.png') - Returns 'c:\\folder1\\folder2'
# print(os.path.basename('c:\\folder1\\folder2\\spam.png') - Returns 'spam.png'
# print(os.path.basename('c:\\folder1\\folder2') - Returns 'folder2'
# print(os.path.exists('c:\\windows\\system32\\calc.exe') - Returns 'True' as the file path exists.
# print(os.path.isfile('c:\\windows\\system32\\calc.exe') - Returns 'True' as "calc.exe" is a valid file.
# print(os.path.isfile('c:\\windows\\system32') - Returns 'False' as "System32" is a folder, not a file.
# print(os.path.isdir('c:\\windows\\system32') - Returns 'True' as this is a directory/folder.
# print(os.path.getsize('c:\\windows\\system32\\calc.exe') - Returns '918528' (Size of the calculator program in bytes).
# print(os.listdir('c:\\automatebook') - Returns a list of strings e.g. - ['.svn', '101programmingprojectideas.txt', ... 'zophie_lowres.jpg'].
# os.makedirs('c:\\delicious\\walnut\\waffles') - Will create a folder called waffles, inside the walnut folder which is inside the delicious folder.

# WINDOWS Example for getsize():
totalSize = 0
for filename in os.listdir('c:\\automatebook'):
    if not os.path.isfile(os.path.join('c:\\automatebook', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\automatebook', filename))

print(totalSize)
