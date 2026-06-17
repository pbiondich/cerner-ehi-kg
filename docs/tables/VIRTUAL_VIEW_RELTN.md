# VIRTUAL_VIEW_RELTN

> this relates the criteria to a view

**Description:** VIRTUAL VIEW RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRITERIA_TYPE_CD` | DOUBLE | NOT NULL |  | The type code for the type of criteria |
| 2 | `CRITERIA_VALUE` | VARCHAR(255) | NOT NULL |  | This is the value for the for the criteria if the not an ID or CD |
| 3 | `CRITERIA_VALUE_ID` | DOUBLE | NOT NULL |  | This is the value of the criteria if an ID or CD |
| 4 | `CRITERIA_VALUE_PARENT_ENTITY` | VARCHAR(32) |  |  | The is the parent entity for criteria_value_id |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The parent entity of the item that this criteria belongs to |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VIRTUAL_VIEW_ID` | DOUBLE |  |  | The ID for the view |
| 12 | `VIRTUAL_VIEW_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

