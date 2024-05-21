class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result



data_iter = Fibonacci()
for i in range(20):
    print(next(data_iter))

