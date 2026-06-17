# MLTM_LABEL

> This table contains the text for warnings that might be placed on a prescription bottle as information for the patient.

**Description:** Contains the text for warnings that might be placed on a prescription bottle.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LABEL` | VARCHAR(50) |  |  | This field contains an abbreviated text description for patient advice associated with a drug. |
| 2 | `LABEL_FULL` | VARCHAR(150) |  |  | This field contains a text description for patient advice associated with a drug. |
| 3 | `LABEL_FULL_SPANISH` | VARCHAR(200) |  |  | This field contains a Spanish text description for patient advice associated with a drug. |
| 4 | `LABEL_ID` | DOUBLE | NOT NULL |  | This field contains an identifier for warning text that may be used to provide patient advice about a drug. |
| 5 | `LABEL_SPANISH` | VARCHAR(70) |  |  | This field contains an abbreviated Spanish text description for patient advice associated with a drug. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

