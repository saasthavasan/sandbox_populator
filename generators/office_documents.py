#!/usr/bin/env python3
"""
Office Documents Generator
Creates realistic office documents (reports, presentations, spreadsheets)
"""

import random
from datetime import datetime, timedelta
from pathlib import Path

from config import USER_NAME, USER_EMAIL, COMPANY_NAME, CURRENT_DATE
from utils.helpers import (
    format_currency,
    ensure_directory,
    random_date,
    create_pdf,
    create_workbook,
    create_presentation,
)


class OfficeDocumentGenerator:
    """Generates realistic office documents"""
    
    def __init__(self, base_path):
        self.base_path = Path(base_path)
    
    def generate_quarterly_report(self, quarter, year):
        """Generate quarterly business report"""
        q_months = {
            1: ("January", "February", "March"),
            2: ("April", "May", "June"),
            3: ("July", "August", "September"),
            4: ("October", "November", "December")
        }
        
        months = q_months[quarter]
        
        content = f"""QUARTERLY BUSINESS REPORT
Q{quarter} {year}

═══════════════════════════════════════════════════════════════════════════

COMPANY: {COMPANY_NAME}
PREPARED BY: {USER_NAME}
DATE: {months[2]} 30, {year}
DEPARTMENT: Engineering & Technology

═══════════════════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY

This report summarizes the key achievements, challenges, and metrics for the
Engineering department during Q{quarter} {year} ({months[0]}-{months[2]}).

Key Highlights:
• Successfully deployed 3 major feature releases
• Improved system uptime to 99.97%
• Reduced average response time by 23%
• Onboarded 2 new senior engineers

═══════════════════════════════════════════════════════════════════════════

PERFORMANCE METRICS

Development Velocity:
  - Story points completed: {random.randint(180, 250)}
  - Sprint velocity average: {random.randint(35, 50)} points/sprint
  - Code commits: {random.randint(450, 750)}
  - Pull requests merged: {random.randint(120, 200)}

System Performance:
  - Uptime: 99.{random.randint(94, 99)}%
  - Average response time: {random.randint(85, 150)}ms
  - Error rate: 0.{random.randint(1, 5):02d}%
  - Peak concurrent users: {random.randint(8000, 15000):,}

Quality Metrics:
  - Test coverage: {random.randint(82, 94)}%
  - Bugs resolved: {random.randint(45, 85)}
  - Production incidents: {random.randint(2, 6)}
  - Customer-reported issues: {random.randint(8, 18)}

═══════════════════════════════════════════════════════════════════════════

MAJOR ACCOMPLISHMENTS

1. MICROSERVICES MIGRATION
   Successfully migrated payment processing service to new microservices
   architecture, resulting in improved scalability and maintainability.
   
2. SECURITY ENHANCEMENTS
   Implemented multi-factor authentication and enhanced encryption for
   sensitive data storage, passing security audit with zero critical findings.
   
3. API PERFORMANCE OPTIMIZATION
   Reduced API latency by 35% through query optimization and caching
   strategies, improving overall user experience.

4. DATABASE UPGRADE
   Completed PostgreSQL upgrade to version 15 with zero downtime,
   leveraging blue-green deployment strategy.

═══════════════════════════════════════════════════════════════════════════

CHALLENGES & LESSONS LEARNED

Challenges:
• Integration issues with third-party payment gateway caused delays
• Unexpected spike in traffic required emergency scaling
• Two key team members left for other opportunities

Lessons Learned:
• Need better integration testing environment
• Auto-scaling policies need refinement
• Knowledge transfer and documentation are critical

═══════════════════════════════════════════════════════════════════════════

UPCOMING PRIORITIES FOR Q{quarter + 1 if quarter < 4 else 1} {year if quarter < 4 else year + 1}

1. Launch mobile app version 2.0
2. Implement real-time analytics dashboard
3. Complete migration to Kubernetes
4. Enhance monitoring and alerting systems
5. Hire 3 additional engineers

═══════════════════════════════════════════════════════════════════════════

BUDGET SUMMARY

                        Budgeted        Actual       Variance
Personnel              {format_currency(180000)}    {format_currency(175000)}     {format_currency(5000)}
Infrastructure         {format_currency(45000)}     {format_currency(48500)}    ({format_currency(3500)})
Software/Tools         {format_currency(25000)}     {format_currency(24200)}      {format_currency(800)}
Training               {format_currency(10000)}     {format_currency(8500)}      {format_currency(1500)}
                       ──────────────────────────────────────────────
TOTAL                  {format_currency(260000)}    {format_currency(256200)}     {format_currency(3800)}

═══════════════════════════════════════════════════════════════════════════

CONCLUSION

Q{quarter} was a productive quarter with significant progress on key initiatives.
The team demonstrated resilience and adaptability in addressing challenges while
maintaining high quality standards. Looking ahead, we are well-positioned to
execute on our roadmap for the next quarter.

Prepared by: {USER_NAME}
Title: Senior Engineering Manager
Date: {months[2]} 30, {year}

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_project_proposal(self):
        """Generate project proposal document"""
        
        project_names = [
            "Customer Portal Redesign",
            "Mobile App Enhancement",
            "Data Analytics Platform",
            "Payment System Upgrade",
            "Real-time Notification Service"
        ]
        
        project_name = random.choice(project_names)
        
        content = f"""PROJECT PROPOSAL

═══════════════════════════════════════════════════════════════════════════

PROJECT TITLE: {project_name}

Submitted by: {USER_NAME}
Department: Engineering
Date: {CURRENT_DATE.strftime('%B %d, %Y')}
Version: 1.0

═══════════════════════════════════════════════════════════════════════════

1. PROJECT OVERVIEW

This proposal outlines the plan to develop and implement {project_name}.
The project aims to improve user experience, increase system efficiency,
and provide better insights into business operations.

═══════════════════════════════════════════════════════════════════════════

2. BUSINESS JUSTIFICATION

Current Challenges:
• Outdated user interface affecting user satisfaction
• Performance bottlenecks during peak usage
• Limited analytics capabilities
• Increasing maintenance costs

Expected Benefits:
• 40% improvement in user engagement
• 50% reduction in page load times
• Enhanced data-driven decision making
• Lower operational costs

ROI: Expected payback period of 18 months with projected annual savings
     of {format_currency(150000)}

═══════════════════════════════════════════════════════════════════════════

3. PROJECT SCOPE

In Scope:
✓ Complete UI/UX redesign
✓ Backend API modernization
✓ Database optimization
✓ Comprehensive testing
✓ User documentation
✓ Staff training

Out of Scope:
✗ Mobile application (separate project)
✗ Third-party integrations (Phase 2)
✗ Marketing campaigns

═══════════════════════════════════════════════════════════════════════════

4. PROJECT TIMELINE

Phase 1: Planning & Design         Weeks 1-3
  - Requirements gathering
  - Architecture design
  - UI/UX mockups

Phase 2: Development               Weeks 4-10
  - Frontend development
  - Backend API development
  - Database implementation

Phase 3: Testing & QA              Weeks 11-13
  - Unit testing
  - Integration testing
  - User acceptance testing

Phase 4: Deployment                Week 14
  - Production deployment
  - Monitoring setup
  - Documentation

Total Duration: 14 weeks

═══════════════════════════════════════════════════════════════════════════

5. RESOURCE REQUIREMENTS

Personnel:
  - Project Manager: 1 (full-time)
  - Senior Engineers: 2 (full-time)
  - Frontend Developers: 2 (full-time)
  - QA Engineers: 1 (full-time)
  - UI/UX Designer: 1 (part-time)

Infrastructure:
  - Development environments
  - Staging environment
  - Testing tools and frameworks

═══════════════════════════════════════════════════════════════════════════

6. BUDGET ESTIMATE

Personnel Costs                    {format_currency(280000)}
Infrastructure & Tools             {format_currency(45000)}
Software Licenses                  {format_currency(15000)}
Training & Documentation           {format_currency(10000)}
Contingency (10%)                  {format_currency(35000)}
                                   ─────────────
TOTAL PROJECT COST                 {format_currency(385000)}

═══════════════════════════════════════════════════════════════════════════

7. RISK ANALYSIS

Risk                           Probability    Impact      Mitigation
──────────────────────────────────────────────────────────────────────
Scope creep                    Medium         High        Clear requirements & change control
Technical challenges           Medium         Medium      Proof of concept early
Resource availability          Low            High        Secure commitments upfront
Third-party dependencies       Medium         Medium      Identify alternatives
Timeline delays                Medium         Medium      Buffer time in schedule

═══════════════════════════════════════════════════════════════════════════

8. SUCCESS CRITERIA

The project will be considered successful when:
✓ All functional requirements are met
✓ Performance targets are achieved (sub-200ms response time)
✓ User satisfaction score > 85%
✓ Zero critical bugs in production
✓ Deployment completed on schedule
✓ Budget variance < 10%

═══════════════════════════════════════════════════════════════════════════

9. RECOMMENDATION

Based on the analysis above, I recommend approval of this project. The
expected benefits significantly outweigh the costs, and the project aligns
well with our strategic objectives for digital transformation.

═══════════════════════════════════════════════════════════════════════════

APPROVALS

Prepared by:
  Name: {USER_NAME}
  Title: Senior Engineering Manager
  Signature: ________________________    Date: _______________

Approved by:
  Name: ___________________________
  Title: VP of Engineering
  Signature: ________________________    Date: _______________

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_meeting_presentation(self):
        """Generate presentation outline"""
        
        topics = [
            "Q4 Engineering Roadmap",
            "System Architecture Review",
            "New Product Launch Strategy",
            "Team Performance Metrics",
            "Technology Stack Modernization"
        ]
        
        topic = random.choice(topics)
        
        content = f"""PRESENTATION OUTLINE
{topic}

═══════════════════════════════════════════════════════════════════════════

Presenter: {USER_NAME}
Date: {CURRENT_DATE.strftime('%B %d, %Y')}
Audience: Executive Team & Stakeholders
Duration: 45 minutes

═══════════════════════════════════════════════════════════════════════════

SLIDE 1: TITLE SLIDE
  - {topic}
  - {USER_NAME}, {COMPANY_NAME}
  - {CURRENT_DATE.strftime('%B %Y')}

═══════════════════════════════════════════════════════════════════════════

SLIDE 2: AGENDA
  1. Current State Overview
  2. Key Challenges
  3. Proposed Solutions
  4. Implementation Timeline
  5. Expected Outcomes
  6. Q&A

═══════════════════════════════════════════════════════════════════════════

SLIDE 3: CURRENT STATE OVERVIEW
  • System Architecture Diagram
  • Current Performance Metrics
    - Uptime: 99.9%
    - Response Time: 120ms avg
    - Daily Active Users: 50,000+
  • Team Structure (15 engineers)

═══════════════════════════════════════════════════════════════════════════

SLIDE 4: KEY CHALLENGES
  ✗ Legacy codebase maintenance
  ✗ Scaling limitations
  ✗ Technical debt accumulation
  ✗ Slow deployment cycles
  ✗ Limited observability

═══════════════════════════════════════════════════════════════════════════

SLIDE 5: PROPOSED SOLUTIONS
  ✓ Microservices architecture migration
  ✓ Containerization with Kubernetes
  ✓ CI/CD pipeline improvements
  ✓ Enhanced monitoring & logging
  ✓ Code quality initiatives

═══════════════════════════════════════════════════════════════════════════

SLIDE 6: IMPLEMENTATION TIMELINE
  
  Month 1-2: Planning & Design
  • Architecture design
  • Team training
  • Tool selection

  Month 3-5: Development
  • Service migration
  • Infrastructure setup
  • Testing framework

  Month 6: Deployment & Optimization
  • Production rollout
  • Performance tuning
  • Documentation

═══════════════════════════════════════════════════════════════════════════

SLIDE 7: EXPECTED OUTCOMES
  
  Technical Benefits:
  • 50% faster deployment cycles
  • 99.99% uptime target
  • 40% reduction in response time
  • Better fault isolation

  Business Benefits:
  • Faster time to market
  • Improved customer satisfaction
  • Reduced operational costs
  • Increased team productivity

═══════════════════════════════════════════════════════════════════════════

SLIDE 8: BUDGET & RESOURCES
  
  Total Investment: {format_currency(450000)}
  
  Breakdown:
  • Infrastructure: {format_currency(200000)}
  • Tools & Licenses: {format_currency(80000)}
  • Training: {format_currency(40000)}
  • Consulting: {format_currency(100000)}
  • Contingency: {format_currency(30000)}

═══════════════════════════════════════════════════════════════════════════

SLIDE 9: RISK MITIGATION
  
  • Phased rollout approach
  • Comprehensive testing at each stage
  • Rollback procedures in place
  • Regular stakeholder updates
  • External expert consultation

═══════════════════════════════════════════════════════════════════════════

SLIDE 10: NEXT STEPS
  
  Immediate (This Month):
  ☐ Get executive approval
  ☐ Finalize budget allocation
  ☐ Form project team

  Short-term (Next 3 Months):
  ☐ Complete architecture design
  ☐ Begin infrastructure setup
  ☐ Start team training

═══════════════════════════════════════════════════════════════════════════

SLIDE 11: Q&A
  
  Questions?
  
  Contact Information:
  {USER_NAME}
  {USER_EMAIL}

═══════════════════════════════════════════════════════════════════════════

NOTES FOR PRESENTER:
• Emphasize business value over technical details
• Have backup slides ready for deep dives
• Prepare for questions about timeline and budget
• Bring up successful case studies from other companies
• Be ready to discuss alternatives if needed

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_spreadsheet_data(self):
        """Generate spreadsheet-like data"""
        
        content = f"""BUDGET TRACKING SPREADSHEET
Engineering Department - {CURRENT_DATE.year}

═══════════════════════════════════════════════════════════════════════════

Category             Jan      Feb      Mar      Q1 Total   Budget    Variance
──────────────────────────────────────────────────────────────────────────────
Salaries           $85,000  $85,000  $87,000   $257,000  $255,000   ($2,000)
Cloud Services     $12,500  $13,200  $12,800    $38,500   $40,000    $1,500
Software Licenses   $5,400   $5,400   $5,600    $16,400   $18,000    $1,600
Office Supplies       $450     $380     $520     $1,350    $1,500      $150
Training            $2,000   $1,500   $3,000     $6,500    $6,000     ($500)
Travel & Meals      $1,800   $2,100     $950     $4,850    $5,000      $150
Equipment           $3,200       $0   $5,600     $8,800   $10,000    $1,200
Contractors         $8,500   $7,200   $9,100    $24,800   $25,000      $200
──────────────────────────────────────────────────────────────────────────────
TOTAL            $118,850 $114,780 $124,570   $358,200  $360,500    $2,300

═══════════════════════════════════════════════════════════════════════════

NOTES:
• Salary increase in March due to annual raises
• Cloud costs higher in Feb due to increased traffic
• Training exceeded budget due to conference attendance
• Equipment purchased for new hires in Q1
• Overall Q1 came in under budget by $2,300

PREPARED BY: {USER_NAME}
DATE: {CURRENT_DATE.strftime('%B %d, %Y')}

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_all_office_documents(self):
        """Generate all office documents"""
        created_files = []
        
        print("\n[*] Generating office documents...")
        
        office_folder = self.base_path / "Desktop" / "Office"
        ensure_directory(office_folder)
        
        # Generate quarterly reports as PDFs
        reports_folder = office_folder / "Reports"
        ensure_directory(reports_folder)
        
        for year in [2024, 2025]:
            for quarter in range(1, 5 if year == 2024 else 1):
                report = self.generate_quarterly_report(quarter, year)
                pdf_path = reports_folder / f"Q{quarter}_{year}_Report.pdf"
                create_pdf(pdf_path, f"Q{quarter} {year} Business Report", [("Content", report)])
                created_files.append(pdf_path)
        
        print(f"    ✓ Generated quarterly reports (PDF)")
        
        # Generate presentations with python-pptx
        presentations_folder = office_folder / "Presentations"
        ensure_directory(presentations_folder)
        
        base_slides = []
        for i in range(3):
            pres = self.generate_meeting_presentation()
            base_slides.append({"title": f"Presentation {i+1}", "bullets": pres.splitlines()[:10]})
        deck_path = presentations_folder / "Quarterly_Roadmap.pptx"
        create_presentation(deck_path, base_slides)
        created_files.append(deck_path)

        ad_hoc_topics = ["Quarterly Townhall", "Incident Postmortem", "Recruiting Update", "Product Strategy"]
        for topic in ad_hoc_topics:
            slides = [
                {"title": topic, "bullets": ["Overview", "Highlights", "Challenges", "Next Steps", "Q&A"]},
                {"title": "Highlights", "bullets": ["Key wins", "Metrics", "Customer feedback"]},
                {"title": "Risks", "bullets": ["Staffing", "Timeline", "Dependencies"]},
            ]
            deck_file = presentations_folder / f"{topic.replace(' ', '_')}.pptx"
            create_presentation(deck_file, slides)
            created_files.append(deck_file)
        
        print(f"    ✓ Generated presentations (PPTX)")
        
        # Generate spreadsheets using openpyxl
        spreadsheets_folder = office_folder / "Spreadsheets"
        ensure_directory(spreadsheets_folder)
        
        for i in range(2):
            budget_file = spreadsheets_folder / f"Budget_Tracking_{i+1}.xlsx"
            create_workbook(
                budget_file,
                [
                    ("Budget", [
                        ["Category", "Jan", "Feb", "Mar", "Q1 Total", "Budget", "Variance"],
                        ["Salaries", "85000", "85000", "87000", "257000", "255000", "-2000"],
                        ["Cloud Services", "12500", "13200", "12800", "38500", "40000", "1500"],
                        ["Software Licenses", "5400", "5400", "5600", "16400", "18000", "1600"],
                        ["Office Supplies", "450", "380", "520", "1350", "1500", "150"],
                        ["Training", "2000", "1500", "3000", "6500", "6000", "-500"],
                    ])
                ],
            )
            created_files.append(budget_file)
        
        print(f"    ✓ Generated spreadsheets (XLSX)")
        
        # Generate project proposals as PDFs
        projects_folder = office_folder / "Projects"
        ensure_directory(projects_folder)
        
        for i in range(2):
            proposal = self.generate_project_proposal()
            pdf_path = projects_folder / f"Project_Proposal_{i+1}.pdf"
            create_pdf(pdf_path, "Project Proposal", [("Proposal", proposal)])
            created_files.append(pdf_path)
        
        print(f"    ✓ Generated project proposals (PDF)")
        
        return created_files
