
#Task-1parta
file=open("running-config.cfg.txt")
dic={}
list=[]
for line in file:
        line=line.strip()
        line=line.split()
        if (line[0]=="nameif"):
                list.append(line[1])
        if (line[0]=="interface"):
                list.append(line[1])
        if (line[0]=="vlan"):
                list.append(line[1])
        if (line[0]=="ip address"):
                list.append(line[1])
print(list)

