a=input()
l=['a','e','i','o','u']
n=len(a)
if a.isalpha():
	if n>1:
		print("Invalid")
	else:
		if a in l:
			print("Vowel")
		else:
			print("Consonant")


else:
	print("invalid")	
	
	
