#!/usr/bin/env python3
"""
Sandbox Population Script - Creates realistic file system content
Generates authentic-looking documents, files, and folder structures
for malware analysis sandbox environments.

This modular script creates:
- Realistic browser data (Chrome, Firefox, Edge) with history and credentials
- Tax documents (Federal & California State) for multiple years
- Investment statements with stocks, bonds, and ETFs
- Office documents (reports, presentations, spreadsheets)
- Personal folders (music, photos, health records)
- Application data and software licenses
- Comprehensive credentials for various services
- Git and SSH configurations

Author: Sandbox Security Team
Version: 2.0
Last Updated: December 2024
"""

import sys
from pathlib import Path
from datetime import datetime

# Import configuration
from config import USER_NAME, USER_EMAIL, COMPANY_NAME

# Import all generators
from generators.browser_data import BrowserDataGenerator
from generators.tax_documents import TaxDocumentGenerator
from generators.investment_documents import InvestmentDocumentGenerator
from generators.office_documents import OfficeDocumentGenerator
from generators.personal_folders import PersonalFoldersGenerator
from generators.credentials import CredentialsGenerator
from generators.application_data import ApplicationDataGenerator
from generators.enhanced_documents import EnhancedDocumentGenerator

# Import utilities
from utils.helpers import ensure_directory, get_windows_paths


class SandboxPopulator:
    """Main class that orchestrates the sandbox population process"""
    
    def __init__(self, base_path=None):
        """
        Initialize the sandbox populator
        
        Args:
            base_path: Base directory path for file creation (default: user's home)
        """
        self.paths = get_windows_paths(base_path)
        self.base_path = self.paths["home"]
        
        self.created_files = []
        
        # Initialize all generators
        self.browser_gen = BrowserDataGenerator(self.base_path, self.paths)
        self.tax_gen = TaxDocumentGenerator(self.base_path)
        self.investment_gen = InvestmentDocumentGenerator(self.base_path)
        self.office_gen = OfficeDocumentGenerator(self.base_path)
        self.personal_gen = PersonalFoldersGenerator(self.base_path)
        self.creds_gen = CredentialsGenerator(self.base_path)
        self.app_gen = ApplicationDataGenerator(self.base_path, self.paths)
        self.enhanced_gen = EnhancedDocumentGenerator(self.base_path)
    
    def create_base_directory_structure(self):
        """Create the base directory structure"""
        
        print("\n[*] Creating base directory structure...")
        
        base_folders = [
            self.paths["desktop"],
            self.paths["documents"],
            self.paths["downloads"],
            self.paths["pictures"],
            self.paths["music"],
            self.paths["videos"],
            self.paths["appdata_local"],
            self.paths["appdata_roaming"],
            self.paths["program_files"],
        ]
        
        for folder_path in base_folders:
            ensure_directory(folder_path)
            print(f"    ✓ {folder_path}")
    
    def populate_all(self):
        """
        Run all population methods to create comprehensive sandbox environment
        """
        
        print("\n" + "="*80)
        print(" "*20 + "SANDBOX FILE SYSTEM POPULATOR")
        print("="*80)
        print(f"\nTarget Directory: {self.base_path}")
        print(f"User: {USER_NAME}")
        print(f"Email: {USER_EMAIL}")
        print(f"Company: {COMPANY_NAME}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("="*80)
        
        try:
            # Step 1: Create base structure
            self.create_base_directory_structure()
            
            # Step 2: Browser data (history, credentials, cookies)
            files = self.browser_gen.generate_all_browser_data()
            self.created_files.extend(files)
            
            # Step 3: Tax documents
            files = self.tax_gen.generate_all_tax_documents()
            self.created_files.extend(files)
            
            # Step 4: Investment documents
            files = self.investment_gen.generate_all_investment_documents()
            self.created_files.extend(files)
            
            # Step 5: Office documents
            files = self.office_gen.generate_all_office_documents()
            self.created_files.extend(files)
            
            # Step 6: Personal folders
            files = self.personal_gen.generate_all_personal_folders()
            self.created_files.extend(files)
            
            # Step 7: Credentials
            files = self.creds_gen.generate_all_credentials()
            self.created_files.extend(files)
            
            # Step 8: Application data
            files = self.app_gen.generate_all_application_data()
            self.created_files.extend(files)
            
            # Step 9: Enhanced documents
            files = self.enhanced_gen.generate_all_enhanced_documents()
            self.created_files.extend(files)
            
            # Success summary
            print("\n" + "="*80)
            print(f"\n[✓] SUCCESS! Created {len(self.created_files)} files")
            print("="*80)
            
            print("\n📊 SUMMARY BY CATEGORY:")
            print("  • Browser Data (Chrome, Firefox, Edge)")
            print("  • Tax Documents (Federal & State, 2022-2025)")
            print("  • Investment Statements (Stocks, Bonds, ETFs)")
            print("  • Office Documents (Reports, Presentations)")
            print("  • Personal Files (Music, Photos, Health)")
            print("  • Credentials (Git, SSH, AWS, Docker, NPM)")
            print("  • Application Data & Licenses")
            print("  • Employment Documents & Reviews")
            
            print("\n🎯 KEY FEATURES:")
            print("  ✓ Realistic browsing history for 3 browsers")
            print("  ✓ Saved passwords for 15+ websites")
            print("  ✓ Complete tax returns with SSN")
            print("  ✓ Investment portfolio with real stock symbols")
            print("  ✓ Professional work documents")
            print("  ✓ Personal music, photos, and health records")
            print("  ✓ Git and development environment configs")
            print("  ✓ Software licenses and installation data")
            
            print("\n" + "="*80)
            print("Your sandbox environment is now populated with realistic data!")
            print("All content is FAKE and designed for malware analysis purposes.")
            print("="*80 + "\n")
            
            return True
            
        except Exception as e:
            print(f"\n[✗] ERROR: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_statistics(self):
        """Get statistics about created files"""
        
        stats = {
            "total_files": len(self.created_files),
            "total_size_bytes": sum(f.stat().st_size for f in self.created_files if f.exists()),
            "directories": set(f.parent for f in self.created_files)
        }
        
        return stats


def print_usage():
    """Print usage information"""
    
    print("""
Sandbox Populator - Usage
=========================

Basic Usage:
    python main.py

Custom Base Path:
    python main.py /path/to/directory

Description:
    This script creates a realistic file system environment for malware
    analysis sandboxes. It generates authentic-looking documents, browser
    data, credentials, and personal files that make the sandbox appear
    as a genuine user environment.

Generated Content:
    • Browser history and credentials (Chrome, Firefox, Edge)
    • Tax documents (Federal and California State returns)
    • Investment statements with stock/bond transactions
    • Office documents (reports, presentations, proposals)
    • Personal files (music playlists, photo catalogs, health records)
    • Development credentials (Git, SSH, AWS, Docker)
    • Application installation data and licenses
    • Employment contracts and performance reviews

Safety:
    All generated data is FAKE and should only be used for:
    - Malware analysis
    - Security research
    - Sandbox environment setup
    
    Do NOT use fake credentials or SSN for any real purposes!

Examples:
    # Populate home directory
    python main.py
    
    # Populate specific directory
    python main.py /opt/sandbox/user_home
    
    # Populate current directory
    python main.py .

For more information, visit: https://github.com/your-repo/sandbox_populator
""")


# ==========================================
# MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    # Check for help flag
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        print_usage()
        sys.exit(0)
    
    # Get base path from command line or use default
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1]).resolve()
        
        # Confirm if path doesn't exist
        if not base_path.exists():
            response = input(f"\nDirectory '{base_path}' doesn't exist. Create it? (y/n): ")
            if response.lower() != 'y':
                print("Aborted.")
                sys.exit(0)
            base_path.mkdir(parents=True, exist_ok=True)
    else:
        base_path = None  # Will use home directory
    
    # Create and run populator
    print("\n" + "🔧 Initializing Sandbox Populator...")
    
    populator = SandboxPopulator(base_path)
    
    try:
        success = populator.populate_all()
        
        if success:
            # Print statistics
            stats = populator.get_statistics()
            print(f"\n📈 STATISTICS:")
            print(f"  Total Files Created: {stats['total_files']}")
            print(f"  Total Size: {stats['total_size_bytes'] / (1024*1024):.2f} MB")
            print(f"  Directories Used: {len(stats['directories'])}")
            
            sys.exit(0)
        else:
            print("\n[!] Population completed with errors.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
