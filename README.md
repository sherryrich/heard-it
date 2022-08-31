# HEARD|it

## Introduction
HEARD|it is an Irish technology news website which encourages users to Create, Read and Shape the news with a focus on technology start-ups.
The website is aimed at users who enjoy sharing news articles with the emphasis on Tech trends.
Users have the ability to create, read, update and delete articles via their own profile and like and comment on articles posted by other users.


## Showcase
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/heardit_amiresponsive.PNG)

### Live Website
A deployed link to the website can be found [here](https://heard-it.herokuapp.com/)

### Video
A video tutorial outlining some features can be viewed [here](https://res.cloudinary.com/dzyxqqpzh/video/upload/v1661449979/New_Tab_-_Google_Chrome_2022-08-25_18-48-29_ptleon.mp4)

### QR Code

 <details>
  <summary>Click here to see QR Code</summary>

  ![](docs/qrcode.PNG)

  </details>


# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux-user-experience)
- [Agile Development Process](#agile-development-process)
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


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
* I want to be able to view all other posts / articles by using the search functionality
* I want to be able to make changes to the post by editing post(s) / article(s)
* I want to be able to Remove / delete post(s) / article(s) permanently

## Agile Development Process
* The MoSCoW method was adopted to approach to prioritizing which project requirements for must have, should have, could have and will not have.
* I used GitHub for Automated Kanban Project Management. [Click Here](https://github.com/sherryrich/heard-it/blob/main/docs/project_user_stories.PNG)
* I used GitHub project board to generate user story templates.
* I used project templates to speed up the process. 
* I used the automated kanban process and when It is connected to my repo. This allowed me to monitor, track and create user stories.
* In my developer environment when I used the keyword "resolve #card_number" in my commit message this automatically moved the card would move to completed column.
* I thought about adding a separate app for the contact page so as to apply separation of concerns however I felt that would be WET (Write Everything Twice) and decided upon KIS (Keep It Simple) / DRY code (Dont Repeat Yourself).


## Design
### Wireframes
 <details>
  <summary>Click here to view all wireframes both Desktop & mobile:</summary>

  ![](docs/wireframe_homepage.PNG)
  ![](docs/wireframe_about.PNG)
  ![](docs/wireframe_signup.PNG)
  ![](docs/wireframe_login.PNG)
   ![](docs/wireframe_contact.PNG)
  ![](docs/wireframe_new.PNG)
  ![](docs/wireframe_logout.PNG)

  ![](docs/wireframe_home_mobile.PNG)
  ![](docs/wireframe_about_mobile.PNG)
  ![](docs/wireframe_signup_mobile.PNG)
  ![](docs/wireframe_signin_mobile.PNG)
  ![](docs/wireframe_contact_mobile.PNG)
  ![](docs/wireframe_post_mobile.PNG)
  ![](docs/wireframe_signout_mobile.PNG)

  </details>

### Navigation

I created a logic flowchart to help organise the site structure.
The ERD entity relationship diagram helped visually to confirm user roles and the permissions.

<details>
  <summary>Click here to view website navigation:</summary>

  ![](docs/navigation.drawio.png)

  </details>

### Database Schema

I created 3 databases for the website. Post, Comment & Contact. There are some objects not present in my database schema such as user and profiles as these are objects that Django automatically creates.

The Post Database is used by users to post articles to the website. It has a Primary Key of ID & a ForeignKey relationship to the Comment Database.
The database also has the following fields, a title, slug (short summary the subject of an article), content, excerpt (short extract), Updated On (date post was updated), Created On (date post was created), status (draft or published) and Likes.

The Comment Database is used by users to comment on articles. It has the following fields a Primary Key of ID, name, email, body, created on, approved and a ForeignKey to the Post Database.

The Contact Database is used by users to submit the contact form. It has the following fields a Primary Key of ID, name, email, body & created on (date contact form was submitted).

 <details>
  <summary>Database Schema:</summary>

  ![](docs/database_schema.PNG)

  </details>


### Color Palette

 <details>
  <summary>Color Palette:</summary>

  ![](docs/color_palette.PNG)

  </details>





## Features
### Existing Features

### Home Page
Homepage displays the Navbar Brand / logo name, About, Sign Up, Login and Contact options on the left and search function on the right.
There is a H1 heading describing what the website is about so that users understand the websites function and target audience.
The main body of the homepage contains 6 articles / posts and once more than 6 articles are posted pagination shows links to the next page.
Social media network links are displayed in the footer.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/homepage1.PNG)

### Navigation Bar
When not logged in the Navbar displays links to About, Sign Up & Login.
When a user hovers over navigation links a thin border appears at the bottom of the links to show responsiveness when the user interacts with the link element(s). When a user is logged in the Navbar displays links to About, Post Article & Logout.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/navbar.PNG)

### Search Page
When a user searches a particular word the result will return articles which contain the word searched with the string "You searched for". Example below user searched "jobs"

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/search.PNG)

### Search Article - No Results
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/search_no_results.PNG)


### About
A short introductory page informs the user(s) when the website was formed and what it aims to achieve and industry awards it has won.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/about.PNG)

### Sign up
When a user goes the Login page they are shown a simple form with username and password to sign in.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/signup.PNG)

### Log in
When a user goes to the Login page they can enter account details as above. If a user however has not created an account yet, they are advised to sign up first.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/login.PNG)

### Log in messaging 
When a user logs in successfully a message is displayed for 3 seconds to confirm. This message then is removed.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/signin_message.PNG)

### Log out
When a user goes to the Logout they are advised to confirm if they want to sign out before further action is taken.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/logout.PNG)

### Log out messaging
When a user logs out successfully a message is displayed for 3 seconds to confirm. This message then is removed.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/signout_message.PNG)

### Admin - Superuser Access
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/admin.PNG)

### Post Article
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/post_article.PNG)

### Post Article - waiting approval
When a user posts an article they are informed the post is waiting approval.
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/post_created_message_awaiting_approval.PNG)

### Edit / Delete Article
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/user_article_update_delete.PNG)

### Edit Article - confirmation of update
When a user successfully edits an article they are informed the post has been updated.
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/post_created_message_awaiting_approval.PNG)

### Delete Article
When an author selects to delete an article they have created they are asked if they want to proceed before permanent deletion as it cannot be undone. Once deletion is confirmed the user is directed back to the homepage.
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/confirm_delete_message.PNG)

### Delete Article Confirmation Message
When an author successfully deletes an article they as shown a confirmation message on screen.
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/post_deletion_confirmation.PNG)

### Article View
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/article_view_1.PNG)

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/article_view_2.PNG)

### Comment Awaiting Approval
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/comment_awaiting_approval.PNG)

### Contact Page
Users can contact the website via a simply form with name, email and body of message. Once the form is successfully sent a message is shown to the user to inform them.
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/contact_page.PNG)

### Contact Page Djano Admin
Messaging sent via the contact page is stored in Django admin under blogs - contact. The name, email, body of message and the date sent is stored.
![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/contact_page_django_admin.PNG)

### Social Links
The footer contains various social network links (Facebook, Twitter, Instagram and YouTube) and Copyright information.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/footer.PNG)

### 404 Page
A 404 page was created to handle potential user navigational errors and give user a link to direct them back to the homepage.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/404.PNG)

### 500 Page
A 500 server error page was created to handle internal server errors.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/500.PNG)

### Default image

A default image is loaded if the user fails to post an image. This is stored in cloudinary.

![Preview](https://github.com/sherryrich/heard-it/blob/main/docs/defaulted_image.PNG)



## Future Features
* Allows users to signup to a newsletter / mailing list.
* Allow users to report already approved content.
* Host audio content for podcasts.
* Allows users to filter by most read or most commented on articles.
* Allow users to contribute to financially support ongoing publication by way of donations.

## Bugs / Errors encountered during development
* Manage.py was not in the root directory. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_1.png)
* App wasn’t deploying to heroku correctly. Updated Procfile from "heard-it" to "heardit"
* Update your requirements.txt - pip3 freeze > requirements.txt and try again. I had a typo in requirements without .txt. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_2.png)
* Template literal typo error "$" instead of "%". [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_3.png)
* Error in views.py. '-created' versus '-created_on'. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_4.png)
* Missing comma at the end of this line "STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]". [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_5.png)
* 500 Error because I didn’t have "redirect" imported at top of views.py file. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_6.png)
* Error in the terminal. Heroku updated database so had go to Heroku config vars and copy and paste the new database_url into the env.py to correct. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_7.png)
* Space in the token provided. Caused CSS not to display on the front end as expected. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_8.png)
* Missing closing span. Caused HTML to fail validator rules. [Click here](https://github.com/sherryrich/heard-it/blob/main/docs/error_9.png)
* Search Button was missing on smaller devices so I added a media query and reduced the size of the element on smaller devices. Please see screen shots [Before](https://github.com/sherryrich/heard-it/blob/main/docs/search_box_before.PNG) and [After](https://github.com/sherryrich/heard-it/blob/main/docs/search_box_after.PNG). 
* I was aware of various pylint and flak8 notifications however none of them are having any functionality implications and were as a result of the template followed from the code institute Django blog project Walkthrough.

### Unfixed Bugs
No known unfixed bugs present at the time of submission

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
* [Pexels](https://www.pexels.com/) Images for this project were sourced from Pexels.
* [Silicon Republic](https://www.siliconrepublic.com/) Content inspiration for articles.
* [Unsplash](https://unsplash.com/) Images for this project were sourced from Unsplash.
* [WAVE](https://wave.webaim.org/extension/) Browser Extension testing.
* [a11y](https://color.a11y.com/) Color Contrast Accessibility Validator.



## Testing

### Validation Testing
|  | Validations |  Pass/Fail |
| ------------- |-------------|  :----: |
| Chrome   | Lighthouse Report | Pass |
| HTML   | W3C Markup Validator | Pass |
| CSS   | W3C CSS Validator | Pass |
| Python   | PEP8 online | Pass |
| JS   | JSHint | Pass |
| Color Contrast   | a11y | Pass |

### Lighthouse Report
* Ran Lighthouse reports audits to gauge performance, accessibility, and SEO. Gain actionable and reportable insights in real time.
 <details>
  <summary>Click here to see the Lighthouse Report</summary>

  ![](docs/lighthouse_result.PNG)

  </details>

### The W3C Markup Validator
  <details>
  <summary>Checked using W3C Markup Validator ensuring there were no errors or warnings present. Click here to see the W3C Markup Validator result</summary>

  ![](docs/w3c_html_validator_result.PNG)

  </details>

### W3C CSS Validator
  <details>
  <summary>Checked using W3C CSS Validator ensuring there were no errors or warnings present. Click here to see the W3C CSS Validator result</summary>

  ![](docs/w3c_css_validator_result.PNG)

  </details>

  ### PEP8 online 
  <details>
  <summary>Checked Python code is formatted according to the PEP 8 standards</summary>

  ![](docs/pep8online_result.PNG)

  </details>

  ### JSHint 
  <details>
  <summary>Checked JavaScript source code complies with coding rules</summary>

  ![](docs/jshint_result.PNG)

  </details>

   ### Color Contrast Accessibility Validator 
  <details>
  <summary>Checked color contrast analysis accessibility</summary>

  ![](docs/color_contrast_accessibility_validator.PNG)

  </details> 

### Manual Testing
* Manual testing was completed for each case and edge case scanerio from user log in, user post article, user delete article and user log out and contact and search articles.
* The site was also manually tested on various browsers (Google Chrome, Safari, Microsoft Edge and Firefox.) and on different screen sizes.
* Dev tools was used often to identify errors within HTML and CSS code, with the console feature to identify errors in Javascript code.
* I also used lighthouse reports to see the performance, quality, and correctness of the website.
* I also used WAVE to check the accessibility of my website and this made me alter my color scheme to account for contracting errors found during development.
* For some further defensive programming I tested SQL Injection attacks by attempting to delete / updated articles via the URL with "update" and "delete" appended when not logged in as admin or users.

### More manual testing scanerios and results
|   | Pass/Fail |
| ------------- | :----: |
| Selecting heardit logo on homepage directs user back to homepage  |  Pass |
| Selecting about link directs user to /about page  |  Pass |
| Selecting Sign Up directs user to /accounts/signup/ page |  Pass |
| Selecting Login directs user to /accounts/login/ page  |  Pass |
| Selecting contact directs user to /contact page  |  Pass |
| Filling in form on /contact page requires name, email and body to send to Django admin  |  Pass |
| Contact form successfully sends data to Django admin as expected  |  Pass |
| Selecting search articles box in navbar and entering a search returns expected result  |  Pass |
| Selecting search articles box in navbar and entering a no results search returns no result page  |  Pass |
| Click on the pagination link at the bottom of the page returns results of the next page (example /?page=2) |  Pass |
| Registering as a user and entering password <8 characters prompts message "This password is too short." |  Pass |
| Registering as a user and entering password >8 characters to create a new user |  Pass |
| Logging in as superuser / admin |  Pass |
| "successfully signed in as (user name)" message shown to user |  Pass |
| Logging in as superuser / admin to approve post |  Pass |
| Navigating site as user / admin is permitted |  Pass |
| Creating a new post directs user to "/new" and required fields send the data successfully to Django admin  |  Pass |
| Confirmation message that post is "waiting for approval" shown to user |  Pass |
| As admin I can view and publish post |  Pass |
| If no image is selected then the default image is used |  Pass |
| Posting a comment as a user / admin on any article |  Pass |
| Liking a comment as a user / admin on any article |  Pass |
| Updating a post as the author |  Pass |
| User is prompted "are you sure you want to delete" before permitting deletion of a post |  Pass |
| Deleting a post as the author |  Pass |
| Confirmation message of deletion is shown |  Pass |
| Not permitted to update a post if not the author |  Pass |
| Not permitted to delete a post if not the author |  Pass |
| Logging out as a user / admin prompts "are you sure" message |  Pass |
| "You have signed out" message shows to user when successfully signed out |  Pass |
| Logging out as a user / admin directs user to homepage |  Pass |
| Posting a new article requires appropriate fields to be filled in |  Pass |
| Clicking on the social media icons in the footer open the link in a new tab |  Pass |


### Responsiveness Browser Compatibility

|  | Chrome | Firefox | Edge | Safari | Pass/Fail |
| ------------- |-------------| -----|  ---------- |  -----| :----: |
| Expected Appearance   | yes | yes  | yes  | yes | Pass |
| Expected Layout   | yes | yes  | yes  | yes | Pass |



## Deployment
* This project was developed using a GitPod workspace. The code was committed to Git and pushed to GitHub using the terminal.

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

* Open [GitHub](https://github.com/sherryrich/heard-it)
* You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
* Once you click the button the fork will be in your repository
* Open a new terminal
* Change the current working directory to the location that you want the cloned directory
* Type 'git clone' and paste the URL copied in step 3
* Press 'Enter' and the project is cloned



## Credits

* Code Institute - [Hello Django](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/121ef050096f4546a1c74327a9113ea6/) - Task Manager Walkthrough
* Code Institute - [I think therefore I blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/
) - Django blog project Walkthrough
* Codemy.com Database Tables With Django - [YouTube](https://youtu.be/z5e_8FgKZig)
* Codemy.com Delete a Blog Post - Django - [YouTube](https://youtu.be/8NPOwmtupiI)
* Corey Schafer Python Django Tutorial [YouTube](https://www.youtube.com/c/Coreyms)
* Create A Simple Blog With Python and Django [YouTube](https://youtu.be/B40bteAMM_M)
* The Web Developer Bootcamp 2002 [Udemy](https://www.udemy.com/course/the-web-developer-bootcamp/)
* How to Use GitHub for Automated Kanban Project Management [YouTube](https://www.youtube.com/watch?v=YVFa5VljCDY)
* Delete confirmation message [Stack Overflow](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown)
* [RTE](https://www.rte.ie/) Content inspiration for articles.

## Acknowledgements
* To create this website, I relied on material covered in the Full Stack Development course by Code Institute.
* I also sourced information and help from a variety of sources such as Slack Community Channels, Udemy, W3Schools, MDN and YouTube for Online Web Tutorials and resources.
* Martina Terlevic for reviewing my work and providing valuable feedback and advice.
* Gerard McBride my Code Institute / UCD Facilitator and Masterclass tutor.
* Róisín Crilly for taking her free time to walk through P4 experience and help with code / logic.

This project is for educational use only and was created for the Code Institute Module.

Created by Richard Sherry 🙌