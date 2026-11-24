import re, sys
from collections import Counter

PAT = re.compile(r"(?:query\[\w+\]\s+|A\?\s+)(\S+)")
BATAS_PANJANG_LABEL = 15

jumlah_domain = Counter()
mencurigakan = []

with open(sys.argv[1], encoding="utf-8-sig", errors="ignore") as f:
    for baris in f:
        m = PAT.search(baris)
        if not m:
            continue
        nama = m.group(1).rstrip(".")
        bagian = nama.split(".")
        domain_induk = ".".join(bagian[-2:])
        jumlah_domain[domain_induk] += 1
        label = bagian[0]
        if len(label) > BATAS_PANJANG_LABEL and re.fullmatch(r"[0-9a-fA-F]+", label):
            mencurigakan.append((len(label), nama))

print("Jumlah query per domain induk:")
for domain, n in jumlah_domain.most_common():
    print(f"  {domain}: {n}")

print("\nQuery mencurigakan (label panjang berisi hex):")
for panjang, nama in mencurigakan:
    print(f"  panjang={panjang}  {nama}")
