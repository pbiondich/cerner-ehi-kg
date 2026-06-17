# STRT_MODEL_ASSAY_ERROR

> Contains each error that can be returned by an analyzer by assay and model.

**Description:** Contains all errors for each discrete assay that can be performed by a model.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | DOUBLE |  |  | Contains the code_value from code_set 14001 which describes an action to take when an error is received from an analyzer. |
| 2 | `DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Future use. Currently not defined |
| 3 | `DESCRIPTION` | VARCHAR(50) |  |  | Contains a description of the error returned by the analyzer for the assay. |
| 4 | `ERROR_CODE` | DOUBLE | NOT NULL |  | Contains the error code returned by the analyzer for the assay. |
| 5 | `SEVERITY_FLAG` | DOUBLE |  |  | Reserved for future use. |
| 6 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned key field value from the strt_assay table. |
| 7 | `STRT_MODEL_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned key field value from the strt_model table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

