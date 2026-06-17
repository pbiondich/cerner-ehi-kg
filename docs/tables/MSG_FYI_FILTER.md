# MSG_FYI_FILTER

> Holds basic information on a results FYI filter. These filters determine which new results will automatically display in the physician's inbox.

**Description:** MSG_FYI_FILTER  
**Table type:** REFERENCE  
**Primary key:** `MSG_FYI_FILTER_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_INCL_IND` | DOUBLE | NOT NULL |  | One indicates associated encounters should be included, not excluded |
| 3 | `EVENT_INCL_IND` | DOUBLE | NOT NULL |  | One indicates associated encounters should be included, not excluded |
| 4 | `FILTER_CREATE_DT_TM` | DATETIME | NOT NULL |  | Date the filter was created |
| 5 | `FILTER_DESC` | VARCHAR(40) |  |  | Optional description of the filter |
| 6 | `FILTER_END_DT_TM` | DATETIME | NOT NULL |  | Date the filter was no longer assigned to any user or position |
| 7 | `FILTER_NAME` | VARCHAR(40) | NOT NULL |  | Name of the filter |
| 8 | `FILTER_OWNER_ID` | DOUBLE | NOT NULL |  | The prsnl_id of the user that owns the filter. This value will be zero if the filter is public. |
| 9 | `FILTER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of fyi filter, 0 - relation, 1 - ad hoc |
| 10 | `LATE_POSTING_FLAG` | DOUBLE | NOT NULL |  | Affects results posted after the associated relationships end. Zero indicates late postings will not be included. One indicates late postings will be included. Two indicates only late postings will be shown. |
| 11 | `MSG_FYI_FILTER_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 12 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | One indicates the filter is public / shared |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MSG_FYI_ASSIGNMENT](MSG_FYI_ASSIGNMENT.md) | `MSG_FYI_FILTER_ID` |
| [MSG_FYI_FILTER_DTL](MSG_FYI_FILTER_DTL.md) | `MSG_FYI_FILTER_ID` |
| [SUBSCRPTN_FILTER_RESULTS_RELTN](SUBSCRPTN_FILTER_RESULTS_RELTN.md) | `MSG_FYI_FILTER_ID` |

