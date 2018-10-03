file=open("running-config.cfg.txt")
list=[]
for line in file:
	line=line.strip()
	line=line.split()
	if(line[0]=="access-list"):
		if(line[1]=="global_access"):
			list.append(line[2])
			print([line[0],"--",line[1],"---",line[2:]])
		elif(line[1]=="fw-management_access_in"):
			list.append(line[2])
			print([line[0],"--",line[1],'---',line[2:]])


