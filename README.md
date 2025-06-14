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

## Getting Started

### Prerequisites

- Python 3.7 or higher installed
- `pip` package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ABDADWANI/YARAAssist.git
cd YARAAssist
