file = open('youtube.txt','w')

try:
    file.write('Hello World')
finally:
    file.close()
    

with open('youtuve.txt','w') as file:
    file.write('How are you?')