# Sandbox Populator

A comprehensive Python script that creates realistic file system environments for malware analysis sandboxes. This tool generates authentic-looking documents, browser data, credentials, and personal files to make sandbox environments appear as genuine user systems.

## 🎯 Purpose

Malware often checks for signs of sandbox environments (empty browser history, lack of personal files, etc.). This tool populates a sandbox with realistic data to evade these detection mechanisms and enable better malware analysis.

## ✨ Features

### Browser Data
- **Chrome, Firefox, and Edge** browsing history (200+ entries)
- **Saved passwords** for 15+ common websites
- **Cookies information** with realistic expiration dates
- Simulated login sessions and user preferences
- Browser artifacts saved into realistic profile folders (`AppData`-style), with SQLite history and JSON login data

### Financial Documents
- **Federal tax returns** (Form 1040, PDF) for 2022-2025
- **California state tax returns** (Form 540, PDF) for 2022-2025
- **W-2 forms** with realistic income and withholding (PDF)
- **Investment statements** (XLSX) with stocks, bonds, and ETFs
- Realistic transaction history with buy/sell orders

### Office Documents
- **Quarterly business reports** with metrics and KPIs (DOCX)
- **Project proposals** with budgets and timelines
- **Meeting presentations** with slide outlines (multiple PPTX decks)
- **Budget spreadsheets** (XLSX) with department expenses
- **Performance reviews** (2022-2024)
- **Employment contracts** and benefits documentation

### Personal Files
- **Music playlists** plus stub MP3 tracks
- **Photo catalogs** with metadata and real JPEG placeholders (with sidecar XMP)
- **Health records** with medical history
- **Shopping receipts** from various stores
- **Insurance policies** (health insurance)

### Development Credentials
- **Git configuration** (.gitconfig format)
- **SSH configuration** for GitHub, GitLab, AWS
- **Docker credentials** for container registries
- **AWS credentials** with access keys
- **NPM configuration** for Node.js development

### Application Data
- **Installed applications list** (20+ common apps) with footprints in `Program Files` and `AppData`
- **Software licenses** with subscription info
- **Recent activity logs** showing usage patterns
- **Download history** with file metadata plus stubbed installers/archives/docs

## 📋 Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/saasthavasan/sandbox_populator.git
cd sandbox_populator

# No additional installation needed - uses Python standard library only!
```

## 💻 Usage

### Basic Usage (Populate Home Directory)
```bash
python main.py
```

### Custom Directory
```bash
python main.py /path/to/sandbox/directory
```

### Help
```bash
python main.py --help
```

> Note: The script resolves Windows-style user folders automatically (`Desktop`, `Documents`, `Downloads`, `AppData`, `Program Files`) using `USERPROFILE`/`LOCALAPPDATA`/`APPDATA` when available, so generated artifacts land in realistic locations.

## 📁 Generated Structure

```
Base Directory/
├── Desktop/
│   ├── Tax Documents/
│   │   ├── 2022/ (Federal & State returns, W-2)
│   │   ├── 2023/
│   │   ├── 2024/
│   │   └── 2025/
│   ├── Investments/
│   │   └── (Annual investment statements, XLSX)
│   ├── Office/
│   │   ├── Reports/
│   │   ├── Presentations/
│   │   ├── Spreadsheets/
│   │   └── Projects/
│   └── Personal/
│       ├── Music/
│       ├── Photos/
│       ├── Health/
│       └── Receipts/
├── Documents/
│   ├── Browser_Data_Chrome/
│   ├── Browser_Data_Firefox/
│   ├── Browser_Data_Edge/
│   ├── Credentials/
│   ├── Work/
│   ├── Personal/
│   ├── Contracts/
│   └── Technical_Docs/
├── Downloads/
│   ├── Software_Installers/ (fake installers with checksums)
│   ├── Download_History.txt
│   ├── Application_Usage_History.txt
│   └── mixed docs/archives referenced by history
├── AppData/ (realistic browser profiles and app traces)
└── Program Files/ (app footprints and configs)
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# User Information
USER_NAME = "John Mathew"
USER_EMAIL = "john.mathew@beingMalicious.com"
COMPANY_NAME = "beingMalicious.com"
USER_SSN = "547-82-9163"  # Fake SSN

# Financial Settings
TAX_YEARS = [2022, 2023, 2024, 2025]
STOCK_HOLDINGS = ["AAPL", "GOOGL", "MSFT", ...]

# Applications
INSTALLED_APPLICATIONS = ["Chrome", "VS Code", "Docker", ...]
```

## 🔧 Project Structure

```
sandbox_populator/
├── main.py                 # Main orchestration script
├── config.py              # Configuration settings
├── generators/            # Content generators
│   ├── __init__.py
│   ├── browser_data.py
│   ├── tax_documents.py
│   ├── investment_documents.py
│   ├── office_documents.py
│   ├── personal_folders.py
│   ├── credentials.py
│   ├── application_data.py
│   └── enhanced_documents.py
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── helpers.py
├── README.md
└── .gitignore
```

## 🎨 Generated Content Examples

### Browser History Entry
```
[2024-12-05 14:32:15] Stack Overflow - Where Developers Learn
  URL: https://stackoverflow.com/questions/tagged/python
  Visits: 45
```

### Tax Return (Excerpt)
```
FORM 1040 - U.S. INDIVIDUAL INCOME TAX RETURN
Tax Year: 2024

Name: John Mathew
Social Security Number: 547-82-9163
Filing Status: ☒ Single

Wages, salaries, tips: $108,000.00
Federal tax withheld: $18,200.00
Refund: $320.00
```

### Investment Statement (Excerpt)
```
STOCK TRANSACTIONS
Date         Type    Symbol   Shares    Price      Total
12/01/2024   BUY     AAPL     25       $185.42    $4,635.50
11/15/2024   SELL    TSLA     10       $245.88    $2,458.80
```

## ⚠️ Important Warnings

### ⚡ FOR SECURITY RESEARCH ONLY

This tool is designed **exclusively** for:
- ✅ Malware analysis in isolated sandbox environments
- ✅ Security research and testing
- ✅ Red team exercises (authorized)
- ✅ Educational purposes in controlled environments

### ❌ DO NOT USE FOR:
- Creating fake identities for fraud
- Tax fraud or financial crimes
- Identity theft or impersonation
- Any illegal activities

### 🔒 Data Safety

- **All generated data is FAKE**
- SSN, addresses, financial data are randomly generated
- Passwords are fake and should never be used
- Names and companies are fictional or test data

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Additional document types (more file formats)
- More realistic content generators
- Support for different locales/countries
- Binary file generation (images, executables)
- Database file generation (SQLite, etc.)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Designed for security researchers working with sandbox environments
- Inspired by the need for realistic sandbox evasion testing
- Thanks to the malware analysis community for feedback

## 📧 Contact

Project Link: [https://github.com/saasthavasan/sandbox_populator](https://github.com/saasthavasan/sandbox_populator)

---

**⚠️ LEGAL DISCLAIMER:** This tool is provided for educational and research purposes only. The authors are not responsible for any misuse or damage caused by this program. Always ensure you have proper authorization before using this tool in any environment.
