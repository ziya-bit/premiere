import os



shoppingword=["buy","mango","tomato","purchase","shop","bought","sell","meat","vegetables","cabbage","egg","eggs","tray","fruit","fruits"]
itemandprice={
"egg tray(1)":38000,"pineapple":7000,"miyazaki mango":4300000,"lettuce":6000,"french melon":21000,"young lamb club":32000,"imperial grade salted egg(6 eggs/one pack)":64000,"zucchini":7000
}
travel_words = [ "travel", "flight", "journey", "trip", "adventure", "vacation", "holiday", "tour", "expedition", "cruise", "getaway", "excursion", "pilgrimage", "voyage", "hiking", "trekking", "backpacking", "roadtrip", "safari", "sightseeing", "explore", "discovery", "destination", "itinerary", "transportation", "accommodation", "hotel", "hostel", "resort", "motel", "camping", "caravan", "glamping", "tent", "beach", "mountain", "city", "country", "passport", "visa", "ticket", "booking", "reservation", "check-in", "luggage", "baggage", "backpack", "suitcase", "customs", "departure", "arrival", "airport", "train", "bus", "taxi", "ride-sharing", "rental", "cruise", "ship", "boat", "ferry", "subway", "metro", "tram", "bike", "motorbike", "ride", "car", "airbnb", "bnb", "guidebook", "map", "tourist", "local", "culture", "food", "cuisine", "restaurant", "cafe", "museum", "gallery", "landmark", "monument", "historical", "art", "architecture", "souvenir", "photography", "adventure", "treasure", "exploration", "serenity", "wonders",
# Adding countries 
"Argentina", "Australia", "Austria", "Belgium", "Brazil", "Canada", "China", "Colombia", "Denmark", "Egypt", "Finland", "France", "Germany", "Greece", "India", "Indonesia", "Ireland", "Italy", "Japan", "Kenya", "Mexico", "Morocco", "Netherlands", "New Zealand", "Norway", "Peru", "Philippines", "Portugal", "Russia", "South Africa", "South Korea", "Spain", "Sweden", "Switzerland", "Thailand", "Turkey", "United Kingdom", "United States", "Vietnam",
"adventure", "globetrotter", "nomad", "journey", "pilgrim", "backpacking", "escapade", "trek", "voyage", "cruise", "fly", "sail", "wander", "roam", "jetset", "seafaring", "explorer", "scenic", "retreat", "excursion", "expedition", "touring", "safari", "jaunt", "rover", "adventurer", "sojourner", "wayfarer", "trip", "hike", "trail", "expedition", "camp", "glamping", "homestay", "eco-tourism", "city break", "staycation", "cultural trip", "culinary tour", "historic site", "natural wonder", "wildlife", "biodiversity", "urban exploration", "rural journey", "island hopping", "beach holiday", "mountain escape", "forest retreat", "desert adventure", "river cruise", "lake trip", "travel photography", "travel blog", "travel vlog", "travel writer", "digital nomad", "passport stamp", "travel insurance", "foreign currency", "exchange rate", "travel agency", "tour operator", "hotel booking", "hostel stay", "couchsurfing", "airline", "cruise line", "ferry ride", "long-haul flight", "stopover", "layover", "connecting flight", "direct flight", "first class", "business class", "economy class", "budget travel", "luxury travel", "solo travel", "group tour", "family vacation", "romantic getaway", "honeymoon", "adventure travel", "cultural tourism", "nature tourism", "wellness retreat", "spa vacation", "ski trip", "snowboarding", "surf trip", "diving holiday", "snorkeling", "scuba diving", "kayaking", "canoeing", "sailing", "fishing trip", "hunting trip", "wildlife safari", "bird watching", "stargazing", "road trip", "car rental", "motorbike rental", "bicycle tour", "hiking trail", "mountain trek", "river rafting", "hot air balloon", "helicopter ride", "paragliding", "bungee jumping", "zip lining", "adventure park", "theme park", "water park", "aquarium", "zoo", "botanical garden", "national park", "marine park", "wildlife reserve", "natural reserve", "heritage site", "UNESCO site", "cultural heritage", "historical landmark", "archaeological site", "museum visit", "gallery tour", "art exhibition", "music festival", "food festival", "wine tasting", "beer tasting", "cultural festival", "street market", "night market", "shopping spree", "boutique shopping", "souvenir shopping", "local craft", "handmade goods", "traditional art", "street performance", "live music", "theater show", "dance performance", "cooking class", "language class", "guided tour", "self-guided tour", "walking tour", "bike tour", "segway tour", "boat tour", "river tour", "lake tour", "island tour", "city tour", "countryside tour", "nature tour", "wildlife tour", "adventure tour", "cultural tour", "historical tour", "scenic tour", "photo tour", "food tour", "drink tour", "local guide", "travel app", "travel blog", "travel tips", "travel advice", "travel hacks", "travel gear", "packing list", "travel essentials", "travel accessories", "travel kit", "first aid kit", "travel journal", "travel diary", "travel planner", "trip itinerary", "travel itinerary", "route planner", "map", "navigation", "GPS", "compass", "travel buddy", "travel companion", "solo traveler", "group traveler", "family traveler", "couple traveler", "business traveler", "luxury traveler", "budget traveler", "backpacker", "holidaymaker", "jetsetter", "globetrotter", "explorer", "adventurer", "wayfarer", "roamer", "wanderer", "seafarer", "pilgrim", "nomad", "migrant", "expat", "settler", "native", "local", "resident", "foreigner", "visitor", "guest", "tourist", "sightseer", "excursionist", "day-tripper", "weekender", "vacationer", "holidaymaker", "traveler", "globetrotter", "nomad", "journeyer", "wayfarer", "pilgrim", "adventurer" ]

totalbelanjaan=0
totalpayment=0

   
print("'ello zis is organic shoppin center. how can i help u today?")

def respond(user_input):
    for everyword in shoppingword:
        if everyword in user_input.lower():
            buy()
            return "okay. here's the catalog"
    for everyword in travel_words:
        if everyword in user_input.lower():
            flight()
            return "okay. here's the catalog"
    return "no we don't have that in here."

def flight(totalpayment=totalpayment):
    print("yalla welcom to the flight. where do you wanna go? im your travel flight agent. here's the option: ")
    travel_and_flight_prices = {
                                "Economy Class Ticket": 1500000, # IDR 
                                 "Business Class Ticket": 5000000, # IDR
                                 "First Class Ticket": 10000000, # IDR
                                 "Passport Application": 300000, # IDR
                                 "Visa Fee (Tourist)": 600000, # IDR
                                 "Travel Insurance": 250000, # IDR
                                 "Luggage (1 piece)": 1000000, # IDR
                                 "Carry-On Bag": 500000, # IDR
                                 "Hotel (per night)": 800000, # IDR
                                 "Hostel (per night)": 150000, # IDR
                                 "Airbnb (per night)": 600000, # IDR
                                 "Travel Guidebook": 200000, # IDR
                                 "Airport Transfer (taxi)": 300000, # IDR
                                 "Rental Car (per day)": 500000, # IDR
                                 "Sightseeing Tour": 700000, # IDR
                                 "Local SIM Card": 100000, # IDR
                                 "Meal at Local Restaurant": 80000, # IDR
                                 "Snack": 20000, # IDR
                                 "Beverage": 30000, # IDR
                                 "Museum Entry Fee": 100000, # IDR
                                 "Souvenirs": 150000 # IDR
                                 }
    
    num=1
    
    for i,j in travel_and_flight_prices.items():
        print(num,".",i,":",j)
        num+=1
    prodctnum=(int)(input("enter a product number: "))
    amount=int(input("how many "+str(list(travel_and_flight_prices.keys())[prodctnum-1])+" do you want to buy: "))
    print(int(list(travel_and_flight_prices.values())[prodctnum-1])*amount)
    
    totalpayment+=int(list(travel_and_flight_prices.values())[prodctnum-1])*amount
    print("your total payment: ",totalpayment)
    

def buy(totalbelanjaan=totalbelanjaan):
    numbr=1
    for i,j in itemandprice.items():
        print(numbr,".", i,":",j)
        numbr+=1
    prodctnum=(int)(input("enter a number from one to eight: "))
    amount=int(input("how many "+str(list(itemandprice.keys())[prodctnum-1])+" do you want to buy: "))
    print(int(list(itemandprice.values())[prodctnum-1])*amount)
    
    totalbelanjaan+=int(list(itemandprice.values())[prodctnum-1])*amount
    print("your total payment: ",totalbelanjaan)
    
    askfoormore=input("wanna buy more?y/n ")
    if askfoormore=="y":
        buy(totalbelanjaan)
    else:
        print("no or other than yes, you're out. sorry.")
        
    


user_input = input("wathcu want? ")
response = respond(user_input)
print(response)



os.system("pause")
