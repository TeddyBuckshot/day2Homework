stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

print('original list: ', stops)
print("\n")
stops.append("Edinburgh Waverley")
stops.insert(0,"Glasgow Queen St")
stops.insert(4,"Polmont")
print('linlithgow is stop no. ', stops.index("Linlithgow"))
print("\n")
stops.remove("Livingston")
del stops[2]
print('the number of stops on the line is: ', len(stops))
print("\n")
sortedList = sorted(stops)
print('alphabetical list:', sortedList)
print("\n")
stops.reverse()
print('Reversed List:', stops)
print("\n")

print("all stations printed from a FOR loop: \n" )
for station in stops:
    print(station)