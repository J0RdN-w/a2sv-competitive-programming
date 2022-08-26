class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.keys = []
        self.sentences = []
        for word in s.split():
            self.keys.append(word[-1])
            self.sentences.append(word[:-1])
        for i in range(1,len(self.keys)):
            key = self.keys[i]
            sentence = self.sentences[i]
            j = i - 1
            while j >= 0 and key < self.keys[j]:
                self.keys[j+1]= self.keys[j]
                self.sentences[j+1] = self.sentences[j]
                j -= 1
            self.keys[j+1] = key    
            self.sentences[j+1] = sentence 
        return ' '.join(self.sentences) 
                
