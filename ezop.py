import sys
import random

def interpret_ezop(code):
    queue = list(code)  
    at_var = 0  

    while queue:
        instruction = queue.pop(0)

        if instruction == 'I' and queue and queue[0] == '@':
            queue.pop(0)
            try:
                at_var = int(input("Zadejte číslo: "))
            except ValueError:
                print("Chyba: Neplatný vstup.")
                return
        elif instruction == 'G' and queue and queue[0] == '@':
            queue.pop(0)
            at_var = random.randint(-1024, 1024)
        elif instruction == 'O' and queue and queue[0] == '@':
            queue.pop(0)
            print(at_var)
        elif instruction == '+':
            at_var += 1
        elif instruction == '-':
            at_var -= 1
        elif instruction == '0':
            at_var = 0
        elif instruction == '#':
            print("Skript ukončen.")
            return
        else:
            print(f"Chyba: Neznámá instrukce '{instruction}'")
            return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pro spuštění zadej: python ezop.py \"I@++O@-O@#\"")
    else:
        interpret_ezop(sys.argv[1])
