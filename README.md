# Lightbulb-Hypothesis-testing

This project is a simple web application built using Flask to perform hypothesis testing on the lifespan of bulbs based on data imported from the Minitab dataset library. The application allows users to upload a CSV file containing bulb lifespan data and then evaluates the company's claim about the average lifespan using statistical methods.

# Project Overview
This project takes a dataset containing the "Hours" of bulb lifespan as input. It then performs a t-test to compare the sample mean from the data with the population mean (provided by the company as a claim). The output is a decision on whether the company's claim about the lifespan of the bulbs is statistically acceptable or not.

# Technologies Used
Python (Flask for web framework, Pandas for data handling, SciPy for statistical calculations)
HTML (Templates for rendering pages)
CSS (for basic styling)

# How to Run the Application
1) Install the required packages: Make sure you have Python installed on your machine. You can install the required packages using the following command:
   pip install Flask pandas numpy scipy
2) Run the Flask Application: To start the application, run the following command:
   python app.py
3) Access the Application: Open your browser and navigate to http://localhost:5001.

# Project Structure
.
├── app.py              
├── templates
│   ├── index.html       
│   ├── result.html      
├── static               
└── README.md  
