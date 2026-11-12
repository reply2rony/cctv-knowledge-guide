#!/usr/bin/env python3
"""Starter learning template: estimate CCTV storage needs.

Usage:
    python3 scripts/storage-estimate.py --cameras 8 --bitrate 4 --hours 24 --days 30
    python3 scripts/storage-estimate.py --cameras 4 --bitrate 2 --hours 12 --days 14

Estimates storage from camera count, bitrate (Mbps per camera),
hours recorded per day, and retention days. Sample numbers only;
it is not a production tool. Always check the recorder's own
calculator or the vendor's guidance for a real system.
"""
import argparse


def estimate_gb(cameras, bitrate_mbps, hours_per_day, days):
    # Mbps -> MB per second: divide by 8. Then seconds per day,
    # times days, times cameras, converted to GB.
    mb_per_second = bitrate_mbps / 8.0
    total_mb = mb_per_second * 3600 * hours_per_day * days * cameras
    return total_mb / 1024.0


def main():
    ap = argparse.ArgumentParser(description="Estimate CCTV storage needs.")
    ap.add_argument("--cameras", type=int, required=True, help="number of cameras")
    ap.add_argument("--bitrate", type=float, required=True,
                    help="bitrate per camera in Mbps (e.g. 4)")
    ap.add_argument("--hours", type=float, default=24,
                    help="hours recorded per day (default 24)")
    ap.add_argument("--days", type=int, required=True,
                    help="retention days (e.g. 30)")
    args = ap.parse_args()

    if args.cameras <= 0 or args.bitrate <= 0 or args.days <= 0:
        print("cameras, bitrate and days must all be greater than 0.")
        raise SystemExit(1)
    if not 0 < args.hours <= 24:
        print("hours must be between 0 and 24.")
        raise SystemExit(1)

    gb = estimate_gb(args.cameras, args.bitrate, args.hours, args.days)
    tb = gb / 1024.0
    print(f"Cameras: {args.cameras}")
    print(f"Bitrate per camera: {args.bitrate} Mbps")
    print(f"Hours recorded per day: {args.hours}")
    print(f"Retention: {args.days} days")
    print(f"Estimated storage: {gb:.1f} GB ({tb:.2f} TB)")
    print()
    print("Notes:")
    print("  - This is a raw estimate before filesystem and recorder overhead.")
    print("  - Motion-only recording or fewer hours per day lowers this a lot.")
    print("  - Doubling the cameras doubles the storage; halving the hours halves it.")


if __name__ == "__main__":
    main()
