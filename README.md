# Dome Restaurant 

## Notes during coding process

I am starting to have second thoughts concerning my setup of having a detailed view for each specific booking. I am now thinking that maybe I should have a layout that gives all the information about each booking directly to the user, and by doing so removing an additional step the user need to take in order to get information.

### List of libraries

- Django-allauth 

### List of bugs

- Problems with search function: Either I got all reservations and the search didn't work, or I didn't get any reservations at all, or non-admin users could see all reservations, and so on.

    - Restructuring the get_queryset method in the IndexReservation class in views.py a number of times until I got the logic to work did the trick.

- Problems with making reservations: There seem to be a problem with updating reservations. Even though I only have one reservation during a specific date and plenty of tables available, I can't seem to update the reservation to another time during the same date. I get "Sorry we do not have a table with that capacity available".
