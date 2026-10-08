import pyjokes

joke= pyjokes.get_joke()
print("Joke of the Moment:")
print(joke)

print()

print("Here Are A Few More")
count=1
while count<=5:
    print(str(count)+"."+ pyjokes)
    count=count+1

print()