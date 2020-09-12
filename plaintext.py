# Module 11 - Files: Reading and Writing Plaintext Files

# helloFile = open('/Users/paulmackay/Desktop/Python/Files/hello.rtf', 'w') - Opens file in write mode (editing).
# helloFile = open('/Users/paulmackay/Desktop/Python/Files/hello.rtf', 'a') - Opens file in append mode (adds given text to the bottom of the file).


helloFile = open('/Users/paulmackay/Desktop/Python/Files/hello.rtf')
content = helloFile.read()
print(content)
helloFile.close() # Closes the file.

helloFile = open('/Users/paulmackay/Desktop/Python/Files/hello.rtf')
helloFile.readlines()

# Does not seem to work on Mac.
# helloFile = open('/Users/paulmackay/Desktop/Python/Files/hello2.rtf', 'w') # Creates the file if it does not already exist.
# helloFile.write('Hello!!!!!!!') # Returns the number of characters given as an integer.

# WINDOWS Example:
# baconFile = open('bacon.txt', 'w')
# baconFile.write('Bacon is not a vegetable')
# baconFile.close()

# import os
# print(os.getcwd()) - Shows that the file was saved in the current working directory.

# baconFile = open('bacon.txt', 'a')
# baconFile.write('\n\nBacon is delicious')
# baconFile.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
