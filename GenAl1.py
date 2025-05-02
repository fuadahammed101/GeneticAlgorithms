import random

class ProductGA:
    def __init__(self, target, length):
        self.target = target
        self.length = length
        self.population_size = 50
        self.generations = 500
        self.mutation_rate = 0.1
        self.population = []

    def create_individual(self):
        # Create a list of random numbers between 0 and 9
        return [random.randint(0, 9) for _ in range(self.length)]

    def create_population(self):
        self.population = [self.create_individual() for _ in range(self.population_size)]

    def fitness(self, individual):
        product = 1
        for num in individual:
            product *= num if num != 0 else 1  # treat 0 as 1 to avoid zero product
        # Fitness is higher when product is closer to target
        return -abs(self.target - product)

    def select(self):
        selected = []
        for _ in range(self.population_size):
            tournament = random.sample(self.population, 3)
            tournament_fitness = [self.fitness(ind) for ind in tournament]
            winner = tournament[tournament_fitness.index(max(tournament_fitness))]
            selected.append(winner)
        return selected

    def crossover(self, parent1, parent2):
        point = random.randint(1, self.length - 1)
        child = parent1[:point] + parent2[point:]
        return child

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            idx = random.randint(0, self.length - 1)
            individual[idx] = random.randint(0, 9)

    def run(self):
        self.create_population()
        for gen in range(self.generations):
            self.population = self.select()
            next_gen = []
            for i in range(0, self.population_size, 2):
                p1 = self.population[i]
                p2 = self.population[(i+1) % self.population_size]
                c1 = self.crossover(p1, p2)
                c2 = self.crossover(p2, p1)
                self.mutate(c1)
                self.mutate(c2)
                next_gen.append(c1)
                next_gen.append(c2)
            self.population = next_gen[:self.population_size]

            best = max(self.population, key=self.fitness)
            best_fit = self.fitness(best)
            if best_fit == 0:
                print(f"Solution found at generation {gen}:")
                print(" ".join(map(str, best)))
                return best
        print("No exact solution found.")
        best = max(self.population, key=self.fitness)
        print("Best solution found:")
        print(" ".join(map(str, best)))
        return best

if __name__ == "__main__":
    T = int(input("Enter the target integer T: "))
    k = int(input("Enter the length k of the list: "))
    ga = ProductGA(T, k)
    ga.run()
