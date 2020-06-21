# moviezap
MovieZap Django based webpage which helps in telling Top50 movies based on year of movie release , language and genre of the movie..

Prerequisites
1. Install Python

    Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System.                           Reference: https://docs.python-guide.org/starting/installation/

2. Setup virtual environment

    #install virtualenv 
    
    sudo pip install virtualenv

    #make directory for virtualenv
    
    mkdir envs

    #Create virtual environment
    
    virtualenv envs

    #Activate virtual environment
        
        . envs/bin/activate

3. Clone git repository

    git clone https://github.com/Dhuvaraggn/moviezap.git
    
4. Install requirements

    cd moviezap/
    pip install -r requirements.txt
    
5. Run the server

     #Make migrations
        python manage.py makemigrations
        python manage.py migrate

    #Run the server
        python manage.py runserver 0:8000

    #your server is up on port 8000
    
    Try opening http://localhost:8001 in the browser. Now you are good to go.

URLS
    start page : http://localhost:8000/intro/
    
