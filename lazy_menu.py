import dmenu
import os
#replace with your own username
home_dir="/home/user"
path = home_dir+"/Documents"
file = "p"
results = []
options = []
output=""
with open(path+"/"+file, 'r') as p:
	for line in p:
		if line[0] != "#":
			lines = str(line).split(" !|! ")
			options.append(str(lines[0]))
			results.append(str(lines[1])[:-1])
entry = dmenu.show(options,prompt="Service:")
for index in range(len(options)):
	if str(entry) == str(options[index]):
		selected = index
output = results[selected]
os.system("sleep 0.5")
os.system("xdotool type --clearmodifiers "+output)
os.system("xdotool key KP_Enter")
