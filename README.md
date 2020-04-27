# Web-Scraping Exercise:

## This repository contains the files regarding a web-scraping exercise.
This folder contains the following:
1.	Jupyter Notebook file:
a.	mission_to_mars.ipynb
2.	Python files:
a.	scrape_mars.py
b.	app.py
3.	Templates Folder that contains an HTML file: 
a.	index.html
4.	Output folder that contains:
a.	6 text files generated from the jupyter notebook file that were used to analyze the HTML extracted from different websites.
b.	HTML file generated from the jupyter notebook file. 
5.	Screenshots of the final website:
a.	2 Screenshots showing the top half and the bottom half of the final webpage.



## WEB SCRAPING:
We created a jupyter notebook file and used Beautiful Soup, Splinter and Pandas to scrape data from the following websites:

### NASA Mars News Website: 
https://mars.nasa.gov/news 
We scraped this website and extracted the title and the description paragraph of the latest Mars news article.

### JPL Mars Space Image Website: 
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars 
We scraped this website and extracted the image url for the current featured Mars image.

### Mars Twitter Page: 
https://twitter.com/marswxreport?lang=en 
We scraped this website and extracted the latest Mars weather tweet. 

### Mars Facts Website: 
https://space-facts.com/mars/
We scraped this website and extracted a table containing facts about Mars such as the planet’s diameter, mass, etc.

### Mars Hemispheres Website: 
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars 
We scraped this website and extracted the titles and the full resolution image for each of Mars’s hemispheres. 



## CREATION OF A SCRAPING FUNCTION AND A WEB-PAGE TO DISPLAY THE RESULTS:

### Creation of a file with a “scrape” function:
We then created a new file called scrape_mars.py.
In this file we created a function called scrape that incorporates all the logic from the jupyter notebook file to scrape the details from the 5 websites mentioned above.

### Creation of an html file:
We then created an html file called index.html to display the results returned from running the scrape function mentioned above. This html file divides the webpage into 5 distinct sections:
1.	Top Section:
This contains the website heading and also a button linked to the scrape function. A user can click this button and that will scrape the data from the 5 websites.
2.	Middle Section - 1:
This contains the title and a description paragraph of the latest Mars news article from the NASA website:
3.	Middle Section – 2 - Left:
This contains the current featured image from the JPL Mars Space Image Website. 
4.	Middle Section – 2 - Right:
This contains the latest Mars weather tweet from the Mars weather twitter account.
This also contains facts about Mars such as the planet’s diameter, mass, etc.
5.	Bottom Section – 1:
This contains a heading for the section on the Mars Hemispheres.
6.	Bottom Section – 2:
This contains the full resolution images of the 4 Mars hemispheres.

### Creation of an “app” file:
We then created a new file called app.py.
In this file we import (as a module) the scrape_mars.py file which contains the “scrape” function.
We then use the render template module to link the html file to the results from running the scrape function, so that we can display the results on a webpage using the template provided by the html file.


## IMAGES OF THE FINAL WEBPAGE:
![](Missions_to_Mars/Website_Screenshot_01.png)



