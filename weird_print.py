class MultiPrinter:
    def __init__(self, count, message):
        self.count = count
        self.message = message

    def display(self):
        for i in range(self.count):
            print(i + 1, self.message)

    def stringify(self):
        return '\n'.join([self.message] * self.count)

weird_printers = []
for i in range(5):
    mp = MultiPrinter(i, f"number {i}")
    weird_printers.append(mp)

print(weird_printers)
weird_printers[0].display()
weird_printers[2].display()
print(weird_printers[3].stringify())