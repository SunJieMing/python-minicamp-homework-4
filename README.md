# Homework #4 - 

## Instructions
---
1. Install Git  [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).



2. Create a Github account - it's free.



3. Fork [this](https://github.com/SunJieMing/python-minicamp-homework-4) repo and clone it to your computer using the terminal command `git clone <url>`.  Navigate into the cloned folder and build your homework project there.

4. As you make changes and decide to commit your code follow these commands:

	```
    git status //You'll see all of the files you've changed show up in red
    git add --all //this command stages all of your changes for commit
    git status //All of the red files should now be green
    git commit -m "<your commit message here>" //this commits your changes
    git status //All of the file names should no longer appear
    git push origin master //This pushes your changes up to the cloud
	```
    
5. Setup your virtual environment and build a simple Flask API with three routes:

	* (`/`) - This route should return your base HTML file.
    * (`/movie`) - This route should accept a POST request and save some info about a movie to your sqlite database.
    * (`/movies`) - This route will return the JSON for all movies in your database.
    * You can verify that you are successfully adding data by uploading your database file [here](http://inloop.github.io/sqlite-viewer/).


6. Create a `/static` folder with a `/styles` folder inside and a `styles.css` inside of the `/styles` folder.  (`/static/styles/styles.css`)  Create a `/templates` folder with a `home.html` file.  Create a form to submit movie data to your API.  Link the stylesheet to your home template and customize the look and feel of your application.


---

### Extra Credit

1. Add a (`/search`) route to retrieve a specific movie from the database.  This will be very similar to the extra credit from the homework for day 3.



2. Fork, clone and run Homework #3's solution branch in the repo.  `git pull origin solution`


3. Continue to play around with building your own routes and think of different ways you can interact with the database.  We will be moving on to more client side coding after this and will be cloning down prebuilt servers for future homework assignments.


---
#### Congratulations on finishing Homework #4!
Apply to our full time or part time immersive program to learn cutting edge technologies that are used by top technology companies around the world.

Our part time and full time courses are 13 intense weeks of focused study on the most relevant technologies.  

Class sizes are small to ensure that each student gets individual attention from our world class instructors to help them succeed.

For more information visit: www.lambdaschool.com
