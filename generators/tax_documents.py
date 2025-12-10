#!/usr/bin/env python3
"""
Tax Document Generator
Creates realistic federal and state tax returns for California
"""

from datetime import datetime
from pathlib import Path

from config import (
    USER_NAME, USER_SSN, USER_ADDRESS, USER_CITY, 
    USER_STATE, USER_ZIP, TAX_YEARS, FEDERAL_TAX_BRACKETS,
    STATE_TAX_BRACKETS, USER_FIRST_NAME, USER_LAST_NAME
)
from utils.helpers import format_currency, ensure_directory, create_pdf


class TaxDocumentGenerator:
    """Generates realistic tax documents"""
    
    def __init__(self, base_path):
        self.base_path = Path(base_path)
    
    def generate_federal_tax_return(self, year):
        """Generate Form 1040 (Federal Tax Return)"""
        tax_data = FEDERAL_TAX_BRACKETS[year]
        
        # Calculate various tax components
        income = tax_data["income"]
        standard_deduction = 12950 if year <= 2022 else 13850 if year <= 2023 else 14600
        taxable_income = income - standard_deduction
        tax_paid = tax_data["tax_paid"]
        refund = tax_data["refund"]
        
        content = f"""FORM 1040 - U.S. INDIVIDUAL INCOME TAX RETURN
Tax Year: {year}

═══════════════════════════════════════════════════════════════════════════

TAXPAYER INFORMATION

Name: {USER_NAME}
Social Security Number: {USER_SSN}
Address: {USER_ADDRESS}
City, State, ZIP: {USER_CITY}, {USER_STATE} {USER_ZIP}

Filing Status: ☒ Single  ☐ Married Filing Jointly  ☐ Head of Household

═══════════════════════════════════════════════════════════════════════════

INCOME

1.  Wages, salaries, tips (W-2)                          {format_currency(income)}
2.  Interest income                                      {format_currency(325)}
3.  Dividend income                                      {format_currency(892)}
4.  State tax refund                                     {format_currency(0)}
5.  Business income                                      {format_currency(0)}

    TOTAL INCOME (Lines 1-5)                            {format_currency(income + 1217)}

═══════════════════════════════════════════════════════════════════════════

ADJUSTED GROSS INCOME

6.  Educator expenses                                    {format_currency(0)}
7.  Student loan interest                                {format_currency(0)}
8.  IRA contributions                                    {format_currency(6500)}

9.  ADJUSTED GROSS INCOME (Total Income - Lines 6-8)    {format_currency(income + 1217 - 6500)}

═══════════════════════════════════════════════════════════════════════════

DEDUCTIONS

10. Standard Deduction                                   {format_currency(standard_deduction)}
    OR Itemized Deductions                               {format_currency(0)}

11. TAXABLE INCOME (Line 9 - Line 10)                   {format_currency(taxable_income)}

═══════════════════════════════════════════════════════════════════════════

TAX COMPUTATION

12. Tax from tax tables                                  {format_currency(tax_paid + refund)}
13. Child tax credit                                     {format_currency(0)}
14. Other credits                                        {format_currency(0)}

15. TOTAL TAX (Line 12 - Lines 13-14)                   {format_currency(tax_paid + refund)}

═══════════════════════════════════════════════════════════════════════════

PAYMENTS

16. Federal income tax withheld (W-2)                    {format_currency(tax_paid)}
17. Estimated tax payments                               {format_currency(0)}
18. Earned income credit                                 {format_currency(0)}

19. TOTAL PAYMENTS (Lines 16-18)                        {format_currency(tax_paid)}

═══════════════════════════════════════════════════════════════════════════

REFUND OR AMOUNT OWED

20. Total Tax (Line 15)                                  {format_currency(tax_paid + refund)}
21. Total Payments (Line 19)                             {format_currency(tax_paid)}

"""
        
        if refund > 0:
            content += f"22. REFUND (Line 21 - Line 20)                          {format_currency(refund)}\n\n"
            content += "    ☒ Direct deposit to checking account\n"
            content += "    Routing Number: 121000248\n"
            content += "    Account Number: ****5678\n"
        else:
            content += f"22. AMOUNT YOU OWE (Line 20 - Line 21)                  {format_currency(abs(refund))}\n"
        
        content += f"""
═══════════════════════════════════════════════════════════════════════════

SIGNATURE

Under penalties of perjury, I declare that I have examined this return and
accompanying schedules and statements, and to the best of my knowledge and
belief, they are true, correct, and complete.

Taxpayer's signature: {USER_NAME}                    Date: 04/12/{year + 1}

═══════════════════════════════════════════════════════════════════════════

For IRS Use Only

Return processed: 04/28/{year + 1}
{"Refund issued: 05/10/" + str(year + 1) if refund > 0 else "Payment received: 04/15/" + str(year + 1)}

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_state_tax_return(self, year):
        """Generate California State Tax Return (Form 540)"""
        state_data = STATE_TAX_BRACKETS[year]
        federal_data = FEDERAL_TAX_BRACKETS[year]
        
        income = state_data["income"]
        state_standard_deduction = 5202 if year <= 2022 else 5363 if year <= 2023 else 5552
        taxable_income = income - state_standard_deduction
        tax_paid = state_data["tax_paid"]
        refund = state_data["refund"]
        
        content = f"""FORM 540 - CALIFORNIA RESIDENT INCOME TAX RETURN
Tax Year: {year}

═══════════════════════════════════════════════════════════════════════════

TAXPAYER INFORMATION

Name: {USER_NAME}
Social Security Number: {USER_SSN}
Address: {USER_ADDRESS}
City: {USER_CITY}      State: CA      ZIP: {USER_ZIP}

Filing Status: ☒ Single  ☐ Married/RDP Filing Jointly

═══════════════════════════════════════════════════════════════════════════

CALIFORNIA INCOME

1.  Federal Adjusted Gross Income                        {format_currency(income)}
2.  CA income adjustments                                {format_currency(0)}
3.  CA additions to income                               {format_currency(0)}
4.  CA subtractions from income                          {format_currency(0)}

5.  CA ADJUSTED GROSS INCOME                            {format_currency(income)}

═══════════════════════════════════════════════════════════════════════════

DEDUCTIONS

6.  CA Standard Deduction                                {format_currency(state_standard_deduction)}
    OR CA Itemized Deductions                            {format_currency(0)}

7.  Exemption credits                                    {format_currency(118)}

8.  CA TAXABLE INCOME (Line 5 - Line 6)                 {format_currency(taxable_income)}

═══════════════════════════════════════════════════════════════════════════

TAX COMPUTATION

9.  Tax from tax table                                   {format_currency(tax_paid + refund)}
10. Other state tax credit (540)                         {format_currency(0)}
11. Dependent parent credit                              {format_currency(0)}
12. Renters credit                                       {format_currency(60)}

13. TOTAL TAX (Line 9 - Lines 10-12)                    {format_currency(tax_paid + refund - 60)}

═══════════════════════════════════════════════════════════════════════════

PAYMENTS

14. CA income tax withheld                               {format_currency(tax_paid)}
15. CA estimated tax payments                            {format_currency(0)}
16. Other payments                                       {format_currency(0)}

17. TOTAL PAYMENTS                                       {format_currency(tax_paid)}

═══════════════════════════════════════════════════════════════════════════

REFUND OR AMOUNT OWED

"""
        
        if refund > 0:
            content += f"18. REFUND (Payments - Total Tax)                       {format_currency(refund)}\n\n"
            content += "    Direct deposit information:\n"
            content += "    ☒ Checking  ☐ Savings\n"
            content += "    Routing: 121000248  Account: ****5678\n"
        else:
            content += f"18. AMOUNT YOU OWE                                       {format_currency(abs(refund))}\n"
        
        content += f"""
═══════════════════════════════════════════════════════════════════════════

SIGNATURE AND DECLARATION

I declare under penalty of perjury that I have examined this return,
including accompanying schedules and statements, and to the best of my
knowledge and belief, it is true, correct, and complete.

Your signature: {USER_NAME}                         Date: 04/12/{year + 1}

═══════════════════════════════════════════════════════════════════════════

FRANCHISE TAX BOARD USE ONLY

Processed: 05/02/{year + 1}
{"Refund issued: 05/15/" + str(year + 1) if refund > 0 else "Payment due: 04/15/" + str(year + 1)}

California Franchise Tax Board
Sacramento, CA 95827

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_w2_form(self, year):
        """Generate W-2 Wage and Tax Statement"""
        income = FEDERAL_TAX_BRACKETS[year]["income"]
        federal_tax = FEDERAL_TAX_BRACKETS[year]["tax_paid"]
        state_tax = STATE_TAX_BRACKETS[year]["tax_paid"]
        
        ss_tax = round(income * 0.062, 2)
        medicare_tax = round(income * 0.0145, 2)
        
        content = f"""W-2 WAGE AND TAX STATEMENT
Tax Year: {year}

═══════════════════════════════════════════════════════════════════════════

EMPLOYER INFORMATION

Employer: beingMalicious.com Inc.
EIN: 94-1234567
Address: 450 Market Street, Suite 1200
City, State, ZIP: San Francisco, CA 94111

═══════════════════════════════════════════════════════════════════════════

EMPLOYEE INFORMATION

Employee: {USER_NAME}
SSN: {USER_SSN}
Address: {USER_ADDRESS}
City, State, ZIP: {USER_CITY}, {USER_STATE} {USER_ZIP}

═══════════════════════════════════════════════════════════════════════════

WAGES AND WITHHOLDING

Box 1  - Wages, tips, other compensation              {format_currency(income)}
Box 2  - Federal income tax withheld                  {format_currency(federal_tax)}
Box 3  - Social security wages                        {format_currency(income)}
Box 4  - Social security tax withheld                 {format_currency(ss_tax)}
Box 5  - Medicare wages and tips                      {format_currency(income)}
Box 6  - Medicare tax withheld                        {format_currency(medicare_tax)}

Box 12a - DD: {format_currency(8500)}  (Cost of employer-sponsored health coverage)

Box 15 - State: CA
Box 16 - State wages, tips, etc.                      {format_currency(income)}
Box 17 - State income tax                             {format_currency(state_tax)}
Box 18 - Local wages, tips, etc.                      {format_currency(0)}
Box 19 - Local income tax                             {format_currency(0)}

═══════════════════════════════════════════════════════════════════════════

This is a copy of your W-2 wage statement for tax year {year}.
Please retain for your records and use when filing your tax return.

Issued: January 28, {year + 1}

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_all_tax_documents(self):
        """Generate all tax documents for specified years"""
        created_files = []
        
        print("\n[*] Generating tax documents...")
        
        tax_folder = self.base_path / "Desktop" / "Tax Documents"
        ensure_directory(tax_folder)
        
        for year in TAX_YEARS:
            year_folder = tax_folder / str(year)
            ensure_directory(year_folder)
            
            # Federal return
            federal_content = self.generate_federal_tax_return(year)
            federal_file = year_folder / f"Form_1040_Federal_{year}.pdf"
            create_pdf(federal_file, f"Form 1040 Federal {year}", [("Return", federal_content)])
            created_files.append(federal_file)
            
            # State return
            state_content = self.generate_state_tax_return(year)
            state_file = year_folder / f"Form_540_California_{year}.pdf"
            create_pdf(state_file, f"Form 540 California {year}", [("Return", state_content)])
            created_files.append(state_file)
            
            # W-2
            w2_content = self.generate_w2_form(year)
            w2_file = year_folder / f"W2_Form_{year}.pdf"
            create_pdf(w2_file, f"W-2 {year}", [("W-2", w2_content)])
            created_files.append(w2_file)
            
            print(f"    ✓ Generated tax documents for {year}")
        
        return created_files
