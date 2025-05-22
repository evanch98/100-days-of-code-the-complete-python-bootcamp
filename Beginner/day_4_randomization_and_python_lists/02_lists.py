fruits = ["Cherry", "Apple", "Pear"]

states_of_america = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee","Texas","Utah",
    "Vermont", "Virginia","Washington"
]

print(states_of_america)

states_of_america.append("West Virginia")

print(states_of_america)

states_of_america.extend(["Wisconsin","Wyoming"])

print(states_of_america)
print(len(states_of_america))
