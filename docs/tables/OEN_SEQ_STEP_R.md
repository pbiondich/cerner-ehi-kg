# OEN_SEQ_STEP_R

> Relation between the OEN_SEQUENCE and OEN_STEP tables.

**Description:** OEN SEQ STEP R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ORDER_NBR` | DOUBLE | NOT NULL |  | The ordering of the steps.Column |
| 3 | `SEQUENCE_ID` | DOUBLE | NOT NULL | FK→ | Sequence ID from OEN_SEQUENCE table.Column |
| 4 | `STEP_ID` | DOUBLE | NOT NULL | FK→ | Step ID from OEN_STEP table.Column |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQUENCE_ID` | [OEN_SEQUENCE](OEN_SEQUENCE.md) | `SEQUENCE_ID` |
| `STEP_ID` | [OEN_STEP](OEN_STEP.md) | `STEP_ID` |

