import os
import json
import time
import logging
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()]
)


def get_directory_snapshot(directory_path):
    snapshot = []
    for root, dirs, files in os.walk(directory_path):
        for name in dirs + files:
            path = os.path.join(root, name)
            modified_time = os.path.getmtime(path)
            snapshot.append({
                "name": path,
                "modified": modified_time
            })
    return snapshot


def save_log_to_file(log_file, changes):
    if changes["new"] or changes["deleted"] or changes["modified"]:
        change_log = {
            "timestamp": datetime.now().isoformat(),
            "changes": changes
        }

        json.dump(change_log, log_file, indent=4)
        log_file.write("\n")


def compare_snapshots(old_snapshot, new_snapshot):
    old_files = {item["name"]: item["modified"] for item in old_snapshot}
    new_files = {item["name"]: item["modified"] for item in new_snapshot}
    
    changes = {"new": [], "deleted": [], "modified": []}

    for path, modified in new_files.items():
        if path not in old_files:
            changes["new"].append(path)
            logging.info(f"(NEW) {datetime.fromtimestamp(modified)}: {path} was created")
        elif old_files[path] != modified:
            changes["modified"].append(path)
            logging.info(f"(MODIFIED) {datetime.fromtimestamp(modified)}: {path} was modified")

    for path in old_files:
        if path not in new_files:
            changes["deleted"].append(path)
            logging.info(f"(DELETED) {datetime.fromtimestamp(old_files[path])}: {path} was deleted")

    return changes


def monitor_directory(directory_path, log_directory, interval_seconds=1):
    initial_snapshot = get_directory_snapshot(directory_path)
    log_file = open(os.path.join(log_directory, "changes_log.json"), "a")

    while True:
        time.sleep(interval_seconds)

        new_snapshot = get_directory_snapshot(directory_path)
        changes = compare_snapshots(initial_snapshot, new_snapshot)

        save_log_to_file(log_file, changes)

        initial_snapshot = new_snapshot


if __name__ == "__main__":
    directory_path = "./dir4/"
    log_directory = "./log/"
    monitor_directory(directory_path, log_directory)

