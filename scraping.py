import wikipedia
from database import insertIntoTable

#classes = "ballon flower flower"

class scrapper:
    def scrap(self,classe):
        try:
            pred = classe+" flower"
            result = wikipedia.summary(pred,sentences=5)
            return result
        except Exception as e:
            insertIntoTable(str(type(e).__name__) + str(__file__))
            return [{"image": str(e)}]


