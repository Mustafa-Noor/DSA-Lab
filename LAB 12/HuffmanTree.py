import heapq
from HuffmanNode import HuffmanNode

class HuffmanCodeTree:
    def __init__(self, freq_dict):
        self.root = self.build_tree(freq_dict)

    def build_tree(self, freq_dict):
        # Create a min-heap of HuffmanNode
        heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

        return heap[0] if heap else None

    def get_root(self):
        return self.root

