# EA_PASSWORD_HISTORY

> Tracks historical changes to a user's password with the intent of preventing users from re-using passwords too frequently.

**Description:** Password History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EA_PASSWORD_HISTORY_ID` | DOUBLE | NOT NULL |  | Generated unique identifier for a historical password record. |
| 2 | `EA_USER_ID` | DOUBLE | NOT NULL | FK→ | Generated unique identifier for a user record. |
| 3 | `PASSWORD_CHANGE_DT_TM` | DATETIME |  |  | The date/time at which the password last changed. |
| 4 | `PASSWORD_HASH` | VARCHAR(1000) | NOT NULL |  | Password hash value |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EA_USER_ID` | [EA_USER](EA_USER.md) | `EA_USER_ID` |

