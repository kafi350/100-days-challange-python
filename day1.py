#Starting with the simple things
#printing something, print from a file, take input and store it.
import textwrap
import os

#printing

print("today is day 1")
firstString = "World"
multiLineStiring = '''
                Hello World
                I am starting today
                bless me!!
                bye
                   '''

print("hello", firstString)
print(multiLineStiring) #not taking care of the indentation
print(textwrap.dedent(multiLineStiring).strip()) #taking care of indentation
print("hello " + os.getlogin() + " how are you?")

#now comes f-String which is awesome! simple word :P

print(f'Hello, {os.getlogin()} How are you?')

#see the difference on normal printing and with f-strings! I don't need that space which is sometimes really bothering

#printing togethe with end perameter
print("checking file...", end='')
print("ok done!")

#seperate parameter

print('Mercury', 'Venus', 'Earth', sep=', ', end=', ')
print('Mars', 'Jupiter', 'Saturn', sep=', ', end=', ')
print('Uranus', 'Neptune', 'Pluto', sep=', ')

#reading from a file
with open('test.txt') as firstFile:
    for line in firstFile:
        print(line, end='')

#writing to file
with open('testwrite.txt', mode='w') as file_writer:
    file_writer.write(textwrap.dedent(multiLineStiring).strip())