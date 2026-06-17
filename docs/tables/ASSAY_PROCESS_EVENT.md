# ASSAY_PROCESS_EVENT

> Contains the errors that a laboratory analyzer can return for a discrete assay and the action to be taken upon reciept of the error, by model.

**Description:** Contains the errors that a laboratory analyzer can return for a discrete assay.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CD` | DOUBLE | NOT NULL |  | Contains the DBMS assigned unique code value for an action to be taken upon receipt of a discrete assay error from a laboratory analyzer. |
| 2 | `APPLY_TO_ALL_IND` | DOUBLE |  |  | Specifies if the error flag applies to all DTAs for the service resource |
| 3 | `AV_FLAG` | DOUBLE | NOT NULL |  | Defines if auto verification is turned on or off by task assay |
| 4 | `INSTRU_ERROR_CODE` | VARCHAR(20) | NOT NULL |  | Contains the error(s) that have been configured for an action upon receipt from an analyzer for a discrete assay. |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Contains the DBMS assigned unique code value indicating service_resource_cd. |
| 6 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned unique key field value from strt_assay table. |
| 7 | `STRT_MODEL_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned unique key field value from strt_model table. |
| 8 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Contains the unique key field value from discrete_task_assay. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

