# RXS_TASK_DISPENSE_RELTN

> Describes the relationship between location tasks and patient activities.

**Description:** RxStation Task Dispense Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the relationship was made. |
| 2 | `PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL |  | Product dispense history information for the dispense event that is related to this location task. |
| 3 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Helps to describe the nature of this relationship. |
| 4 | `RXS_LOCATION_TASK_ID` | DOUBLE | NOT NULL | FK→ | The location task that is related to this prod dispense. |
| 5 | `RXS_TASK_DISPENSE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RXS_TASK_DISPENSE_RELTN table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RXS_LOCATION_TASK_ID` | [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_LOCATION_TASK_ID` |

