class HashTableOpenAddressing:
    def __init__(self, capacity=8):
        self.capacity = max(1, capacity)
        self.size = 0
        self.table = [None] * self.capacity
        self._deleted = object()

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for entry in old_table:
            if entry is None or entry is self._deleted:
                continue
            key, value = entry
            self.put(key, value)

    def put(self, key, value):
        if self.size / self.capacity > 0.6:
            self._resize()

        index = self._hash(key)
        first_deleted = None

        for _ in range(self.capacity):
            entry = self.table[index]
            if entry is None:
                target = first_deleted if first_deleted is not None else index
                self.table[target] = (key, value)
                self.size += 1
                return
            if entry is self._deleted:
                if first_deleted is None:
                    first_deleted = index
            else:
                k, _ = entry
                if k == key:
                    self.table[index] = (key, value)
                    return
            index = (index + 1) % self.capacity

    def get(self, key, default=None):
        index = self._hash(key)
        for _ in range(self.capacity):
            entry = self.table[index]
            if entry is None:
                return default
            if entry is not self._deleted:
                k, v = entry
                if k == key:
                    return v
            index = (index + 1) % self.capacity
        return default

    def remove(self, key):
        index = self._hash(key)
        for _ in range(self.capacity):
            entry = self.table[index]
            if entry is None:
                return False
            if entry is not self._deleted:
                k, _ = entry
                if k == key:
                    self.table[index] = self._deleted
                    self.size -= 1
                    return True
            index = (index + 1) % self.capacity
        return False

    def contains(self, key):
        return self.get(key, default=None) is not None

    def __len__(self):
        return self.size

    def __repr__(self):
        pairs = []
        for entry in self.table:
            if entry is None or entry is self._deleted:
                continue
            k, v = entry
            pairs.append(f"{k}: {v}")
        return "{" + ", ".join(pairs) + "}"


if __name__ == "__main__":
    ht = HashTableOpenAddressing()
    ht.put("apple", 3)
    ht.put("banana", 5)
    ht.put("orange", 2)

    print("apple:", ht.get("apple"))
    print("banana:", ht.get("banana"))
    print("grape:", ht.get("grape", "not found"))

    ht.put("apple", 10)
    print("updated apple:", ht.get("apple"))

    ht.remove("banana")
    print("after removing banana:", ht)
