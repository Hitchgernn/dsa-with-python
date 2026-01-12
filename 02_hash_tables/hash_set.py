class HashSet:
    def __init__(self, capacity=8):
        self.capacity = max(1, capacity)
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key in bucket:
                self.add(key)

    def add(self, key):
        if self.size / self.capacity > 0.75:
            self._resize()

        index = self._hash(key)
        bucket = self.buckets[index]
        if key in bucket:
            return
        bucket.append(key)
        self.size += 1

    def contains(self, key):
        index = self._hash(key)
        return key in self.buckets[index]

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, k in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return "{" + ", ".join(str(item) for item in items) + "}"


if __name__ == "__main__":
    hs = HashSet()
    hs.add("apple")
    hs.add("banana")
    hs.add("orange")
    hs.add("apple")

    print("contains apple:", hs.contains("apple"))
    print("contains grape:", hs.contains("grape"))
    print("set:", hs)

    hs.remove("banana")
    print("after removing banana:", hs)
