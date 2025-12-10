#!/usr/bin/env python3
"""
Browser Data Generator
Creates realistic browser history, credentials, and cookies for Chrome, Firefox, and Edge
"""

import json
import random
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

from config import (
    USER_NAME,
    USER_EMAIL,
    USER_USERNAME,
    COMMON_WEBSITES,
    FAKE_CREDENTIALS,
    BROWSER_PROFILE_NAMES,
)
from utils.helpers import (
    random_string,
    random_date,
    ensure_directory,
    chrome_timestamp,
    firefox_timestamp,
    write_text_file,
)


class BrowserDataGenerator:
    """Generates realistic browser data (history, credentials, cookies)"""
    
    def __init__(self, base_path, paths=None):
        self.base_path = Path(base_path)
        self.paths = paths or {}
        self.browser_data = {}
        self.profile_paths = self._build_profile_paths()

    def _build_profile_paths(self):
        """
        Build realistic browser profile paths under the base path
        to mirror Windows AppData layout.
        """
        return {
            "chrome": (
                Path(self.paths.get("appdata_local", self.base_path / "AppData" / "Local"))
                / "Google"
                / "Chrome"
                / "User Data"
                / BROWSER_PROFILE_NAMES.get("chrome", "Default")
            ),
            "edge": (
                Path(self.paths.get("appdata_local", self.base_path / "AppData" / "Local"))
                / "Microsoft"
                / "Edge"
                / "User Data"
                / BROWSER_PROFILE_NAMES.get("edge", "Default")
            ),
            "firefox": (
                Path(self.paths.get("appdata_roaming", self.base_path / "AppData" / "Roaming"))
                / "Mozilla"
                / "Firefox"
                / "Profiles"
                / f"{USER_USERNAME}.{BROWSER_PROFILE_NAMES.get('firefox', 'default-release')}"
            ),
        }
        
    def generate_browsing_history(self, num_entries=200):
        """Generate realistic browsing history"""
        history = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=90)
        
        # Weight different types of sites
        site_weights = {
            "work": 35,
            "social": 15,
            "news": 20,
            "finance": 10,
            "shopping": 10,
            "entertainment": 8,
            "email": 2
        }
        
        for _ in range(num_entries):
            # Select category
            category = random.choices(
                list(site_weights.keys()),
                weights=list(site_weights.values()),
                k=1
            )[0]
            
            # Select site from category
            site = random.choice(COMMON_WEBSITES[category])
            
            # Generate random path for some sites
            paths = [
                "", "/dashboard", "/search?q=python+tutorial", "/docs",
                "/settings", "/profile", "/notifications", "/about"
            ]
            path = random.choice(paths)
            
            # Random visit time
            visit_time = random_date(start_date, end_date)
            
            # Visit count (some sites visited more often)
            visit_count = random.choices([1, 2, 3, 5, 10], weights=[50, 25, 15, 7, 3])[0]
            
            history.append({
                "url": f"https://{site}{path}",
                "title": self._generate_page_title(site, path),
                "visit_time": visit_time,
                "visit_count": visit_count,
                "typed_count": 1 if visit_count > 5 else 0
            })
        
        # Sort by visit time
        history.sort(key=lambda x: x["visit_time"])
        return history
    
    def _generate_page_title(self, site, path):
        """Generate realistic page title"""
        titles = {
            "github.com": "GitHub: Where the world builds software",
            "stackoverflow.com": "Stack Overflow - Where Developers Learn",
            "linkedin.com": "LinkedIn: Log In or Sign Up",
            "amazon.com": "Amazon.com: Online Shopping",
            "youtube.com": "YouTube",
            "gmail.com": "Gmail - Email by Google",
            "netflix.com": "Netflix - Watch TV Shows Online",
            "reddit.com": "Reddit - Dive into anything",
        }
        
        for key, title in titles.items():
            if key in site:
                return title
        
        # Generic title
        domain = site.split('.')[0].capitalize()
        return f"{domain} - Home"

    def _write_history_summary(self, browser_label, history, summary_dir):
        """Write a lightweight human-readable summary file for quick review."""
        ensure_directory(summary_dir)
        summary_file = Path(summary_dir) / "History_Summary.txt"

        content = f"# {browser_label} Browsing History Summary\n"
        content += f"# User: {USER_NAME}\n"
        content += "# Generated for sandbox realism\n\n"

        for entry in history[-50:]:
            content += f"[{entry['visit_time'].strftime('%Y-%m-%d %H:%M:%S')}] "
            content += f"{entry['title']}\n"
            content += f"  URL: {entry['url']}\n"
            content += f"  Visits: {entry['visit_count']}\n\n"

        summary_file.write_text(content, encoding='utf-8')
        return summary_file

    def _write_chromium_history_db(self, history, profile_path, filename="History"):
        """
        Write a minimal but correctly shaped Chromium history SQLite DB.
        """
        ensure_directory(profile_path)
        db_path = Path(profile_path) / filename
        if db_path.exists():
            db_path.unlink()

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY,
                url LONGVARCHAR,
                title LONGVARCHAR,
                visit_count INTEGER,
                typed_count INTEGER,
                last_visit_time INTEGER,
                hidden INTEGER DEFAULT 0
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS visits (
                id INTEGER PRIMARY KEY,
                url INTEGER NOT NULL,
                visit_time INTEGER,
                from_visit INTEGER DEFAULT 0,
                transition INTEGER DEFAULT 805306368,
                segment_id INTEGER,
                visit_duration INTEGER DEFAULT 0
            )
            """
        )

        for idx, entry in enumerate(history, 1):
            visit_ts = chrome_timestamp(entry["visit_time"])
            cur.execute(
                """
                INSERT INTO urls (id, url, title, visit_count, typed_count, last_visit_time, hidden)
                VALUES (?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    idx,
                    entry["url"],
                    entry["title"],
                    entry["visit_count"],
                    entry["typed_count"],
                    visit_ts,
                ),
            )
            cur.execute(
                """
                INSERT INTO visits (id, url, visit_time, from_visit, transition, segment_id, visit_duration)
                VALUES (?, ?, ?, 0, 805306368, NULL, ?)
                """,
                (idx, idx, visit_ts, random.randint(5, 180) * 1_000_000),
            )

        conn.commit()
        conn.close()
        return db_path

    def _write_firefox_history_db(self, history, profile_path):
        """
        Write a Firefox-like places.sqlite with core tables populated.
        """
        ensure_directory(profile_path)
        db_path = Path(profile_path) / "places.sqlite"
        if db_path.exists():
            db_path.unlink()

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS moz_places (
                id INTEGER PRIMARY KEY,
                url LONGVARCHAR,
                title LONGVARCHAR,
                rev_host TEXT,
                visit_count INTEGER,
                hidden INTEGER DEFAULT 0,
                typed INTEGER DEFAULT 0,
                frecency INTEGER DEFAULT 0,
                last_visit_date INTEGER
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS moz_historyvisits (
                id INTEGER PRIMARY KEY,
                from_visit INTEGER,
                place_id INTEGER,
                visit_date INTEGER,
                visit_type INTEGER,
                session INTEGER
            )
            """
        )

        for idx, entry in enumerate(history, 1):
            visit_ts = firefox_timestamp(entry["visit_time"])
            rev_host = ".".join(entry["url"].split("//")[-1].split(".")[::-1])
            frecency = entry["visit_count"] * 100
            cur.execute(
                """
                INSERT INTO moz_places (id, url, title, rev_host, visit_count, typed, frecency, last_visit_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    idx,
                    entry["url"],
                    entry["title"],
                    rev_host,
                    entry["visit_count"],
                    entry["typed_count"],
                    frecency,
                    visit_ts,
                ),
            )
            cur.execute(
                """
                INSERT INTO moz_historyvisits (id, from_visit, place_id, visit_date, visit_type, session)
                VALUES (?, 0, ?, ?, 1, 0)
                """,
                (idx, idx, visit_ts),
            )

        conn.commit()
        conn.close()
        return db_path
    
    def generate_chrome_history(self, output_dir):
        """Generate Chrome browsing history"""
        history = self.generate_browsing_history(250)
        profile_dir = self.profile_paths["chrome"]

        history_db = self._write_chromium_history_db(history, profile_dir, "History")
        summary_file = self._write_history_summary("Google Chrome", history, output_dir)
        return [history_db, summary_file]
    
    def generate_firefox_history(self, output_dir):
        """Generate Firefox browsing history"""
        history = self.generate_browsing_history(200)
        profile_dir = self.profile_paths["firefox"]

        history_db = self._write_firefox_history_db(history, profile_dir)
        summary_file = self._write_history_summary("Mozilla Firefox", history, output_dir)
        return [history_db, summary_file]
    
    def generate_edge_history(self, output_dir):
        """Generate Microsoft Edge browsing history"""
        history = self.generate_browsing_history(180)
        profile_dir = self.profile_paths["edge"]

        history_db = self._write_chromium_history_db(history, profile_dir, "History")
        summary_file = self._write_history_summary("Microsoft Edge", history, output_dir)
        return [history_db, summary_file]
    
    def generate_saved_passwords(self):
        """Generate saved passwords for browser"""
        passwords = []
        
        for site, creds in FAKE_CREDENTIALS.items():
            password_entry = {
                "url": f"https://{site}",
                "username": creds.get("username", creds.get("email")),
                "password": creds["password"],
                "date_created": datetime.now() - timedelta(days=random.randint(30, 500)),
                "times_used": random.randint(5, 100)
            }
            passwords.append(password_entry)
        
        return passwords
    
    def generate_chrome_credentials(self, output_dir):
        """Generate Chrome saved passwords file"""
        passwords = self.generate_saved_passwords()
        profile_dir = self.profile_paths["chrome"]

        creds_json = [
            {
                "origin_url": pwd["url"],
                "username": pwd["username"],
                "password": pwd["password"],
                "date_created": pwd["date_created"].isoformat(),
                "times_used": pwd["times_used"],
            }
            for pwd in passwords
        ]
        
        creds_profile_file = write_text_file(
            Path(profile_dir) / "Login Data.json",
            json.dumps(creds_json, indent=2),
        )

        summary_file = Path(output_dir) / "Saved_Passwords.txt"
        content = "# Google Chrome - Saved Passwords (summary)\n"
        content += f"# User: {USER_NAME} ({USER_EMAIL})\n"
        content += "# WARNING: FAKE credentials for sandbox analysis\n\n"
        content += f"Total saved passwords: {len(passwords)}\n\n"
        content += "="*70 + "\n\n"
        for pwd in passwords:
            content += f"Website: {pwd['url']}\n"
            content += f"Username: {pwd['username']}\n"
            content += f"Password: {pwd['password']}\n"
            content += f"Created: {pwd['date_created'].strftime('%Y-%m-%d')}\n"
            content += f"Times Used: {pwd['times_used']}\n"
            content += "-"*70 + "\n\n"
        summary_file.write_text(content, encoding='utf-8')

        return [creds_profile_file, summary_file]
    
    def generate_firefox_credentials(self, output_dir):
        """Generate Firefox saved passwords file"""
        passwords = self.generate_saved_passwords()
        profile_dir = self.profile_paths["firefox"]

        # Firefox stores JSON logins file; mimic that structure
        creds_json = {
            "nextId": len(passwords) + 1,
            "logins": [
                {
                    "id": idx + 1,
                    "hostname": pwd["url"],
                    "httpRealm": None,
                    "formSubmitURL": pwd["url"],
                    "usernameField": "username",
                    "passwordField": "password",
                    "encryptedUsername": pwd["username"],
                    "encryptedPassword": pwd["password"],
                    "timeCreated": firefox_timestamp(pwd["date_created"]),
                    "timePasswordChanged": firefox_timestamp(pwd["date_created"]),
                    "timesUsed": pwd["times_used"],
                }
                for idx, pwd in enumerate(passwords)
            ],
        }
        creds_profile_file = write_text_file(
            Path(profile_dir) / "logins.json", json.dumps(creds_json, indent=2)
        )

        summary_file = Path(output_dir) / "Saved_Passwords_Firefox.txt"
        content = "# Mozilla Firefox - Saved Passwords (summary)\n"
        content += f"# User: {USER_NAME} ({USER_EMAIL})\n"
        content += "# WARNING: FAKE credentials for sandbox analysis\n\n"
        content += f"Total saved logins: {len(passwords)}\n\n"
        content += "="*70 + "\n\n"
        for pwd in passwords:
            content += f"Site: {pwd['url']}\n"
            content += f"Username: {pwd['username']}\n"
            content += f"Password: {pwd['password']}\n"
            content += f"Date Created: {pwd['date_created'].strftime('%Y-%m-%d %H:%M:%S')}\n"
            content += f"Used {pwd['times_used']} times\n"
            content += "-"*70 + "\n\n"
        summary_file.write_text(content, encoding='utf-8')

        return [creds_profile_file, summary_file]
    
    def generate_edge_credentials(self, output_dir):
        """Generate Edge saved passwords file"""
        passwords = self.generate_saved_passwords()
        profile_dir = self.profile_paths["edge"]

        creds_json = [
            {
                "origin_url": pwd["url"],
                "username": pwd["username"],
                "password": pwd["password"],
                "date_created": pwd["date_created"].isoformat(),
                "times_used": pwd["times_used"],
            }
            for pwd in passwords
        ]
        creds_profile_file = write_text_file(
            Path(profile_dir) / "Login Data.json",
            json.dumps(creds_json, indent=2),
        )

        summary_file = Path(output_dir) / "Saved_Passwords_Edge.txt"
        content = "# Microsoft Edge - Saved Passwords (summary)\n"
        content += f"# User: {USER_NAME} ({USER_EMAIL})\n"
        content += "# WARNING: FAKE credentials for sandbox analysis\n\n"
        content += f"Total passwords saved: {len(passwords)}\n\n"
        content += "="*70 + "\n\n"
        for pwd in passwords:
            content += f"URL: {pwd['url']}\n"
            content += f"Username: {pwd['username']}\n"
            content += f"Password: {pwd['password']}\n"
            content += f"Created: {pwd['date_created'].strftime('%Y-%m-%d')}\n"
            content += f"Usage Count: {pwd['times_used']}\n"
            content += "-"*70 + "\n\n"
        summary_file.write_text(content, encoding='utf-8')

        return [creds_profile_file, summary_file]
    
    def generate_cookies_file(self, browser_label, profile_dir, output_dir):
        """Generate cookies information file"""
        ensure_directory(output_dir)

        content = f"# {browser_label} - Cookies Information\n"
        content += f"# User: {USER_NAME}\n"
        content += f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        content += "Common cookies stored:\n\n"
        
        cookie_types = [
            ("session_id", "Session identifier"),
            ("auth_token", "Authentication token"),
            ("user_prefs", "User preferences"),
            ("tracking_id", "Analytics tracking"),
            ("csrf_token", "CSRF protection"),
            ("language", "Language preference"),
            ("timezone", "Timezone setting")
        ]
        
        cookie_profile_entries = []
        for site_category, sites in COMMON_WEBSITES.items():
            sample_site = random.choice(sites)
            cookie_name, description = random.choice(cookie_types)
            value = random_string(32)
            expires = (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')
            
            content += f"Domain: .{sample_site}\n"
            content += f"  Cookie: {cookie_name}\n"
            content += f"  Description: {description}\n"
            content += f"  Value: {value}\n"
            content += f"  Expires: {expires}\n"
            content += f"  Secure: Yes\n"
            content += f"  HttpOnly: Yes\n\n"

            cookie_profile_entries.append(
                {
                    "domain": f".{sample_site}",
                    "name": cookie_name,
                    "value": value,
                    "expirationDate": expires,
                    "secure": True,
                    "httpOnly": True,
                }
            )
        
        cookies_info_file = Path(output_dir) / "Cookies_Info.txt"
        cookies_info_file.write_text(content, encoding='utf-8')

        cookies_profile_file = write_text_file(
            Path(profile_dir) / "Cookies.json", json.dumps(cookie_profile_entries, indent=2)
        )
        return [cookies_info_file, cookies_profile_file]
    
    def generate_all_browser_data(self):
        """Generate all browser data for Chrome, Firefox, and Edge"""
        created_files = []
        
        browsers = {
            "Chrome": {
                "profile": self.profile_paths["chrome"],
                "history": self.generate_chrome_history,
                "credentials": self.generate_chrome_credentials,
                "cookies": lambda d: self.generate_cookies_file("Google Chrome", self.profile_paths["chrome"], d),
            },
            "Firefox": {
                "profile": self.profile_paths["firefox"],
                "history": self.generate_firefox_history,
                "credentials": self.generate_firefox_credentials,
                "cookies": lambda d: self.generate_cookies_file("Mozilla Firefox", self.profile_paths["firefox"], d),
            },
            "Edge": {
                "profile": self.profile_paths["edge"],
                "history": self.generate_edge_history,
                "credentials": self.generate_edge_credentials,
                "cookies": lambda d: self.generate_cookies_file("Microsoft Edge", self.profile_paths["edge"], d),
            },
        }
        
        print("\n[*] Generating browser data...")
        
        for browser_name, generators in browsers.items():
            browser_dir = self.base_path / "Documents" / f"Browser_Data_{browser_name}"
            ensure_directory(browser_dir)
            
            print(f"\n    {browser_name}:")
            
            # Generate history
            history_files = generators["history"](browser_dir)
            created_files.extend(history_files)
            print(f"      ✓ History stored under {generators['profile']}")
            
            # Generate credentials
            creds_files = generators["credentials"](browser_dir)
            created_files.extend(creds_files)
            print(f"      ✓ Credentials saved ({len(creds_files)} files)")
            
            # Generate cookies info
            cookies_files = generators["cookies"](browser_dir)
            created_files.extend(cookies_files)
            print(f"      ✓ Cookies cached ({len(cookies_files)} files)")
        
        return created_files
