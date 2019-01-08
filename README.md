# CookieCover

A script that automatically fills a resume with the information from employers. This was created to automate the making of cover letters for Co-op

## Getting Started

Clone the repository or copy the 3 files

### Prerequisites

Install Python 3

### Installing

Install a chrome webdriver and change the following line to reflect its path

```
driver = webdriver.Chrome("C:/Users/Bradley/AppData/Local/Programs/Python/Python35/Scripts/chromedriver.exe")
```

Enter your username and password into the config file

```
{
  "username" : "Your username here",
  "password" : "Your password here"
}
```

## Running
Run the program using the following command

```
python htmlParser.py
```

Wait for the program to bring up the website and log in
Navigate to the job posting of your choosing
When you have selected the desired job posting, enter "y" in the command line to generate a cover letter

```
Are you ready?
y
```

## Authors

* **Bradley Leonard**
