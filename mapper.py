
class MAPPER:
    
    @staticmethod
    def mapRow(row):
        pubinf = lambda: None
        for column in (row):
            print(column)
            pubinf["column"] = row[column]
        print(pubinf)
        return pubinf