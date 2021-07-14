#importing argparse module
import argparse
from argparse import ArgumentParser


if __name__ == "__main__":
    #specifying parser 
    parser = argparse.ArgumentParser()
    #argument filename
    parser.add_argument('filename', type=argparse.FileType('r'))

    arguments = parser.parse_args()

    #reading file data
    print(arguments.filename.readlines())