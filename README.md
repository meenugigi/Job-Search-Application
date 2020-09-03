CS50 FINAL PROJECT

This application makes use of Django, Javascript and MySQL database.
(note: javacript is written within the required HTML files)

This is a jobsearch application named 'JobHunt' that supports multiple user-types. 
In this application we have 2 types on users. 
Type 1: WebUsers (they are any users who log into the application to search jobs).
Type 2: Employers (they are people who log into the application to register their companies on the application and hire people).
To support mutiple user type, I have used view decorators, Django’s built-in permissions framework, to acheive this functionality.


Features of this application

- 2 types of users can create accounts. 
	Type 1 --> Users (searchng for jobs)
	Type 2 --> Employers (hiring users)

- Employers can fill forms to register their companies on the website. The registered details will be visible to other employers as well as users.

- Users can search companies by typing in the company name on the search bar.

- Users can see a list of all companies registered. Clicking on a company will display all details related to that particular company. Any previous ratings provided for that company will also be displayed along with the average ratings for that company.

- Users can give ratingd to any company. These ratings will ve visible to all other users as well as employers.

- Users will be able to send applications to any companies registered on the website.
Users will be able to upload their resumes while filling up their application forms. On succesfully submitting the applications, users will receive an email.

- Employers will be able to view applications receieved only for their companies.

- Employers can update or delete the company details registered by them. Employers will not have access to update or delete information related to companies registered by other employers.

- Users can download free resume templates from the website.

- The application is mobile responsive.



Functionalities implemented for Webuser:
- search companies
- view list of companies registered with the application
- view ratings for each companies along with the average rating for each company.
- rate a company
- send job applications
- upload resumes (any file format)
- download resume templates from the application

Functionalities implemented for Employer:
- register companies
- view list of companies registered with the application
- view ratings for each companies along with the average rating for each company.
- view list of job applications received by a company registered by them
- update details of companies registered by them
- delete details of companies registered by them

(An employer does not have access to update/delete information of companies registered by other employers. An employer can view job applications recieved for only the company registered by him/her.)




Walkthrough of the code:

- myapp --> this directory contains the main code. i.e, the view the models and the forms required for the application

- myapp/views/common.py --> it checks whether the user trying to login is a webuser or an employer. and depending on the usertype, it redirects to them to the appropriate webpage.

- myapp/views/employer.py --> it contains the code for all employer actions like registering a company, updating the registered compant informartion, deleting the registered company and viewing receieved applications for the registered company.

- myapp/views/webuser.py --> it contains the code for all user actions like searching for companies, viewing list of companies, rating a company, sending job applications to multiple companies, uploading resumes and downloading resume template.

- myapp/admin.py --> list of registered models on the admin site.

- myapp/models.py --> creating all the required models.

- myapp/forms.py --> contains the code for all the forms used by the application. (form required for employer to register a company, form required by users to send job applications, form required by users to rate companies etc).

- myapp/decorator.py --> contains views that checks whether the logged in user is a webuser or an employer and redirects them to the log-in page if necessary.

- templates --> contains the entire html code for the application.

- static/myapp --> contains static files like image files and css files used in the application.

To run Application:
- open cmd
- navigate to project folder (on cmd)
- type 'pip install -r requirements.txt'
- type 'python manage.py runserver'

Application Demo Link: https://youtu.be/q1bF6bfpmaY
