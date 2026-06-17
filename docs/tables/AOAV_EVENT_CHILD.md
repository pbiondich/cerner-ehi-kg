# AOAV_EVENT_CHILD

> The child event associated with AOAV_EVENT

**Description:** AOAV_EVENT_CHILD  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state |
| 2 | `AOAV_COMP_CHILD_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for AOAV COMPONENT CHILD |
| 3 | `AOAV_EVENT_CHILD_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `AOAV_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for AOAV EVENT |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | unique identifier for the parent entity i.e. AOAV EVENT ID |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Name of the parent entity i.e. AOAV EVENT |
| 7 | `RESULT_DT_TM` | DATETIME |  |  | The result date/time of this child event. |
| 8 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | The result units of measure of this child event. |
| 9 | `RESULT_VALUE` | DOUBLE |  |  | The result value of this child event. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AOAV_COMP_CHILD_REF_ID` | [AOAV_COMP_CHILD_REF](AOAV_COMP_CHILD_REF.md) | `AOAV_COMP_CHILD_REF_ID` |
| `AOAV_EVENT_ID` | [AOAV_EVENT](AOAV_EVENT.md) | `AOAV_EVENT_ID` |

