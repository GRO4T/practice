import shelve
shelfFile = shelve.open('mydata')
print("Restored data!")
for key, value in shelfFile.items():
    print(key, ' : ', value)
shelfFile.close()
