# HF_D_ANTIMICROBIAL

> This is the HealthFacts dimension table that contains standard values for antimicrobials

**Description:** HF_D_Antimicrobial  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOGRAM_CLASS` | VARCHAR(30) |  |  | A grouping of antimicrobials used by the Antibiogram solution |
| 2 | `ANTIBIOGRAM_IND` | DOUBLE |  |  | Indicates if this antimicrobial is used as a part of the Antibiogram solution |
| 3 | `ANTIMICROBIAL_DCODE` | VARCHAR(6) |  |  | The Multum drug classification code used to associate this antimicrobial to a drug classification |
| 4 | `ANTIMICROBIAL_DESC` | VARCHAR(50) |  |  | The textual description of an antimicrobial |
| 5 | `ANTIMICROBIAL_ID` | DOUBLE |  |  | A unique non-intelligent identifier for the table |
| 6 | `ANTIMICROBIAL_MNEMONIC` | VARCHAR(10) |  |  | A standard (NCLS) abbreviation for an antimicrobial |
| 7 | `DRUG_CLASSIFICATION` | VARCHAR(45) |  |  | The Multum drug classification for this antimicrobial |
| 8 | `LOINC_CD` | VARCHAR(10) |  |  | The LOINC Code ( Character field - not a Millennium code value ) |
| 9 | `LOINC_CODE` | VARCHAR(10) |  |  | ** OBSOLETE - see/use column LOINC_CD |
| 10 | `LOINC_LONG` | VARCHAR(255) |  |  | The standard RELMA long description for the LOINC code. |
| 11 | `LOINC_SHORT` | VARCHAR(60) |  |  | The standard RELMA short description for the LOINC code. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |
| 15 | `URINE_ONLY_IND` | VARCHAR(1) |  |  | Indicates if this antimicrobial should only be considered in the Antibiogram solution if the isolate source is Urine |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

