# Simple task for Luxonis interview

The project consists of two services
* scraper 
  * scrapes first 500 flats for sale from sreality.cz server, stores them in database and exits
* web
  * Displays simple web page with all 500 offers scraped

The project was written as a prototype, so the simplicity and speed of development was preferred against best practices and maintainability.

**Possible improvements**
 * Use pip-compile to track requirements
 * Do not hardcode waiting for db
 * Use migrations instead of db init script
 * Use db connection pool instead of opening separate connection each time
 * Better design of listed flats
 * Preserve order of flats
 * Ensure there are no duplicates or missing offers in case the list of offers changes during crawling SReality
 * Better code format and structure
