# MM_COMMENT

> Mat Mgmt Comments

**Description:** MM COMMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of comment. |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 5 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Foreign Key to long_text table. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Entity ID |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Defines the parent table for parent_entity_id |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

