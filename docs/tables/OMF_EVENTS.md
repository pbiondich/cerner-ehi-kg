# OMF_EVENTS

> List of events such as 'Order', 'Requested Collection', 'In Transit', 'In Lab'.

**Description:** OMF EVENTS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTUAL_TAT_STR` | VARCHAR(255) |  |  | The request structure member that stores the actual TAT. |
| 3 | `DESCRIPTION` | VARCHAR(80) |  |  | Event description. |
| 4 | `DETAIL_IND` | DOUBLE |  |  | Indicates whether the clinical event is at the order or detail level. 0 = order level; 1 = detail level |
| 5 | `EVENT_NUM` | DOUBLE | NOT NULL |  | Unique id of event. |
| 6 | `EVENT_SEQ` | DOUBLE |  |  | Event order of occurrence. |
| 7 | `EXP_TAT_STR` | VARCHAR(255) |  |  | The request structure member that stores the actual TAT. |
| 8 | `MONITOR_IND` | DOUBLE |  |  | Not used. |
| 9 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Code value that identifies the type of transaction being processed. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

