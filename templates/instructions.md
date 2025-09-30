# Project Context for GitHub Copilot

## Project: [PROJECT_NAME]
- **Framework**: Kivy (Python mobile app framework)
- **Purpose**: [DESCRIBE_YOUR_APP_PURPOSE]
- **Target Platform**: Android (eventually iOS)
- **APIs**: [LIST_YOUR_APIS]

## Current Setup
- Conda environment: `[ENVIRONMENT_NAME]`
- Main file: `main.py`
- Dependencies: [LIST_DEPENDENCIES]

## File Structure
```
C:\Users\marti\VSC\[PROJECT_FOLDER]\
├── main.py (main app file)
├── config.py (API keys and settings)
├── requirements.txt
├── buildozer.spec (for Android build)
├── README.md
├── .gitignore
└── templates/ (template files)
```

## Development Notes
- Always provide full file paths: C:\Users\marti\VSC\[PROJECT_FOLDER]\filename
- User is on Windows using Git Bash
- Building for real phone deployment
- [ADD_SPECIFIC_PROJECT_REQUIREMENTS]

## API Integration
- [API_NAME]: [PURPOSE_AND_SETUP_NOTES]

## Mobile Features
- GPS location detection
- [OTHER_MOBILE_FEATURES]

## Build Instructions
1. Create conda environment: `conda create -n [ENV_NAME] python=3.11`
2. Activate: `conda activate [ENV_NAME]`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy and configure: `cp templates/config_template.py config.py`
5. Add API keys to config.py
6. Test: `python main.py`
7. Build for Android: `buildozer android debug`