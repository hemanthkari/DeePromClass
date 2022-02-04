import time, random, sys

seq_len = int(sys.argv[1])
seq = {
    150: "",
    80: "80", 
    300: "300",
}
if seq_len not in seq:
    sys.exit(1)
with open(f"pdata{seq[seq_len]}.fasta") as fl:
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
    tmp = "1" + "".join(tmp)
    if "N" not in tmp:
        out.append(tmp)

with open(f"ndata{seq[seq_len]}.fasta") as fl:
    data =  fl.read().split("\n")
i = 0
while i < len(data):
    tmp = []
    if data[i].startswith(">"):
        while i < len(data) - 1 and not data[i+1].startswith(">"):
            tmp.append(data[i+1])
            i += 1
    i += 1
    tmp = "0" + "".join(tmp)
    if "N" not in tmp:
        out.append(tmp)

random.shuffle(out)
random.shuffle(out)
random.shuffle(out)
random.shuffle(out)
random.shuffle(out)
with open(f"train_data{seq[seq_len]}.csv", "w+") as fl:
    fl.write("\n".join([ ",".join([ __ for __ in _]) for _ in out]).replace("A", "0").replace("T", "1").replace("G", "2").replace("C", "3"))

print(f"Execution Time = {time.perf_counter() - st}")