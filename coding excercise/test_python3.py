#!/usr/bin/env python

import sys
import os


def main(name):
    """
    Print Hello {name}!!! string
    name: string
    :rtype: None
    """
    print("Hello {}!".format(name))


if __name__ == "__main__":
    main(sys.argv[1])
