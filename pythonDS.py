
def mergeAlternately(self, word1: str, word2: str) -> str:
    tmpStr = ""
    for i in range(max(len(word1), len(word2))):
        # tmpString += word1[i] if i < len(word1) else word2[i]
        if (len(word1) > len(word2)):
            if (i < len(word2)):
                tmpStr += word1[i]
                tmpStr += word2[i]
            else:
                tmpStr += word1[i]
        else:
            if (i < len(word1)):
                tmpStr += word1[i]
                tmpStr += word2[i]
            else:
                tmpStr += word2[i]
    
    return tmpStr


if __name__ == "__main__":
    print(mergeAlternately("abc", "defg"))

