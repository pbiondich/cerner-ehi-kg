# DM_FLAGS_LOCAL

> This is a duplicate (clone) of the DM_FLAGS table in the Admin DB. It will be used by solution code to look up column flag values and definition.

**Description:** DM_FLAGS_LOCAL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | The FLAG or TFLG column being documented |
| 2 | `DEFINITION` | VARCHAR(500) |  |  | A long definition of he FLAG or TFLG column |
| 3 | `DESCRIPTION` | VARCHAR(80) |  |  | A short description of the flag value for a FLAG column or the textual value for the TFLG column |
| 4 | `FLAG_VALUE` | DOUBLE | NOT NULL |  | The numeric flag value associated to the FLAG column. Or just a sequential meaningless number for a TFLG column. |
| 5 | `OWNER` | VARCHAR(30) | NOT NULL |  | The schema owner. Defaults to V500 |
| 6 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | The table being documented |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

