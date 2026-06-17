# HF_D_ARRIVAL_MODE

> Dimension table for potential arrival modes.

**Description:** HF_D_ARRIVAL_MODE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARRIVAL_MODE_CODE` | VARCHAR(10) |  |  | The mode of arrival value per HL7 table 0430. |
| 2 | `ARRIVAL_MODE_DESC` | VARCHAR(100) |  |  | The mode of label value per HL7 table 0430/ |
| 3 | `ARRIVAL_MODE_ID` | DOUBLE | NOT NULL |  | primary key |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

