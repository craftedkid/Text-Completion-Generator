
#  Text-Completion-Generator

# Sentence Completion using GPT-2

This project is a Flask-based web application that utilizes the GPT-2 model from Hugging Face for sentence completion. The project includes continuous integration and deployment (CI/CD) using GitHub Actions for installation, code formatting, linting, and testing workflows.

The user interface is generated from an `index.html` file. For example, when the input "My Name is craftedkid and I " is submitted, the app generates a full sentence using GPT-2. All front-end and model assets are included or hosted via GitHub.

The app can be run locally or accessed through a hosted URL.


---

## 🚀 Features

- Sentence completion using Hugging Face's GPT-2 API
- Flask web app with HTML templates
- Environment variable management with `.env`
- Makefile for automation (install, test, lint)

---

## 📂 Project Structure

```
├── app.py               # Main Flask app
├── requirements.txt     # Python dependencies
├── Makefile             # Automation commands
├── pro.env              # Environment variables (example)
├── templates/           # HTML templates
│   ├── index.html
│   └── result.html
└── static/              # (Optional) CSS/JS files
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Setup Environment

Create a `.env` file (or rename `pro.env`) and add your Hugging Face token:

```
HF_TOKEN=your_huggingface_token
```

### 3. Install Dependencies

```bash
make install
```

Or manually:

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ✏️ Usage

- Enter a sentence prompt on the landing page.
- Submit to see the GPT-2 generated continuation.

Example Input:
> "The future of AI is"

Example Output:
> "The future of AI is rapidly evolving with transformative potential in every sector."

---

## ⚙️ DevOps and CI/CD

This project includes:
- `Makefile` for install, lint, test automation
- GitHub Actions workflow files (add your `.github/workflows` directory)
- Compatible with Docker and cloud platforms

---

## 🧪 Makefile Commands

```bash
make install    # Install Python dependencies
make format     # Format code using black
make lint       # Run pylint checks
make test       # Run tests (if configured)
```

---
## File Index

Files in this repository include:


## 1. Readme
  The `README.md` file is a markdown file that contains basic information about the repository, what files it contains, and how to consume them


## 2. Requirements
  The `requirements.txt` file has a list of packages to be installed for any required project. Currently, my requirements file contains some basic python packages.


## 3. Codes
  This folder contains all the code files used in this repository - the files named "Test_" will be used for testing and the remaining will define certain functions


## 4. Resources and Templates
  -  This folder contains any other files relevant to this project. Currently, I have added -
    -  `index.html` - an HTML File containing the front end view of the text generator page
    -  `result.html` - an HTML File containing the result view of the text generator model


## 5. CI/CD Automation Files


  ### 5(a). Makefile
  The `Makefile` contains instructions for installing packages (specified in `requirements.txt`), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term *'Check...'* ), and linting the code using pylint


  ### 5(b). Github Actions
  Github Actions uses the `main.yml` file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions


  ### 5(c). Devcontainer
  * `devcontainer.json` is a json file that specifies the environment variables including the installed extensions in the virtual environment
