# Dictionary
programming_dict = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  123: "Call out this number repeatedly.",
}
# Retrieving values from dictionary   
# print(programming_dict["Bug"])
# Adding new item to dictionary
programming_dict["Loop"] = "The action of doing something over and over again."


# Create an empty dictionary or make a dictionary empty
empty_dict = {} 
# programming_dict = {}

# Edit an item in your dictionary
programming_dict["Bug"] = "A moth in your computer."
# print(programming_dict)

# Loop through a dictionary
for key in programming_dict:
  print(key)
  print(programming_dict[key])

# Exercise 1: Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] > 70:
    student_grades[student] = "Acceptable"
  elif student_scores[student] <= 70:
    student_grades[student] = "Fail"
  else:
    student_grades[student] = "Not Graded"
print(student_grades)

# Nesting Dictionary in Dictionary
travel_log = {
  "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "Total_visits": 12},
  "Germany": {"Cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "Total_visits": 5}
}

# Nesting List in Dictionary
travelling_log = [
  {
    "Country": "France",
    "Cities_visited": ["Paris", "Lille", "Dijon"],
    "Total_visits": 12
  }, 
  {
    "Country": "Germany",
    "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "Total_visits": 5
  }
]


# Exercise 2: Dictionary in List
travel_log = [
  {
    "Country": "France",
    "Visits": 12,
    "Cities": ["Paris", "Lille", "Dijon"]
  }, 
  {
    "Country": "Germany",
    "Visits": 5,
    "Cities": ["Berlin", "Hamburg", "Stuttgart"]
  }
]
def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["Country"] = country_visited
  new_country["Visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

## Project: Blind Auction
from replit import clear
from art import logo_gavel
print(logo_gavel)
print("Welcome to the blind aution program.")
is_auction_ongoing = True
auction = {}

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = ""
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
    
while is_auction_ongoing:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  auction[name] = price
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == "yes":
    clear()
    is_auction_ongoing = True
  elif other_bidders == "no":
    is_auction_ongoing = False
    highest_bidder(auction)