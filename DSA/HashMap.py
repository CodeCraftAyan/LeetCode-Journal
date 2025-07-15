# Creating a HashMap
strawhat_hashmap = {
    "total": 10,
    "yonko_crew": True,
    "ships": {
        1: "Going Merry",
        2: "Thousand Sunny"
    },
    "chance_of_KOTP": 94.9,
    "crew": {
        "captain": "Luffy",
        "vice_captain": "Zoro",
        "navigator": "Nami",
        "sniper": "Ussop",
        "cook": "Sanji",
        "doctor": "Chopper",
        "archaeologist": "Robin",
        "shipwright": "Frankey",
        "musician": "Brook",
        "helmesman": "Jinbei" 
    }
}

# Add Values
strawhat_hashmap["current_ship"] = strawhat_hashmap["ships"][2]

# Edit Values
strawhat_hashmap["chance_of_KOTP"] = 96.8

# Access Value
print(strawhat_hashmap)
print(strawhat_hashmap.get("yonko_crew"))
print(strawhat_hashmap["crew"]["captain"])

# Delete a Key
del strawhat_hashmap["current_ship"] # or, strawhat_hashmap.pop("current_ship")

# Interate Over Keys & Values
for key, value in strawhat_hashmap.items():
    print(key, "=", value)
