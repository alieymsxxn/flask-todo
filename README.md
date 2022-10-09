# HOW TO RUN
1. Open the terminal and get into the project directory.
2. Install the required dependencies using the command below in the terminal.
> pip install -r requirements.txt

Note: It is preferable to have a separate python environment for the project.

3. Set the FLASK_RUN environment variable by running this command in the terminal. 
> export FLASK_RUN=server.py
4. Run the following command to start the server. 
> flask run
5. There is one root user created by default with username: root and password: root. It can be used to access all endpoints. 

# HOW TO DECRYPT
1. A demonstartion of implemented encryption and decryption is depicted in the test.py file.
2. It is assumed that the key.key file is accquired by both encrypting and decrypting parties.

