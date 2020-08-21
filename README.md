# BlackProduct.Review-backend

This is the backend project for BlackProduct.Review.  We will be using pip and
pyenv for this project due to deployment ease.  Make sure to follow these
steps:  

1) make sure pip is up to date
2) install python 3.8.5
3) run virtual environment with pipenv shell

The reason why we can get it off the ground like this is because we are 
starting our development period right now and it would be best for everyone to 
be able to just clone it and go rather than trying to figure out which 
dependencies are needed.  Poetry is better for collaborative work, but pyenv 
best for deployment as Heroku has build packs that supplement pyenv, but not poetry.  That being said, Here is what we are going for in terms of fields:

1) Business (model)

   -owner
   
   -urlfield
   
   -emailfield
   
   -address
 
2) Product (model)

   -like and dislike(field)
   
   -rating(field)
   
   -business
   
   -market
   
   -product type
   
   -file upoloading
   
   -urlfield
   
   -reviews
   
   -tag
   
   -times viewed
   
3) Reviews (model)

   -Like and dislike (field
   
   -rating
   
   -CustomStaffUser

   -Time Posted

4) CustomStaffUser

5) Market
   - How many times something was searched
