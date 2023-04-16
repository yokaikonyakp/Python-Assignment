import json

# Create a dictionary of Indian states and their capitals

indian_states = {
    "Andhra Pradesh": "Amaravati",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow"
}


# Write the dictionary into a JSON file
with open('indian_states.json', 'w') as f:
    json.dump(indian_states, f)
