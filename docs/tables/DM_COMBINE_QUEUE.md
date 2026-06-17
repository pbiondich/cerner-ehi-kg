# DM_COMBINE_QUEUE

> Queue for performing combines in batch mode.

**Description:** DM COMBINE QUEUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ERR_MSG` | VARCHAR(100) |  |  | Error message |
| 2 | `COMBINED_FLAG` | DOUBLE |  |  | Shows status of combine. 0-not attempted, 1-successful, 2-attempted but not successful, 4-marked as "do combine" |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | Date and time the row was created. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 5 | `FROM_ID` | DOUBLE | NOT NULL |  | Value of the id for the from person/encounter of the combine. |
| 6 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | Parent table of the combine (person or encounter). |
| 7 | `QUEUE_ID` | DOUBLE | NOT NULL |  | Primary key of the table - a sequence generated number. |
| 8 | `TO_ID` | DOUBLE | NOT NULL |  | Value of the id for the to person/encounter of the combine. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

