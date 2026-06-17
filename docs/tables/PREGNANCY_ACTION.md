# PREGNANCY_ACTION

> Used for tracking access and interaction with a person's pregnancy history record.

**Description:** Pregnancy Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Date/time at which the action was taken |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Type of action taken |
| 3 | `ACTION_TZ` | DOUBLE | NOT NULL |  | Time zone in which the action was taken |
| 4 | `PREGNANCY_ACTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `PREGNANCY_ID` | DOUBLE | NOT NULL | FK→ | Pregnancy on which the action was taken |
| 6 | `PREGNANCY_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | The PREGNANCY_INSTANCE_ID value from the PREGNANCY_INSTANCE table that this action corresponds to. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Provider taking the action |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREGNANCY_ID` | [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PREGNANCY_INSTANCE_ID` |
| `PREGNANCY_INSTANCE_ID` | [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PREGNANCY_INSTANCE_ID` |

