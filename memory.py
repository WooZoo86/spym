class Memory(object):
    def __init__(self, size):
        self.size = size
        self.memory = bytearray([0] * size)

    def read(self, addr, count):
        if addr + count > self.size:
            raise Exception('read exceeds memory bounds')
        return str(self.memory[addr:addr+count])

    def write(self, addr, buffer):
        if addr + len(buffer) > self.size:
            raise Exception('write exceeds memory bounds')
        self.memory[addr:addr+len(buffer)] = buffer

    def dump(self):
        print repr(self.memory)
