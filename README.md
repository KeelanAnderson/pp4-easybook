# EasyBook

EasyBook is an app designed for small business owners to make a post for their business and display all the relevant information about their business such as location, opening hours, services, contact info etc. By displaying this information it will make it easy for customers to find out about their business and make appointments online. Site users can create an account and then create a business post on our site. They have full CRUD functionality and can Create, Update and Delete posts. This Project was created during Agile development and is in its early stages with plans to add increasing functionality and value to the website.

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

#### HomePage

#### Post Detail page

#### Services section

#### Manage Posts 

#### Create Services Form

#### Create Post Form

### Future Features

## Testing

### Manual Testing
I have manually tested this project be doing the following:

#### Navigation
- Expected:
- Testing:
- Result:
- Fix:

#### Forms
- Expected:
- Testing:
- Result:
- Fix:

#### Responsiveness
- Expected:
- Testing:
- Result:
- Fix:

#### User Account
- Expected:
- Testing:
- Result:
- Fix:

#### Content
- Expected:
- Testing:
- Result:
- Fix:

#### Performance
- Expected:
- Testing:
- Result:
- Fix:

### Bugs


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
- [Google Fonts](https://fonts.google.com/) - for typography in project

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