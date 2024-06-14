import os



MANHATTAN_COORDINATES = {"latitude": 40.7831, "longitude": -73.9712}
BINGHAMTON_COORDINATES = {"latitude": 42.0987, "longitude": -75.9180}

# Calculate movement increments
LATITUDE_INCREMENT = (BINGHAMTON_COORDINATES['latitude'] - MANHATTAN_COORDINATES['latitude']) / 100
LONGITUDE_INCREMENT = (BINGHAMTON_COORDINATES['longitude'] - MANHATTAN_COORDINATES['longitude']) / 100