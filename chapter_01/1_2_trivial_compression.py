class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 #Start with sentinel
        for nuclieotide in gene.upper():
            self.bit_string <<= 2 # shift left two bits
            if nuclieotide == "A": 
                self.bit_string |= 0b00
            elif nuclieotide == "C":
                self.bit_string |= 0b01
            elif nuclieotide == "G":
                self.bit_string |= 0b10
            elif nuclieotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}")
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length()-1, 2): # sentinel
            bits: int = self.bit_string >> i & 0b11 
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: # A
                gene += "C"
            elif bits == 0b10: # A
                gene += "G"
            elif bits == 0b11: # A
                gene += "T"
            else:
                raise ValueError("invalid bits:{}".format(bits))
        return gene[::-1]
    
    def __str__(self):
        return self.decompress()
    

if __name__ == "__main__":
    from sys import getsizeof
    original: str ="TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)  # decompress
    print("original and decompressed are the same: {}".format(original ==compressed.decompress()))