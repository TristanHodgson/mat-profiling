import subprocess
from tabulate import tabulate
import matplotlib.pyplot as plt
from tqdm import tqdm

STRATEGIES = {
    "large": [[1000, 2000, 3000, 4000, 5000], 1],
    "medium": [[i for i in range(200, 1001, 100)], 3],
    "small": [[i for i in range(10, 101, 10)], 200]
}

"""
gcc ikj.c -o ikj.out
gcc ijk.c -o ijk.out
"""


def getTime(type, n):
    if type == "ikj":
        result = subprocess.run(["./ikj.out", str(n)], stdout=subprocess.PIPE)
    elif type == "ijk":
        result = subprocess.run(["./ijk.out", str(n)], stdout=subprocess.PIPE)
    return float(result.stdout)



table_data = []

for NAME, (ns, REPEATS) in STRATEGIES.items():
    ys = []
    zs = []

    for n in tqdm(ns):
        ijkTime, ikjTime = 0, 0
        for _ in range(REPEATS):
            ijkTime += getTime("ijk", n)
            ikjTime += getTime("ikj", n)
        ijkTime /= REPEATS
        ikjTime /= REPEATS
        ys.append(ijkTime)
        zs.append(ikjTime)
        table_data.append([n, ijkTime, ikjTime])

    plt.plot(ns, ys, label="ijk", color="blue")
    plt.plot(ns, zs, label="ikj", color="red")
    plt.xlabel("Matrix Size (n)")
    plt.ylabel("Time (s)")
    plt.title("Matrix Multiplication Performance")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{NAME}.png", dpi=300, bbox_inches="tight")
    plt.close()

print(tabulate(table_data, headers=["n", "ijk (s)", "ikj (s)"], tablefmt="github"))
