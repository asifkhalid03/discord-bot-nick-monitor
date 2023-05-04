If you are looking for a specific Discord bot for users who set their server profile nickname or original profile username as blank, making them difficult to locate, this bot can help you overcome that issue. It will change the user's nickname to a valid one.

"These are the actions that will be performed by the bot:

If the nickname is invalid or blank:

If the user has a valid username, the bot will update the nickname accordingly.
Otherwise, it will set the nickname as "No-Nick-123", where 123 is the user's tag number."

#INSTALLATION PROCCESS

However, if you prefer to use a virtual environment to keep the dependencies for this project separate from your global Python environment, you can follow these steps:

Navigate to the folder where you want to create the virtual environment and store your project files.

Now in this project place the file in root directory "nick_monitor_discord_bot.py" and place your bot token in that file at the end "bot.run("YOUR_BOT_TOKEN")"

Run the following commands to create and activate the virtual environment:

For Windows:
python -m venv venv
.\venv\Scripts\activate


For macOS/Linux:
Copy code
python -m venv venv
.\venv\Scripts\activate


Once the virtual environment is activated, the terminal or command prompt should show the environment name (e.g., (venv)).

Now, install the discord.py library within the virtual environment by running:
pip install discord.py
By doing this, the discord.py library will be installed only in the virtual environment and not globally on your system. To deactivate the virtual environment, just type deactivate in the terminal or command prompt.


Remember to replace "YOUR_BOT_TOKEN" with your Discord bot's token.

Run the Python file:
python nick_monitor_discord_bot.py


Your kind words mean the world to me! If you found my assistance helpful, I would be grateful if you could leave me a star rating. And if you're feeling extra generous, I would love nothing more than a cup of coffee as a small token of appreciation.





