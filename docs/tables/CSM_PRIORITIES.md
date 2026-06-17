# CSM_PRIORITIES

> This table holds specific priorities for client services.

**Description:** CSM PRIORITIES  
**Table type:** REFERENCE  
**Primary key:** `CSM_PRIOR_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSM_ACTIVE_IND` | DOUBLE | NOT NULL |  | Indicates that the priority is active. |
| 2 | `CSM_DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates that this priority should be used as a default when any request is ordered. There can only be one default priority. |
| 3 | `CSM_PRIOR_DESC` | CHAR(40) | NOT NULL |  | The priorities description. |
| 4 | `CSM_PRIOR_ID` | DOUBLE | NOT NULL | PK | A unique id for a priority. |
| 5 | `CSM_TAT_IND` | DOUBLE | NOT NULL |  | The indicator denoting whether the TAT is in days or hours. |
| 6 | `CSM_TAT_LEN_IND` | DOUBLE | NOT NULL |  | The numerical value for turn around time. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CSM_REQUESTS](CSM_REQUESTS.md) | `CSM_PRIOR_ID` |
| [CSM_REQUESTS_ARCHIVE](CSM_REQUESTS_ARCHIVE.md) | `CSM_PRIOR_ID` |

