from re import S
from typing import List
from math import log2, log10, log

events: List[float] = [0.3, 0.5, 0.2]
events2: List[float] = [0.9, 0.1, 0.0]
entropy2: float = 0


def inf(v: float) -> float:
    return - (v * log2(v))


shannon: List[float] = [1/7, 1/7, 1/7, 3/7, 1/7]
entropy: float = 0

for event in shannon:
    if event != 0:
        entropy += inf(event)

print(round(entropy, 2))  # 2.13 bits


for event in events2:
    if event != 0:
        entropy2 += inf(event)

print(round(entropy2, 2))  # 0.33
