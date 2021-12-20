class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


stack_1 = Stack()
stack_2 = Stack()
stack_3 = Stack()

def move_disc(discs, stack_1, stack_2, stack_3):
    """Argumenty(4): discs- liczba dysków, stack_1 - stos początkowy, stack_2 - stos pomocniczy, stack_3 - stos końcowy
    Funkcja przekłada dyski ze stosu stack_1 na stos 3, tak aby dyski wieksze nie mogły leżeć na dyskach mniejszych."""
    if discs >= 1:
        move_disc(discs-1, stack_1, stack_3, stack_2)
        stack_3.push(stack_1.pop())
        move_disc(discs-1, stack_2, stack_1, stack_3)
        return(stack_1.size(), stack_2.size(), stack_3.size())

def fun(discs):
    """Argumenty(1): discs- liczba dysków
    Funkcja rozwiązuje problem wieży Hanoi rekurencyjnie. Wykorzystuje powyższą funkcję move_disc."""
    if discs <= 0:
        IndexError ("Number of discs cannot be a positive number.")
    if discs >= 1:
        for i in range(discs):
            stack_1.push(discs-i)
    return move_disc(discs, stack_1, stack_2, stack_3)

if __name__ == "__main__":
    print(fun(8))