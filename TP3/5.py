class Hanoi():
    def __init__(self, n):
        self.n = n
        self.tours = [[], [], []]
        for i in range(n, 0, -1):
            self.tours[0].append(i)
        
    def show(self):
        print(self.tours)

    def rec_move(self, n, depart, arrivee, aux):
        if n != 0:
            self.rec_move(n-1, depart, aux, arrivee)
            print(f"Déplacer le disque {n} du pillier {depart} vers le pillier {arrivee}")
            self.tours[arrivee].append(self.tours[depart].pop())
            self.show()
            self.rec_move(n-1, aux, arrivee, depart)
    
    def solve(self):
        self.show()
        self.rec_move(self.n, 0, 2, 1)


if __name__ == "__main__":
    hanoi = Hanoi(3)
    hanoi.solve()
