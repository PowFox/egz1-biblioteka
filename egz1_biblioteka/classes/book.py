
class Book:

    def __init__(self, author: str, caption: str, year_of_release: int, genre: str) -> None:
        self.author = author
        self.caption = caption
        self.year_of_release = year_of_release
        self.genre = genre

    def __str__(self) -> str:
        return(f'{self.author}, {self.caption} ({self.year_of_release})')

    def __repr__(self) -> str:
        return(f'{self.author}, {self.caption} ([){self.year_of_release})')
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.author == other.author and
                    self.caption == other.caption and
                    self.year_of_release == other.year_of_release)
        return False

    def __hash__(self):
        return hash((self.author, self.caption, self.year_of_release))
