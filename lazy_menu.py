#Fill the output of the selected input
#Warning! Do not use & symbol in your output!

import dmenu
import os
path = "/home/plato/Documents"
file = "p"
results = []
options = []
output=""
with open(path+"/"+file, 'r') as p:
	for line in p:
		if line[0] != "#" and line != "\n":
			lines = str(line).split(" & ")
			options.append(str(lines[0]))
			results.append(str(lines[1])[:-1])
entry = dmenu.show(options,prompt="Service:")
for index in range(len(options)):
	if str(entry) == str(options[index]):
		selected = index
output = str(results[selected])
if "&" in output:
	print("output "+str(lines[1])+" contain (&) symbol, please remove it and try again.")
	exit()
#print(output)
os.system("sleep 0.5")
os.system("xdotool type --clearmodifiers "+str(output))
os.system("xdotool key KP_Enter")
