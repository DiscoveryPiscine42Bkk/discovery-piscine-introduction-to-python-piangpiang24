#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]

    if not args:
        print("none")
        return

    suffix = "ism"
    for word in args[:-1]:
        print(f"{word}{suffix}")

if __name__ == "__main__":
    main()
