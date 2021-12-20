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
    """
    Function moves discs from stack_1 to stack_3 using stack_2
    discs: amount of discs
    """
    if discs >= 1:
        move_disc(discs-1, stack_1, stack_3, stack_2)
        stack_3.push(stack_1.pop())
        move_disc(discs-1, stack_2, stack_1, stack_3)
        return stack_1.size(), stack_2.size(), stack_3.size()


def recur_han(discs):
    """
    Function solves Hanoi Tower recursively using above function move_disc
    discs: amount of discs
    """
    if discs <= 0:
        IndexError ("Number of discs cannot be a positive number.")
    if discs >= 1:
        for i in range(discs):
            stack_1.push(discs-i)
    return move_disc(discs, stack_1, stack_2, stack_3)


if __name__ == "__main__":
    print(recur_han(8))
