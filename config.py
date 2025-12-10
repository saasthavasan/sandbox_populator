#!/usr/bin/env python3
"""
Configuration file for Sandbox Populator
Contains all user-specific settings and constants
"""

from datetime import datetime

# ==========================================
# USER INFORMATION
# ==========================================
USER_NAME = "John Mathew"
USER_FIRST_NAME = "John"
USER_LAST_NAME = "Mathew"
USER_EMAIL = "john.mathew@beingMalicious.com"
USER_USERNAME = "jmathew"
COMPANY_NAME = "beingMalicious.com"

# Personal Information (Fake data for sandbox)
USER_SSN = "547-82-9163-1234"  # Fake SSN for tax documents
USER_ADDRESS = "18470001 Silicon Blvd, Apt 1998119"
USER_CITY = "San Francisco"
USER_STATE = "California"
USER_ZIP = "971174"
USER_PHONE = "(4315) 5545-01452"
USER_DOB = "04/15/1985"

# ==========================================
# BROWSER SETTINGS
# ==========================================
BROWSER_PROFILE_NAMES = {
    "chrome": "Default",
    "firefox": "default-release",
    "edge": "Default"
}

# Typical browser installation paths (Windows)
BROWSER_PATHS = {
    "chrome": "C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data",
    "firefox": "C:\\Users\\{username}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles",
    "edge": "C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data"
}

# ==========================================
# APPLICATION SETTINGS
# ==========================================
INSTALLED_APPLICATIONS = [
    "Google Chrome",
    "Mozilla Firefox",
    "Microsoft Edge",
    "Google Drive",
    "Box",
    "Dropbox",
    "Microsoft OneDrive",
    "Microsoft Office 365",
    "Microsoft Teams",
    "Zoom",
    "VLC Media Player",
    "WinRAR",
    "7-Zip",
    "Adobe Acrobat Reader DC",
    "Visual Studio Code",
    "Git",
    "Python 3.11",
    "Node.js",
    "Docker Desktop",
    "Slack",
    "Notepad++",
    "FileZilla",
    "Putty",
    "Spotify"
]

# ==========================================
# FINANCIAL SETTINGS
# ==========================================
# Tax information
TAX_YEARS = [2022, 2023, 2024, 2025]
FEDERAL_TAX_BRACKETS = {
    2022: {"income": 95000, "tax_paid": 14250, "refund": 450},
    2023: {"income": 102000, "tax_paid": 16800, "refund": 0},
    2024: {"income": 108000, "tax_paid": 18200, "refund": 320},
    2025: {"income": 115000, "tax_paid": 19500, "refund": 0}
}

STATE_TAX_BRACKETS = {
    2022: {"income": 95000, "tax_paid": 5700, "refund": 180},
    2023: {"income": 102000, "tax_paid": 6630, "refund": 0},
    2024: {"income": 108000, "tax_paid": 7020, "refund": 95},
    2025: {"income": 115000, "tax_paid": 7475, "refund": 0}
}

# Investment portfolio
STOCK_HOLDINGS = [
    "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "NVDA", "META", 
    "NFLX", "AMD", "INTC", "JPM", "BAC", "V", "MA", "DIS", "PYPL", "ADBE", "SMCI", "MSTR"
]

ETF_HOLDINGS = [
    "SPY", "QQQ", "VTI", "VOO", "IVV", "VEA", "VWO", "AGG", "BND", "TLT"
]

BOND_HOLDINGS = [
    "US Treasury 10Y", "US Treasury 5Y", "Corporate Bond AAA", 
    "Municipal Bond CA", "TIPS 2030"
]

# ==========================================
# CONTENT SETTINGS
# ==========================================
# Number of each type of file to generate
NUM_MEETING_NOTES = 8
NUM_EMAILS = 10
NUM_CODE_SNIPPETS = 6
NUM_INVOICES = 6
NUM_PHOTOS = 15
NUM_MUSIC_FILES = 20

# Current date for timestamp generation
CURRENT_DATE = datetime.now()

# ==========================================
# FOLDER STRUCTURE
# ==========================================
DESKTOP_FOLDERS = {
    "Tax Documents": ["2022", "2023", "2024", "2025"],
    "Investments": [],
    "Office": ["Reports", "Presentations", "Spreadsheets", "Projects"],
    "Personal": ["Music", "Photos", "Health", "Receipts"]
}

DOCUMENTS_FOLDERS = {
    "Work": [
        "Projects",
        "Meetings", 
        "Budgets",
        "Performance_Reviews",
        "Training_Materials"
    ],
    "Personal": [
        "Finances",
        "Medical",
        "Insurance",
        "Recipes"
    ],
    "Technical_Docs": [],
    "Code_Snippets": [],
    "Credentials": [],
    "Invoices": [],
    "Contracts": []
}

DOWNLOADS_FOLDERS = [
    "Software_Installers",
    "Documentation",
    "Archive",
    "Temp"
]

# ==========================================
# WEBSITE DATA (for browser history)
# ==========================================
COMMON_WEBSITES = {
    "work": [
        "github.com",
        "stackoverflow.com",
        "docs.microsoft.com",
        "aws.amazon.com",
        "gitlab.com",
        "jenkins.io",
        "docker.com",
        "kubernetes.io"
    ],
    "social": [
        "linkedin.com",
        "twitter.com",
        "reddit.com",
        "facebook.com"
    ],
    "news": [
        "news.ycombinator.com",
        "techcrunch.com",
        "arstechnica.com",
        "theverge.com",
        "wired.com"
    ],
    "finance": [
        "chase.com",
        "wellsfargo.com",
        "mint.com",
        "robinhood.com",
        "fidelity.com",
        "vanguard.com"
    ],
    "shopping": [
        "amazon.com",
        "ebay.com",
        "walmart.com",
        "target.com",
        "bestbuy.com"
    ],
    "entertainment": [
        "youtube.com",
        "netflix.com",
        "spotify.com",
        "reddit.com",
        "twitch.tv"
    ],
    "email": [
        "gmail.com",
        "outlook.com",
        "yahoo.com"
    ]
}

# ==========================================
# CREDENTIALS DATA (fake passwords)
# ==========================================
FAKE_CREDENTIALS = {
    "github.com": {
        "username": USER_USERNAME,
        "email": USER_EMAIL,
        "password": "SecureP@ss123!"
    },
    "gitlab.com": {
        "username": USER_USERNAME,
        "email": USER_EMAIL,
        "password": "GitL@b2024!"
    },
    "gmail.com": {
        "email": USER_EMAIL,
        "password": "Gm@ilPass456"
    },
    "linkedin.com": {
        "email": USER_EMAIL,
        "password": "LinkedIn#789"
    },
    "amazon.com": {
        "email": USER_EMAIL,
        "password": "Am@z0nSecure"
    },
    "chase.com": {
        "username": USER_USERNAME,
        "password": "Ch@seBank999"
    },
    "fidelity.com": {
        "username": USER_USERNAME,
        "password": "Invest$2024"
    },
    "zoom.us": {
        "email": USER_EMAIL,
        "password": "Zo0m!Meeting"
    },
    "slack.com": {
        "email": USER_EMAIL,
        "password": "Sl@ckWork123"
    },
    "office.com": {
        "email": USER_EMAIL,
        "password": "Office365@!"
    },
    "dropbox.com": {
        "email": USER_EMAIL,
        "password": "Dr0pb0x#Secure"
    },
    "docker.com": {
        "username": USER_USERNAME,
        "email": USER_EMAIL,
        "password": "D0cker!Hub"
    },
    "aws.amazon.com": {
        "username": USER_USERNAME,
        "email": USER_EMAIL,
        "password": "AWS@ccess2024"
    },
    "spotify.com": {
        "email": USER_EMAIL,
        "password": "Sp0tify#Music"
    },
    "netflix.com": {
        "email": USER_EMAIL,
        "password": "Netfl1x!Stream"
    }
}
