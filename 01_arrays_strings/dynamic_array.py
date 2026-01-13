class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = max(1, capacity)
        self.size = 0
        self.data = [None] * self.capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty DynamicArray")
        value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        if self.size > 0 and self.size <= self.capacity // 4:
            self._resize(max(1, self.capacity // 2))
        return value

    def get(self, index):
        self._check_bounds(index)
        return self.data[index]

    def set(self, index, value):
        self._check_bounds(index)
        self.data[index] = value

    def _check_bounds(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")

    def __len__(self):
        return self.size

    def __repr__(self):
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"


if __name__ == "__main__":
    arr = DynamicArray()
    for num in range(1, 9):
        arr.append(num)
    print("array:", arr)
    print("len:", len(arr))

    print("pop:", arr.pop())
    print("after pop:", arr)
    arr.set(0, 99)
    print("after set:", arr)
