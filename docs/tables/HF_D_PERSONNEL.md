# HF_D_PERSONNEL

> HF_D_PERSONNEL table

**Description:** HF_D_PERSONNEL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MEDICAL_SPECIALTY` | VARCHAR(40) |  |  | The physician medical specialty |
| 2 | `PERSONNEL_ADDRESS` | VARCHAR(255) |  |  | The personnel address |
| 3 | `PERSONNEL_CITY` | VARCHAR(100) |  |  | The personnel city |
| 4 | `PERSONNEL_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely defines a personnel record |
| 5 | `PERSONNEL_NAME` | VARCHAR(200) |  |  | The personnel name |
| 6 | `PERSONNEL_PHONE` | VARCHAR(50) |  |  | The personnel's phone number |
| 7 | `PERSONNEL_POSITION` | VARCHAR(40) |  |  | The personnel's position |
| 8 | `PERSONNEL_STATE` | VARCHAR(40) |  |  | The personnel state |
| 9 | `PERSONNEL_ZIP_CODE` | VARCHAR(25) |  |  | The personnel's zip code |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, MANUAL should be entered. |
| 12 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

