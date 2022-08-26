class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.words = s.split()
        for i in range(1,len(self.words)):
            key = int(self.words[i][-1])
            word = self.words[i]
            j = i - 1
            while j >= 0 and key < int(self.words[j][-1]):
                self.words[j+1]= self.words[j]
                j -= 1
            self.words[j+1] = word
        return ' '.join([word[:-1] for word in self.words])
                
