import tkinter as tk
import requests
import json

# Yelp API Key (Replace with your actual Yelp API Key)
API_KEY = 'PJTkJ9KrjZxFs0uxvoELgdKI6-ERd9XliyPe6I2ILBEi3hDtRzPToRgUhvljRhD88OnZKny6TH7PJOUw4Zt-egNBxOOyhdLhuLKfVehPBTsGDjsPlBdsygw5oM0tZXYx'

# Function to search for halal restaurants nearby
def find_halal_restaurants():
    location = location_entry.get()
    term = "halal"
    
    # Make a request to the Yelp Fusion API
    url = f'https://api.yelp.com/v3/businesses/search?term={term}&location={location}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        display_results(data['businesses'])
    else:
        result_label.config(text="Error: Unable to fetch data")

# Function to display search results
def display_results(restaurants):
    result_text = ""
    for restaurant in restaurants:
        result_text += f"Name: {restaurant['name']}\n"
        result_text += f"Rating: {restaurant['rating']}\n"
        result_text += f"Address: {restaurant['location']['address1']}\n"
        result_text += "\n"
    result_label.config(text=result_text)

# Create the main application window
app = tk.Tk()
app.title("Halal Restaurant Finder")

# Create and place widgets in the window
location_label = tk.Label(app, text="Enter Location:")
location_label.pack()
location_entry = tk.Entry(app)
location_entry.pack()

find_button = tk.Button(app, text="Find Halal Restaurants", command=find_halal_restaurants)
find_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
