str = "hello hello llo ello hello llo"

l1 = str.split(" ")
count = 0
for i in l1:
	if i == "llo":
		count += 1
		
print("number of occurence = ", count)