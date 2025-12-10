#!/usr/bin/env python3
"""
Enhanced Document Generator
Creates additional realistic documents for Documents and Downloads folders
"""

import random
from datetime import datetime, timedelta
from pathlib import Path

from config import USER_NAME, USER_EMAIL, COMPANY_NAME, USER_ADDRESS, USER_CITY, USER_STATE, USER_ZIP
from utils.helpers import format_currency, ensure_directory, random_date


class EnhancedDocumentGenerator:
    """Generates additional realistic documents"""
    
    def __init__(self, base_path):
        self.base_path = Path(base_path)
    
    def generate_contract(self):
        """Generate employment contract"""
        
        content = f"""EMPLOYMENT CONTRACT

═══════════════════════════════════════════════════════════════════════════

THIS AGREEMENT is entered into as of January 15, 2020

BETWEEN:

{COMPANY_NAME} Inc.
450 Market Street, Suite 1200
San Francisco, CA 94111
("Employer")

AND:

{USER_NAME}
{USER_ADDRESS}
{USER_CITY}, {USER_STATE} {USER_ZIP}
("Employee")

═══════════════════════════════════════════════════════════════════════════

1. POSITION AND DUTIES

The Employee is employed as Senior Software Engineer and will perform duties
including but not limited to:

• Design and develop software applications
• Collaborate with cross-functional teams
• Participate in code reviews and technical discussions
• Mentor junior team members
• Contribute to architectural decisions

═══════════════════════════════════════════════════════════════════════════

2. COMPENSATION

Base Salary: $115,000 per year, payable bi-weekly
Performance Bonus: Up to 15% of base salary annually
Stock Options: 10,000 shares vesting over 4 years

═══════════════════════════════════════════════════════════════════════════

3. BENEFITS

• Health insurance (medical, dental, vision)
• 401(k) retirement plan with 4% company match
• 15 days paid vacation per year
• 10 days sick leave per year
• Professional development budget: $2,000/year

═══════════════════════════════════════════════════════════════════════════

4. WORKING HOURS

Standard working hours: 40 hours per week
Flexible schedule with core hours 10 AM - 4 PM
Remote work: Up to 3 days per week

═══════════════════════════════════════════════════════════════════════════

5. CONFIDENTIALITY

Employee agrees to maintain confidentiality of all proprietary information
and trade secrets of the Employer during and after employment.

═══════════════════════════════════════════════════════════════════════════

6. TERMINATION

Either party may terminate this agreement with 30 days written notice.
Severance: 2 weeks pay per year of service (minimum 4 weeks).

═══════════════════════════════════════════════════════════════════════════

SIGNATURES:

Employee: {USER_NAME}
Signature: ________________________    Date: January 15, 2020

Employer: Sarah Johnson, VP Human Resources
Signature: ________________________    Date: January 15, 2020

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_performance_review(self, year):
        """Generate performance review"""
        
        content = f"""ANNUAL PERFORMANCE REVIEW
{year}

═══════════════════════════════════════════════════════════════════════════

EMPLOYEE INFORMATION

Name: {USER_NAME}
Position: Senior Software Engineer
Department: Engineering
Review Period: January 1, {year} - December 31, {year}
Review Date: January 15, {year + 1}
Manager: Mike Chen, Engineering Manager

═══════════════════════════════════════════════════════════════════════════

PERFORMANCE RATINGS
(Scale: 1=Needs Improvement, 2=Meets Expectations, 3=Exceeds Expectations,
        4=Outstanding)

Technical Skills                              4
Problem Solving                               4
Communication                                 3
Teamwork & Collaboration                      4
Leadership & Mentorship                       3
Project Management                            3
Innovation                                    4

OVERALL RATING: 3.6 - EXCEEDS EXPECTATIONS

═══════════════════════════════════════════════════════════════════════════

KEY ACCOMPLISHMENTS

1. Successfully led the microservices migration project, completing ahead
   of schedule and under budget.

2. Mentored 3 junior engineers, contributing to their professional growth
   and team capabilities.

3. Implemented performance optimizations that reduced API response time
   by 40%, significantly improving user experience.

4. Contributed to open-source projects that enhanced company's technical
   reputation in the developer community.

5. Designed and documented system architecture for new payment processing
   service, now used as reference by entire team.

═══════════════════════════════════════════════════════════════════════════

AREAS FOR DEVELOPMENT

1. Continue developing project management skills through formal training

2. Increase involvement in cross-departmental initiatives

3. Enhance technical writing and documentation practices

═══════════════════════════════════════════════════════════════════════════

GOALS FOR {year + 1}

1. Lead 2 major technical initiatives from conception to production

2. Present at 2 technical conferences or meetups

3. Complete AWS Solutions Architect certification

4. Improve system observability and monitoring capabilities

5. Contribute to technical hiring and interview process

═══════════════════════════════════════════════════════════════════════════

COMPENSATION ADJUSTMENT

Current Base Salary: ${95000 + (year - 2022) * 5000}
New Base Salary: ${100000 + (year - 2022) * 5000}
Increase: 5.3%
Effective Date: January 1, {year + 1}

Performance Bonus: {format_currency(random.randint(8000, 15000))}

═══════════════════════════════════════════════════════════════════════════

EMPLOYEE COMMENTS

I appreciate the feedback and recognition. I'm excited about the goals we've
set for next year and look forward to continuing to contribute to the team's
success. I plan to focus especially on expanding my leadership capabilities
and sharing knowledge more effectively across the organization.

═══════════════════════════════════════════════════════════════════════════

SIGNATURES

Employee: {USER_NAME}
Signature: ________________________    Date: _______________

Manager: Mike Chen
Signature: ________________________    Date: _______________

HR Representative: Sarah Johnson
Signature: ________________________    Date: _______________

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_training_certificate(self):
        """Generate training certificate"""
        
        courses = [
            "AWS Solutions Architect Professional",
            "Kubernetes Administration",
            "Advanced Python Programming",
            "Microservices Architecture Patterns",
            "Security Best Practices for Developers"
        ]
        
        course = random.choice(courses)
        completion_date = datetime.now() - timedelta(days=random.randint(30, 365))
        
        content = f"""CERTIFICATE OF COMPLETION

═══════════════════════════════════════════════════════════════════════════

This is to certify that

{USER_NAME}

has successfully completed the course

{course}

Date of Completion: {completion_date.strftime('%B %d, %Y')}
Duration: {random.choice([8, 16, 24, 40])} hours
Provider: TechAcademy Online Learning

═══════════════════════════════════════════════════════════════════════════

COURSE OBJECTIVES MET:

✓ Understand core concepts and principles
✓ Apply knowledge to real-world scenarios
✓ Demonstrate proficiency through hands-on projects
✓ Pass final assessment with score of {random.randint(85, 98)}%

═══════════════════════════════════════════════════════════════════════════

Certificate ID: CERT-{random.randint(100000, 999999)}
Verify at: www.techacademy.com/verify

Instructor: Dr. Robert Anderson
Academic Director

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_insurance_policy(self):
        """Generate insurance policy document"""
        
        content = f"""INSURANCE POLICY DOCUMENT
Policy Number: POL-{random.randint(100000000, 999999999)}

═══════════════════════════════════════════════════════════════════════════

POLICYHOLDER INFORMATION

Name: {USER_NAME}
Address: {USER_ADDRESS}
         {USER_CITY}, {USER_STATE} {USER_ZIP}
Email: {USER_EMAIL}

═══════════════════════════════════════════════════════════════════════════

POLICY DETAILS

Policy Type: Comprehensive Health Insurance
Insurance Company: Blue Cross Blue Shield
Plan Name: PPO Gold Plus
Effective Date: January 1, 2024
Expiration Date: December 31, 2024
Premium: $450/month

═══════════════════════════════════════════════════════════════════════════

COVERAGE SUMMARY

Annual Deductible:
  Individual: $1,500
  Family: $3,000

Out-of-Pocket Maximum:
  Individual: $6,000
  Family: $12,000

Coinsurance: 80/20 (Plan pays 80% after deductible)

═══════════════════════════════════════════════════════════════════════════

COVERED SERVICES

Office Visits:
  Primary Care: $25 copay
  Specialist: $50 copay
  
Emergency Care:
  Emergency Room: $500 copay (waived if admitted)
  Urgent Care: $75 copay

Hospital Services:
  Inpatient: 20% coinsurance after deductible
  Outpatient Surgery: 20% coinsurance after deductible

Preventive Care: Covered 100% (no copay or deductible)

Prescription Drugs:
  Tier 1 (Generic): $10 copay
  Tier 2 (Preferred Brand): $40 copay
  Tier 3 (Non-Preferred Brand): $70 copay

Mental Health: Same as office visit copays

═══════════════════════════════════════════════════════════════════════════

PROVIDER NETWORK

In-Network: Full coverage as outlined above
Out-of-Network: 60/40 coinsurance, higher deductible applies

Provider Directory: www.bcbs.com/find-a-doctor
Customer Service: 1-800-123-4567 (24/7)

═══════════════════════════════════════════════════════════════════════════

EXCLUSIONS

This policy does not cover:
• Cosmetic procedures
• Experimental treatments
• Services not medically necessary
• Services provided by non-licensed practitioners

═══════════════════════════════════════════════════════════════════════════

IMPORTANT NOTICES

• ID cards will arrive within 10 business days
• For emergencies, call 911 or go to nearest ER
• Pre-authorization required for some services
• Claims must be filed within 12 months

═══════════════════════════════════════════════════════════════════════════

For questions or to file a claim:
Phone: 1-800-123-4567
Website: www.bcbs.com
Email: customerservice@bcbs.com

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_all_enhanced_documents(self):
        """Generate all enhanced documents"""
        created_files = []
        
        print("\n[*] Generating enhanced documents...")
        
        documents_folder = self.base_path / "Documents"
        ensure_directory(documents_folder)
        
        # Contracts folder
        contracts_folder = documents_folder / "Contracts"
        ensure_directory(contracts_folder)
        
        contract = self.generate_contract()
        contract_file = contracts_folder / "Employment_Contract_2020.txt"
        contract_file.write_text(contract, encoding='utf-8')
        created_files.append(contract_file)
        
        # Performance reviews
        perf_folder = documents_folder / "Work" / "Performance_Reviews"
        ensure_directory(perf_folder)
        
        for year in [2022, 2023, 2024]:
            review = self.generate_performance_review(year)
            review_file = perf_folder / f"Performance_Review_{year}.txt"
            review_file.write_text(review, encoding='utf-8')
            created_files.append(review_file)
        
        # Training certificates
        training_folder = documents_folder / "Work" / "Training_Materials"
        ensure_directory(training_folder)
        
        for i in range(3):
            cert = self.generate_training_certificate()
            cert_file = training_folder / f"Training_Certificate_{i+1}.txt"
            cert_file.write_text(cert, encoding='utf-8')
            created_files.append(cert_file)
        
        # Insurance
        insurance_folder = documents_folder / "Personal" / "Insurance"
        ensure_directory(insurance_folder)
        
        insurance = self.generate_insurance_policy()
        insurance_file = insurance_folder / "Health_Insurance_Policy_2024.txt"
        insurance_file.write_text(insurance, encoding='utf-8')
        created_files.append(insurance_file)
        
        print(f"    ✓ Generated {len(created_files)} enhanced documents")
        
        return created_files
