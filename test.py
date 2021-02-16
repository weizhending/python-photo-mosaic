Tiles = []
file_open = open("tiles.txt", "r")

for line in file_open:
    Tiles.append("images/"+line.rstrip("\n"))

print(Tiles)

file_open.close()
