# Web-Scraping Exercise:

## This repository contains the files regarding a web-scraping exercise.
This folder contains the following:
<br>
1 Jupyter Notebook file called mission_to_mars.ipynb.
<br>
2 Python files called scrape_mars.py and app.py.
<br>
1 folder called Templates that contains an HTML file called index.html.
<br>
1 folder called Output that contains 6 text files generated from the jupyter notebook file that were used to analyze the HTML extracted from different websites, and 1 HTML file generated from the jupyter notebook file. 
<br>
2 screenshots of the final website.


## WEB SCRAPING:
We created a jupyter notebook file and used Beautiful Soup, Splinter and Pandas to scrape data from the following 5 websites:

### NASA Mars News Website: 
https://mars.nasa.gov/news 
<br>
We scraped this website and extracted the title and the description paragraph of the latest Mars news article.

### JPL Mars Space Image Website: 
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars 
<br>
We scraped this website and extracted the image url for the current featured Mars image.

### Mars Twitter Page: 
https://twitter.com/marswxreport?lang=en 
<br>
We scraped this website and extracted the latest Mars weather tweet. 

### Mars Facts Website: 
https://space-facts.com/mars/
<br>
We scraped this website and extracted a table containing facts about Mars such as the planet’s diameter, mass, etc.

### Mars Hemispheres Website: 
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars 
<br>
We scraped this website and extracted the title and the full resolution image for each of Mars’s hemispheres. 



## CREATION OF A SCRAPING FUNCTION AND A WEB-PAGE TO DISPLAY THE RESULTS:

### Creation of a file with a “scrape” function:
We then created a new file called scrape_mars.py.
<br>
In this file, we created a function called "scrape" that incorporates all the logic from the jupyter notebook file to scrape the details from the 5 websites mentioned above.

### Creation of an html file:
We then created an html file called index.html to display the results returned from running the scrape function mentioned above. This html file divides the webpage into 5 distinct sections:
<br>
•	Top Section: 
<br>
This contains the website heading and also a button linked to the scrape function. A user can click this button and that will scrape the data from the 5 websites.
<br>
•	Middle Section - 1:
<br>
This contains the title and a description paragraph of the latest Mars news article from the NASA website.
<br>
•	Middle Section – 2 - Left:
<br>
This contains the current featured image from the JPL Mars Space Image Website.
<br>
•	Middle Section – 2 - Right:
<br>
This contains the latest Mars weather tweet from the Mars weather twitter account.
<br>
This also contains facts about Mars such as the planet’s diameter, mass, etc.
<br>
•	Bottom Section – 1:
<br>
This contains a heading for the section on the Mars Hemispheres.
<br>
•	Bottom Section – 2:
<br>
This contains the full resolution images of the 4 Mars hemispheres.


### Creation of an “app” file:
We then created a new file called app.py.
<br>
In this file we import (as a module) the scrape_mars.py file which contains the “scrape” function.
<br>
We then use the render template module to link the html file to the results from running the scrape function, so that we can display the results on a webpage using the template provided by the html file.


## IMAGES OF THE FINAL WEBPAGE:

### Top Portion of the Webpage:
![](images/Website_Screenshot_01.PNG)

### Bottom Portion of the Webpage:
![](images/Website_Screenshot_02.PNG)
