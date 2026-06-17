# STRT_MODEL_EVENT_LIST

> Contains the errors that can be returned by a laboratory analyzer by discrete assay.

**Description:** Contains the errors that can be returned by a laboratory analyzer.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(50) |  |  | Contains a description of the error returned by the analyzer. |
| 2 | `INSTRU_ERROR_CODE` | VARCHAR(20) | NOT NULL |  | Contains the error returned by the model by discrete assay. |
| 3 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned unique key field value from strt_assay table. |
| 4 | `STRT_MODEL_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned unique key field value from strt_model table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

