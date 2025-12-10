#!/usr/bin/env python3
"""
Investment Document Generator
Creates realistic investment statements with stocks, bonds, and ETFs
"""

import random
from datetime import datetime, timedelta
from pathlib import Path

from config import (
    USER_NAME, USER_ADDRESS, USER_CITY, USER_STATE, USER_ZIP,
    STOCK_HOLDINGS, ETF_HOLDINGS, BOND_HOLDINGS, TAX_YEARS
)
from utils.helpers import format_currency, ensure_directory, random_date


class InvestmentDocumentGenerator:
    """Generates realistic investment statements"""
    
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        
        # Stock prices (fake but realistic ranges)
        self.stock_prices = {
            "AAPL": (150, 195), "GOOGL": (90, 145), "MSFT": (250, 380),
            "AMZN": (95, 175), "TSLA": (150, 410), "NVDA": (200, 495),
            "META": (120, 350), "NFLX": (300, 600), "AMD": (75, 165),
            "INTC": (25, 50), "JPM": (120, 165), "BAC": (25, 40),
            "V": (200, 275), "MA": (320, 450), "DIS": (80, 180)
        }
        
        self.etf_prices = {
            "SPY": (360, 470), "QQQ": (300, 420), "VTI": (190, 250),
            "VOO": (350, 450), "IVV": (360, 470), "VEA": (40, 52),
            "VWO": (38, 50), "AGG": (95, 108), "BND": (70, 82),
            "TLT": (90, 105)
        }
        
        self.bond_prices = {
            "US Treasury 10Y": (95, 102), "US Treasury 5Y": (97, 101),
            "Corporate Bond AAA": (98, 103), "Municipal Bond CA": (99, 104),
            "TIPS 2030": (96, 101)
        }
    
    def generate_stock_transaction(self, symbol, year, transaction_type="buy"):
        """Generate a realistic stock transaction"""
        price_range = self.stock_prices.get(symbol, (50, 200))
        price = round(random.uniform(price_range[0], price_range[1]), 2)
        shares = random.choice([5, 10, 15, 20, 25, 50, 100])
        
        # Generate date within the year
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        trans_date = random_date(start_date, end_date)
        
        total = round(price * shares, 2)
        commission = 0  # Most brokers are commission-free now
        
        return {
            "date": trans_date,
            "type": transaction_type,
            "symbol": symbol,
            "shares": shares,
            "price": price,
            "commission": commission,
            "total": total
        }
    
    def generate_etf_transaction(self, symbol, year, transaction_type="buy"):
        """Generate an ETF transaction"""
        price_range = self.etf_prices.get(symbol, (100, 300))
        price = round(random.uniform(price_range[0], price_range[1]), 2)
        shares = random.choice([10, 20, 30, 50, 100])
        
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        trans_date = random_date(start_date, end_date)
        
        total = round(price * shares, 2)
        
        return {
            "date": trans_date,
            "type": transaction_type,
            "symbol": symbol,
            "shares": shares,
            "price": price,
            "commission": 0,
            "total": total
        }
    
    def generate_bond_transaction(self, bond_name, year, transaction_type="buy"):
        """Generate a bond transaction"""
        price_range = self.bond_prices.get(bond_name, (95, 105))
        price = round(random.uniform(price_range[0], price_range[1]), 2)
        face_value = random.choice([1000, 5000, 10000])
        units = random.choice([1, 5, 10])
        
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        trans_date = random_date(start_date, end_date)
        
        total = round((price / 100) * face_value * units, 2)
        
        return {
            "date": trans_date,
            "type": transaction_type,
            "bond": bond_name,
            "face_value": face_value,
            "units": units,
            "price": price,
            "total": total
        }
    
    def generate_annual_statement(self, year):
        """Generate complete annual investment statement"""
        
        # Generate transactions
        stock_transactions = []
        etf_transactions = []
        bond_transactions = []
        
        # Randomly select securities to trade
        num_stocks = random.randint(5, 10)
        num_etfs = random.randint(3, 6)
        num_bonds = random.randint(2, 4)
        
        selected_stocks = random.sample(STOCK_HOLDINGS, num_stocks)
        selected_etfs = random.sample(ETF_HOLDINGS, num_etfs)
        selected_bonds = random.sample(BOND_HOLDINGS, num_bonds)
        
        # Generate buy transactions
        for stock in selected_stocks:
            stock_transactions.append(self.generate_stock_transaction(stock, year, "BUY"))
            # Some stocks have sells too
            if random.random() > 0.6:
                stock_transactions.append(self.generate_stock_transaction(stock, year, "SELL"))
        
        for etf in selected_etfs:
            etf_transactions.append(self.generate_etf_transaction(etf, year, "BUY"))
        
        for bond in selected_bonds:
            bond_transactions.append(self.generate_bond_transaction(bond, year, "BUY"))
        
        # Sort all transactions by date
        stock_transactions.sort(key=lambda x: x["date"])
        etf_transactions.sort(key=lambda x: x["date"])
        bond_transactions.sort(key=lambda x: x["date"])
        
        # Calculate totals
        total_invested = sum(t["total"] for t in stock_transactions + etf_transactions + bond_transactions if t["type"] == "BUY")
        total_proceeds = sum(t["total"] for t in stock_transactions if t["type"] == "SELL")
        
        # Calculate portfolio value at year end
        portfolio_value = total_invested - total_proceeds + random.randint(5000, 25000)
        
        content = f"""ANNUAL INVESTMENT STATEMENT
Year: {year}

═══════════════════════════════════════════════════════════════════════════

ACCOUNT INFORMATION

Account Holder: {USER_NAME}
Account Number: ****-****-5827
Account Type: Individual Brokerage Account
Statement Period: January 1, {year} - December 31, {year}

Brokerage Firm: Fidelity Investments
Address: 245 Summer Street, Boston, MA 02210
Phone: 1-800-343-3548

═══════════════════════════════════════════════════════════════════════════

ACCOUNT SUMMARY

Beginning Balance (Jan 1, {year}):              {format_currency(portfolio_value - (total_invested - total_proceeds))}
Deposits & Contributions:                       {format_currency(total_invested)}
Withdrawals & Distributions:                    {format_currency(total_proceeds)}
Net Investment Gain/Loss:                       {format_currency(random.randint(2000, 15000))}

Ending Balance (Dec 31, {year}):                {format_currency(portfolio_value)}

═══════════════════════════════════════════════════════════════════════════

STOCK TRANSACTIONS

Date         Type    Symbol   Shares    Price      Commission   Total
───────────────────────────────────────────────────────────────────────────
"""
        
        for trans in stock_transactions:
            content += f"{trans['date'].strftime('%m/%d/%Y')}   {trans['type']:4}   "
            content += f"{trans['symbol']:6}   {trans['shares']:4}    "
            content += f"${trans['price']:7.2f}    ${trans['commission']:5.2f}    "
            content += f"{format_currency(trans['total']):>12}\n"
        
        content += "\n"
        content += f"Total Stock Purchases:                          {format_currency(sum(t['total'] for t in stock_transactions if t['type'] == 'BUY'))}\n"
        content += f"Total Stock Sales:                              {format_currency(sum(t['total'] for t in stock_transactions if t['type'] == 'SELL'))}\n"
        
        content += f"""
═══════════════════════════════════════════════════════════════════════════

ETF TRANSACTIONS

Date         Type    Symbol   Shares    Price      Commission   Total
───────────────────────────────────────────────────────────────────────────
"""
        
        for trans in etf_transactions:
            content += f"{trans['date'].strftime('%m/%d/%Y')}   {trans['type']:4}   "
            content += f"{trans['symbol']:6}   {trans['shares']:4}    "
            content += f"${trans['price']:7.2f}    ${trans['commission']:5.2f}    "
            content += f"{format_currency(trans['total']):>12}\n"
        
        content += "\n"
        content += f"Total ETF Purchases:                            {format_currency(sum(t['total'] for t in etf_transactions))}\n"
        
        content += f"""
═══════════════════════════════════════════════════════════════════════════

BOND TRANSACTIONS

Date         Type    Bond Name                 Units   Price    Total
───────────────────────────────────────────────────────────────────────────
"""
        
        for trans in bond_transactions:
            content += f"{trans['date'].strftime('%m/%d/%Y')}   {trans['type']:4}   "
            content += f"{trans['bond']:25} {trans['units']:4}   "
            content += f"{trans['price']:6.2f}   {format_currency(trans['total']):>12}\n"
        
        content += "\n"
        content += f"Total Bond Purchases:                           {format_currency(sum(t['total'] for t in bond_transactions))}\n"
        
        content += f"""
═══════════════════════════════════════════════════════════════════════════

CURRENT HOLDINGS (as of December 31, {year})

STOCKS:
"""
        
        # Show current stock holdings
        for stock in selected_stocks:
            # Use default price range if stock not in dictionary
            price_range = self.stock_prices.get(stock, (50, 200))
            current_price = round(random.uniform(price_range[0], price_range[1]), 2)
            shares_owned = sum(t["shares"] for t in stock_transactions if t["symbol"] == stock and t["type"] == "BUY")
            shares_owned -= sum(t["shares"] for t in stock_transactions if t["symbol"] == stock and t["type"] == "SELL")
            
            if shares_owned > 0:
                market_value = shares_owned * current_price
                content += f"  {stock:6}  {shares_owned:4} shares @ ${current_price:7.2f}  =  {format_currency(market_value)}\n"
        
        content += "\nETFs:\n"
        
        for etf in selected_etfs:
            # Use default price range if ETF not in dictionary
            price_range = self.etf_prices.get(etf, (100, 300))
            current_price = round(random.uniform(price_range[0], price_range[1]), 2)
            shares_owned = sum(t["shares"] for t in etf_transactions if t["symbol"] == etf)
            market_value = shares_owned * current_price
            content += f"  {etf:6}  {shares_owned:4} shares @ ${current_price:7.2f}  =  {format_currency(market_value)}\n"
        
        content += "\nBONDS:\n"
        
        for bond in selected_bonds:
            trans = [t for t in bond_transactions if t["bond"] == bond]
            if trans:
                total_value = sum(t["total"] for t in trans)
                content += f"  {bond:30}  {format_currency(total_value)}\n"
        
        content += f"""
═══════════════════════════════════════════════════════════════════════════

YEAR-END TAX INFORMATION

Total Dividends Received:                       {format_currency(random.randint(500, 2500))}
Total Interest Received:                        {format_currency(random.randint(200, 800))}
Short-term Capital Gains:                       {format_currency(random.randint(0, 3000))}
Long-term Capital Gains:                        {format_currency(random.randint(1000, 8000))}

Form 1099-DIV and 1099-INT will be mailed by January 31, {year + 1}

═══════════════════════════════════════════════════════════════════════════

IMPORTANT INFORMATION

This statement is provided for informational purposes. Please review carefully
and contact us immediately if you have any questions or notice any discrepancies.

For customer service: 1-800-343-3548
Online access: www.fidelity.com

Thank you for choosing Fidelity Investments.

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_all_investment_documents(self):
        """Generate investment statements for all years"""
        created_files = []
        
        print("\n[*] Generating investment documents...")
        
        investments_folder = self.base_path / "Desktop" / "Investments"
        ensure_directory(investments_folder)
        
        for year in TAX_YEARS:
            statement_content = self.generate_annual_statement(year)
            statement_file = investments_folder / f"Investment_Statement_{year}.xlsx"
            statement_file.write_text(statement_content, encoding='utf-8')
            created_files.append(statement_file)
            
            print(f"    ✓ Generated investment statement for {year}")
        
        return created_files
