class Solution:
    def sortSentence(self, s: str) -> str:
        wordslist = s.split(" ")
        sentence = ["" for w in wordslist]
        for word in wordslist:
            i = int(word[len(word) - 1]) - 1
            w = word[:len(word) - 1]
            sentence[i] = w
            
        return " ".join(sentence)
