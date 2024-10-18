1. Open the project in your terminal

2. Create a venv using "python -m venv venv"

3. Install the requirements for the project by running "pip install -r requirements.txt"

4. Make sure you have "make" and "docker" correctly installed on your system

5. Start by building the project by running "make build" in your terminal
   (Here you will also notice we have an Automatic Pytest that will run our test code that checks if everything is working correctly)
   (Also after the project is built you will only have to do step 6 (make run) to make it run again after you shut it down by pressing SHIFT+C)

6. After the project is built run "make run" (if any error occure after the first time running make run, try running it again)

7. After it is up and running paste "http://127.0.0.1:8009/" into your browser (or "localhost:8009)

8. If you wish to test with pytest localy, run "pytest" when your standing in the "BurgerOrder" folder
