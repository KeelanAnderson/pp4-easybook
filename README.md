# EasyBook

EasyBook is an app designed for small business owners to make a post for their business and display all the relevant information about their business such as location, opening hours, services, contact info etc. By displaying this information it will make it easy for customers to find out about their business and make appointments online. Site users can create an account and then create a business post on our site. They have full CRUD functionality and can Create, Update and Delete posts. This Project was created during Agile development and is in its early stages with plans to add increasing functionality and value to the website.

![EasyBook](/media/easybook.jpg )

Live link can be found here - [EasyBook](#)

## User Stories

### Admin

- Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my services content
- Manage services: As a Site Admin I can create, read, update and delete services so that I can manage my content
- Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later

### Site User

- As a site user I want to view all the available Business posts on the app so that I can view each post
- As a site user I want to view all the available Business services on the app so that I can choose the service I want to use
- As a site User I want to be able to find the neccessary information about the business such as contact information and loction so that i can interact with the business and use their services

### Business Owner

- As a Business Owner I can register an account so that I can list my business
- As a Business Owner I want to fill out a form to provide all the necessary information about my business so it can be listed
- As a Business owner I want to be able to update my post and change information when signed in from the Front end without having to be use site admin panel
- As a Business Owner I want to be able to create, update and delete my post 
- As a Business owner I should not be able to update or change other businesses data


### Navigation

- As a Site User, I can immediately understand the website purpose so that I can decide if it meets my needs.
- As a Site User, I can easily and intuitively navigate the site so that I can find the desired content.
- As a Site User, I can view a paginated list of Business posts so that I can choose and select the ones I am interested in.
- As a Site User, I can click on a post so that I can view the full details and information

### Future Features

- As a site user I want to be able to make a booking at an available time for the service I want
- As a site user I want to be and to be able to rate and review the services I have used

## Data Model

- User model as part of the Django allauth library contains basic information about authenticated user and contains folowing fields:
username, password,email

- Post Model is a custom model that contains all the information about the business so the posts and detail page can be created, it has foreign key to the User model to associate each post with the account that created it contains the following fields:
title,
slug,
account,
profession,
about,
display_services,
city,
location,
featured_image,
carousel_images,
phone_number,
email,
status,
created_on

| Field              | Type              | Description                                            |
|--------------------|-------------------|--------------------------------------------------------|
| title              | CharField        | max_length=80, unique=True                            |
| slug               | SlugField         | max_length=80, unique=True                            |
| account            | ForeignKey       | User, on_delete=models.CASCADE, default=1              |
| profession         | CharField        | max_length=80, default='n/a'                          |
| about              | CharField        | max_length=200, default=''                            |
| display_services   | ManyToManyField  | 'Service', blank=True                                  |
| city               | CharField        | max_length=255, default='n/a'                         |
| location           | PlainLocationField | based_fields=['city'], zoom=7, default='n/a'          |
| featured_image     | CloudinaryField  | 'image', default='placeholder'                        |
| carousel_images    | CloudinaryField  | 'images', default='placeholder'                       |
| phone_number       | CharField        | validators=[phone_regex], max_length=17, blank=False, default='n/a' |
| email              | EmailField       | validators=[validate_email], blank=False, default='n/a' |
| status             | IntegerField     | choices=STATUS, default=0                              |
| created_on         | DateTimeField    | default=timezone.now    


- Service Model is a custom model that contains all the information about the Services created by the business owner so thet can be displayed on the post detail pageand contains the following fields:
service_name,
title,
price

| Field          | Type           | Description                                          |
|----------------|----------------|------------------------------------------------------|
| service_name   | CharField      | max_length=80                                        |
| title          | ForeignKey     | Post, on_delete=models.CASCADE, related_name='services' |
| price          | DecimalField   | max_digits=10, decimal_places=2                       |

## Features

### Existing Features

#### Nav-bar and Logo

- This feature is present throughout entire project and contains links to 'login' or 'register' at first and when a user who is logged in the displays links to 'manage posts' or 'logout'. the navbar is clean and simplistic and makes navigation around the site easy.
- Feature is fully responsive and on smaller screen sizes it coverts into a 'Hamburger menu'

![Navbar](/media/easybook-navbar.jpg )
![Navbar small](/media/easybook-navbar-sm.jpg )

#### HomePage

- The HomePage consists of the business posts. The posts are displayed in a list view as cards. Once their are more than 8 posts the page is paginated and the user can navigate through the pages searching the posts. Each posts is displayed in a card with a featured image, the post title, the profession of the business owner, their location and a link to the post detail page.

![Homepage](/media/easybook-homepage-1.jpg )
![Homepage2](/media/easybook-homepage-2.jpg )

#### Post Detail page

- The post detail page consists are all the businesses information provided in the business post form. At the top of the page is the post title. Under the title is a carousel containing the feature image and any gallery images for the business. On the right hand side of the page is a coloumn containing more business information. at the top is a google maps iframe that will display the businesses location. Under here there is an About section where they can write a paragraph about their business. under this is the contact section displaying their email and phone number. their is also a opening hours section and socials section. Then there is the services section where the businesses can display all of their services they have created. The service name, price and duration is displayed. For Authenticated users there are buttons at the bottom of the page to update and delete the post list. when clicked the update buttom will bring users to a form page where then can update the post and the delete button to a page where they must submit the deletion.

![EasyBook](/media/easybook-post-detail.jpg )
![EasyBook](/media/easybook-post-detail-2.jpg )


#### Services section
- Then there is the services section where the businesses can display all of their services they have created. The service name, price and duration is displayed. Services are cretaed using the create service form on the manage posts page, They are linked to the post when created and then diplayed on the post detail page.

![EasyBook](/media/easybook-services.jpg )
![EasyBook](/media/easybook-services-2.jpg )

#### Manage Posts 

- The Manage Posts page can be access through the link in the navbar. Only authenticated users can access this page. the page is very simple and contains two buttons linking the the create business post form and the create services forms.

![EasyBook](/media/easybook-manage-posts.jpg )

#### Create Services Form

- The create services form is very short and smiple. Users must provide the services name and the price and also provide the post the service is linked to. If a user tries to add a service to a post they didnt create they will be taken to a 404 error page. There is also an update services form where the user can change the service name and price. and a delete service form where they can delete the service from the page and the database.

![EasyBook](/media/easybook-create-service.jpg )
![EasyBook](/media/easybook-update-service.jpg )
![EasyBook](/media/easybook-delete-service.jpg )

#### Post Forms

- The create post form consists are the post title, slug, profession, about, location, city, feature image field and gallery image field along with their phone number and email which both have validators. their is also a stautus input where the user can make their post public or a draft for the admin panel. There is also an update post form where the user can change all the current data and a delete form where then can delete the post from the website and the database. All of the forms are styled with crispy forms and are connected to the database.

![EasyBook](/media/easybook-create-post.jpg )
![EasyBook](/media/easybook-create-post-2.jpg )
![EasyBook](/media/easybook-update-post.jpg )
![EasyBook](/media/easybook-delete-post.jpg )

![EasyBook](/media/easybook-create-service.jpg )

#### Sign Up page
- The sign up page has a form for users to fill out asking for a username, email and password. There is also a message about why users should sign up. when a user successfully signs in there is an alert message displayed on the homepage. Once signed up users have access to our business post features.

![EasyBook](/media/easybook-register.jpg )![EasyBook](/media/easybook-signin-alert.jpg )

#### Sign In page
- The sign in page asks for the users username and password and they can be authenticated.

![EasyBook](/media/easybook-sign-in.jpg )![EasyBook](/media/easybook-signin-alert.jpg )

#### Sign Out page
- The sign out page is also very simple and users must confirm if they want to sign out. There is also an alert displayed when the users signs out. Once they sign out they will be redirected to the homepage but cannot access the account features anymore.

![EasyBook](/media/easybook-signout.jpg )![EasyBook](/media/easybook-signout-alert.jpg )

### Future Features
- Eventually I would like to have Account registion for customers where they have access to more features such as a rate and reviews section where then can rate the business they have used. I would also like to add a booking system so that users can make appointments as a specific time and date where they would also have full CRUD functionality where then can change and cancel appointments. The Business owner would also receive notice of the appointments made and could change or cancal dates to suit their needs aswell. 

- I would also like to add a search bar to the homepage where users can search through posts and services by name, location and Industry. this would only be neccessary if their was a large number of users on the website and navigation through the site became tedious

## Testing

### Manual Testing
I have manually tested this project be doing the following:

#### Navigation
- Expected: All naviation links direct users to the intended pages. Only authenticated users can access the manage posts page.
- Testing: Clicked all link to see if they worked and made sure theyre were no dead links in my code or incorrectly linked. Logged out and navigated through the site looking for a link
- Result: All links work as expected. The link is only displayed in the navbar when users are logged in.
- Fix: No Fix needed.

#### Forms
- Expected: The create post form posts all the data to the database correctly and displayes the post. The users should also be alerted if the posts is created successfully. All required links must be filled and validated correctly.

- Testing: I filled out the form multiple times leaving out each field to see if a was prompted to fill them In. The phone and Email field have validators so they must be in the correct format I checked if these validators were working. once the form was submitted I checked if the user was alerted of the changes and if the post was now being displayed in the Homepage. 

- Result: All fields and validators seemed to be working fine and prompted my when they werent filled out. When the form was filled out and sumbitted I noticed that I was not alerted if it was successful or not. I there checked if the post was diplaying which it was but I noticed that the placeholder for the images was still displaying and this was unexpected. I then went to the admin panel to see if the data in the form was successfully posted to the database. I learned that everything was working perfectly except for the images files so there were a number of things that needed fixing. I also noticed that my delete post form page had the heading "List Your Businees" which would've been misleading so this had to be changed. The form where not responsive for smaller screen and were very basic so needed some styling

- Fix: I had to add enctype="multipart/form-data" to the form element so that images could be uploaded. This fixed the images problem straight away. I then fixed the heading on the Delete post form by creating a new template for the form and adjucting the view. I also installed crispy forms to make my forms look better and added some styling with bootstrap classes to make it fully responsive. I also added alerts for when the forms were created updated and deleted. I done this by adding the get_success_method()
to my views. 

#### Responsiveness
- Expected: That all pages are fully responsive on all screen sizes small, medium and large.

- Testing: I checked the responsiveness of each page in the chrome dev tools and selected every different screen size that was available.

- Result: the and the forms were not responsive so they needed to be adjusted. The post detail page was also not responsive so needed some adjustment to the bootstrap classes. The card images where also not responsive as they were a fixed height so this needed to be adjusted.

- Fix: I adjusted my bootstrap classes and divs to make everything more responsive on small screens.

#### User Account
- Expected: Users can login, sign up and logout sucesssfully. They must provide a valid username and password. Once users are logged in they can use the authenticated functionality eg. making posts. When users login, logout or register they should be alerted if successful. If the user provides details that do not match the criteria they should be prompted and not able to make an account.

- Testing: I first registered for an account. I typed 'TEST' into the email field and first then a properly formatted email. I then typed 'test123' for the password and then 'test1234' then a matching password. Then I typed a more complicated password. then I typed the username 'Test Account 123' and then 'TestAccount123'

- Result: I was promped correctly for each, the mismatched passwords, for the password being to similar to username and also being to small. The username and passwords must not contain spaces and the user was prompted correctly. If an incorrect email was typed in it was not accepted and the user was prompted to fix it. Everything was working perfectly expect the user was not alerted upon a successful sign in or when logging out.

- Fix: I had to add alert messages for when the user registered, logged in and logged out successfully. I added the messages for loop to the 'base.html' file and the alert popped under just under the nave bar. I added "from django.contrib.messages import constants as messages" to the settings.py file along with all the message tags. I also added some JavaScript so that the messages faded away after 3 seconds. I done this by adding a script tag to the bottom of my 'base.html' page defining my messages by ID and a alert variable also and used the setTimeout function. 


#### Validators
- HTML: No errors with Html although the Django tags were causing errors [HTML Validator](https://validator.w3.org/)
- CSS: No errors found when passed through [CSS Validator](https://jigsaw.w3.org/css-validator/validator)
- Python: No errors when passed through [PEP8 Linter](https://pep8ci.herokuapp.com/) and also Flake8 in the gitpod terminal.
- JavaScript: I tested my javascript manually by checking if all of my message alerts dissappeared after 3 seconds.

#### Performance

- lighthouse: This was my performance result on lighthouse.

![LightHouse](/media/easybook-lighthouse.jpg )

## Technologies Used

### Languages & Frameworks

- HTML 
- CSS
- Javascript
- Boostrap 4
- Python
- Django

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/) was usedfor creating the multi-device mock-up at the top of this README.md file
- [Bootstrap 4.2](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer Pagination, Navbar)
- [Cloudinary](https://cloudinary.com/) to store static files
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/) - for the typography in the project
- [Cripsy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - for styling my forms
- Paint - for photoshop and editing images.

## Deployment

This Project was initailly deployed on Heroku. To avoid any potential deployment issues when deploying I made sure that the database and static files were accessible right from the start of the project.

### Creating The Database

1. To generate a managed PostgreSQL database, Go to [ElephantSQL](https://customer.elephantsql.com/) and sign up to your account using Github. Once you've logged in, click on the 'Create New Instance' button.

2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'

3. Select your preferred region and create the database instance. After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section copy the PostgreSQL URL and paste into Heroku App.

### Heroku Deployment

1. Login to Heroku and make a new app from the dashboard.

2. Once your app has been created, select the 'Settings' tab from the dashboard and navigate to 'Reveal Config Vars'. From there, paste the: 
    - ElephantSQL Database URL into the DATABASE_URL environment variable.
    - SECRET_KEY variable  into the SECRET_KEY environment variable.
    - CLOUDINARY_URL variable  into the CLOUDINARY_URL environment variable.
    - add DISABLE_COLLECTSTATIC variablewith value of 1 (for initial deployment, later this variable can be removed)
    - add variable named PORT with value of 8000

3. Connect you app to your GitHub repository in the 'Deploy' section 

4. At the bottom of the page, Deploy your project either Automatically or Manually by branch

## Credits

- To my mentor, Andre Aquilina , for guiding me through the process and offering assistance when neccesary to point me in the right direction.
- The Slack community. The help a student is able to receive from the other students is a really great tool to have.
- To all at Code Institute, the videos and information I received helped me create my Fourth portfolio project.
- To the Very Academy Youtube Channel, their series on Django class based views was very informative and helped massively in my project.
- To the Django Documentation which I revised constantly throughout the project.
- To Heroku for the live version of the deployed project
- To ElelpantSQL where I stored my Database data
- To Cloudinary where I stored my images for this project
- To Google where I got my API key for my Google maps iFrame
- To Gitpod and Github where I coded the program and held this Repository
- To StackOverflow which helped be to solve bugs in my code and helped with my understanding of python and Django.