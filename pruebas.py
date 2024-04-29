import sys
def limpiar(n=1):
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line


num = range(1,11)  # hace 10 lineas
for n in num:
    print(n)
limpiar(5)  # limpia (5) lineas