
<h1>iStudy</h1>


# iStudy

iStudy is a web-based platform designed to revolutionize online learning and collaboration among students and instructors. With its intuitive interface and powerful features, iStudy offers a seamless experience for both educators and learners.

## Description

iStudy provides a comprehensive suite of tools for managing courses, assignments, discussions, and more. Whether you're a student looking to engage with course materials or an instructor seeking to streamline your teaching process, iStudy has you covered. From assignment submissions to grading, from lively discussions to course enrollment, iStudy simplifies every aspect of online education.

## Getting Started

Follow these steps to set up iStudy on your local machine:

### Prerequisites

- Python 3.x installed on your system
- pip package manager

### Installation


# cloning project 

git clone <repository_url>

cd iStudy

# create virtual environnement
python -m venv env   

# activate the virtual environnement
.\env\Scripts\activate  

# istall requirements

pip install -r requirements.txt

# Database Setup 

python manage.py migrate
python manage.py createsuperuser


# Running the Server

python manage.py runserver


Access iStudy in your web browser at http://localhost:8000.


