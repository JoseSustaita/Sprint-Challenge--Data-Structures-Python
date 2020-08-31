class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = 0

# Queue is empty or still has room
    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
# Queue is full
        elif len(self.storage) == self.capacity:
            self.storage[self.current] = item
            # Self.current + 1 % capacity  = 0
            self.current = (self.current + 1) % self.capacity

    def get(self):
        return self.storage
