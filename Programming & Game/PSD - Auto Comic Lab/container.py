class container():
    def __init__(self, content, coor_x, coor_y):
        self.content = content
        self.coor_x = coor_x
        self.coor_y = coor_y

    def content_read(self, split:int = 2):

        text = self.content.split("TRS:", 1)[-1]
        words = text.split()
        cut_text = []

        for i in range(0, len(words), split):
            
            two_words = ' '.join(words[i:i+split])
            cut_text.append(two_words)
        
        return '\r'.join(cut_text)
    
    def coor_read(self):
        return self.coor_x, self.coor_y