worldmap = ["..XXX","..XXX","...XX","X....","XXX.."]
n = len(worldmap)
m = len(worldmap[0])
count = 0
x, y =0, 0
for i in range(len(worldmap)):
    worldmap[i] += "X"
worldmap.append("X"*len(worldmap[0]))
while True:
    if x==n-1and y==m-1:
        break
    if worldmap[x+1][y] == "." and worldmap[x][y+1] == "." and worldmap[x+1][y+1] == "." :
        x+=1
        y+=1
        count+=1
        continue
    if worldmap[x+1][y] == "." and worldmap[x][y+1] == "." and worldmap[x+1][y+1] == ".":
print(worldmap)