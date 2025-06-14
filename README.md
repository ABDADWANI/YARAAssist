# YARAAssist


**YARAAssist** is a beginner-friendly web app that helps users generate custom YARA rules by simply entering keywords and metadata. It outputs a fully formatted YARA rule ready to use for malware detection and threat hunting.

---

## Features

- Enter a custom rule name (default: `GeneratedRule`)
- Add multiple strings to detect within files
- Provide metadata such as author name and description
- Select a condition (default: any of the strings)
- View and copy the generated YARA rule instantly

---

## How to Run

1. Clone this repo:  
```bash
git clone https://github.com/ABDADWANI/YARAAssist.git

2. Install dependencies:
pip install -r requirements.txt

3.Run the app:
streamlit run app.py

The app will open in your browser.
