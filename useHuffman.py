from huffman import HuffmanCode
import sys

path = "sample.txt"

h = HuffmanCode(path)

output_path = h.compress()
print("Compressed file path: " + output_path)
