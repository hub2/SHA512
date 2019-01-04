#!/usr/bin/python3

import struct, copy
from hashlib import sha512


def main():
        haszyk = sha512("abc".encode("utf-8")).hexdigest()
        print(haszyk)

if __name__ == "__main__":
        main()
