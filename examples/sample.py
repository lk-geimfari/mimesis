# Test
db = []
with open('f.txt') as file:
    for line in file.readlines():
        if line != '\n':
            db.append(line.strip().strip())

print(db)
