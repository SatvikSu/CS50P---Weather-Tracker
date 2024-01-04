# Project title: Weather Tracker
#### Video demo: https://youtu.be/wQceZC1YIuM
#### Description:
The Weather Tracker gets its data from OpenWeatherMap API. To get this data, I first needed to make an account and get an API key (which I stored in a text file called api_key.txt in my project directory). 

To encapsulate the whole project, I created a class called City_2 (the first version was City, but I ended up deleting this and restarting because it had too many problems). The City_2 class has one important instance variable: a list called cities [], which contains the dicts that represent the data for each city. The other two instance variables are the API key and the base URL. To access the API key from its .txt file, I used the open() method and the read() method to get everything that is in the api_key.txt file.

The first method I made in the City_2 class was the __init__ method, which creates a dict representing the city the user has inputted and adds it to the cities [] list. The most important thing in this method was to get the JSON file from OpenWeatherMap. I did this using Python’s requests library: I used the requests.get().json() method on the url made by adding the user’s city at the end of the base url. This gave me a JSON file containing various weather data. The fields I was interested in were the name, temperature, “feels like”, humidity, and local time. 

To check that the city the user inputted even exists, I used a try and except clause; if the requests.get() method caused any exception, this meant that the user’s city didn’t exist, so I raised a ValueError. 

After getting all of the data in my __init__ method, I finished the method by self.add_city(self). This called a new method I made called add_city. The add_city method creates a dict representing the city the user chose, with keys of “name”, “temperature”, “feels like”, “humidity”, and “local time”. The method then appends this new city to the cities [] instance variable.

To format the local time, I created a method (outside of the class, as the final project requirements state you need at least 3 methods in the same indentation as main()) called format_time, where I turned a Unix timestamp (which is what the JSON file returned) to a formatted time like 12:00 PM. 

Next, I created the method called at the beginning of main(), which is the select_city() method. This creates an infinite loop (while True:) that asks the user to input a valid city. The method then calls the __init__ method to add the city to cities[], and will only break out of the loop if a ValueError isn’t raised (the __init__ method raises a ValueError if a city doesn’t exist). 

To print out the cities, I used the tabulate class we used earlier in CS50p. The printing of the cities [] list was handled by the method print_cities(), which gets called every time the cities [] list is updated.

In order to update the list, I made a get_action() method that lists all of the possible actions the user can do (ex. Add city, remove city) and asks for user input. I used a match - case clause here to match the user’s input with the action to be taken.

I then made a method called sort_by(), to sort the cities [] list by a certain category specified by the user. To do this, I made a method outside of the class called sort(), which uses a lambda function to sort dicts by a certain key provided as an argument to the method.

Lastly, I made a method called remove_cities() that removed a city from cities [] if the specified name was in the list. I also made a simple method called k_to_f () outside of the class, which converted the temperature provided by the JSON file (in Kelvin) to Fahrenheit.

All that was left was to create the main method. The main method calls the select_city() method, which starts up the program and asks the user to select a city. It then infinitely (while True:) calls the get_action() method, which essentially asks the user to update the cities [] list until the user stops the program.

