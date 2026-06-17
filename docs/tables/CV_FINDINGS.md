# CV_FINDINGS

> This table holds the details of the clinical diagnosis findings for the staged documents.

**Description:** Cardiovascular Diagnosis findings  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_SYSTEM_TXT` | VARCHAR(255) |  |  | The standard code system that defines the meaning of the symbol in the code. |
| 2 | `CODE_TXT` | VARCHAR(80) |  |  | The standard code value which is a symbol in syntax defined by the system. |
| 3 | `CV_FINDINGS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `CV_STG_METADATA_ID` | DOUBLE |  | FK→ | The staging metadata identifier. |
| 5 | `DISPLAY_TXT` | VARCHAR(255) |  |  | The display text of the standard code that represents the meaning of the code in the system. |
| 6 | `EVENT_ID` | DOUBLE |  |  | Event Identifier for a parent row from clinical event which the finding is associated too. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_STG_METADATA_ID` | [CV_STG_METADATA](CV_STG_METADATA.md) | `CV_STG_METADATA_ID` |

