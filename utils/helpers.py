#!/usr/bin/env python3
"""
Helper utilities for file creation and manipulation
"""

import os
import random
import string
from pathlib import Path
from datetime import datetime, timedelta


def ensure_directory(path):
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)
    return path


def random_string(length=10, include_special=False):
    """Generate a random string"""
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))


def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return start_date + timedelta(days=random_days)


def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"


def generate_fake_ssn():
    """Generate a fake SSN (for sandbox use only)"""
    area = random.randint(100, 899)
    group = random.randint(10, 99)
    serial = random.randint(1000, 9999)
    return f"{area}-{group}-{serial}"


def generate_fake_phone():
    """Generate a fake phone number"""
    area = random.randint(200, 999)
    prefix = random.randint(200, 999)
    line = random.randint(1000, 9999)
    return f"({area}) {prefix}-{line}"


def generate_fake_email(name, domain="example.com"):
    """Generate a fake email address"""
    name = name.lower().replace(" ", ".")
    return f"{name}@{domain}"


def random_ip_address():
    """Generate a random IP address"""
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"


def random_mac_address():
    """Generate a random MAC address"""
    return ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)])


def file_size_string(size_bytes):
    """Convert bytes to human-readable string"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def generate_guid():
    """Generate a GUID-like string"""
    return f"{random_string(8)}-{random_string(4)}-{random_string(4)}-{random_string(4)}-{random_string(12)}"


def weighted_random_choice(choices, weights):
    """Select random item with weights"""
    return random.choices(choices, weights=weights, k=1)[0]


def create_file_safely(filepath, content, encoding='utf-8'):
    """Create a file with proper error handling"""
    try:
        ensure_directory(os.path.dirname(filepath))
        Path(filepath).write_text(content, encoding=encoding)
        return True
    except Exception as e:
        print(f"Error creating file {filepath}: {e}")
        return False


def write_text_file(path, content, encoding='utf-8'):
    """
    Write text content to a file and ensure its parent directory exists.
    Returns the created Path for convenience.
    """
    file_path = Path(path)
    ensure_directory(file_path.parent)
    file_path.write_text(content, encoding=encoding)
    return file_path


def write_binary_file(path, data: bytes):
    """
    Write binary data to a file and ensure its parent directory exists.
    Returns the created Path for convenience.
    """
    file_path = Path(path)
    ensure_directory(file_path.parent)
    file_path.write_bytes(data)
    return file_path


def chrome_timestamp(dt: datetime) -> int:
    """
    Convert a datetime to Chrome/Webkit timestamp (microseconds since Jan 1, 1601 UTC).
    """
    epoch_start = datetime(1601, 1, 1)
    delta = dt - epoch_start
    return int(delta.total_seconds() * 1_000_000)


def firefox_timestamp(dt: datetime) -> int:
    """
    Convert a datetime to Firefox timestamp (microseconds since Unix epoch).
    """
    return int(dt.timestamp() * 1_000_000)


def get_windows_paths(base_override: str | Path | None = None):
    """
    Resolve Windows-style user directories (Desktop, Documents, Downloads, AppData, Program Files).
    Falls back to Path.home() when environment variables are missing.
    """
    base_home = (
        Path(base_override)
        if base_override
        else Path(os.environ.get("USERPROFILE", Path.home()))
    )

    appdata_local = Path(os.environ.get("LOCALAPPDATA", base_home / "AppData" / "Local"))
    appdata_roaming = Path(os.environ.get("APPDATA", base_home / "AppData" / "Roaming"))
    program_files = Path(os.environ.get("ProgramFiles", base_home / "Program Files"))

    return {
        "home": base_home,
        "desktop": base_home / "Desktop",
        "documents": base_home / "Documents",
        "downloads": base_home / "Downloads",
        "pictures": base_home / "Pictures",
        "music": base_home / "Music",
        "videos": base_home / "Videos",
        "appdata_local": appdata_local,
        "appdata_roaming": appdata_roaming,
        "program_files": program_files,
    }
