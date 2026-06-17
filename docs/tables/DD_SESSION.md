# DD_SESSION

> This table is used to store session level information, such as the lock status of a note, related to Dynamic Documentation.

**Description:** Dynamic Documentation - Session  
**Table type:** ACTIVITY  
**Primary key:** `DD_SESSION_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DD_SESSION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a session lock that is being held by a row in one of the dynamic document tables. This must be supplied by a consumer when attempting to save a document. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the locked row on the table. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table in which the locked row exists. |
| 4 | `SESSION_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time the lock was obtained. |
| 5 | `SESSION_USER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person holding the lock. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SESSION_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DD_SESSION_DATA](DD_SESSION_DATA.md) | `DD_SESSION_ID` |

