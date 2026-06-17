# DM_CMB_WARNING

> Holds the most recent warnings from combine scripts performing questionable combnies/uncombines.

**Description:** Combine Warning  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMBINE_ENTITY_ID` | DOUBLE | NOT NULL |  | ID of Combine which generated the warning. |
| 2 | `COMBINE_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table which the combine_id comes from - e.g. 'PERSON_COMBINE','ENCNTR_COMBINE','COMBINE'. |
| 3 | `DM_CMB_WARNING_ID` | DOUBLE | NOT NULL |  | Sequence generated primary key |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of entity being uncombined. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Table name of entity being uncombined. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WARNING_TYPE_CD` | DOUBLE | NOT NULL |  | Type of warning noted when a questionable combine/uncombine is performed. For example, FUTUREORDER |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

