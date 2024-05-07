# Phish Hook
Your ultimate Webtool-box for detecting phishing content in emails, links, and webpages. Equiped with AI and database analysis reeling in a safer browsing experience.

## Demo
Demo it here: [https://ezipor.pythonanywhere.com/](https://ezipor.pythonanywhere.com/)

## Overview
This project involves deploying a Logistic Regression Model (LRM) using Flask in a Chrome Extension.

## Resources
- Flask: [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)
- Chrome Extension: [Getting Started with Chrome Extension](https://developer.chrome.com/docs/extensions/get-started/)
- LRM Documentation: [Python Pickle Module](https://docs.python.org/3/library/pickle.html)

## Loading the Chrome Extension
1. Download "phish_hook_packed_extension.zip"
2. Extract the ZIP file to a location on your computer.
3. Open Google Chrome and go to `chrome://extensions/`.
4. Enable Developer Mode by toggling the switch in the top-right corner.
5. Click on "Load unpacked" and select the extracted folder containing the Chrome Extension files.
6. Once loaded, the Phish Hook Chrome Extension should now be visible in your extensions list. We recommend pinning it for easier access.

## Loading Virtual Environment plus Flask
To run the Flask application with the virtual environment, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the root directory of the project where the `main.py` file is located.
3. Create and activate a virtual environment (optional but recommended):
4. Install the required packages from the `requirements.txt` file:
5. Set up the necessary environment variables by creating a `.env` file in the root directory. Include any sensitive information or configuration settings here.
6. Run the Flask application:
7. Access the application in your web browser at the specified address (usually `http://localhost:5000/`).

## Project Structure
- `models`: Directory for storing machine learning models or related files.
- `static`: Directory for static assets like images, CSS, and JavaScript.
- `templates`: Directory for HTML templates used by Flask.
- `.env`: Configuration file for environment variables.
- `main.py`: Main Flask application file.
- `phish_hook_classifier.pkl`: Pre-trained phishing classifier model.
- `requirements.txt`: File listing required Python packages and versions.

