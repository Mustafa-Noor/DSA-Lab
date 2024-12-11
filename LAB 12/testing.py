from HuffmanTree import HuffmanCodeTree
from HuffmanCodeBookFile import HuffmanCodeBook

def test_huffman():
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    tree = HuffmanCodeTree(freq_dict)
    codebook = HuffmanCodeBook(tree)

    # Check codes
    assert codebook.codes['f'] == '0'
    assert 'a' in codebook.codes

    # Check encoding and decoding
    text = "abcdef"
    encoded = codebook.encode(text)
    decoded = codebook.decode(encoded, tree.get_root())
    assert decoded == text

test_huffman()
print("All tests passed!")
