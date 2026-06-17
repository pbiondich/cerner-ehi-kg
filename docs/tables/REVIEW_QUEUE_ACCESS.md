# REVIEW_QUEUE_ACCESS

> Defines other users that a specific user has granted review queue access to.

**Description:** Review Queue Access  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GRANT_TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who has been granted access to another user's queue. It is a foreign key reference to the primary key of the personnel table. |
| 2 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who is granting review queue access to another user. It also identifies the review queue for which the access is granted. It is a foreign key reference to the primary key of the personnel table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GRANT_TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

