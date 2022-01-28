Colter Tucker practical for Accendero


To run the project follow the following steps:
1. Download the project from Github and navigate to project directory in command line
2. Activate the virtual environment by navigating to ./env/Scripts/activate.bat
3. Return to project directory, then step into the Accendero Folder
4. Start the local server by running "python manage.py runserver"
5. Open another instance of command line and navigate to project directory
6. Continue into ./Accendero/frontend
7. Start the frontend with "npm start"


After the server and frontend have been started the project can be found:

Frontend and GUI interaction
http://localhost:3000/

Backend administration
http://localhost:8000/admin/

Api
http://localhost:8000/items/
http://localhost:8000/forecasts/


To run unit & integration tests
1. Open another instance of command line and navigate to project directory
2. Activate the virtual environment by navigating to ./env/Scripts/activate.bat
3. Return to project directory then into ./Accendero
4. run all tests with "python manage.py test"

Below is a list of primary material that was consumed to create this project.

https://www.tabnine.com/blog/how-to-create-django-projects-in-pycharm-community-edition/
https://docs.djangoproject.com/en/4.0/ref/models/fields/
https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
https://www.w3schools.com/html/html_form_input_types.asp
https://docs.djangoproject.com/en/4.0/topics/testing/overview/