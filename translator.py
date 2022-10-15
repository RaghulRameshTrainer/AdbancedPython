class Englishtotamil:
    def __init__(self):
        self.words={'car':'vehicle',
                    'fridge':'cooler',
                    'coctail':'bird'}
        
    def translate(self,word):
        return self.words.get(word,'Not Exists')


class Englishtochinese:
    def __init__(self):
        self.words = {'car': 'rac',
                      'fridge': 'egdirf',
                      'coctail': 'liatcoc'}

    def translate(self, word):
        return self.words.get(word, 'Not Exists')


class Englishtogerman:
    def __init__(self):
        self.words = {'car': 'ca',
                      'fridge': 'fr',
                      'coctail': 'co'}

    def translate(self, word):
        return self.words.get(word, 'Not Exists')

def Factory(language="Chinese"):
    lang={
        "Chinese":Englishtochinese,
        "Tamil":Englishtotamil,
        "Germen":Englishtogerman,
        "Hindi":Englishtogerman,
        "Japanese":Englishtogerman
    }
    return lang[language]()

if __name__=="__main__":
    c=Factory("Chinese")
    t=Factory("Tamil")
    g=Factory("Germen")

    data=['car','mouse','fridge']

    for w in data:
        print("TAMIL:",t.translate(w))
        print("CHINESE:", c.translate(w))
        print("GERMEN:", g.translate(w))