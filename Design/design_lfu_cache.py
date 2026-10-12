class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.frequency = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self._size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def pop_tail(self) -> Node:
        if self._size == 0:
            return None
        lru_node = self.tail.prev
        self.remove(lru_node)
        return lru_node

    def __len__(self) -> int:
        return self._size


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}    
        self.freq_to_dll = {}   

    def _update_frequency(self, node: Node) -> None:
        old_freq = node.frequency
        self.freq_to_dll[old_freq].remove(node)

        if self.min_freq == old_freq and len(self.freq_to_dll[old_freq]) == 0:
            self.min_freq += 1

        node.frequency += 1
        new_freq = node.frequency

        if new_freq not in self.freq_to_dll:
            self.freq_to_dll[new_freq] = DoublyLinkedList()

        self.freq_to_dll[new_freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_frequency(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                evicted = self.freq_to_dll[self.min_freq].pop_tail()
                del self.key_to_node[evicted.key]

            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.min_freq = 1

            if 1 not in self.freq_to_dll:
                self.freq_to_dll[1] = DoublyLinkedList()
            self.freq_to_dll[1].add_to_head(new_node)