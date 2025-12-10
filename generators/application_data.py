#!/usr/bin/env python3
"""
Application Data Generator
Creates realistic application installation info and data
"""

from datetime import datetime, timedelta
import hashlib
import random
from pathlib import Path

from config import INSTALLED_APPLICATIONS, USER_NAME, USER_EMAIL
from utils.helpers import ensure_directory, file_size_string, write_binary_file


class ApplicationDataGenerator:
    """Generates realistic application data"""
    
    def __init__(self, base_path, paths=None):
        self.base_path = Path(base_path)
        self.paths = paths or {}
        self.app_metadata = self._build_app_metadata()

    def _build_app_metadata(self):
        """
        Construct consistent metadata for installed applications so logs and
        manifests share the same install dates and versions.
        """
        metadata = {}
        for app in INSTALLED_APPLICATIONS:
            install_date = datetime.now() - timedelta(days=random.randint(30, 1000))
            version = f"{random.randint(1, 20)}.{random.randint(0, 9)}.{random.randint(0, 99)}"
            size_mb = random.randint(50, 2000)
            last_used = datetime.now() - timedelta(days=random.randint(0, 30))
            metadata[app] = {
                "install_date": install_date,
                "version": version,
                "size_mb": size_mb,
                "last_used": last_used,
            }
        return metadata

    def _make_stub_binary(self, path: Path, size_kb: int = 256):
        """
        Create a small placeholder binary so executables exist on disk.
        """
        size_bytes = max(size_kb, 32) * 1024
        header = b"MZ"  # Windows binary header magic
        padding = random.randbytes(size_bytes - len(header))
        return write_binary_file(path, header + padding)
    
    def generate_installed_apps_list(self):
        """Generate list of installed applications"""
        
        content = f"""INSTALLED APPLICATIONS
Computer: {USER_NAME}'s Workstation
Last Updated: {datetime.now().strftime('%B %d, %Y %H:%M:%S')}

═══════════════════════════════════════════════════════════════════════════

        This system has the following applications installed:

"""
        
        for i, app in enumerate(INSTALLED_APPLICATIONS, 1):
            details = self.app_metadata[app]
            content += f"\n{i}. {app}\n"
            content += f"   Version: {details['version']}\n"
            content += f"   Installed: {details['install_date'].strftime('%m/%d/%Y')}\n"
            content += f"   Size: {file_size_string(details['size_mb'] * 1024 * 1024)}\n"
            content += f"   Last Used: {details['last_used'].strftime('%m/%d/%Y')}\n"
        
        content += f"""

═══════════════════════════════════════════════════════════════════════════

SYSTEM INFORMATION

Operating System: Windows 11 Pro
Version: 22H2
Build: 22621.2715
Processor: Intel Core i7-12700K @ 3.60GHz
RAM: 32 GB
Storage: 1 TB SSD

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_recent_apps_activity(self):
        """Generate recent applications activity"""
        
        apps_with_activity = [
            ("Google Chrome", "Browsing sessions, 50+ tabs managed"),
            ("Visual Studio Code", "Active development, 15 projects"),
            ("Microsoft Office", "Document editing, presentations"),
            ("Zoom", "Video meetings, 20+ calls this month"),
            ("Slack", "Team communication, daily active"),
            ("Git", "Version control, 150+ commits"),
            ("Docker Desktop", "Container management, 8 running containers"),
            ("Spotify", "Music streaming, 40+ hours this month")
        ]
        
        content = f"""RECENT APPLICATION ACTIVITY
User: {USER_NAME}
Period: Last 30 Days

═══════════════════════════════════════════════════════════════════════════

"""
        
        for app, activity in apps_with_activity:
            last_used = datetime.now() - timedelta(hours=random.randint(1, 48))
            usage_time = random.randint(20, 300)
            
            content += f"{app}\n"
            content += f"  Last Used: {last_used.strftime('%B %d, %Y at %I:%M %p')}\n"
            content += f"  Total Time: {usage_time} hours\n"
            content += f"  Activity: {activity}\n"
            content += "-"*70 + "\n\n"
        
        return content
    
    def generate_software_licenses(self):
        """Generate software license information"""
        
        licenses = [
            ("Microsoft Office 365", "Subscription", "Annual", "$99.99/year", "Active"),
            ("Adobe Acrobat Pro", "Perpetual", "One-time", "$449.99", "Active"),
            ("WinRAR", "Trial", "40-day trial", "Free", "Expired (Still works)"),
            ("Zoom Pro", "Subscription", "Monthly", "$14.99/month", "Active"),
            ("Spotify Premium", "Subscription", "Monthly", "$9.99/month", "Active"),
            ("JetBrains All Products", "Subscription", "Annual", "$249/year", "Active"),
            ("Slack Business+", "Subscription", "Per user/month", "$12.50/user", "Active")
        ]
        
        content = f"""SOFTWARE LICENSE INFORMATION
{USER_NAME}
{USER_EMAIL}

Generated: {datetime.now().strftime('%B %d, %Y')}

═══════════════════════════════════════════════════════════════════════════

"""
        
        for software, license_type, billing, cost, status in licenses:
            renewal = datetime.now() + timedelta(days=random.randint(30, 365))
            
            content += f"SOFTWARE: {software}\n"
            content += f"License Type: {license_type}\n"
            content += f"Billing: {billing}\n"
            content += f"Cost: {cost}\n"
            content += f"Status: {status}\n"
            
            if status == "Active" and license_type == "Subscription":
                content += f"Next Renewal: {renewal.strftime('%B %d, %Y')}\n"
            
            content += "-"*70 + "\n\n"
        
        content += f"""
TOTAL ANNUAL SOFTWARE COSTS: Approximately $600/year

═══════════════════════════════════════════════════════════════════════════

NOTES:
• All subscriptions set to auto-renew
• Payment method: Visa ending in 5847
• Renewal notifications sent to {USER_EMAIL}
• Keep licenses backed up in secure location

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_download_history(self):
        """Generate download history"""
        
        downloads = [
            ("ChromeSetup.exe", "Google Chrome installer", 1.3, "Chrome"),
            ("FirefoxInstaller.exe", "Firefox installer", 54.2, "Firefox"),
            ("MicrosoftEdgeSetup.exe", "Edge installer", 2.1, "Edge"),
            ("vlc-3.0.20-win64.exe", "VLC installer", 40.5, "Chrome"),
            ("ZoomInstallerFull.msi", "Zoom client", 67.2, "Edge"),
            ("winrar-x64-701.exe", "WinRAR archive utility", 3.4, "Firefox"),
            ("7z2408-x64.exe", "7-Zip archive utility", 1.7, "Chrome"),
            ("Docker_Desktop_Installer.exe", "Docker Desktop", 512.0, "Chrome"),
            ("Git-2.42.0-64-bit.exe", "Git for Windows", 48.5, "Edge"),
            ("NotepadPlusPlus-8.6.2-x64.exe", "Notepad++", 4.5, "Firefox"),
            ("BoxDrive.msi", "Box Drive client", 34.4, "Chrome"),
            ("SlackSetup.exe", "Slack desktop", 93.7, "Chrome"),
            ("spotify_installer.exe", "Spotify", 1.1, "Edge"),
            ("AdobeReader_DC_Installer.exe", "Adobe Acrobat Reader", 201.2, "Firefox"),
            ("project_budget.xlsx", "Q4 budget spreadsheet", 0.9, "Chrome"),
            ("client_contract.docx", "Client contract draft", 0.4, "Edge"),
            ("tax_returns_2024.zip", "Tax returns bundle", 12.8, "Chrome"),
            ("logs_archive_2024-01-05.7z", "System logs", 6.1, "Firefox"),
            ("meeting_notes.txt", "Team sync notes", 0.02, "Edge"),
            ("design_assets_v3.rar", "Design assets", 48.2, "Chrome"),
            ("invoice_2024-11-15.pdf", "Vendor invoice", 0.3, "Edge"),
            ("aws_architecture_diagram.png", "Architecture diagram", 0.8, "Firefox"),
        ]
        
        content = f"""DOWNLOAD HISTORY
User: {USER_NAME}
Last 30 Days

═══════════════════════════════════════════════════════════════════════════

"""
        
        for filename, description, size_mb, source in downloads:
            download_date = datetime.now() - timedelta(days=random.randint(1, 30))
            
            content += f"File: {filename}\n"
            content += f"Description: {description}\n"
            content += f"Size: {file_size_string(int(size_mb * 1024 * 1024))}\n"
            content += f"Downloaded: {download_date.strftime('%B %d, %Y at %I:%M %p')}\n"
            content += f"Status: Complete via {source}\n"
            content += "-"*70 + "\n\n"
        
        return content

    def generate_fake_installers(self):
        """
        Create fake installer binaries in Downloads/Software_Installers with
        realistic filenames and checksum metadata.
        """
        installers_dir = self.base_path / "Downloads" / "Software_Installers"
        ensure_directory(installers_dir)

        created = []
        manifest_lines = ["FAKE INSTALLERS (placeholders for sandbox realism)\n"]

        extension_overrides = {
            "Google Chrome": "ChromeSetup.exe",
            "Mozilla Firefox": "FirefoxInstaller.exe",
            "Microsoft Edge": "MicrosoftEdgeSetup.exe",
            "Microsoft Teams": "TeamsSetup.exe",
            "Zoom": "ZoomInstallerFull.msi",
            "VLC Media Player": "vlc-3.0.20-win64.exe",
            "WinRAR": "winrar-x64-701.exe",
            "7-Zip": "7z2408-x64.exe",
            "Visual Studio Code": "VSCodeUserSetup-x64-1.84.2.exe",
            "Docker Desktop": "Docker Desktop Installer.exe",
            "Git": "Git-2.42.0-64-bit.exe",
            "Google Drive": "GoogleDriveFSSetup.exe",
            "Dropbox": "DropboxInstaller.exe",
            "Microsoft OneDrive": "OneDriveSetup.exe",
            "Box": "BoxDrive.msi",
            "Spotify": "spotify_installer.exe",
            "Slack": "SlackSetup.exe",
            "Notepad++": "NotepadPlusPlus-8.6.2-x64.exe",
            "Adobe Acrobat Reader DC": "AdobeReader_DC_Installer.exe",
        }

        for app, details in self.app_metadata.items():
            installer_name = extension_overrides.get(
                app, f"{app.replace(' ', '_')}_Setup.exe"
            )
            installer_path = installers_dir / installer_name

            # vary size to look more natural
            size_kb = random.randint(1800, 52000)  # ~2MB to ~50MB
            self._make_stub_binary(installer_path, size_kb=size_kb)

            checksum = hashlib.sha256(installer_path.read_bytes()).hexdigest()
            created.append(installer_path)
            manifest_lines.append(
                f"{installer_name} | v{details['version']} | "
                f"{details['install_date'].strftime('%Y-%m-%d')} | "
                f"sha256={checksum}"
            )

        manifest = installers_dir / "INSTALLERS_MANIFEST.txt"
        manifest.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
        created.append(manifest)
        return created

    def _write_text_placeholder(self, path: Path, title: str, body: str):
        path.write_text(f"{title}\n\n{body}\n", encoding="utf-8")
        return path

    def create_download_artifacts(self):
        """
        Materialize files referenced in download history so the disk reflects
        actual downloads (archives, docs, spreadsheets, pdfs, text).
        """
        downloads_dir = self.base_path / "Downloads"
        ensure_directory(downloads_dir)
        created = []

        archive_targets = [
            ("tax_returns_2024.zip", 12.8),
            ("logs_archive_2024-01-05.7z", 6.1),
            ("design_assets_v3.rar", 48.2),
        ]
        doc_targets = [
            ("client_contract.docx", "Client Contract Draft", "Contract terms and placeholders for signatures."),
            ("project_budget.xlsx", "Budget Worksheet", "Quarterly budget allocations."),
            ("invoice_2024-11-15.pdf", "Invoice 2024-11-15", "Vendor invoice and line items."),
            ("meeting_notes.txt", "Meeting Notes", "Key decisions and action items."),
            ("aws_architecture_diagram.png", "AWS Architecture Diagram", "PNG placeholder"),
        ]

        # Archives
        for filename, size_mb in archive_targets:
            path = downloads_dir / filename
            size_kb = max(int(size_mb * 1024), 512)
            self._make_stub_binary(path, size_kb=size_kb)
            created.append(path)

        # Documents / PDFs / text
        for filename, title, summary in doc_targets:
            path = downloads_dir / filename
            if filename.endswith((".docx", ".xlsx", ".pdf")):
                # use binary so size isn't too small
                self._make_stub_binary(path, size_kb=random.randint(250, 1200))
            elif filename.endswith(".png"):
                self._make_stub_binary(path, size_kb=random.randint(120, 600))
            else:
                self._write_text_placeholder(path, title, summary)
            created.append(path)

        return created

    def generate_application_usage_history(self):
        """
        Generate a consolidated application usage history file.
        """
        lines = [
            f"APPLICATION USAGE HISTORY - Last 60 Days",
            f"User: {USER_NAME}",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
        ]
        for app, details in self.app_metadata.items():
            sessions = random.randint(3, 45)
            avg_minutes = random.randint(5, 80)
            last_session = details["last_used"].strftime('%Y-%m-%d %H:%M:%S')
            lines.append(f"{app}")
            lines.append(f"  Sessions: {sessions}")
            lines.append(f"  Avg Session Length: {avg_minutes} minutes")
            lines.append(f"  Last Used: {last_session}")
            lines.append("  Launch Method: Start Menu / Taskbar")
            lines.append("-" * 70)
        return "\n".join(lines) + "\n"

    def materialize_installation_folders(self):
        """
        Create realistic installation directories so the filesystem looks used.
        """
        created_files = []
        program_files = Path(self.paths.get("program_files", self.base_path / "Program Files"))
        roaming_appdata = Path(self.paths.get("appdata_roaming", self.base_path / "AppData" / "Roaming"))
        ensure_directory(program_files)
        ensure_directory(roaming_appdata)

        for app, details in self.app_metadata.items():
            safe_name = app.replace(" ", "_")
            install_dir = program_files / safe_name
            ensure_directory(install_dir)

            install_log = install_dir / "install.log"
            install_log.write_text(
                (
                    f"{app} installation log\n"
                    f"Version: {details['version']}\n"
                    f"Installed: {details['install_date'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"Last Launched: {details['last_used'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    "Status: Completed successfully\n"
                ),
                encoding="utf-8",
            )
            created_files.append(install_log)

            settings_file = install_dir / "config.ini"
            settings_file.write_text(
                (
                    "[General]\n"
                    f"install_path={install_dir}\n"
                    f"user={USER_NAME}\n"
                    "auto_update=true\n"
                    f"last_update_check={datetime.now().strftime('%Y-%m-%d')}\n"
                ),
                encoding="utf-8",
            )
            created_files.append(settings_file)

            usage_log_dir = roaming_appdata / safe_name
            ensure_directory(usage_log_dir)
            usage_log = usage_log_dir / "usage.log"
            usage_log.write_text(
                (
                    f"App: {app}\n"
                    f"Sessions this month: {random.randint(3, 40)}\n"
                    f"Last used: {details['last_used'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    "Recent files opened: cache.db; settings.json; preferences.xml\n"
                ),
                encoding="utf-8",
            )
            created_files.append(usage_log)

        return created_files
    
    def generate_all_application_data(self):
        """Generate all application-related data"""
        created_files = []
        
        print("\n[*] Generating application data...")
        
        # Create Downloads folder content
        downloads_folder = self.base_path / "Downloads"
        ensure_directory(downloads_folder)
        
        # Installed apps list
        apps_list = self.generate_installed_apps_list()
        apps_file = downloads_folder / "Installed_Applications.txt"
        apps_file.write_text(apps_list, encoding='utf-8')
        created_files.append(apps_file)
        print(f"    ✓ Installed applications list")
        
        # Recent activity
        activity = self.generate_recent_apps_activity()
        activity_file = downloads_folder / "Recent_App_Activity.txt"
        activity_file.write_text(activity, encoding='utf-8')
        created_files.append(activity_file)
        print(f"    ✓ Application activity")
        
        # Software licenses
        licenses = self.generate_software_licenses()
        licenses_file = downloads_folder / "Software_Licenses.txt"
        licenses_file.write_text(licenses, encoding='utf-8')
        created_files.append(licenses_file)
        print(f"    ✓ Software licenses")
        
        # Download history
        download_history = self.generate_download_history()
        history_file = downloads_folder / "Download_History.txt"
        history_file.write_text(download_history, encoding='utf-8')
        created_files.append(history_file)
        print(f"    ✓ Download history")

        install_files = self.materialize_installation_folders()
        created_files.extend(install_files)
        print(f"    ✓ Application install footprints ({len(install_files)} files)")

        installer_files = self.generate_fake_installers()
        created_files.extend(installer_files)
        print(f"    ✓ Fake installers created ({len(installer_files)} files)")

        artifact_files = self.create_download_artifacts()
        created_files.extend(artifact_files)
        print(f"    ✓ Download artifacts created ({len(artifact_files)} files)")

        usage_history = self.generate_application_usage_history()
        usage_file = downloads_folder / "Application_Usage_History.txt"
        usage_file.write_text(usage_history, encoding="utf-8")
        created_files.append(usage_file)
        print("    ✓ Application usage history")
        
        return created_files
