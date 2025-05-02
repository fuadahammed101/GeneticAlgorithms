import random

class NQueensGA:
    def __init__(self, n):
        self.n = n
        self.pop_size = 50
        self.gen_limit = 500
        self.mut_rate = 0.1
        self.population = []

    def make_individual(self):
        arr = list(range(self.n))
        random.shuffle(arr)
        return arr

    def make_population(self):
        self.population = []
        for _ in range(self.pop_size):
            self.population.append(self.make_individual())

    def fitness(self, ind):
        attacks = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if abs(ind[i] - ind[j]) == abs(i - j):
                    attacks += 1
        max_pairs = (self.n * (self.n - 1)) // 2
        return max_pairs - attacks

    def select(self):
        selected = []
        for _ in range(self.pop_size):
            tour = random.sample(self.population, 3)
            fit_vals = [self.fitness(x) for x in tour]
            winner = tour[fit_vals.index(max(fit_vals))]
            selected.append(winner)
        return selected

    def crossover(self, p1, p2):
        start = random.randint(0, self.n - 2)
        end = random.randint(start + 1, self.n - 1)
        child = [None] * self.n
        for i in range(start, end + 1):
            child[i] = p1[i]
        pos = (end + 1) % self.n
        for i in range(self.n):
            c = p2[(end + 1 + i) % self.n]
            if c not in child:
                child[pos] = c
                pos = (pos + 1) % self.n
        return child

    def mutate(self, ind):
        if random.random() < self.mut_rate:
            i, j = random.sample(range(self.n), 2)
            ind[i], ind[j] = ind[j], ind[i]

    def run(self):
        self.make_population()
        max_fit = (self.n * (self.n - 1)) // 2
        for gen in range(self.gen_limit):
            self.population = self.select()
            next_gen = []
            for i in range(0, self.pop_size, 2):
                p1 = self.population[i]
                p2 = self.population[(i+1) % self.pop_size]
                c1 = self.crossover(p1, p2)
                c2 = self.crossover(p2, p1)
                self.mutate(c1)
                self.mutate(c2)
                next_gen.append(c1)
                next_gen.append(c2)
            self.population = next_gen[:self.pop_size]
            best = max(self.population, key=self.fitness)
            best_fit = self.fitness(best)
            if best_fit == max_fit:
                print("Solution found at generation", gen)
                self.print_board(best)
                return best
        print("No solution found")
        return None

    def print_board(self, ind):
        for r in range(self.n):
            line = ""
            for c in range(self.n):
                if ind[c] == r:
                    line += "Q "
                else:
                    line += ". "
            print(line)

if __name__ == "__main__":
    n = 8
    game = NQueensGA(n)
    game.run()
