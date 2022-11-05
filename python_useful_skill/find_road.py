worldmap = ["..XXX","..XXX","...XX","X....","XXX.."]
n = len(worldmap)
m = len(worldmap[0])
for i in range(len(worldmap)):
    worldmap[i] += "X"
worldmap.append("X"*len(worldmap[0]))
while True:

print(worldmap)