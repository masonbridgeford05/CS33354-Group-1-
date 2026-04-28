**CS3354-Group-1**

**Comet Grid**

This is a python web game designed to 

**How to Run Tests**

1. Clone the Phase 4 Repository
2. Open the folder in your prefered IDE and run setup.bat (This will automatically install all the python libraries into a virtual environment.
3. Make sure you are in the CometGrid directory and start the virtual environment by running '.\.venv\Scripts\activate.bat'
4. Enter 'python manage.py migrate' in terminal to make sure all the databases are set up
5. Now run 'python manage.py test apps/game' to run testcases for game functionality
6. Run 'python manage.py test apps/accounts' to run testcases for account functionality
7. Run 'python manage.py test apps.leaderboard.tests.leaderboard-tests' to run testcases for leaderboard functionality
   
