
import os
import shutil
import time
import requests

DATASETS = ["fhvhv"]          # options: "fhvhv", "yellow", "green"

START_YEAR = 2019
START_MONTH = 2


TARGET_TOTAL_GB = 30


OUTPUT_DIR = os.path.expanduser("~/nyc_tlc_raw")

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
TARGET_TOTAL_BYTES = TARGET_TOTAL_GB * (1024 ** 3)

REQUIRED_FREE_BYTES = int(TARGET_TOTAL_BYTES * 1.1)


def check_disk_space():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    free = shutil.disk_usage(OUTPUT_DIR).free
    free_gb = free / (1024 ** 3)
    needed_gb = REQUIRED_FREE_BYTES / (1024 ** 3)
    print(f"Free space at {OUTPUT_DIR}: {free_gb:.1f} GB "
          f"(need ~{needed_gb:.1f} GB with buffer)")
    if free < REQUIRED_FREE_BYTES:
        print("\n*** WARNING: not enough free disk space")
        resp = input("Continue anyway? [y/N] ").strip().lower()
        if resp != "y":
            raise SystemExit("Aborted — not enough disk space.")


def month_iter(year, month):
    while True:
        yield year, month
        month += 1
        if month > 12:
            month = 1
            year += 1


def download_file(url, dest_path, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            with requests.get(url, stream=True, timeout=60) as r:
                if r.status_code == 404:
                    return None  # month not published (e.g. future month)
                r.raise_for_status()
                total = 0
                with open(dest_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 1024):
                        f.write(chunk)
                        total += len(chunk)
                return total
        except requests.exceptions.RequestException as e:
            print(f"    attempt {attempt}/{max_retries} failed: {e}")
            time.sleep(3)
    return -1  # failed after retries


def main():
    check_disk_space()

    running_total = 0
    downloaded = []  # (filename, bytes)
    months = month_iter(START_YEAR, START_MONTH)

    print(f"\nTarget: {TARGET_TOTAL_GB} GB | Output dir: {OUTPUT_DIR}\n")

    while running_total < TARGET_TOTAL_BYTES:
        year, month = next(months)
        ym = f"{year}-{month:02d}"

        for ds in DATASETS:
            fname = f"{ds}_tripdata_{ym}.parquet"
            url = f"{BASE_URL}/{fname}"
            dest = os.path.join(OUTPUT_DIR, fname)

            if os.path.exists(dest):
                size = os.path.getsize(dest)
                print(f"[skip, already have] {fname} ({size / 1e6:.1f} MB)")
            else:
                print(f"[downloading] {fname} ...", end=" ", flush=True)
                size = download_file(url, dest)
                if size is None:
                    print("not published yet (404) — stopping here.")
                    running_total = TARGET_TOTAL_BYTES  # force stop
                    break
                elif size == -1:
                    print("FAILED after retries, skipping this file.")
                    continue
                else:
                    print(f"{size / 1e6:.1f} MB")

            running_total += size
            downloaded.append((fname, size))

            if running_total >= TARGET_TOTAL_BYTES:
                break

    print("\n" + "=" * 60)

    print("=" * 60)
    for fname, size in downloaded:
        print(f"  {fname:35s} {size / 1e9:6.3f} GB")
    total_gb = running_total / (1024 ** 3)
    print("-" * 60)
    print(f"  TOTAL: {len(downloaded)} files, {total_gb:.2f} GB")
    print(f"  Saved to: {OUTPUT_DIR}")
   

if __name__ == "__main__":
    main()
