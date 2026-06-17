# AOAV_OUTCOME_COMP

> This table contains the relationship between an outcome to its corresponding components

**Description:** AOAV_OUTCOME_COMPONENT  
**Table type:** ACTIVITY  
**Primary key:** `AOAV_OUTCOME_COMP_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state |
| 2 | `AOAV_COMP_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for component |
| 3 | `AOAV_OUTCOME_COMP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `AOAV_OUTCOME_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the Outcome |
| 5 | `COMP_SCORE_VALUE` | DOUBLE |  |  | Score value for the component |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AOAV_COMP_REF_ID` | [AOAV_COMP_REF](AOAV_COMP_REF.md) | `AOAV_COMP_REF_ID` |
| `AOAV_OUTCOME_ID` | [AOAV_OUTCOME](AOAV_OUTCOME.md) | `AOAV_OUTCOME_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AOAV_OUTCOME_COMP_COND_R](AOAV_OUTCOME_COMP_COND_R.md) | `AOAV_OUTCOME_COMP_ID` |
| [AOAV_OUTCOME_COMP_EVENT_R](AOAV_OUTCOME_COMP_EVENT_R.md) | `AOAV_OUTCOME_COMP_ID` |

