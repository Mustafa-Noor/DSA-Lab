import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None



def generate_huffman_codes(node, current_code="", codes={}):
    if node is None:
        return

    # If it's a leaf node, add to the codes dictionary
    if node.char is not None:
        codes[node.char] = current_code

    # Traverse the left and right children
    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)

    return codes



freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
huffman_tree_root = build_huffman_tree(freq_dict)
huffman_codes = generate_huffman_codes(huffman_tree_root)

print("Huffman Codes:", huffman_codes)
