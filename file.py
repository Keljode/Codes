#file = open('example.txt', 'w')
#file.write('Hello\n')
#file.write('Date: 12/04/2025\n')
#file.write('Dear Francesca')

#with open('example1.txt', 'w') as file:
  #file.write('Date: March 19, 2024 \n')
#  file.write('Dear Diary...\n')
 # file1 = ['This is a line.\n', 'This is the next line.\n']
  #file.writelines(file1)
  #file.close()
#file= open('example1.txt','r')
#print(file.read())
#print(file.readline(), end='')
#print(file.readline(), end='')
#print(file.readlines())


liked_song = {'I was here': 'Beyonce',
               'Gonna': 'Rihanna',
               'what\'s': 'Jayson'}
def display_and_write_liked_songs(liked_songs, filename):
    with open(filename, 'w') as file:
    #file = open('filename', 'w')
        file.write('Liked songs:\n')
        for song, artist in liked_songs.items():
            file.write(song + ' by ' + artist + '\n')
    #file.close()
    print("Liked songs have been added succesfully!!!")
    
#display_and_write_liked_songs(liked_song, "kel.txt")
sent_message = 'I have 2 children.'
with open('sent_message.txt', 'w') as file:
    file.write(sent_message)
with open('sent_message.txt', 'r+') as file:
    original = file.read()
    file.seek(0)
    unsent_message = 'unsent messages.'
    file.truncate(len(unsent_message))
    file.write(unsent_message)
    file.write('Hello')
print("original: ", original)
print(unsent_message)


# Task 1: The Secret Message
sent_messages = "Hey there! This is a secret message."

# Save the sent message to a file
with open('sent_messages.txt', 'w') as file:
    file.write(sent_messages)

# Task 2: Simulate Unsending the Message
with open('sent_messages.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()

    # Move the cursor to the beginning of the file
    file.seek(0)

    # Modify the message to simulate unsending
    unsent_message = "This message has been unsent."

    # Truncate the file to the length of the modified message
    file.truncate(len(unsent_message))

    # Write the modified message to the file
    file.write(unsent_message)

# Display the modified message
print("Original Message:", original_message)
print("Unsent Message:", unsent_message)
