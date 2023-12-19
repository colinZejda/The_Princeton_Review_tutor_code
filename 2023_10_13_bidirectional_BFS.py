import time

def generate_adjacents(current, words_set):
    return {word for word in words_set if sum(w != c for w, c in zip(word, current)) == 1}

def check_adj(words_set):
    # The 'target' set is defined directly inside the function
    target = {'listee', 'listel', 'litten', 'lister', 'listed'}
    return generate_adjacents('listen', words_set) == target

def bi_bfs(start, goal, words_set):
    if start == goal:
        return [start]

    # Changed to use a set for faster membership checks
    exploredDict = {start: [start], goal: [goal]}
    mySet = set()

    while exploredDict:
        # Find the node with the shortest path
        cur = min(exploredDict, key=lambda x: len(exploredDict[x]))
        curPath = exploredDict[cur]
        origin = curPath[0]

        curAdj = generate_adjacents(cur, words_set) - mySet
        curAdj -= exploredDict.keys()

        for n in curAdj:
            if origin != exploredDict[n][0]:
                return curPath + exploredDict[n]

        mySet.update(curAdj)
        exploredDict.pop(cur)

    return None

def main():
    filename = input("Type the word file: ")
    with open(filename, "r") as file:
        # Use a set comprehension to create 'words_set'
        words_set = {word.strip() for word in file}

    if check_adj(words_set):
        initial = input("Type the starting word: ")
        goal = input("Type the goal word: ")

        cur_time = time.time()
        path = bi_bfs(initial, goal, words_set)
        if path:
            print(path)
           
