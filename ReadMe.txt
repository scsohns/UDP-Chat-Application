Project by: Stephen Sohns and Destinee Higgs

The file "sc.py" contains both the server and client. This version
only supports one of each. 

To run:
Execute sc.py in two separate windows

Enter 0, to create the server in the first window
Enter 1, to create the client in the second window

Enter the IP from the server display on the client window
Enter a valid port in the client window

The chat should now be functional. Type anything on either side
and press enter to send

There are three commands: hist(), quit(), and file()

hist() will display the chat history since the beginning of the 
chat.

quit() will send a message to the other to tell them you are 
disconnecting, then closes the socket and ends the program.

file() will ask for a file name, then send the file as bytes to
the recipient. They will be prompted to name the file, then it 
will appear in the same folder as the running program.
(Currently, the recipient must send a message after a file has
been sent in order to receive the file, this is an unresolved 
problem.)