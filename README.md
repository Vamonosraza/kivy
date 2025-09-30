# Kivy App

A simple Kivy application.

## Setup# Location-Based Photo App

A Kivy mobile app that gets random photos from Unsplash based on user location using GPS.

## Features
- GPS location detection
- Location-based photo search using Unsplash API
- Mobile-ready interface
- Android deployment ready

## Setup
1. Create conda environment: `conda create -n kivy-project python=3.11`
2. Activate environment: `conda activate kivy-project`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy config template: `cp templates/config_template.py config.py`
5. Get Unsplash API key from https://unsplash.com/developers
6. Add your API key to `config.py`

## Run
```bash
python main.py
```

## Build for Android
```bash
pip install buildozer
buildozer init
buildozer android debug
```

## Requirements
- Python 3.11+
- Kivy 2.1.0+
- Internet connection for photo API
- GPS capability for location detection

## API Keys Required
- Unsplash Access Key (free at https://unsplash.com/developers)

## Project Structure
```
C:\Users\marti\VSC\kivy\
├── main.py              # Main application file
├── config.py            # API keys and settings (not in git)
├── requirements.txt     # Python dependencies
├── buildozer.spec      # Android build configuration
├── templates/          # Template files for setup
└── README.md           # This file
```

## Development Status
- [x] Basic Kivy app structure
- [x] Unsplash API integration
- [ ] GPS location detection
- [ ] Location-based photo queries
- [ ] Android deployment testing
1. Install dependencies: `pip install kivy`
2. Run: `python main.py`

## Requirements
- Python 3.x
- Kivy