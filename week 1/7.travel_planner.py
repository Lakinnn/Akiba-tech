print ("=====Travel Information=====")

destiny = input("Enter destination: ")
distance = float(input("Enter the distance in kilometer: "))
avg_speed = float(input("Enter average speed in km/h: "))

time = distance/avg_speed

print ("="*25)
print("Travel Planner")
print ("="*25,"\n")


print (f"Destination ",destiny)
print (f"Distance: ", distance,"km")
print (f"Average Speed ", avg_speed,"km/h", "\n")

print (f"Estimated travel time:  ", time, "hrs")
 #bonus
minute = time * 60

print (f"Time in minutes: ",minute,"min")
