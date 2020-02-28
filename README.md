# YouFic #

## Integration status ##

[![Build Status](https://travis-ci.com/andrewdempsey2018/youfic.svg?branch=master)](https://travis-ci.com/andrewdempsey2018/youfic)

YouFic, short for "You Fiction", is a website that facilitates the sharing of short fiction works by aspiring writers. All visitors to the web site can browse the available works and filter them by genre. If a visitor registers and has logged in, that user will have the ability to upload their own content to the website.

## UX ##

## Website Goal ##

## User Stories ##

**User story 1:**

**User story 2:**

**User story 3:**

**User story 4:**

**Wireframes**

**Creative**

An attractive one page Bootstrap theme perfect for creative portfolios and businesses

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

## Testing

**Testing with Jasmine?**

**Continuous testing with Travis**

**Testing models with Django test framework**

Details of the test cases on Story model

**Stakeholder testing**

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

**Testing the store on various devices / emulators / browsers**

**Bugs found / issues**

## Deployment

**Running the website locally**

Give details on the development webserver bundled with Django.

If one wanted to run the website from downloading the GitHub repository zip they would...

Uses SQLite database for development and testing (not suitable for production)

**How the website was deployed on Heroku**

* Gunicorn
* Explain the contents of the procfile

## Credits

The Code Institute team

Spencer Barriball

Code Institute students on Slack

@ckz8780 on Slack for fixing my MEDIA_ROOT issue

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
