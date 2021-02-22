class MultiPrinter:
    def display(self, s):
        for _ in range(self.count):
            print(s)

mp = MultiPrinter()
mp.count = 3
mp.display("hello")
mp.display("goodbye")
