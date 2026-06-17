import heapq
import os
import json

class HuffmanNode:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison for the priority queue (Min-Heap)
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanZipper:
    @staticmethod
    def _build_freq_map(data):
        freq_map = {}
        for byte in data:
            freq_map[byte] = freq_map.get(byte, 0) + 1
        return freq_map

    @staticmethod
    def _build_tree(freq_map):
        heap = [HuffmanNode(b, f) for b, f in freq_map.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            
            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)
            
        return heap[0] if heap else None

    @staticmethod
    def _generate_codes(root, current_code, codes):
        if root is None:
            return
        if root.byte is not None:
            codes[root.byte] = current_code
            return
        HuffmanZipper._generate_codes(root.left, current_code + "0", codes)
        HuffmanZipper._generate_codes(root.right, current_code + "1", codes)

    @classmethod
    def compress(cls, input_path, output_path):
        with open(input_path, 'rb') as f:
            raw_data = f.read()

        if not raw_data:
            raise ValueError("Input file is empty.")

        freq_map = cls._build_freq_map(raw_data)
        root = cls._build_tree(freq_map)
        
        codes = {}
        cls._generate_codes(root, "", codes)

        # Convert text bytes into a string of bits
        bit_stream = "".join(codes[byte] for byte in raw_data)
        
        # Calculate trailing padding to fit 8-bit chunks
        padding = (8 - len(bit_stream) % 8) % 8
        bit_stream += "0" * padding

        # Pack bits into a standard byte array
        compressed_bytes = bytearray()
        for i in range(0, len(bit_stream), 8):
            compressed_bytes.append(int(bit_stream[i:i+8], 2))

        # Create metadata header using string keys for JSON compatibility
        header = {
            "padding": padding,
            "freq": {str(k): v for k, v in freq_map.items()}
        }
        header_encoded = json.dumps(header).encode('utf-8')
        header_len = len(header_encoded)

        # Write output: [Header Length (4B)] + [JSON Header Data] + [Payload]
        with open(output_path, 'wb') as f:
            f.write(header_len.to_bytes(4, byteorder='big'))
            f.write(header_encoded)
            f.write(compressed_bytes)

    @classmethod
    def decompress(cls, input_path, output_path):
        with open(input_path, 'rb') as f:
            header_len = int.from_bytes(f.read(4), byteorder='big')
            header_encoded = f.read(header_len)
            compressed_data = f.read()

        header = json.loads(header_encoded.decode('utf-8'))
        padding = header["padding"]
        freq_map = {int(k): v for k, v in header["freq"].items()}

        # Reconstruct the tree from metadata
        root = cls._build_tree(freq_map)

        # Reconstruct the original bit sequence
        bit_stream = "".join(f"{byte:08b}" for byte in compressed_data)
        if padding > 0:
            bit_stream = bit_stream[:-padding]

        # Decode the bitstream back to raw bytes using the tree
        decoded_bytes = bytearray()
        current_node = root
        for bit in bit_stream:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.byte is not None:
                decoded_bytes.append(current_node.byte)
                current_node = root

        with open(output_path, 'wb') as f:
            f.write(decoded_bytes)

# --- Execution Example ---
if __name__ == "__main__":
    # Create a dummy sample text file
    with open("sample.txt", "w") as f:
        f.write("BEEP BOOP BEER FLOOP ROOP! " * 100)

    # Execute pipeline
    HuffmanZipper.compress("sample.txt", "compressed.huff")
    HuffmanZipper.decompress("compressed.huff", "restored.txt")

    print(f"Original Size: {os.path.getsize('sample.txt')} bytes")
    print(f"Compressed Size: {os.path.getsize('compressed.huff')} bytes")
