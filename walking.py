# Module 11 - Files: Walking a Directory Tree

# WINDOWS Example 1:

import os

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

# Output:
The folder is c:\delicious
The subfolders in c:\delicious are: ['foo', 'walnut']
The filenames in c:\delicious are: ['spam.txt', 'spamspamspam.txt']

The folder is c:\delicious\foo
The subfolders in c:\delicious\foo are: []
The filenames in c:\delicious\foo are: ['spam.txt']

The folder is c:\delicious\walnut
The subfolders in c:\delicious\walnut are: ['waffles']
The filenames in c:\delicious\walnut are: ['eggs.txt']

The folder is c:\delicious\walnut\waffles
The subfolders in c:\delicious\walnut\waffles are: []
The filenames in c:\delicious\walnut\waffles are: ['bacon.txt', 'ham.txt']

# WINDOWS Example 2:
import os, shutil

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder: # Looks for subfolders with "fish" in their name.
            os.rmdir(subfolder) # Removes the subfolders with "fish" in their name.

    for file in filenames:
        if file.endswith('.py'): # Looks for files ending in ".py"
            shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup')) # Creates an absolute path to the file within the folder.
            # The file is then renamed to have ".backup" appended e.g "bacon.txt" would become "bacon.txt.backup".
