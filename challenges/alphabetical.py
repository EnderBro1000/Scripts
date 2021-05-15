# import tracemalloc
# tracemalloc.start()
import inspect

start = "aiemckgobjfndlhp"

def list_to_str(list):
    out = ""
    for item in list:
        out += item
    return out

def insert(str, idx, addition):
    return str[:idx] + addition + str[idx:]

def remove_duplicates(str):
    out = ""
    for letter in str:
        if out.find(letter) == -1:
            out += letter
    return out

def order_alphabet(str):
    return list_to_str(sorted(str))

def find_missing(str):
    goal = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    missing = 0
    for idx, letter in enumerate(goal):
        print(f"{len(str)} > {idx}")
        if len(str) <= idx:
            missing += 1
        out += letter
    return out, missing
        


def main():
    str = remove_duplicates(start)
    str = order_alphabet(str)
    str, missing = find_missing(str)
    print(str)
    print(missing)

print(inspect.getsourcefile(sorted))

# main()
