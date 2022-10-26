books = [
    {
        'id': 1,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'year_published': '1992'
    },
    {
        'id': 2,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin', 
        'year_published': '1973'
    },
    {
        'id': 3,
        'title': 'Dhalgren',  
        'author': 'Samuel R. Delany',
        'year_published': '1975'
    },
    {
        'id': 4,
        "title":"Speaking JavaScript",
        "author":"Axel Rauschmayer",
        "year_published":"2014"
    },
    {
        'id': 5,
        "title":"Learning JavaScript Design Patterns",
        "author":"Addy Osmani",
        "year_published":"2012"

    },
    {
        'id': 6,
        "title":"You Don't Know JS Yet",
        "author":"Kyle Simpson",
        "year_published":"2019"
    },
    {
        "title":"Pro Git",
        "author":"Scott Chacon and Ben Straub",
        "year_published":"2014",
        "id":7
    },
    {
        "title":"JavaScript: The Good Parts",
        "author":"Douglas Crockford",
        "year_published":"2008",
        "id":8
    },
    {
        "title":"Git Pocket Guide",
        "author":"Richard E. Silverman",
        "year_published":"2013",
        "id":9
    },
    {
        "id": 10,
        "title":"Rethinking Productivity in Software Engineering",
        "author":"Caitlin Sadowski, Thomas Zimmermann",
        "year_published":"2017"
    }
]

def getBooks(startYear, endYear):
    selectedBooks = []
    for book in books:
        if book['year_published'] >= startYear and book['year_published'] <= endYear:
            selectedBooks.append(book)
    return selectedBooks

if __name__ == "__main__":
    print("This is a Historical Book record (in-progress):\n")
    startYear = input("Please enter starting year for range of books you like: ")
    endYear = input("Please enter ending year for range of books you like: ")
    selectedBooks = getBooks(startYear, endYear)
    if len(selectedBooks) == 0:
        print("\nNo books found for that year range")
    else:
        print("\nBooks found for that year range:")
        for book in selectedBooks:
            print(book['title'] + " by " + book['author'] + " (" + book['year_published'] + ")")