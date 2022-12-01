#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    """print all names defined by hidden_4 module"""
    for name in dir(hidden_4):
        if "__" not in name:
            print(name)
