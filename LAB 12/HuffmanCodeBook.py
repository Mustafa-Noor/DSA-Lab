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