def group_anagrams(words):
    result = {}
    for word in words:
        key = hasher(word)
        if key not in result:
            result[key] = [word]
        else:
            result[key].append(word)
    return list(result.values())

def hasher(word):
    return ''.join(sorted(word))

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))