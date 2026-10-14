print("="*5,"Palindrome Checker","="*5)
word= word.lower()
word =input("Enter a word: ")
#A palindrome reads the same forward and backward.
if word== word[::-1]:
	print("The word is a palindrome")
else:
	print("The word is not plaindrome")