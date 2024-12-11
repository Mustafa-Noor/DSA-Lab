class HuffmanCodeBook:
    def __init__(self, tree):
        self.codes = self.generate_codes(tree.get_root())

    def generate_codes(self, node, current_code="", codes=None):
        if codes is None:
            codes = {}
        if node is None:
            return codes
        if node.char is not None:  # Leaf node
            codes[node.char] = current_code
        self.generate_codes(node.left, current_code + "0", codes)
        self.generate_codes(node.right, current_code + "1", codes)
        return codes

    def encode(self, text):
        return "".join(self.codes[char] for char in text)

    def decode(self, encoded_text, tree_root):
        decoded = []
        current = tree_root

        for bit in encoded_text:
            current = current.left if bit == "0" else current.right
            if current.char is not None:  # Reached a leaf node
                decoded.append(current.char)
                current = tree_root

        return "".join(decoded)


class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __repr__(self):
        return f"HuffmanNode(char={self.char}, freq={self.freq})"



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




def test_huffman():
    # Frequency dictionary
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    print("Frequency Dictionary:", freq_dict)

    # Create Huffman Tree
    tree = HuffmanCodeTree(freq_dict)
    print("Huffman Tree Root Node:", tree.get_root())

    # Generate Codebook
    codebook = HuffmanCodeBook(tree)
    print("Generated Huffman Codes:", codebook.codes)

    # Test encoding
    text = "abcdef"
    encoded = codebook.encode(text)
    print(f"Original Text: {text}")
    print(f"Encoded Text: {encoded}")

    # Test decoding
    decoded = codebook.decode(encoded, tree.get_root())
    print(f"Decoded Text: {decoded}")

    # Assertions
    assert decoded == text
    print("Assertions Passed: Encoding and Decoding are correct.")

test_huffman()
