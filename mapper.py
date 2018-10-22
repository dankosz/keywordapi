
class MAPPER:
    
    @staticmethod
    def mapRow(row):
        pubinf = lambda: None
        for column in (row):
            setattr(pubinf, column, row[column])
        return pubinf