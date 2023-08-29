# Customers Reviews on Restaurants
## Author
### BETT AYUB
## Project Description:

This is a coding challenge where we're creating something similar to Yelp. There are three main things we're working with: Restaurants, Customers, and Reviews. The main goal is to connect these things together and make them work using different methods.

## Content Outline
Introduction
Getting Started
Usage
Class Descriptions
Dependencies
Contributing
License
Introduction

In this project, we construct a basic model for a system that handles restaurant reviews. The primary categories are:

Customer: Represents an individual who can compose reviews.
Restaurant: Represents an eatery open to receiving reviews.
Review: Represents a write-up penned by a customer regarding a restaurant.
Each of these categories possesses distinct characteristics and functions meant to generate, oversee, and engage with examples.

## Technologies Used
* Python: Python is a popular high-level programming language known for its simplicity, readability, and versatility.
Installation
To get started with Toy Problem, follow these steps:

Clone the repository to your local machine using the following command:

https://github.com/bettayub/Restaurants_with_pythonNavigate to the project directory:
    

* cd Restaurant
Install the required dependencies:

* pipenv --python 3.10

* pipenv install

* pipenv shell
Usage
The project showcases the process of creating connections between different classes, generating examples of those classes, and utilizing the provided functions to engage with these examples.

Class Descriptions
Customer
* Represents a customer.
* Attributes:
    - given_name: The customer's given name.
    - family_name: The customer's family name.
    - reviews: A list of reviews written by the customer.
* Methods:
    - get_given_name(): Get the customer's given name.
    - get_family_name(): Get the customer's family name.
    - full_name(): Get the full name of the customer.
    - add_review(review): Associate a review with this customer.
    - get_reviews(): Get all reviews associated with this customer.
Restaurant
* Represents a restaurant.
* Attributes:
    - restaurant_name: The name of the restaurant.
    - restaurant_reviews: A list of reviews received by the restaurant.
* Methods:
    - get_name(): Get the restaurant's name.
    - add_review(review): Associate a review with this restaurant.
    - get_reviews(): Get all reviews associated with this restaurant.
    - get_customers(): Get all customers who reviewed this restaurant.
    - average_star_rating(): Calculate the average star rating of the restaurant.
Review
- Represents a review.
- Attributes:
    - customer: The customer who wrote the review.
    - restaurant: The restaurant being reviewed.
    - rating: The rating given in the review.
* Methods:
    - get_rating(): Get the rating of the review.
    - get_customer(): Get the customer associated with the review.
    - get_restaurant(): Get the restaurant associated with the review.
Dependencies
* Python 3.9 or higher is recommended for this program as it was developed in version 3.8 but should work on any newer
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests

# License
MIT License

Copyright (c) 2023 BETT AYUB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,