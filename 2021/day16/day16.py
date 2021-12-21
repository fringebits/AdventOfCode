import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 16 *****")

    #puzzle = Puzzle("D2FE28")
    #puzzle = Puzzle("C0015000016115A2E0802F182340")
    #puzzle = Puzzle("C200B40A82")  # 1 + 3 = 3

    #lines = load_input('sample_input.txt')
    lines = load_input('input.txt')
    puzzle = Puzzle(lines[0])

    result = puzzle.ReadNextPacket()

    # part 1:
    print(f"part1: version = {puzzle.part1}")

    # part 2:
    print(f"part2: result = {result}")

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input

class Puzzle:
    def __init__(self, input):
        self.part1 = 0

        self.binary = ""
        for ch in input:
            val = int(ch,16)
            self.binary += f"{val:04b}"
        #print(f"{input} -> {self.binary}")
        # reset the read pos
        self.pos = 0

    def ReadNextPacket(self):
        # read first 3 bits (version)
        version = self.ReadBits(3)
        # print(f"Version = {version}")

        self.part1 += version

        packetType = self.ReadBits(3)
        # print(f"packetType = {packetType}")

        if packetType == 4: # literal value packet
            return self.ReadLiteralPacket()

        return self.ReadOperatorPacket(packetType)

    def ReadLiteralPacket(self):
        value = ""
        while True:
            stopBit = self.ReadBits(1)
            word = self.ReadBitsRaw(4)
            value += word
            if stopBit == 0:
                break
        # print(f"Literal = {value} = {int(value,2)}")
        return int(value,2)

    def ReadOperatorPacket(self, packetType):
        lengthType = self.ReadBits(1)
        packets = []
        if lengthType == 0:
            # next 15 bits represent total packet length
            totalLength = self.ReadBits(15)
            endPos = self.pos + totalLength
            while self.pos < endPos:
                packets.append(self.ReadNextPacket())
        else:
            # next 11 bits are number of sub-packets
            numPackets = self.ReadBits(11)
            for ii in range(numPackets):
                packets.append(self.ReadNextPacket())

        result = 0
        if packetType == 0: #sum
            result = sum(packets)
        elif packetType == 1: #prod
            result = packets[0]
            for p in packets[1:]:
                result = result * p
        elif packetType == 2: #minimum
            result = min(packets)
        elif packetType == 3: #maximum
            result = max(packets)
        elif packetType == 5: #greater than
            assert len(packets) == 2
            result = 1 if packets[0] > packets[1] else 0
        elif packetType == 6: #less than
            assert len(packets) == 2
            result = 1 if packets[0] < packets[1] else 0
        elif packetType == 7: #equality
            assert len(packets) == 2
            result = 1 if packets[0] == packets[1] else 0

        return result
        




        

    def ReadBits(self, count):
        # read some number of bits from current 'pos'
        bits = self.binary[self.pos:self.pos+count]
        self.pos += count
        return int(bits, 2)

    def ReadBitsRaw(self, count):
        # read some number of bits from current 'pos'
        bits = self.binary[self.pos:self.pos+count]
        self.pos += count
        return bits

if __name__ == "__main__":
    run()