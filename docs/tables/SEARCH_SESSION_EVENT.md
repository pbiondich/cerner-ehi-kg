# SEARCH_SESSION_EVENT

> Tracks search data, including origination of the search criteria, and results associated with a search event (query_ triggered within a search session.

**Description:** Search Session Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NUMBER_OF_RESULTS_TOT` | DOUBLE | NOT NULL |  | Number of unique results (ids) returned in the search query. |
| 2 | `RESULT_CD` | DOUBLE | NOT NULL |  | The result of the search query. |
| 3 | `SEARCH_DT_TM` | DATETIME | NOT NULL |  | The date and time the search query was initiated. |
| 4 | `SEARCH_DURATION_MSEC` | DOUBLE | NOT NULL |  | The time, in milliseconds, it took to execute the search query. |
| 5 | `SEARCH_SESSION_EVENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SEARCH_SESSION_EVENT table. |
| 6 | `SEARCH_SESSION_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row ont he parent table SEARCH_SESSION. |
| 7 | `SEARCH_SUB_MODE_CD` | DOUBLE |  |  | Identifies the Search Mode for the search session event. |
| 8 | `SITE_CD` | DOUBLE | NOT NULL |  | The database that is associated with the search event (what database was searched). |
| 9 | `TYPE_CD` | DOUBLE | NOT NULL |  | The origination of the search criteria. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEARCH_SESSION_ID` | [SEARCH_SESSION](SEARCH_SESSION.md) | `SEARCH_SESSION_ID` |

