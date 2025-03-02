# Interpret ezoterického programovacího jazyka

## Popis projektu
Implementace jednoduchý interpret ezoterického programovacího jazyka `ezop`, který podporuje následující sadu příkazů:

- `I@`, `G@`, `O@`, `+`, `-`, `0`, `#`

## Použité jazyky
-Python

-Markdown

## Podporované příkazy
| Instrukce | Popis |
|-----------|----------------------------------------------|
| `I@`      | Načte celočíselnou hodnotu od uživatele a uloží ji do `@`. |
| `G@`      | Vygeneruje náhodné číslo v rozmezí -1024 až 1024 a uloží ho do `@`. |
| `O@`      | Vypíše hodnotu `@` na standardní výstup. |
| `+`       | Inkrementuje hodnotu `@` o 1. |
| `-`       | Dekrementuje hodnotu `@` o 1. |
| `0`       | Nastaví hodnotu `@` na 0. |
| `#`       | Ukončí interpretaci a vypíše "Skript ukončen.". |

## Spuštění 
```python
python ezop.py "I@++O@-O@#"
```

### Výstup (při vstupu 5)
```
7
6
Skript ukončen.
```
## Implementované příkazy v kódu
### Načtení vstupu (I@)
```python
if instruction == 'I' and queue and queue[0] == '@':
    queue.pop(0)
    try:
        at_var = int(input("Zadejte číslo: "))
    except ValueError:
        print("Chyba: Neplatný vstup.")
        return
```
### Generování náhodného čísla (G@)
```python
elif instruction == 'G' and queue and queue[0] == '@':
    queue.pop(0)
    at_var = random.randint(-1024, 1024)
```

### Výpis hodnoty (O@)
```python
elif instruction == 'O' and queue and queue[0] == '@':
    queue.pop(0)
    print(at_var)
```
### Inkrementace (+)
```python
elif instruction == '+':
    at_var += 1
```
### Dekrementace (-)
```python
elif instruction == '-':
    at_var -= 1
```
### Resetování hodnoty (0)
```python
elif instruction == '0':
    at_var = 0
```
### Ukončení skriptu (#)
```python
elif instruction == '#':
    print("Skript ukončen.")  # Ukončení skriptu
    return
```
### Chybová hláška pro neznámé instrukce
```python
else:
    print(f"Chyba: Neznámá instrukce '{instruction}'")  # Chybová zpráva pro neznámé instrukce
    return
```
## Chybové zprávy
- **Neplatná instrukce:** Pokud je zadána neznámá instrukce, interpret vypíše chybu a ukončí se.
- **Nečíselný vstup při I@:** Pokud uživatel zadá nečíselný vstup, interpret zobrazí chybu a ukončí se.
