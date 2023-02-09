class Bucket:
    # initialize the bucket here
    def __init__(self):
        # store (key, value) tuple where keys all map to same hash key
        self.bucket = []

    # get the value from the bucket
    def get(self, key: int) -> int:
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    # update the value associated from the bucket
    # if the key is not existed in the bucket, add it to the bucket. Otheerwise, update its value
    def update(self, key: int, value: int) -> None:
        found = False
        for index, kv in enumerate(self.bucket):
            if key == kv[0]:  # found the key
                self.bucket[index] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    # Remove the (key, value) from the bucket
    def remove(self, key: int) -> None:
        for index, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[index]
                return


class MyHashMap:

    """
    Some questions we should ask before proceeding to solve this problem:
        - Can I use linear chaining to handle hash collions?
        - What is hash collison? That's when two or different keys mapping to a same hash key
        - Can I assume the key is integer?

    """

    def __init__(self):
        self.capacity = 2069  # choose a large prime number to avoid hash collision
        self.bucket = [Bucket() for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        if key is None or value is None:
            return
        hash_key = key % self.capacity
        # put the (key, value) to its associated hash key
        self.bucket[hash_key].update(key, value)

    def get(self, key: int) -> int:
        if key is None:
            return -1
        hash_key = key % self.capacity
        return self.bucket[hash_key].get(key)

    def remove(self, key: int) -> None:
        if key is None:
            return
        hash_key = key % self.capacity
        self.bucket[hash_key].remove(key)

    # time: O(N / K) where K is predefined capacity (2069 in my case), N is the number of possible keys. This TC applies for all methods
    # space: O(K + M), where M is the number of unique keys inserted into our map


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
