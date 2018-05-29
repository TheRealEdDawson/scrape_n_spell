import enchant
import subprocess
import re
import string
import sys

# Checking that all the arguments were entered on the command line, exiting with a message if not.
def checkstart():
    if len(sys.argv) != 3:
        argumentsNotSet = 'Missing argument(s).\nUsage is like so:\nPython scrape_n_spell.py http://WEB-ADDRESS LOG-FILENAME'
        print (argumentsNotSet)
        sys.exit(1)

checkstart() # Check the command line arguments were passed
# Example usage: python scrape_n_spell.py http://docs.learnosity.com logfile.txt

startPage = sys.argv[1] # The URL where the scraping will begin
logFileName = sys.argv[2] # Command-line argument that specifies the log file filename

wordyWord = "." # String to temporarily store words / text we are checking
spellingResult = "" # String variable holding the correct or incorrect verdict from the dictionary
spellingSuggestion = "" # Object(?) variable holding the suggested words from the dictionary
spellingSuggestionString = "" # A string variable holding the suggested words from the dictionary

print ("Scrape 'n' Spell begins!\n.")

d = enchant.Dict("en_US")   # Use US English Dictionary
# d.check("enchant") #spellcheck -- succeeds (spelling correct)
# d.check("enchnt") #spellcheck - fails (spelling incorrect)
# d.suggest("enchnt") # Get suggestions for words that nearly match this incorrect spelling

# Run Lynx on the console to get a text-only read of the web page.
webPageTextDump = subprocess.run(["lynx", "-dump", startPage, "/dev/null"], stdout=subprocess.PIPE)

print ("Website scraping complete.\n.") # (Website scraping) complete.

f = open(logFileName, 'w') # Open the log file (overwriting old one)
stringFromDump = str(webPageTextDump)  # convert the page text to string

# Remove massive blocks of spaces and newline commands from the string
stringFromDump = stringFromDump.replace("  ", "")

# Remove other troublesome text from the string
stringFromDump = stringFromDump.replace("\\n", " ") # Delete all "newline" control chars(can we kill all non-intra-word punctuation?)
stringFromDump = stringFromDump.replace("[", " ")   # delete all left-handed square brackets.
stringFromDump = stringFromDump.replace("]", " ")   # delete all right-handed brackets.
stringFromDump = stringFromDump.replace("<", " ")
stringFromDump = stringFromDump.replace(">", " ")
stringFromDump = stringFromDump.replace("(", " ")
stringFromDump = stringFromDump.replace(")", " ")
stringFromDump = stringFromDump.replace("+", " ")
stringFromDump = stringFromDump.replace("=", " ")
stringFromDump = stringFromDump.replace("&", " ")
stringFromDump = stringFromDump.replace("*", " ")
stringFromDump = stringFromDump.replace(",", " ")
stringFromDump = stringFromDump.replace("|", " ")
stringFromDump = stringFromDump.replace("\"", " ")
stringFromDump = stringFromDump.replace("__", " ")

# Stripping out own program artifacts
stringFromDump = stringFromDump.replace("CompletedProcess", " ")
stringFromDump = stringFromDump.replace("args", " ")
stringFromDump = stringFromDump.replace("\'lynx\'", " ")
stringFromDump = stringFromDump.replace("\'-dump\'", " ")
stringFromDump = stringFromDump.replace("\'/dev/null\'", " ")
stringFromDump = stringFromDump.replace("returncode", " ")
stringFromDump = stringFromDump.replace("stdout", " ")

# Strings that were troublesome to remove:
#stringFromDump = stringFromDump.replace(".", " ") # killed real property names and sentences
#stringFromDump = stringFromDump.replace(":", " ") # caused URL text to be fragmented

# If it's not a URL AND it's not a junk entry, it's probably a word we can spellcheck!
# Feed it into the spellchecker, and record the result (correct/incorrect spelling) into 
# the log file, then take another word and repeat.

# Convert the giant string of text into an array of values
arrayOfWords = stringFromDump.split(' ')

# Take one word out of the text dump (space-to-space) range
for each in arrayOfWords:
	wordyWord = each # Copy the current "word" to a temporary value

	# and then check the URLs array to see if this entry is already in there. If it is, discard it. 
	# If it's NOT in there, copy it into the URLs array as a new array entry.

	if (wordyWord == ""): continue # if string is blank, skip to the next value 
	if "http" in wordyWord: continue # if string contains "http", then skip to the next value
	if d.check(wordyWord): # correct spelling execution block
		f.write(wordyWord) # Write the word to disk
		spellingResult = " -- CORRECT SPELLING"
		f.write(spellingResult)
	else: #incorrect spelling execution block
		f.write("\n")
		f.write(wordyWord) # Write the word to disk
		spellingResult = " -- *** INCORRECT SPELLING ***"
		f.write(spellingResult)
		f.write("\n")
		spellingSuggestion = d.suggest(wordyWord)
		spellingSuggestionString = str(spellingSuggestion)
		f.write("suggest: ")
		f.write(spellingSuggestionString)
		f.write("\n")
# end if statement
	f.write("\n")
	print (wordyWord) # echo the word to console
#end for loop

f.close() # Close off the log file
print ("\n")
print ("Spellcheck complete!")
print ("Output written to log file: ", logFileName)

#End of file.

