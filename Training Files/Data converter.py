import time
import random

with open("pdata.fasta") as fl:
    data =  fl.read().split("\n")

st = time.perf_counter()
out = []
i = 0
while i < len(data):
    tmp = []
    if data[i].startswith(">"):
        while i < len(data) - 1 and not data[i+1].startswith(">"):
            tmp.append(data[i+1])
            i += 1
    i += 1
    out.append("1" + "".join(tmp))

with open("ndata.fasta") as fl:
    data =  fl.read().split("\n")
i = 0
while i < len(data):
    tmp = []
    if data[i].startswith(">"):
        while i < len(data) - 1 and not data[i+1].startswith(">"):
            tmp.append(data[i+1])
            i += 1
    i += 1
    out.append("0" + "".join(tmp))


random.shuffle(out)
random.shuffle(out)
random.shuffle(out)
random.shuffle(out)
random.shuffle(out)
with open("train_data.csv", "w+") as fl:
    fl.write("\n".join([ ",".join([ __ for __ in _]) for _ in out]).replace("A", "0").replace("T", "1").replace("G", "2").replace("C", "3"))

print(f"Execution Time = {time.perf_counter() - st}")