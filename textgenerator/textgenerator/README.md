# Individual Project #4: Auto Scaling Flask App Using a Serverless Platform

# Sentence Completion using GPT-2

This project is a Flask-based web application that utilizes the *GPT-2* model from Huggingface for sentence completion. The application is hosted on Azure ACR using an image pushed to Dockerhub, which allows it to automatically scale based on demand. The project is set up with continuous integration/continuous deployment (CI/CD) using GitHub Actions.

The user interface is generated from an index.html file, and an example of the application's functionality is shown with the input "My Name is Divya and I ".

The app can be run by the user locally or can be accessed via the hosted link.

---

### Instructions

There are two ways to access this application:

- **Method 1**: Visit the hosted link: [ds655-ind4.azurewebsites.net](https://ds655-ind4.azurewebsites.net/)
- **Method 2**: Run locally
  1. Clone this repository
  2. Install dependencies:
     ```bash
     make install
     ```
  3. Run the app:
     ```bash
     python app.py
     ```
  4. Open `http://127.0.0.1:5000` in your browser
  5. Use `Ctrl+C` in the terminal to stop the app

---

### App Usage

- `index.html`: Input screen template
- `result.html`: Output screen template

---

### Components

#### Flask App
The Flask app exposes two routes:
- `/`: Renders the input template
- `/analyze`: Accepts POST input, sends it to the GPT-2 API for sentence completion, and displays the result

#### Use of DockerHub
The Docker image contains the full Flask app and is pushed to DockerHub.

To build and tag the image locally:

```bash
docker build -t image-name .
