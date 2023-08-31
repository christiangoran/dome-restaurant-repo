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
