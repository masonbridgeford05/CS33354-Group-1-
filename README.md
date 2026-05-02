**CS3354-Group-1**

**Comet Grid**

This is a python web game designed to 

**How to Run Tests**

1. Clone the Phase 5 Repository
2. Open the folder in your prefered IDE and run setup.bat This will automatically install all the python libraries into a virtual environment.
3. Make sure you are in the CometGrid directory and start the virtual environment by running '.\.venv\Scripts\activate.bat' and wait a minute till completion.
4. Depending on OS:
      Windows run '.venv\Scripts\activate.ps1'
      Linux run '.venv\Scripts\activate.bat'
      MAC run 'source .venv/bin/activate'
6. Enter 'python manage.py migrate' in terminal to set up the databases
7. Run 'python manage.py load_game_images' in the command line to load all the game images into the database
8. Now run 'python manage.py test apps/game' to run testcases for game functionality
9. Run 'python manage.py test apps/accounts' to run testcases for account functionality
