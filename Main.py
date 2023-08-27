from Restaurant import Restaurant
from Customer import Customer
from Review import Review

# Creating instances
restaurant1 = Restaurant("Chips Palace")
restaurant2 = Restaurant("Kwa Mathe Fishpoint")

customer1 = Customer("John", "kamau")
customer2 = Customer("Musyoka", "Brian")

# Creating reviews
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer1, restaurant2, 3)

# Displaying average ratings
print(f"Average rating for {restaurant1.get_name()}: {restaurant1.average_star_rating()}")
print(f"Average rating for {restaurant2.get_name()}: {restaurant2.average_star_rating()}")

# Displaying customer reviews
for customer in [customer1, customer2]:
    print(f"{customer.given_name} {customer.family_name} has reviewed:")
    for review in customer.reviews:
        print(f"- {review.get_rating()} stars for {review.get_restaurant().get_name()}")

#returning all the reviews
print("All reviews:")
for review in Review.all():
    print(f"- {review.get_customer().given_name} reviewed {review.get_restaurant().get_name()} with {review.get_rating()} stars")
