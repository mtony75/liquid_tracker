README
This is my practice program to track liquid that is put in a refrigerator.
It tracks the name of the liquid, expiration date, and how long till the 
liquid expires.  

Note 8/25/2015 1:20 am
Added logic to checkValidDate function to check if date entered by user is before
current day's date. If so a check fails and a message is sent to the user. 

11:24 am
Importing os library to use clearscreen method (os.system('cls')) to implement menu

Note 8/24/2015 1:53 am
Added basic logic for function checkValidDate to do date check.
added code to convert user inputed date (that is a string) into a datetime date.