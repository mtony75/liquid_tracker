README
This is my practice program to track liquid that is put in a refrigerator.
It tracks the name of the liquid, expiration date, and how long till the 
liquid expires.  

Note 9/2/2015 1:12 am
Modified made execution block to print attributes of liquid. Will prefect
and move into separate method. 
Created isLeft function to return int value of amount of liquid left.
Modified whenExpire to return date of expiration of liquid. 
Moved code to list liquids to listLiquid function. Function accepts the
liquidInventory list so it can perform its operation "listLiquid(liquidInventory)"


Note 9/1/2015 12:28 am
Added way to add objects to list for Inventory storing (no state save).
Will modularize functions during week.

Note 8/29/2015 11:19 am
Will create a list called liquidInventory to hold liquid objects.
11:55 pm
Need to create an exception for accepting date so program does not 
halt when a none date is entered. 
Added menu for initial selection.

Note 8/26/2015 11:13 pm
May have to implement a sub menu for liquid specific functions
i.e. Pour, Delete, isGood, daysLeft.
Will research best way to implement.
Note 8/25/2015 1:20 am
Added logic to checkValidDate function to check if date entered by user is before
current day's date. If so a check fails and a message is sent to the user. 

11:24 am
Importing os library to use clearscreen method (os.system('cls')) to implement menu

Note 8/24/2015 1:53 am
Added basic logic for function checkValidDate to do date check.
added code to convert user entered date (that is a string) into a datetime date.
