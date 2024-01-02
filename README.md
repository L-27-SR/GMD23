# Global Military Database 2023 (GMD 23)
#### Video Demo:  <https://youtu.be/u8G6jRVFX1w>
#### Description:

The project is a website which displays the military information of all the countries divided into different webpages for each category in the form of a searchable and sortable table.

Technologies used:

Front-end:
- HTML
- JavaScript
- CSS
- Bootstrap
Back-end:
- Python
- sqlite3
Frameworks:
- Flask
- other small libraries or packages

## How the webpage works?

The webpage consists of a navigation bar which leads you to 4 different webpages:

- Homepage (Global Military Database 2023)
- Navy
- Army
- Airforce

### Homepage

This is the main page of the website and consists of a search bar, which allows you to search for any information on google.
Below the search bar is a button, which on clicking displays your current location (the latitude and longitude).
Below the coordinates button is a sortable table that displays the details of the countries possessing nuclear power. This table is sortable
and can be sorted by countries alphabetically or by Total, Active, Available and Retired nuclear power in the ascending or descending order.

### Navy

The Navy page can be accessed by clicking the first link on the right hand corner of the navigation bar. This web page consists of a quote right below the navigation bar, followed by a search bar that lets you search for a particular country in the table followed by a searchable and sortable table which can be ordered alphabetically by country or by Total Ships, Carriers, Heli Carriers, Submarines, Destroyers and Frigates in the ascending or descending order.
The information in this table is stored in the navy table in the details.db database.

### Army

The Army page can be accessed by clicking the second link on the right hand corner of the navigation bar. This web page consists of a quote right below the navigation bar, followed by a search bar that lets you search for a particular country in the table followed by a searchable and sortable table which can be ordered alphabetically by country or by Active Personnel, Para Military, Reserves, Total and Population in the ascending or descending order.
The information in this table is stored in the arm table in the details.db database.

### Air Force

The Air Force page can be accessed by clicking the third link on the right hand corner of the navigation bar. This web page consists of a quote right below the navigation bar, followed by a search bar that lets you search for a particular country in the table followed by a searchable and sortable table which can be ordered alphabetically by country or by Total Aircrafts, Air Force, Army, Navy and Marines in the ascending or descending order.
The information in this table is stored in the air table in the details.db database.

### Database

The Database details.db contains 4 tables:
- arm
- air
- navy
- nuclear

These tables contain information about all the countries and the respective fields which were used to display information in the website in the form of tables.

## References

- Bootstrap
    Used for the aesthetic art of the webpage.
- www.globalfirepower.com
    To get data about the firepowers of various nations.
- konbert.com
    To convert .json files to .sql files.
- www.w3schools.com
    To gain information about creating more presentable and attractive webpages.
