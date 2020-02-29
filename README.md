# YouFic #

## Integration status ##

[![Build Status](https://travis-ci.com/andrewdempsey2018/youfic.svg?branch=master)](https://travis-ci.com/andrewdempsey2018/youfic)

YouFic, short for "You Fiction", is a website that facilitates the sharing of user created fiction stories. The name "YouFic" (short for You "Fiction") is a play on the title of the iconic website "YouTube". With YouTube, users can upload videos created by themselves for all to see. YouFic offers a similar service for people who want to share their fiction stories with the world.

## Website Goal ##

The goal of the website is to provide a central place where readers of fiction can access the latest user created stories. It also aims to be a place where aspiring writers could potentially get noticed by publishers.

The website is designed to be pleasant to use on both desktop and mobile devices. Good user experience on mobile devices is essential as many many people read whilst on the move on-board public transport etc. This dual functionality is achieved through the use of responsive design principles.

## UX ##

## User Stories ##

**User story 1:**

As a regular reader of fiction, I would like to browse the stories available and quickly select the one I am interested in. The short descriptions featured on the website for each story helped me select the stories I was interested in.

**User story 2:**

As a fan of science fiction, I would like to filter my browsing session to only display science fiction stories. I was able to use the websites category links to achieve this.

**User story 3:**

As an aspiring writer, I would like a service where I can quickly and easily publish my work and build a name for myself. After registering with the website, I was able to submit my stories for all to read.

**User story 4:**

As a fan of amateur fiction, I like that there is a resource for writers and fans to consume and create content. I was able to support the website by clicking on the donate link and helping pay for the upkeep of the website.

**Wireframes**

**Creative**

An attractive one page Bootstrap theme perfect fpor creative portfolios and businesses

![](assets/readme/creative.png)

*Image 1. The Creative theme*

Image of Stripe payments made sucsessfully

aaa
**Portfolio Item**

A simple portfolio item details page example built with Bootstrap 4. Used for dedicated item screen.

[https://startbootstrap.com/snippets/portfolio-item/](https://startbootstrap.com/snippets/portfolio-item/)

![](assets/readme/portfolio.png)

*Image 1. The Portfolio template*

## Features ##

- Responsive
- Browse as guest
- Browse as member (allowing upload of content)
- Make a donation to the running of the website

## Technologies used ##

## Testing ##

Image of Stripe payments made successfully

### Existing Features

## Directory structure

Describe the directory structure of the project with diagram

### Features Left to Implement

## Django Apps ##

- Accounts
- Story
- Donate

## Models ##

**Story:**
title (CharField)
author (CharField)
description (TextField)
image (ImageField)
category (CharField)
text (TextField)
published (DateTimeField)

Category's: Adventure, Fantasy, Mystery, SciFi

## Key code explanations ##

## Technologies Used

The website utilises a heavily modified version of the "Accounts" Django app created by Code Institute as part of the tutorial series "Authentication and Authorisation". 

[https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation)

**Forms Bootstrap**

**Whitenoise**

**Django**

A Python based web framework

Version: 3.0.3

[https://www.djangoproject.com/](https://www.djangoproject.com/)

**Visual Studio Code**

**Languages**

HTML5, Javascript, CSS, Python

**Paint.Net**

To retouch product photographs.

[https://www.getpaint.net/](https://www.getpaint.net/)

**Travis**

[https://travis-ci.com/](https://travis-ci.com/)

**Stripe**

[https://stripe.com/](https://stripe.com/)

**GitHub**

[https://github.com/](https://github.com/)

**Pillow 7.0.0**

For image processing used version 7.0.0 of Pillow. Pillow is a Python imaging

Python Imaging Library (abbreviated as PIL) (in newer versions known as Pillow) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

[https://pypi.org/project/Pillow/](https://pypi.org/project/Pillow/)

**Gunicorn**

**Django-forms-bootstrap**

**Modified accounts app based on Code Institute tutorial**

**Pillow**

**VSCode**

**Chrome**

**Web validator**

**Travis**

**Heroku**

**Whitenoise**

**Git and GitHub**

**Python3, Javascript, CSS, HTML5, Django 2**

**SQLite3**

**Pencil**

## Testing

**Continuous testing with Travis**



**Testing models with Django test framework**

Details of the test cases on Story model

**Functional testing**

The following tests were conducted on the website to test its functionality.

Test 1. Index page - All category's

1. Visit the website
2. Click the link to the side labelled "All category's"
3. A list of all story's currently held in the database should be displayed

Test 2. Index page - Single category

1. Visit the website
2. Click the link to the side labelled "Fantasy"
3. A list of all story's currently held in the database belonging to the 'Fantasy' should be displayed 

Test 3. Home button

1. Visit the website
2. Click the link in the navigation bar for the 'Donate' page
3. The user should be brought to the Donate page
4. Now click the 'Home' button
5. The user should be redirected to the index page showing all story's currently in the database

Test 4. Donate page tests

1. Visit the donate page
2. Click the donate button
3. On the pop-up dialogue, enter and email address and an incorrect credit card number
4. Click the 'Make Payment' button
5. The pop up should give an error message relating to the incorrect credit card number
6. Now enter a working test credit card number (4242 4242 4242 4242).
7. Enter an expiry date for the year 2019.
8. Click the 'Make Payment' button
9. The pop up should give an error message relating to the incorrect expiry date
10. Now enter an expiry year of 2022.
11. Enter a CVV number of only two digits
12. Click the 'Make Payment' button
13. The pop up should give an error message relating to the incorrect CVV number
14. Enter a correct CVV number (of any three digits)
15. Click the 'Make Payment' button
16. The payment should be processed
17. The user should be redirected to a 'thank you' page

Test 5. Login / Register tests

1. Visit the website
2. If the user is logged in, click the logout button
3. The footer should display the message "Currently browsing as Guest"
4. Now click the 'Register' button
5. Enter a user name of 'TestUser' and and email address of 'testuser@gmail.com'
6. Leave the password field blank
7. Click the 'Register button'
8. The form should inform the user that a password must be entered
9. Enter a password in the password field as well as the confirmation field
10. The user should now be redirected to the index page and the footer should read 'Logged in as TestUser'
11. Click the logout button
12. The user should be redirected to the index page
13. The footer should again read "Currently browsing as Guest"

Test 6 Submit page tests

1. With the user logged out, click the 'submit a story' button
2. The user should be redirected to the 'submit' page
3. The user should be informed that only registered users can submit story's
4. Click the login button
5. The user should be redirected to the login page
6. Enter some valid details and login
7. Again click the 'submit a story' button
8. The user should be redirected to the 'submit' page only this time, there should be a number of fields for entering some story details
9. Fill out all of these fields with the exception of the field labeled 'title'
10. Click the 'Publish story' button
11. The user should be informed that the 'title' field needs to be filled in
12. Now enter a title and click the 'Publish story' button
13. The user should be directed to the index page
14. Click the category selector for the category of the story input in step 9
15. The story should no be available for reading

**Testing the store on various devices / emulators / browsers**

**Bugs found / issues**

## Deployment

**Running the website locally**

Here are the steps required to run this website with the VSCode IDE

1. Download this GitHub repo and unzip
2. Open the unzipped folder in VSCode
3. Open a terminal
4. Type: 'python -m venv env' to create a virtual environment
5. Type: 'env\scripts\activate' to activate the virtual environment
6. Type: 'pip3 install django' to install Django 2
7. Type: 'python manage.py makemigrations' followed by
'python manage.py migrate' to create a database based on the models defined in the repository source code
8. Type: 'python manage.py runserver' to activate the inbuilt Django test server
9. Open a browser on the address 'localhost:8000'
10. You should now see the index page however there will be no story's currently in the database. These can be easily input by creating a user account and entering them from the 'submit' page
11. In order to access the admin functionality,go to the terminal
12. Type 'python manage.py createsuperuser'
13. Enter a name, email address and password
14. Now go to a browser and type the address 'localhost:8000/admin'
15. You can now log in and manipulate the database from Django's admin software

**How the website was deployed on Heroku**

* Gunicorn
* Explain the contents of the procfile

## Credits

- The Code Institute team
- Spencer Barriball
- Code Institute students on Slack
- @ckz8780 on Slack for fixing my MEDIA_ROOT issue

## Sources of information

Django documentation v3.0:

[https://docs.djangoproject.com/en/3.0/](https://docs.djangoproject.com/en/3.0/)

Code Institute tutorials....

**Start Bootstrap**

Theme templates.

[https://startbootstrap.com/](https://startbootstrap.com/)

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X

# TODO / Notes

* Change DEBUG = True in Django settings file to False
* Add a tonne of tests in tests.py on the models
