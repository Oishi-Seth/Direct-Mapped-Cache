# Made by Oishi Seth- IMT2020525
# Made by V L Sahithi- IMT2020047

import math

def hexadecimalToBinary(n):
    return str("{0:08b}".format(int(n, 16)).zfill(32))

def binaryToDecimal(n):
    return int(n, 2)

def getIndex(address, lines, block_size):
    index_size = int(math.log2(lines))
    offset_size = int(math.log2(block_size))
    return address[32 - index_size - offset_size : 32 - offset_size]

def getTag(address, lines, block_size):
    index_size = int(math.log2(lines))
    offset_size = int(math.log2(block_size))
    tag_size = 32 - index_size - offset_size
    return address[0: tag_size]

def hitRate(hits, count):
    return "{0: .8f}".format(hits/count)

def missRate(miss, count):
    return "{0: .8f}".format(miss/count)

def hit_by_miss(hits, count):
    return "{0: .8f}".format(hits/miss)


print("Enter cache_size in kB:")
cache_size = int(input())

print("Enter block size in bytes: ")
block_size = int(input())

lines = cache_size * 1024 // block_size
print("Number of lines in cache is: " + str(lines))
print("\n")

hits = 0
miss = 0
count = 0
valid = []
for i in range(lines):
    valid.append(0)

tags = []
for i in range(lines):
    tags.append(-1)


files = ["gcc.trace", "gzip.trace", "mcf.trace", "swim.trace", "twolf.trace"]

for file_name in files:
    f = open(file_name, "r")
    print("Name of file is: ", f.name)
    data = f.readlines()

    for i in data:
        count += 1
        word = i.split(' ')
        address = hexadecimalToBinary(word[1][2:])
        index = binaryToDecimal(getIndex(address, lines, block_size))
        tag = getTag(address, lines, block_size)

        if valid[index] == 1:
            if tags[index] == tag:
                hits += 1
            else:
                tags[index] = tag
                miss += 1

        elif valid[index] == 0:
            valid[index] = 1
            tags[index] = tag
            miss += 1

    f.close()
    print("Hits: " + str(hits))
    print("Misses: " + str(miss))
    print("Hit ratio: " + hitRate(hits, count))
    print("Miss ratio: " + missRate(miss, count))
    print("Hits/Misses: " + hit_by_miss(hits, miss))
    print("\n")
