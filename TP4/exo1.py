def tri_selection(tableau):
    for i in range(len(tableau)):
        min = i
        for j in range(i+1, len(tableau)):
            if tableau[j] < tableau[min]:
                min = j
        tableau[i], tableau[min] = tableau[min], tableau[i]
    return tableau


if __name__ == "__main__":
    print(tri_selection([1,4,5,2,3,6,10]))
    