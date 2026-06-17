# PAT_ED_DOC_LEAFLET_ACTIVITY

> This table stores Patient Education Medication Leaflet from Multum given to Patients from Fistnet Patient Education Module

**Description:** Patient Education Medication Leaflet Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `INSTRUCTION_DT_TM` | DATETIME | NOT NULL |  | Date and time when instruction given |
| 3 | `INSTRUCTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl_id of the user who educated patient from prsnl table |
| 4 | `LEAFLET_NAME` | VARCHAR(150) | NOT NULL |  | Stores the name of the medication for instruction is given |
| 5 | `MED_LEAFLET_CKI` | VARCHAR(255) | NOT NULL |  | Stores the CKI value for the Medication Leaflet |
| 6 | `PAT_ED_DOC_ID` | DOUBLE | NOT NULL | FK→ | Foreign key stores the PAT_ED_DOCUMENT row from the parent table |
| 7 | `PAT_ED_DOC_LEAFLET_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Primary Key of the table |
| 8 | `PRINT_IND` | DOUBLE | NOT NULL |  | Indicator to show if the instruction is printed |
| 9 | `SUGGESTED_IND` | DOUBLE | NOT NULL |  | Determines if the leaflet instruction was suggested during selection. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INSTRUCTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PAT_ED_DOC_ID` | [PAT_ED_DOCUMENT](PAT_ED_DOCUMENT.md) | `PAT_ED_DOCUMENT_ID` |

