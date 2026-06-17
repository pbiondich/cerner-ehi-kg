# MSG_CONFIG_PUB_ASNMNT

> Assigns a particular user context to a configuration

**Description:** Messaging Configuration Public Assignment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE |  |  | Application Context Modifier |
| 2 | `MSG_CONFIG_ID` | DOUBLE | NOT NULL | FK→ | Selected Configuration |
| 3 | `MSG_CONFIG_PUB_ASNMNT_ID` | DOUBLE | NOT NULL |  | Primary key |
| 4 | `POSITION_CD` | DOUBLE | NOT NULL |  | Assigned Position |
| 5 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Assigned Pool |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Assigned User |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MSG_CONFIG_ID` | [MSG_CONFIG](MSG_CONFIG.md) | `MSG_CONFIG_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

