# NURSING_USER_ACCESS

> Keeps track of the last time a user performed a transaction within a given application

**Description:** NURSING USER ACCESS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_SOLUTION_CD` | DOUBLE | NOT NULL |  | Specifies which solution the audit information applies to |
| 2 | `LAST_ACCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the user last accessed the specific solution |
| 3 | `NURSING_USER_ACCESS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `SERVER_NAME` | VARCHAR(100) |  |  | The name of the server that the user last accessed. May be NULL for some solutions. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `USER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the user related to the record of when they last used the solution. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

