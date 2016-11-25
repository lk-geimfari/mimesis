lista = []

with open('file.txt', 'r') as file:
    for line in file.readlines():
        x = line.split(' → ')
        lista.append(x[0].strip())

print(lista)
