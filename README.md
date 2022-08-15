# HEARD|it

## Introduction
HEARD|it is an Irish technology news website which encourages users to Create, Read and Shape the news with a focus on technology start-ups.

A deployed link to the website can be found [here](https://heard-it.herokuapp.com/)

## Showcase
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/heardit_amiresponsive.PNG)


# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UX](#ux-user-experience)
    - [User Stories](#user-stories)
 - [Skeleton](#skeleton)
 - [Design](#design)
 - [Testing](#testing)
 - [Deployment](#deployment)
 - [Credits](#credits)
 - [Acknowledgements](#acknowledgements)

 ## Design

## UX User Experience
### User Stories

### As the site creator/admin:
* I want to have full access and functionality as a superuser
* I want to be able to create, read, edit and delete all post(s) / article(s)
* I want to be able to view / reject pending posts from users before publication

### As the site user:
* I want to be able to register an account
* I want to be able create, read, edit and delete my post(s) / article(s)
* I want to be able to leave comments on all posts
* I want to be able to Like & unlike post(s) / article(s)
* I want to be able to view all other posts / articles by using the search functionailty
* I want to be able to make changes to the post by editing post(s) / article(s)
* I want to be able to Remove / delete post(s) / article(s) permentatly

## Skeleton
### Wireframes
* To view all wireframes both Desktop & mobile [Click Here](https://github.com/sherryrich/heard-it/blob/main/docs/heardit_wireframes.pdf)

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/homepage.PNG)

## Design

### Color Palette

## Lighthouse Report

## Technologies Used
### Languages Used
  * [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  * [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  * [JavaScript](https://www.javascript.com/)
  * [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used
* [amiresponsive](http://ami.responsivedesign.is/) to see how responsive the site is on different devices.
* [Balsamiq](https://balsamiq.com/) was used to create the Wireframes.
* [Cloudinary](https://cloudinary.com/) was used to upload, store, manage, manipulate, and deliver images.
* [Color-hex](https://www.color-hex.com/) once I identified the colors I wanted I used color-hex to generate the palette.
* [Django](https://www.djangoproject.com/) is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.
* [Font Awesome](https://fontawesome.com/) was used for icons for aesthetic and UX purposes on the buttons.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
* [Gitpod](https://www.gitpod.io/) An online IDE linked to the GitHub repository used to write my code.
* [Google Chrome Dev tools](https://developer.chrome.com/docs/devtools/) for debugging.
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) used for audits to measure the quality of web pages.
* [Heroku](https://www.heroku.com/) used to deploy this app, a cloud platform as a service supporting several programming languages.
* [WAVE](https://wave.webaim.org/extension/) Browser Extension testing.


## Testing

#### **Navigation Testing**

### W3C Validator Testing

### The W3C Markup Validator

### W3C CSS Validator
  <details>
  <summary>Click here to see the W3C CSS Validator result</summary>

  ![](docs/w3c_css_validator_result.PNG)

  </details>

### Lighthouse
* Lighthouse Report
 <details>
  <summary>Click here to see the Lighthouse Report</summary>

  ![](docs/lighthouse_result.PNG)

  </details>

## Bugs
* Manage.py was not in the root directory. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_1.png)
* App wasn’t deploying to heroku correctly. Updated Procfile from "heard-it" to "heardit"
* Update your requirements.txt - pip3 freeze > requirements.txt and try again. I had a typo in requirements without .txt. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_2.png)
* Template litteral typo error "$" instead of "%". [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_3.png)
* Error in views.py. '-created' versus '-created_on'. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_4.png)
* Missing comma at the end of this line "STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]". [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_5.png)
* 500 Error because I didn’t have "redirect" imported at top of views.py file. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_6.png)
* Error in the terminal. Heroku updated databse so had go to Heroku config vars and copy and paste the new database_url into the env.py to correct. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_7.png)
* Space in the token provided. Caused CSS not to display on the front end as expected.  [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_8.png)
* Missing closing span. Caused HTML to fail validator rules.  [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_9.png)







### Unfix Bugs

## Deployment
* This project was developed using a GitPod workspace. The code was commited to Git and pushed to GitHub using the terminal.

* Log in to [Heroku](https://id.heroku.com/login) or create an account
* On the main page click New and Create New App
* Note: new app name must be unique
* Next select your region, I chose Europe.
* Click Create App button
* Click in resources and select Heroku Postgres database
* Click Reveal Config Vars and add new config "SECRET_KEY"
* Click Reveal Config Vars and add new config "CLOUDINARY_URL"
* Click Reveal Config Vars and add new config "DISABLE_COLLECTSTATIC = 1"
* The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
* Next, go to Buildpack section click Add Buildpack select python and Save Changes
* Scroll to the top of the page and choose the Deploy tab
* Select Github as the deployment method
* Confirm you want to connect to GitHub
* Search for the repository name and click the connect button
* Scroll to the bottom of the deploy page and select the preferred deployment type
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

### Final Deployment 

* Create a runtime.txt `python-3.8.13`
* Create a Procfile `web: gunicorn heardit.wsgi`
* When development is complete change the debug setting to: `DEBUG = False` in settings.py
* In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to
   settings.py.
* In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

### Forking This Project

* Open [GitHub](https://github.com/sherryrich/heard-it)
* Find the 'Fork' button at the top right of the page
* Once you click the button the fork will be in your repository

### Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/sherryrich/heard-it)
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type 'git clone' and paste the URL copied in step 3
7. Press 'Enter' and the project is cloned




## Credits

* Code Institute - Database Management Systems - Task Manager Walkthrough
* Code Institute - 'I think therefore I blog' Django blog project Walkthrough
* Corey Schafer Python Django Tutorial[YouTube](https://www.youtube.com/c/Coreyms)
* Create A Simple Blog With Python and Django[YouTube](https://youtu.be/B40bteAMM_M)
* The Web Developer Bootcamp 2002 [Udemy](https://www.udemy.com/course/the-web-developer-bootcamp/)

## Acknowledgements
To create this website, I relied on material covered in the Full Stack Development course by Code Institute.
I also sourced information and help from a variety of sources such as Slack Community Channels, Udemy, W3Schools, MDN and YouTube for Online Web Tutorials and resources.
Martina Terlevic for reviewing my work and providing valuable feedback and advice.
Gerard McBride my Code Institute / UCD Facilitator and Masterclass tutor.
Róisín Crilly for taking her free time to walk through P4 experience and logic

This project is for educational use only and was created for the Code Institute Module.

Created by Richard Sherry 🙌