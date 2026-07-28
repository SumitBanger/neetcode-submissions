class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        pattern2WordsMap, length = defaultdict(list), len(beginWord)
        for word in wordList:
            for index in range(length):
                pattern = word[:index] + '*' + word[index + 1:]
                pattern2WordsMap[pattern].append(word)

        Q, result, visited = deque([beginWord]), 1, set([beginWord])
        while Q:
            for i in range(len(Q)):
                word = Q.popleft()
                if word == endWord:
                    return result
                for index in range(length):
                    pattern = word[:index] + '*' + word[index + 1:]
                    for neighbor in pattern2WordsMap[pattern]:
                        if neighbor not in visited:
                            Q.append(neighbor)
                            visited.add(neighbor)
            result += 1

        print(pattern2WordsMap)
        return 0

        