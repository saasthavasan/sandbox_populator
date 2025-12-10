#!/usr/bin/env python3
"""
Personal Folders Generator
Creates realistic personal files (music, photos, health records, receipts)
"""

import random
import base64
from datetime import datetime, timedelta
from pathlib import Path

from config import USER_NAME, USER_PHONE, USER_ADDRESS, USER_CITY, USER_STATE, USER_ZIP, USER_DOB
from utils.helpers import (
    format_currency,
    ensure_directory,
    write_binary_file,
)

# Minimal 1x1 JPEG used to seed realistic photo files
SAMPLE_JPEG_BYTES = base64.b64decode(
    "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////"
    "2wBDAf//////////////////////////////////////////////////////////////////////////////////////"
    "wAARCAAQABADASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAX/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAgP/"
    "xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCfAAH/2Q=="
)


class PersonalFoldersGenerator:
    """Generates realistic personal files and folders"""
    
    def __init__(self, base_path):
        self.base_path = Path(base_path)
    
    def generate_music_playlist(self):
        """Generate music playlist file"""
        
        songs = [
            ("Bohemian Rhapsody", "Queen", "4:55"),
            ("Stairway to Heaven", "Led Zeppelin", "8:02"),
            ("Hotel California", "Eagles", "6:30"),
            ("Imagine", "John Lennon", "3:03"),
            ("Sweet Child O' Mine", "Guns N' Roses", "5:56"),
            ("Billie Jean", "Michael Jackson", "4:54"),
            ("Smells Like Teen Spirit", "Nirvana", "5:01"),
            ("November Rain", "Guns N' Roses", "8:57"),
            ("One", "Metallica", "7:27"),
            ("Wonderwall", "Oasis", "4:18"),
            ("Lose Yourself", "Eminem", "5:26"),
            ("Rolling in the Deep", "Adele", "3:48"),
            ("Shape of You", "Ed Sheeran", "3:53"),
            ("Blinding Lights", "The Weeknd", "3:20"),
            ("Someone Like You", "Adele", "4:45"),
            ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "4:30"),
            ("Thinking Out Loud", "Ed Sheeran", "4:41"),
            ("Stay", "The Kid LAROI & Justin Bieber", "2:21"),
            ("Levitating", "Dua Lipa", "3:23"),
            ("Good 4 U", "Olivia Rodrigo", "2:58")
        ]
        
        content = "MY MUSIC PLAYLIST\n"
        content += f"Owner: {USER_NAME}\n"
        content += f"Created: {datetime.now().strftime('%B %d, %Y')}\n"
        content += f"Total Songs: {len(songs)}\n\n"
        content += "="*70 + "\n\n"
        
        for i, (title, artist, duration) in enumerate(songs, 1):
            content += f"{i:2}. {title:40} - {artist:30} [{duration}]\n"
        
        return content
    
    def generate_photo_catalog(self, num_photos=15):
        """Generate photo catalog/list"""
        
        photo_categories = [
            "Vacation", "Family", "Friends", "Work Event", "Birthday",
            "Holiday", "Weekend Trip", "Concert", "Sports", "Nature"
        ]
        
        content = "PHOTO CATALOG\n"
        content += f"Owner: {USER_NAME}\n"
        content += f"Last Updated: {datetime.now().strftime('%B %d, %Y')}\n\n"
        content += "="*70 + "\n\n"
        
        entries = []
        for i in range(num_photos):
            date = datetime.now() - timedelta(days=random.randint(1, 365*3))
            category = random.choice(photo_categories)
            filename = f"IMG_{random.randint(1000, 9999)}.jpg"
            entries.append(
                {
                    "filename": filename,
                    "date": date,
                    "category": category,
                    "resolution": random.choice(["4032x3024", "3024x4032", "1920x1080", "3840x2160"]),
                    "size_mb": f"{random.randint(1, 8)}.{random.randint(1, 9)}MB",
                }
            )
            
            content += f"File: {filename}\n"
            content += f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            content += f"Category: {category}\n"
            content += f"Size: {entries[-1]['size_mb']}\n"
            content += f"Resolution: {entries[-1]['resolution']}\n"
            content += "-"*70 + "\n\n"
        
        return content, entries
    
    def generate_health_records(self):
        """Generate health records summary"""
        
        content = f"""PERSONAL HEALTH RECORDS
{USER_NAME}

═══════════════════════════════════════════════════════════════════════════

PERSONAL INFORMATION

Name: {USER_NAME}
Date of Birth: {USER_DOB}
Blood Type: O+
Allergies: None known
Emergency Contact: Sarah Mathew - (415) 555-0198

═══════════════════════════════════════════════════════════════════════════

PRIMARY CARE PHYSICIAN

Dr. Emily Rodriguez, MD
Bay Area Medical Group
1234 Healthcare Drive, Suite 200
San Francisco, CA 94110
Phone: (415) 555-0123
Fax: (415) 555-0124

═══════════════════════════════════════════════════════════════════════════

RECENT VISITS

Date: November 15, 2024
Type: Annual Physical Examination
Provider: Dr. Emily Rodriguez
Notes: Routine checkup. All vitals normal.
       Blood pressure: 118/76
       Weight: 175 lbs
       Height: 5'10"
       Recommended: Continue regular exercise routine

Date: June 22, 2024
Type: Follow-up Appointment
Provider: Dr. Emily Rodriguez
Notes: Reviewed lab results. All values within normal range.
       Cholesterol: 185 mg/dL (optimal)
       Blood glucose: 92 mg/dL (normal)

Date: March 10, 2024
Type: Flu Vaccination
Provider: Nurse Johnson
Notes: Seasonal flu vaccine administered. No adverse reactions.

═══════════════════════════════════════════════════════════════════════════

IMMUNIZATION RECORD

Influenza:              Annually (Last: October 2024)
Tetanus/Diphtheria:     2019 (Next due: 2029)
COVID-19:               Boosted September 2024
MMR:                    Childhood (Documented)
Hepatitis B:            Childhood (Documented)

═══════════════════════════════════════════════════════════════════════════

CURRENT MEDICATIONS

None

OVER-THE-COUNTER:
• Daily multivitamin
• Vitamin D supplement (2000 IU)
• Omega-3 fish oil

═══════════════════════════════════════════════════════════════════════════

INSURANCE INFORMATION

Provider: Blue Cross Blue Shield
Plan: PPO Gold
Member ID: BC12345678901
Group: BEING001
Phone: 1-800-123-4567

═══════════════════════════════════════════════════════════════════════════

NOTES

• Exercise regularly (3-4x per week)
• No chronic conditions
• Annual physical scheduled for November each year
• Maintain healthy diet and lifestyle
• No smoking, moderate alcohol consumption

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content

    def create_photo_files(self, photos_folder, entries):
        """
        Materialize small JPEGs so the photo directory is not just text.
        """
        created = []
        metadata_folder = photos_folder / "metadata"
        ensure_directory(metadata_folder)

        for entry in entries:
            photo_path = photos_folder / entry["filename"]
            # Pad the base image so file sizes differ slightly
            padded_bytes = SAMPLE_JPEG_BYTES + random.randbytes(random.randint(512, 2048))
            write_binary_file(photo_path, padded_bytes)
            created.append(photo_path)

            # Write sidecar metadata to make the folder look populated
            metadata = (
                f"filename={entry['filename']}\n"
                f"captured_at={entry['date'].isoformat()}\n"
                f"category={entry['category']}\n"
                f"resolution={entry['resolution']}\n"
                f"size={entry['size_mb']}\n"
                f"camera=Pixel 7 Pro\n"
            )
            sidecar = metadata_folder / f"{photo_path.stem}.xmp"
            sidecar.write_text(metadata, encoding="utf-8")
            created.append(sidecar)

        return created
    
    def generate_receipt(self):
        """Generate shopping receipt"""
        
        stores = [
            ("Whole Foods Market", "Groceries"),
            ("Best Buy", "Electronics"),
            ("Target", "General Merchandise"),
            ("CVS Pharmacy", "Pharmacy/Health"),
            ("Home Depot", "Home Improvement"),
            ("Amazon.com", "Online Shopping"),
            ("Costco", "Wholesale")
        ]
        
        store, category = random.choice(stores)
        date = datetime.now() - timedelta(days=random.randint(1, 90))
        
        items = [
            ("Organic Bananas", 3.99),
            ("Greek Yogurt", 5.49),
            ("Whole Wheat Bread", 4.29),
            ("Chicken Breast", 12.99),
            ("Mixed Greens", 4.99),
            ("Coffee Beans", 14.99),
            ("Almond Milk", 3.79),
            ("Pasta", 2.99),
            ("Olive Oil", 9.99),
            ("Tomatoes", 4.50)
        ]
        
        # Select random items
        num_items = random.randint(3, 7)
        selected_items = random.sample(items, num_items)
        
        content = f"""{store}
{category}

{USER_ADDRESS}
{USER_CITY}, {USER_STATE} {USER_ZIP}
Phone: {USER_PHONE}

═══════════════════════════════════════════════════════════════════════════

Transaction #{random.randint(100000, 999999)}
Date: {date.strftime('%m/%d/%Y %I:%M %p')}
Cashier: #{random.randint(100, 999)}

═══════════════════════════════════════════════════════════════════════════

ITEMS PURCHASED:

"""
        
        subtotal = 0
        for item, price in selected_items:
            content += f"{item:40} {format_currency(price):>10}\n"
            subtotal += price
        
        tax = round(subtotal * 0.0875, 2)  # CA sales tax
        total = subtotal + tax
        
        content += "\n"
        content += "─"*70 + "\n"
        content += f"{'SUBTOTAL':40} {format_currency(subtotal):>10}\n"
        content += f"{'TAX (8.75%)':40} {format_currency(tax):>10}\n"
        content += "─"*70 + "\n"
        content += f"{'TOTAL':40} {format_currency(total):>10}\n\n"
        
        content += f"PAYMENT METHOD: Visa ending in 5847\n"
        content += f"APPROVAL CODE: {random.randint(100000, 999999)}\n\n"
        
        content += "Thank you for shopping with us!\n"
        content += "Please visit www.{}.com for deals\n".format(store.lower().replace(" ", ""))
        
        content += "\n" + "═"*70 + "\n"
        
        return content
    
    def generate_all_personal_folders(self):
        """Generate all personal folders and files"""
        created_files = []
        
        print("\n[*] Generating personal folders...")
        
        personal_folder = self.base_path / "Desktop" / "Personal"
        ensure_directory(personal_folder)
        
        # Music folder
        music_folder = personal_folder / "Music"
        ensure_directory(music_folder)
        
        playlist = self.generate_music_playlist()
        playlist_file = music_folder / "My_Playlist.m3u"
        playlist_file.write_text(playlist, encoding='utf-8')
        created_files.append(playlist_file)
        
        # Additional playlists
        playlists_names = ["Workout Mix", "Chill Vibes", "Road Trip"]
        for name in playlists_names:
            simple_content = (
                f"#EXTM3U\n#PLAYLIST:{name}\n# Created for {name.lower()} moments.\n"
                f"# Contains 15-20 carefully selected songs.\n"
            )
            playlist_file = music_folder / f"{name.replace(' ', '_')}.m3u"
            playlist_file.write_text(simple_content, encoding='utf-8')
            created_files.append(playlist_file)

        # Add a few fake MP3 files to make the folder feel populated
        sample_tracks = ["morning_run.mp3", "focus_beats.mp3", "weekend_chill.mp3"]
        for track in sample_tracks:
            track_path = music_folder / track
            # Use stub bytes so file has size and correct extension
            padded = SAMPLE_JPEG_BYTES + random.randbytes(random.randint(1500, 4000))
            write_binary_file(track_path, padded)
            created_files.append(track_path)
        
        print(f"    ✓ Generated music files")
        
        # Photos folder
        photos_folder = personal_folder / "Photos"
        ensure_directory(photos_folder)
        
        photo_catalog, entries = self.generate_photo_catalog(15)
        catalog_file = photos_folder / "Photo_Catalog.txt"
        catalog_file.write_text(photo_catalog, encoding='utf-8')
        created_files.append(catalog_file)
        created_files.extend(self.create_photo_files(photos_folder, entries))
        
        print(f"    ✓ Generated photo catalog")
        
        # Health folder
        health_folder = personal_folder / "Health"
        ensure_directory(health_folder)
        
        health_record = self.generate_health_records()
        health_file = health_folder / "Health_Records.pdf"
        health_file.write_text(health_record, encoding='utf-8')
        created_files.append(health_file)
        
        print(f"    ✓ Generated health records")
        
        # Receipts folder
        receipts_folder = personal_folder / "Receipts"
        ensure_directory(receipts_folder)
        
        for i in range(8):
            receipt = self.generate_receipt()
            date = datetime.now() - timedelta(days=random.randint(1, 90))
            receipt_file = receipts_folder / f"Receipt_{date.strftime('%Y%m%d')}_{i+1}.pdf"
            receipt_file.write_text(receipt, encoding='utf-8')
            created_files.append(receipt_file)
        
        print(f"    ✓ Generated receipts")
        
        return created_files
