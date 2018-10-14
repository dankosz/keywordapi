class KEYWORDCLASS:
    
    def __init__(self, article, source):
        #The article we are referring to
        self.article = article
        #The source of the keyword
        self.source = source
        #The keyword
        self.word = ''
    
    # ensuring == can be used reliably
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    # ensuring != can be used reliably
    def __ne__(self, other):
        return not self.__eq__(other)
        
    
    