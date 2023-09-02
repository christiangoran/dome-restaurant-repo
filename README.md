# Dome Restaurant 

<img src="https://res.cloudinary.com/dzw4z92rn/image/upload/v1692852991/static/images/bg.c2eb0cc111ba.jpg" ><br>
<hr>

## Notes during coding process

I am starting to have second thoughts concerning my setup of having a detailed view for each specific booking. I am now thinking that maybe I should have a layout that gives all the information about each booking directly to the user, and by doing so removing an additional step the user need to take in order to get information.

### List of libraries

- Django-allauth 

### List of bugs

- Problems with search function: Either I got all reservations and the search didn't work, or I didn't get any reservations at all, or non-admin users could see all reservations, and so on.

    - Restructuring the get_queryset method in the IndexReservation class in views.py a number of times until I got the logic to work did the trick.

- Problems with making reservations: There seem to be a problem with updating reservations. Even though I only have one reservation during a specific date and plenty of tables available, I can't seem to update the reservation to another time during the same date. I get "Sorry we do not have a table with that capacity available".


## Table of contents
  * [Overview](#overview)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope-hr-)
    + [Structure](#structure-hr-)
    + [Skeleton](#skeleton-hr-)
    + [Surface](#surface-hr-)
      - [Color Scheme](#color-scheme)
      - [Fonts](#fonts)
      - [Visual Effects](#visual-effects)
  * [Agile Methodology](#agile-methodology)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Create bookings](#create-bookings)
      - [Menu](#menu)
      - [Profiles](#profiles)
      - [Staff bookings management](#staff-bookings-management)
    + [Future Feature Considerations](#future-feature-considerations)
  * [Responsive Layout and Design](#responsive-layout-and-design)
  * [Tools Used](#tools-used)
    + [Python packages](#python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Deploy on heroku](#deploy-on-heroku)
    + [FORK THE REPOSITORY](#fork-the-repository)
    + [CLONE THE REPOSITORY](#clone-the-repository)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Code](#code)
  * [Acknowledgements](#acknowledgements)

## Overview
This project serves as a comprehensive booking and management platform for the Dome Restaurant. The platform allows customers to easily reserve tables, add special notes for their bookings, and specify the number of guests. On the other side, staff members can manage these bookings efficiently through a staff-only interface. The system ensures that only available tables are offered to the customers, considering variables like time, date, and capacity. The platform is designed to handle real-world scenarios with ease. The application was built using Python (Django), HTML, CSS, and JavaScript, with data being stored in a PostgreSQL database and images on a Cloudinary account.

<br><br>
The deployed project can be accessed at [this link](https://dome-restaurant-hero-9071346b8ec2.herokuapp.com/).
<br><br>

## UX
This site was created according to the Five Planes Of Website Design:<br>
### Strategy<hr>

**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**Base Setup**                         |  ||
|                                       |1A| As a developer, I need to create the base.html page and structure so that other pages can reuse the layout|             
|                                       |1B| As a developer, I need to create static resources so that images, css and javascript work on the website|
|                                       |1C| As a site user I can see a navigation menu so that I can easily navigate through the site|
|                                       |1D| As a site user I can have a good UX/UI experience when browsing the site so that I am encouraged to stay on the website and eventually also visit the restaurant|
|                                       |1E| As a developer, I need to set up the project so that it is ready for implementing the necessary features|
|                                       |1F| As a developer, I need to create the footer for social media links and contact information|
|**Stand Alone Pages**                  |  ||
|                                       |2A| As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist|
|                                       |2B| As a developer, I need to implement a 500 error page to alert users when an internal server error occurs|
|                                       |2C| As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views|
|                                       |2D| As a restaurant owner, I would like a home page so that customers can view information on my restaurant|
|**Authentication**                     |  ||
|                                       |3A| As a site user I can create an account so that I can create reservations in my name|
|                                       |3B| As a site user I can use my email and password to login so that my account is secure|
|                                       |3C| As a site user I can logout from my account so that I keep my account secure|
|                                       |3D| As a site user I can reset my password by sending a link so that I can login even if I forgot my password|
|**Contact**                            |  ||
|                                       |4A| As a user, I want to see the restaurant's opening and closing hours|
|                                       |4B| As a user, I want to see location information on the website|
|                                       |4C| As a user, I want to see contact information on the website|
|                                       |4D| As a user, I want to see relevant information on the website|
|**Menu**                               |  ||
|                                       |5A| As a user, I want to see the restaurant's menu with details about ingredients and price, so that I can be completely aware of everything I want to order|
|                                       |5B| As a staff member I can update menu items so that I have an easier time managing dish items|
|**Bookings**                           |  ||
|                                       |6A| As a logged in user I can se a list of my reservations so that I can have a better overview|
|                                       |6B| As a logged-in staff member I can see upcoming reservations so that we can prepare the working day|
|                                       |6C| As a logged-in staff member I can filter  reservations so that I can see reservations for a specific date|
|                                       |6D| As a logged-in user I can update a selected reservation so that choose a more convenient time|
|                                       |6E| As a logged-in staff member I can update a selected reservation to help clients|X
|                                       |6F| As a logged-in user I can delete reservations so that I have control over my bookings|
|                                       |6G| As a logged-in staff member I can cancel bookings so that I can help a client with the cancellation|
|                                       |6H| As a logged-in user I can select a time and date so that to finalize my reservation|
|                                       |6I| As a logged-in user I can see available tables for a specific date and time so that I can easier devide where to sit|
|                                       |6J| As a site user I get confirmation email when making a reservation so that the risk of becoming a no-show-reservation is minimized|
|**Deployment**                         |  ||
|                                       |7A| As a developer, I need to remove comments, turn of DEBUG so that my project is ready for final deployment|
|                                       |7B| As a developer, I need to deploy the project to heroku so that it is live for customers|
|**Documentation**                      |  ||
|                                       |8A| As a developer I need to write automated tests  and testing documentation so that others and myself can better understand my project|
|                                       |8B| As a developer I need to write readme.md so that others and myself can better understand my project|

**Project Goal:**<br>
The goal for the project is to create a website with good UX/UI in mind that is usefull to staff members and clients. The website should convey an emotional response in the user.

**Project Objectives:**<br>
* To create a simple and intuitive website that with the help of UX conveys an positive emotional response in the user;
* The design and content should help instill a better image of the client and their business;
* To make to clear categories of login accounts for staff members and clients;
* To implement features and design that upgrade the users experience;
* To make a responsive website that works on every device.<br><br>

### Scope<hr>
**Simple and Intuitive UX**<br>
* Create a website that follows the graphical profile and theme of the client;
* Create a header and a footer;
* Create a navbar that is visible throughout the website;
* Ensure that all user changes are notified to the user visually;
* Ensure that the user keeps their orientation during their navigation througout the website.

**Relevant Content**<br>
* Add relevant information about the restaurant, including its name, location, phone number and email;
* Create a clear and attrative presentation of the restaurant menu;
* Add photos that depict some of the food offered at the restaurant.

**Features for Upgraded Experience**<br>
* Create a reservation section that allows the users to see all the reservations  available for a specific date and time:
* Create a Menu feature that displays all the menu information;
* Create a Profile page for the user to see his upcoming bookings and favourite meals;
* Create a staff-member account to manage all the bookings for all the users;

**Clints % Staff Members Different Accounts**<br>
* Allow access to Profile page only for client type of users;
* Allow access to Manage Bookings page only for staff members type of users;
* Create a filter function only visible for staff-members for them to find specific reservations.

**Responsiveness**<br>
* Create a responsive website that works on every device and screen size.<br><br>

### Structure<hr>
The website is designed with a focus on user experience and is divided into 6 distinct pages, each serving a specific purpose. The content displayed on these pages varies based on whether the user is authenticated and whether they are a client or staff member. Here are the details:

* Register/Login: These pages allow users to create an account or authenticate into an existing one, providing access to various exclusive features.
* Logout: This is implemented as a modal dialog that allows users to securely log out of their accounts.
* Home: Accessible to all users, this page showcases the restaurant's ambiance, popular dishes, opening & closing times and contact info.
* Menu: This page displays the restaurant's menu items. An "Add to Favourite" feature is available only to logged-in clients.
* Reservations/profile: Exclusive to authenticated users, this page enables both clients and staff members to make or manage bookings.
* Staff Manage Bookings: Accessible only to staff members, this page displays all registered bookings, which can be grouped and filtered by date.

* FLOWCHARTS
The project flow chart was created using <b>LucidChart</b>.<br><br>
[![N|Solid](static/images/flow_chart.png)](static/images/flow_chart.png)<br><br>

### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed [here](link goes here)<br>

**Database**<br>
The project uses ElephantSQL as PostgreSQL relational database for storing the data.<br>
Two diagrams were created to represent the relationships between the tables. The first diagram was created before the website was developed, and it was used to identify the most relevant and useful attributes and tables. The final diagram was created after the website was developed, and it reflects the changes that were made to the attributes and tables.

<details>
  <summary>Initial Schema</summary>
<img src="static/images/datamodel_plan.png" ><br>
</details>

<details>
  <summary>Final Schema</summary>
<img src="static/images/datamodel.png"><br>
</details><br>

### Surface<hr>

#### Color Scheme

#### Fonts

#### Visual Effects

## Agile Methodology

## Features

### Existing Features

#### Create bookings

#### Menu

#### Profiles

#### Staff bookings management

### Future Feature Considerations

## Responsive Layout and Design

## Tools Used

### Python packages

## Testing

## Deployment

### Deploy on Heroku

### FORK THE REPOSITORY

### CLONE THE REPOSITORY

## Credits

### Content

### Media

### Code

## Acknowledgements
