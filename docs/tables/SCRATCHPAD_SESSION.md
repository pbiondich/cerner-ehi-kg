# SCRATCHPAD_SESSION

> Contains information for a scratchpad session. Scratchpad session is used as a temporary data storage for information that is being prepared to commit to Millennium.

**Description:** Scratchpad Session  
**Table type:** ACTIVITY  
**Primary key:** `SCRATCHPAD_SESSION_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXPIRE_DT_TM` | DATETIME | NOT NULL |  | The date/time as which point this scratchpad session expires. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The id of the patient to which this scratchpad session is associated. |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the personnel to which this scratchpad session is associated. |
| 5 | `SCRATCHPAD_CONCEPT_NAME` | VARCHAR(100) | NOT NULL |  | The concept used to identify the scratchpad session. |
| 6 | `SCRATCHPAD_SESSION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the scratchpad_session table. |
| 7 | `TIMEOUT_IN_MINS` | DOUBLE | NOT NULL |  | The number of minutes the session can be without modification before the session expires. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCRATCHPAD_ITEM](SCRATCHPAD_ITEM.md) | `SCRATCHPAD_SESSION_ID` |

