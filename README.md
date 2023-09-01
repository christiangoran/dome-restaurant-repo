# Dome Restaurant 



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
|**Bookings**      KLAR                     |  ||
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


### Strategy

### Scope

<hr>

### Structure

<hr>

### Skeleton

<hr>

### Surface

<hr>

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
