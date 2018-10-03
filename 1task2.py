
#Task-2parta
def task2():
file=open("running-config.cfg.txt")
list=[]
for line in file:
	line=line.strip()
	line=line.split()
	if (line[0]=="security-level"):
		line[1]=10
		print("security-level",line[1])
	if (line[0]=="ip" and line[1]=="address"):
		x=line[2].split(".")
		x[0]=10
		print(x[0:])
task2()
