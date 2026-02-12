# Documentation Conversion Plan

This file tracks the progress of converting the "Full Repatriation Guide" PDF into Mintlify documentation.

## Phase 1: Setup
- [x] Split PDF into 10-page chunks (`pdf_chunks/`)
- [x] Initialize `docs.json` structure (if needed)

## Phase 2: Content Migration
We will process the PDF in chunks. For each chunk, we will:
1.  Read the chunk.
2.  Extract content and identify sections.
3.  Create MDX files in `essentials/` (or a more specific subdirectory).
4.  Update `docs.json` to include the new pages.

### Progress Tracker

- [x] **Chunk 1 (Pages 1-10)**
    - Status: Completed
    - Content covered: Country Info, Repat Armenia, Planning, Arrival, First Steps, Cost of Living, Moving Belongings, Financials (Intro).
    - Files created: `country-info.mdx`, `repat-armenia.mdx`, `planning.mdx`, `arrival.mdx`, `first-steps.mdx`, `cost-of-living.mdx`, `moving-belongings.mdx`, `financials.mdx`.
    - `docs.json` updated: [x]

- [x] **Chunk 2 (Pages 11-20)**
    - Status: Completed
    - Content covered: Financials (Banks, Loans, Savings), Marriage & Divorce, Employment (Rights, Permits, Freelancing).
    - Files created: Updated `financials.mdx`, created `marriage-divorce.mdx`, `employment.mdx`.
    - `docs.json` updated: [x]

- [x] **Chunk 3 (Pages 21-30)**
    - Status: Completed
    - Content covered: Legal Status (Residency, Citizenship, Military), Embassies, Accommodations (Renting, Buying), Getting Around.
    - Files created: `legal-status.mdx`, `accommodations.mdx`, `getting-around.mdx`.
    - `docs.json` updated: [x]

- [x] **Chunk 4 (Pages 31-40)**
    - Status: Completed
    - Content covered: Purchasing a Car, Medical (System, Insurance, Pregnancy), Education (Schools, Universities, TUMO).
    - Files created: `medical.mdx`, `education.mdx`, updated `getting-around.mdx` (car purchase).
    - `docs.json` updated: [x]

- [x] **Chunk 5 (Pages 41-50)**
    - Status: Completed
    - Content covered: International Schools, Special Needs Education, Sports, Military Service (Details), Day-to-Day Life, Entrepreneurship, Taxes.
    - Files created: `entrepreneurship.mdx`, `taxes.mdx`, updated `education.mdx`, `medical.mdx`, `legal-status.mdx`.
    - `docs.json` updated: [x]

- [x] **Chunk 6 (Pages 51-60)**
    - Status: Completed
    - Content covered: Tax Details (Filing, Types), Daily Life (Food, Safety, Language), Useful Apps, Shopping, Leisure, Retirement.
    - Files created: `daily-life.mdx`, updated `taxes.mdx`.
    - `docs.json` updated: [x]

- [x] **Chunk 7 (Pages 61-70)**
    - Status: Completed
    - Content covered: Retirement (Details, Homes), Emergency Contacts, Appendices (Institutions, Holidays, Polyclinics).
    - Files created: `retirement.mdx`, `emergency-contacts.mdx`.
    - `docs.json` updated: [x]

- [ ] **Chunk 8 (Pages 71-73)**
    - Status: Pending
    - Content covered: (To be filled)
    - Files created:
    - `docs.json` updated: [ ]

## Phase 3: Review and Polish
- [ ] Verify all links and navigation
- [ ] Check formatting and accessibility
- [ ] Clean up temporary files (`pdf_chunks/`, `split_pdf.py`)
