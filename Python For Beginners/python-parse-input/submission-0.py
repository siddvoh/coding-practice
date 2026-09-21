from typing import List

def read_integers() -> List[int]:
    ip = input().split(",")
    return [int(i) for i in ip]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
