def rainbow(string):
	colours = ["red", "orange", "yellow", "limegreen", "cyan", "blue", "violet"]
	f = open("latex_output.txt", "w")
	f.write("$$\\Huge \\text{")
	for n in range(len(string)):
		f.write("\\color{{{}}}".format(colours[n%len(colours)]))
		f.write(string[n])
	f.write("}$$")
	f.close()

def rainbow_matrix(string):
	colours = ["red", "orange", "yellow", "limegreen", "cyan", "blue", "violet"]
	f = open("latex_output.txt", "w")
	f.write("$$\\Huge \\begin{matrix}")
	for n in range(len(string)):
		f.write("\\color{{{}}}".format(colours[n%len(colours)]))
		f.write(string[n])
		if n != len(string)-1:
			f.write("\\\\")
	f.write("\\end{matrix}$$")
	f.close()

options = ["Rainbow", "Rainbow Matrix"]
print("Select option:")
for n in range(len(options)):
	print("{}: {}".format(n+1, options[n]))
try:
	select = int(input())
except:
	print("ERROR")
	exit()

	
string = input("String: ")

if select == 1:
	rainbow(string)
elif select == 2:
	rainbow_matrix(string)
else:
	print("Invalid option.")
	exit()


