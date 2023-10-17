
# College Faculty Feedback Automation

## Overview
This Python script automates the process of providing feedback on faculty members for each semester. The project was developed to simplify and streamline the time-consuming task of filling out lengthy feedback forms on the college portal, which typically consists of over 150+ questions.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User Inputs**: The script takes the SAP ID, password, and the desired rating as user inputs.
- **Automation**: It automates the entire process of logging in and submitting feedback.
- **Generalized**: The code is generalized to work with different branches and years of engineering students.

## Requirements
- [Python](https://www.python.org/) 3.x
- [Selenium](https://selenium-python.readthedocs.io/) Python library
- [Chrome WebDriver](https://sites.google.com/chromium.org/driver/)

## Usage
1. Clone this repository to your local machine.
   ```
   git clone https://github.com/yourusername/college-faculty-feedback-automation.git
   ```

2. Install the required Python libraries.
   ```
   pip install selenium
   ```

3. Download and set up the Chrome WebDriver according to your system specifications.

4. Edit the script with your favorite code editor, providing your SAP ID, password, and the desired rating.

5. Run the script.
   ```
   python feedback_automation.py
   ```

6. Sit back and watch as the script automates the feedback submission process for you.

## Future Improvements
- **Randomized Ratings**: Add a feature to randomize ratings for more authentic feedback.
- **Specific Feedback**: Allow users to specify particular professors or subjects for different ratings.
- **Improved Error Handling**: Enhance error handling and provide detailed error messages.
- **Data Logging**: Implement a logging system to keep track of feedback provided.

## Contributing
Contributions to the project are welcome! Feel free to submit pull requests, report issues, or suggest new features or improvements.
