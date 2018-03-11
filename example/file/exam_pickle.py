import pickle
colors = ['red', 'green', 'black', 'white']
f = open('colors.pickle', 'wb')
pickle.dump(colors,f)
f.close()

del colors

f = open('colors.pickle', 'rb')
colors = pickle.load(f)
f.close()

print(colors)
