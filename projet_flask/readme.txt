Architecture du projet:

├───Authentication   #module
│   ├───static
│   │   ├───css
│   │   └───images # image file
│   ├───templates #contains different web pages of my project : home.html  - register.html -  login.html -  profile.html
│   │   └───partials #contains common  a common _navbar html script that is extended through out the rest of the templates
│   └───__pycache__
└───__pycache__


__init__  :
                contains statement and imports used to create the app
routes :
                  contains different endpoints of my project
forms :
             flask creation of forms which i used to create the Registrationform and loginforms and their validation
models :
                    contains the statemsnts of the User creation 
ecommerce.db  :
                an sqlite database for our User table
main :
                        the run point of the ├───Authentication application


Owner: Israel AHONYO 

Note:  the static/css/ navbar.css  wasn't effectively working on the pages  so I had to put all my styles  directly on the pages using the style tag  