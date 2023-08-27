class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def get_name(self):
        return self.name

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.get_rating() for review in self.reviews)
        return total_ratings / len(self.reviews)
