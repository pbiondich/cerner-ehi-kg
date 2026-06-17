# PIP_PREFS

> PIP properties for section and column definitions.

**Description:** PIP PREFS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MERGE_ID` | DOUBLE | NOT NULL |  | ID of property value. |
| 2 | `MERGE_NAME` | VARCHAR(100) |  |  | Name of merge entity specified in MERGE_ID. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID of parent Entity. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(100) |  |  | Name of entity specified in PARENT_ENTITY_ID. |
| 5 | `PIP_PREFS_ID` | DOUBLE | NOT NULL |  | Unique identifier for preference. |
| 6 | `PREF_NAME` | VARCHAR(100) |  |  | Name of preference. |
| 7 | `PREF_VALUE` | VARCHAR(255) |  |  | Value of preference. |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL |  | ID of user preference is specified for. 0 indicates it is the default. |
| 9 | `SEQUENCE` | DOUBLE |  |  | sequence of preference. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

