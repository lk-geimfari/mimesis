# Test
db = []
with open('f.txt') as file:
    for line in file.readlines():
        db.append(line.strip())

print(db)
