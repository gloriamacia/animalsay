import sys
from animalsay.utils import say

if __name__ == "__main__":
    say(sys.argv[1] ,' '.join(sys.argv[2:]))


