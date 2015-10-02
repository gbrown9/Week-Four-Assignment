# Gabe Brown

# CIS-125

# Collaberated with Devin and Google



# Define a function called piggy(string) that returns a string

def piggy(word):
	# Magic Happens Here
	vowels = "aeiouAEIOU"
	pig = ""
	w = 0
	endWord = ""
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			# True?  We are done
			if w == 0:
				pig = word + "yay"
			else:
				pig = word[w:] + endWord + "ay"
			break
		else:
			# False? Consonant
			endWord = endWord + letter
			w = w + 1
	return pig
	

# Open the file *getty.txt* for reading.  
myFile = open("getty.txt", "r")
# Open a new file *piggy.txt* for writing.  
newFile = open("piggity.txt", "w")
# Read the getty.txt file into a string.  
myString = myFile.read()
# Strip out bad characters (, - .).  
myString = myString.replace(",", "")
myString = myString.replace("-", "")
myString = myString.replace(".", "")
# Split the string into a list of words.  
myList = myString.split()
# Create a new empty string.  
newGetty = ""
# Loop through the list of words, pigifying each one.  
for word in myList:
	newGetty = newGetty + piggy(word) + " "
# Write the new string to piggy.txt.  
newFile.write(newGetty)
# close the files.
myFile.close()
newFile.close()