import json
from pprint import pp

def nuevo_tablero():
    with open("tablero.json", "r") as f:
        return json.load(f)

def print_tablero(tab):
    print(f"Tablero con {numero_fichas(tab)} fichas")
    for i in range(len(tab)):
        print(f"{i} | ", end="")
        for j in range(len(tab[i])):
            print(tab[i][j], sep=" ", end=" ")
        print()
    print("   --------------")
    print("    0 1 2 3 4 5 6\n")

def calcular_movs(tab):
    movs = []
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] != "1":
                continue

            # Arriba
            if i-2 >= 0:
                if tab[i-2][j] == "0" and tab[i-1][j] == "1":
                    movs.append(f"{i}{j}u")

            # Abajo
            if i + 2 <= 6:
                if tab[i + 2][j] == "0" and tab[i + 1][j] == "1":
                    movs.append(f"{i}{j}d")

            # Izquierda
            if j - 2 >= 0:
                if tab[i][j - 2] == "0" and tab[i][j - 1] == "1":
                    movs.append(f"{i}{j}l")

            # Derecha
            if j + 2 <= 6:
                if tab[i][j + 2] == "0" and tab[i][j + 1] == "1":
                    movs.append(f"{i}{j}r")

    return movs

def numero_fichas(tab):
    n = 0
    for i in tab:
        n += i.count("1")
    return n

def hacer_movimiento(tab,mov):
    i = int(mov[0])
    j = int(mov[1])
    tab[i][j] = "0"
    match mov[2]:
        case "u":
            tab[i-2][j] = "1"
            tab[i-1][j] = "0"

        case "d":
            tab[i+2][j] = "1"
            tab[i+1][j] = "0"

        case "r":
            tab[i][j+2] = "1"
            tab[i][j+1] = "0"

        case "l":
            tab[i][j-2] = "1"
            tab[i][j-1] = "0"

def simulacion(movs):
    tab = nuevo_tablero()
    for mov in movs:
        hacer_movimiento(tab,mov)
    return tab

def historia_recursiva(his):
    nueva_his = []
    if not his:
        tab = nuevo_tablero()
        for mov in calcular_movs(tab):
            nueva_his.append([mov])
    else:
        for movs in his:
            tab = simulacion(movs)
            pos_mov = calcular_movs(tab)
            if pos_mov:
                for mov in pos_mov:
                    nueva_his.append(movs + [mov])
    return nueva_his

def main():
    his = []
    tab = nuevo_tablero()
    n = numero_fichas(tab)

    print_tablero(tab)

    for _ in range(n-1):
        his = historia_recursiva(his)

    pp(his)
    print("Soluciones encontradas: " + str(len(his)))

if __name__ == "__main__":
    main()