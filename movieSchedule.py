schedule = {'Kaantara': '11:00AM',
          'Leo': '2:00PM',
          'PS2': '5:00PM'}
print('We are showing the following movies')
for key in schedule:
    print(key)

movie = input("What is the movie that you want to check?\n")

if schedule.get(movie):
    print('The schedule for the movie is', schedule.get(movie))
else:
    print('The movie that you are looking isnt availalble!')    
