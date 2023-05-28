from colorama import Fore, Style
print(Fore.BLUE + "<01nodo/enigma>" + Style.RESET_ALL)
filename = input("name the textfile: ")
a= []
f = open (filename + ".txt","w+")
wordcount= int (input ("number of words:"))
Min = int (input ("minimum length of generated word: "))-1
Max = int (input ("maximum length of generated word: "))+1

for x in range (0,wordcount):
	ele=str (input ())
	a.append(ele)
	
	
for n in range(0,wordcount):
	for m in range(0,wordcount):
		k=a[n] + a[m]
		if Min< len(k) <Max:
			f.write(k + "\n")
		else:
			for j in range (0,wordcount):	
				p=k +a[j]
				if Min< len(p) <Max:
					f.write(p + "\n")
				else:continue	
	
		
f.close			
		


