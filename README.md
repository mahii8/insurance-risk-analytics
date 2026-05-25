# Insurance Risk Analytics

## Project Overview
End-to-end insurance risk analytics and predictive modeling for AlphaCare Insurance Solutions (ACIS). Analysis of 18 months of historical car insurance claim data (Feb 2014 – Aug 2015) to optimize pricing and identify low-risk segments.

## Tasks
| Task | Description | Branch |
|------|-------------|--------|
| Task 1 | EDA on insurance data | task-1 |
| Task 2 | Data Version Control (DVC) | task-2 |
| Task 3 | A/B Hypothesis Testing | task-3 |
| Task 4 | Statistical Modeling & Risk-Based Pricing | task-4 |

## Key Metrics
- **Loss Ratio** = TotalClaims / TotalPremium
- **Margin** = TotalPremium − TotalClaims

## How to Reproduce
1. Clone the repository
2. Create and activate virtual environment:
   python -m venv venv
   source venv/Scripts/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Pull data via DVC:
   dvc pull

## Author
Bamla | 10 Academy x Kifiya | Week 3 | May 2026
