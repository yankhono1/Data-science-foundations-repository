# assumes there is only one ticket being bought

# Define the function calculate_hotel_cost
def calculate_hotel_cost(num_nights, hotel_cost=120):  
    total_hotel_cost = num_nights * hotel_cost
    print(f"{num_nights} nights at ${hotel_cost} per night = ${total_hotel_cost}")
    return total_hotel_cost

# Define the function calculate_car_rental
def calculate_car_rental(num_days, car_rental=50):  
    car_rental_cost = num_days * car_rental
    print(f"{num_days} days at ${car_rental} per day = ${car_rental_cost}")
    return car_rental_cost
  
city_flight = input("Please enter the city you will be travelling to (Tokyo, Lagos, Paris, New York): ").capitalize()

# Dictionary containing the price of each flight
city_dict = {"Tokyo": 1100, "Lagos": 800, "Paris": 70, "New York": 250}

# Check if the entered city is valid (case-insensitive)
if city_flight.lower() in map(str.lower, city_dict.keys()):
    # Access the corresponding price value
    plane_cost = city_dict[city_flight]
    
    # Calculate the total flight price
    total_flight_price = plane_cost
    
    print(f"The flight cost to {city_flight} is: ${total_flight_price}")
    
    # Input number of nights at hotel
    num_nights = int(input("Please input the number of nights you are staying at the hotel: "))
    
    # Calculate and display the total hotel cost
    total_hotel_cost = calculate_hotel_cost(num_nights)
    
    # Input number of days for car rental
    rental_days = int(input("Please input the number of days you will be hiring a car: "))
    
    # Calculate and display the total car rental cost
    total_car_rental_cost = calculate_car_rental(rental_days)
    
    # Display total trip cost
    total_trip_cost = total_flight_price + total_hotel_cost + total_car_rental_cost
    print(f"The total trip cost is: ${total_trip_cost}")
else:
    print("Invalid city entered.")
