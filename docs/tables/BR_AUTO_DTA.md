# BR_AUTO_DTA

> autobuild assays

**Description:** BEDROCK AUTO DTA  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | activity type |
| 2 | `BB_RESULT_PROCESSING_CD` | DOUBLE | NOT NULL |  | result processing type associated to the Blood Bank DTA |
| 3 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 4 | `DESCRIPTION` | VARCHAR(100) |  |  | legacy long name |
| 5 | `MNEMONIC` | VARCHAR(50) |  |  | legacy short name |
| 6 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | result type |
| 7 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | dta id |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

