# CSM_SYS_PARAMS

> Global default parameters needed for the Client Services product.

**Description:** CSM SYS PARAMS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHG_DUE_DATE_IND` | DOUBLE |  |  | Allows the administrator to decide whether or not to allow CSM due dates to be reset by the users. |
| 2 | `CSM_CHARTABLE_IND` | DOUBLE |  |  | Indicates whether or not callback info is to be charted. |
| 3 | `CSM_DEF_PRIOR_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the CSM system should default a priority when service requests are ordered. |
| 4 | `CSM_PARAMS` | VARCHAR(10) | NOT NULL |  | Blank key. |
| 5 | `CSM_PURGE_DAYS_DEF` | DOUBLE | NOT NULL |  | Default number of purge days taht will be used if the request does not have a number of purge days. |
| 6 | `CSM_TEMPL_IND` | DOUBLE |  |  | A global indicator for the use of templates. |
| 7 | `DEF_RSLT_COM_IND` | DOUBLE |  |  | Reserved for future use. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

