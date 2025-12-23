#Weather app
import requests

# API Details
API_KEY="1505930e29b1d8be7c72face45ebc181"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

#Function to get weather data
def get_weather(city):
    try:
        #construct request url
        url=f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code==200:
            data = response.json()
            weather= {
                "city" : data["name"],
                "Temperature": data['main']["temp"],
                "Weather":data['weather'][0]["description"],
                "Humidity": data['main']['humidity']

            }
            return weather
        elif response.status_code==404:
            return "City not found, Please check the name and try again!"
        else:
            return "Error Fetching data. Please try again later."
    
    except requests.exceptions.RequestException as e:
        return f"An error Occured: {e}"  
    
#main Program
def main():
    print("weather app")
    while True:
        city = input("\nEnter city name (or type 'exit') to quit.  ")
        if city.lower()=="exit":
            break
        result= get_weather(city)
        if isinstance(result,dict):
            print(f"\nWeather in {result['city']}: ")
            print(f"\nTemperature: {result['Temperature']}C")
            print(f"\nWeather: {result['Weather']}")
            print(f"\nHumidity: {result['Humidity']}%")
        else:
            print(result)

if __name__=="__main__":
    main()                    
   

