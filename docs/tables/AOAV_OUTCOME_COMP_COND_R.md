# AOAV_OUTCOME_COMP_COND_R

> This table has the list of conditions for each component that contributed to the outcome

**Description:** AOAV_OUTCOME_COMPONENT_CONDITION_RELATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AOAV_CONDITION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifer for AOAV CONDITION |
| 3 | `AOAV_OUTCOME_COMP_COND_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `AOAV_OUTCOME_COMP_ID` | DOUBLE | NOT NULL | FK→ | Unique identifer for AOAV COMPONENT |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AOAV_CONDITION_ID` | [AOAV_CONDITION](AOAV_CONDITION.md) | `AOAV_CONDITION_ID` |
| `AOAV_OUTCOME_COMP_ID` | [AOAV_OUTCOME_COMP](AOAV_OUTCOME_COMP.md) | `AOAV_OUTCOME_COMP_ID` |

