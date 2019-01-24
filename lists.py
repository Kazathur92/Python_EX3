planet_list = []

planet_list.append("Mercury")
planet_list.extend({"Jupiter", "Saturn"})
planet_list.insert(1, "Earth")
planet_list.insert(2, "Mars")
planet_list.insert(3, "Venus")
planet_list.append("Pluto")
# print(planet_list)
# print("Rocky Planets", planet_list[0:4])

del(planet_list[5])

# print("After Removing Pluto", planet_list)

missions = [("Astron", "Mars"), ("Prometheus", "Mercury"), ("Millenium Falcon", "Earth"), ("Supremacy", "Venus"), ("X-wing", "Saturn"), ("Star Destroyer", "Jupiter"), ("J-04889", "Pluto")]

print("Missions", missions)

for planet in planet_list:
  for mission in missions:
    if planet == mission[1]:
      print("Planet {0} was visited by {1}".format(planet, mission[0]))
      # print(mission[1])
