# MLLD_DDM_CONDITION

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DDM_CONDITION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SYSTEM_ID` | DOUBLE | NOT NULL |  | Body System ID - FK from MLTM_DDM_BODY_SYSTEM table |
| 2 | `CONDITION_ID` | DOUBLE | NOT NULL |  | Condition ID - PK Column for this table. Also FK from MLTM_DDM_CONDITION_LIST table |
| 3 | `MEDICAL_SPECIALTY_ID` | DOUBLE | NOT NULL |  | Medical Specialty ID - FK from MLTM_MEDICAL_SPECIALTY table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

