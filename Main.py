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

