# TL_MULTPAT_COL_CONTENT

> The column names defined for a specific tab while in multipatient mode.

**Description:** TL MULTPAT COL CONTENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_MEANING` | VARCHAR(12) |  |  | The column header of the specific column.Column |
| 2 | `COLUMN_NBR` | DOUBLE | NOT NULL |  | A number that identifies which column in the list that this entry corresponds with. |
| 3 | `MULTIPATIENT_IND` | DOUBLE | NOT NULL |  | An indicator used to determine if the parent_entity_cd is a person, position, or application default. 0 = person, 1 = position, 2 = app default. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | A unique number that is used to identify a specific person, position, or app default. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | parent entity name |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

