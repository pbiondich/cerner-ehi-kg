# VIRTUAL_VIEW_CRITERIA

> shows the criteria that applies to this row on the parent_entity_name

**Description:** VIRTUAL VIEW CRITERIA  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRITERIA_TYPE_CD` | DOUBLE | NOT NULL |  | The type of criteria used. |
| 2 | `CRITERIA_VALUE` | VARCHAR(255) | NOT NULL |  | This is the value for the criteria. |
| 3 | `CRITERIA_VALUE_ID` | DOUBLE | NOT NULL |  | this column is used if the criteria value is an ID or a CD |
| 4 | `CRITERIA_VALUE_PARENT_ENTITY` | VARCHAR(32) |  |  | used on conjunction with the criteria_value_id column |
| 5 | `PARENT_ENTITY_ID` | DOUBLE |  |  | The object that we are entering the criteria for. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The parent entity of the parent_entity_id number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VIRTUAL_VIEW_CRITERIA_ID` | DOUBLE | NOT NULL |  | Unique, sequence generated number that uniquely identifies a row in the table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

