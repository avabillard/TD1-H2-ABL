import sys
for caractere in sys.stdin.read():
    print(caractere)
sys.stderr.write("Une erreur est survenue\n")
