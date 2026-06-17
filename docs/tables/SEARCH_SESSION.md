# SEARCH_SESSION

> Parent table to track search sessions (regardless if search is initiated by user interaction.

**Description:** Search Session  
**Table type:** ACTIVITY  
**Primary key:** `SEARCH_SESSION_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NBR` | DOUBLE | NOT NULL |  | The application number, if applicable, that is initiating the search session. When the search session is initiated by an interactive workflow the application will be assigning the value. Will be 0 when the context of the application is not known. |
| 2 | `DEVICE_LOCATION_TXT` | VARCHAR(255) |  |  | The location of the device ("device_location" logical registry setting) from where the user initiated an interactive search session. |
| 3 | `PCID_TXT` | VARCHAR(255) |  |  | The pc identifier ("personmgmt:pcid" logical registry setting) from where the user initiated an interactive search session. |
| 4 | `QUERY_IDENTIFICATION_CD` | DOUBLE | NOT NULL |  | Identifies the query associated with the search session. |
| 5 | `SEARCH_CONTEXT_KEY_TXT` | VARCHAR(255) |  |  | The configuration path associated with the Java search session. This key uniquely defines the consuming workflow associated with the search. |
| 6 | `SEARCH_MODE_CD` | DOUBLE | NOT NULL |  | The search style/mode associated with the search session. this should correspond with the query_identification_cd. |
| 7 | `SEARCH_SESSION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SEARCH_SESSION table. |
| 8 | `SESSION_DT_TM` | DATETIME | NOT NULL |  | The date and time the search session is initiated by an interactive workflow, service, or query. |
| 9 | `TASK_NBR` | DOUBLE | NOT NULL |  | The task number, if applicable, associated with the search session. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `USER_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that initiated a search. |
| 16 | `USER_POSITION_CD` | DOUBLE | NOT NULL |  | The position associated with the person from the personnel table (prsnl) when the search session was initiated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SEARCH_SESSION_EVENT](SEARCH_SESSION_EVENT.md) | `SEARCH_SESSION_ID` |
| [SEARCH_SESSION_OUTCOME](SEARCH_SESSION_OUTCOME.md) | `SEARCH_SESSION_ID` |

