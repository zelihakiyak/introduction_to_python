class Movie:
    def __init__(self, title, director, duration):
        self.title =title
        self.director=director
        self.duration=duration
        print("movie objesi olusturukdu.")
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print ("film objesi silindi")
        
m=Movie("film adi","yonetmen adi", 120)
print(m)
del m
print(m)