# DM_XNTR_README_DATA

> Stores readme information from admin during package install that is necessary for the XnTR process

**Description:** Database Architecture Extract and Transform Retrieve readme data  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_XNTR_README_DATA_ID` | DOUBLE | NOT NULL |  | Non-intelligent PK of table |
| 2 | `EXECUTE_DT_TM` | DATETIME | NOT NULL |  | Holds the most recent date time that the readme instance was executed for the environment |
| 3 | `PARENT_README_ID` | DOUBLE | NOT NULL |  | Holds the Parent readme id of the readme from DM_README.PARENT_README_ID |
| 4 | `README_ID` | DOUBLE | NOT NULL |  | Value from admin table = DM_README.README_ID |
| 5 | `README_INSTANCE` | DOUBLE | NOT NULL |  | Holds the instance of readme from DM_README.INSTANCE |
| 6 | `SCRIPT` | VARCHAR(100) | NOT NULL |  | Holds the Script associated with the README from DM_README.SCRIPT |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

