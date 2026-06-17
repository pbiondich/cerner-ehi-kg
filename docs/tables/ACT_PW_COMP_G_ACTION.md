# ACT_PW_COMP_G_ACTION

> A record of actions performed on activity component groups.

**Description:** ACT_PW_COMP_G_ACTION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date/time that the action was performed. |
| 2 | `ACTION_TZ` | DOUBLE | NOT NULL |  | The time zone in which the action was performed. |
| 3 | `ACT_PW_COMP_G_ACTION_ID` | DOUBLE | NOT NULL |  | Primary Key - uniquely identifies a row in the table |
| 4 | `ACT_PW_COMP_G_ID` | DOUBLE | NOT NULL | FK→ | The id of the group upon which the action was performed. First column of 2-column foreign key from ACT_PW_COMP_G table. |
| 5 | `ACT_PW_COMP_ID` | DOUBLE | NOT NULL | FK→ | value from the same field in the ACT_PW_COMP_G table and correlates with the ACT_PW_COMP_G_ID field to make up the compound foreign key. |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the person who performed the action. |
| 7 | `REASON_CD` | DOUBLE | NOT NULL |  | A codified reason that the action was performed. |
| 8 | `REASON_COMMENT` | VARCHAR(512) |  |  | A free text reason that the action was performed. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | A sequence to track the order in which actions were performed on the group. |
| 10 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | A flag to designate the type of the action performed. 0 = None, 1 = Override |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACT_PW_COMP_G_ID` | [ACT_PW_COMP_G](ACT_PW_COMP_G.md) | `ACT_PW_COMP_G_ID` |
| `ACT_PW_COMP_ID` | [ACT_PW_COMP_G](ACT_PW_COMP_G.md) | `ACT_PW_COMP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

