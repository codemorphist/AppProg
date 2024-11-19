import os
from utils import sizeof_fmt
from typing import TypeAlias


ExtStat: TypeAlias = list[int, int]
ExtStats: TypeAlias = dict[str, ExtStat]


def get_stats(dir: str) -> ExtStats:
    stats: ExtStats = {}
    
    for dir, _, files in os.walk(dir):
        for file in files:
            path = os.path.join(dir, file)
            size = os.path.getsize(path)
            name, ext = os.path.splitext(file)

            if ext in stats:
                stats[ext][0] += 1
                stats[ext][1] += size
            else:
                stats[ext] = [1, size]

    return stats


def stats_fmt(stats: ExtStats, out: str):
    TEMP = "| {ext:<20} | Count: {count:<10} | Total size: {size:>10} |\n"
    with open(out, "w") as f:
        for ext, stat in stats.items():
            count, total_size = stat
            if ext == "":
                ext = "other"
            f.write(TEMP.format(ext=ext, 
                                count=count, 
                                size=sizeof_fmt(total_size)))



if __name__ == "__main__":
    dir = "./dir4/"
    stats = get_stats(dir)
    stats_fmt(stats, "t22_14_result.txt")
