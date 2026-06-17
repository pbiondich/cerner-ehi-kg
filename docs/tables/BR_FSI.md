# BR_FSI

> FSI Supplier Information

**Description:** BEDROCK FSI  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ADT_IND` | DOUBLE |  |  | Define as 1 for ADT indicator |
| 4 | `ALLERGY_IND` | DOUBLE |  |  | Define as 1 for allergy indicator |
| 5 | `CHARGE_IND` | DOUBLE |  |  | Define as 1 for charge indicator |
| 6 | `CLAIMS_IND` | DOUBLE |  |  | Define as 1 for claims indicator |
| 7 | `DICTATION_IND` | DOUBLE |  |  | Define as 1 for dictation indicator |
| 8 | `DOCUMENT_IND` | DOUBLE |  |  | Define as 1 for document indicator |
| 9 | `FSI_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 10 | `FSI_SUPPLIER_NAME` | VARCHAR(100) |  |  | Supplier name |
| 11 | `FSI_SYSTEM_NAME` | VARCHAR(100) |  |  | System name |
| 12 | `IMMUN_IND` | DOUBLE |  |  | Define as 1 for immunization indicator |
| 13 | `MISC_TYPE_DESC` | VARCHAR(100) |  |  | Define as 1 for misc type description |
| 14 | `MISC_TYPE_IND` | DOUBLE |  |  | Define as 1 for misc type indicator |
| 15 | `ORDER_IND` | DOUBLE |  |  | Define as 1 for order indicator |
| 16 | `PHYS_MFN_IND` | DOUBLE |  |  | Define as 1 for phys mfn indicator |
| 17 | `PROBLEM_IND` | DOUBLE |  |  | Define as 1 for problem indicator |
| 18 | `RESULT_IND` | DOUBLE |  |  | Define as 1 for result indicator |
| 19 | `RLI_IND` | DOUBLE |  |  | Define as 1 for RLI indicator |
| 20 | `SCHEDULE_IND` | DOUBLE |  |  | Define as 1 for schedule indicator |
| 21 | `SUPPLY_IND` | DOUBLE |  |  | Define as 1 for supply indicator |
| 22 | `TRANSCRIPTION_IND` | DOUBLE |  |  | Define as 1 for transcription indicator |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

