class HashTableChaining:
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
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        if self.size / self.capacity > 0.75:
            self._resize()

        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return default

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def contains(self, key):
        return self.get(key, default=None) is not None

    def __len__(self):
        return self.size

    def __repr__(self):
        pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                pairs.append(f"{k}: {v}")
        return "{" + ", ".join(pairs) + "}"


if __name__ == "__main__":
    ht = HashTableChaining()
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
