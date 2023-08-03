from itertools import combinations

def solve(wordList, target):
    res = []
    comb_wordList = combinations(wordList,2)
    for comb in comb_wordList:
        if comb[0]+comb[1] == target:
            res.append(comb)
    if len(res):
        return res
    else:
        return None

def main():
    ex = ["ab","bc","cd"]
    target = "abcd"
    print(solve(ex,target))

if __name__ == "__main__":
    main()

