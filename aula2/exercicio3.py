texto = 'Linguagem de Programação Python'

for i in range(5):
    if i == 0 or i == 4:
        print(chr(177) * (len(texto) + 10))
    elif i == 2:
        print(chr(177) + ' ' * 4 + texto + ' ' * 4 + chr(177))
    else:
        print(chr(177) + ' ' * (len(texto) + 8) + chr(177))

print()

print(chr(177) * (len(texto) + 10) + '\n' +
      chr(177) + ' ' * (len(texto) + 8) + chr(177) + '\n' +
      chr(177) + ' ' * 4 + texto + ' ' * 4 + chr(177) + '\n' +
      chr(177) + ' ' * (len(texto) + 8) + chr(177) + '\n' +
      chr(177) * (len(texto) + 10))
