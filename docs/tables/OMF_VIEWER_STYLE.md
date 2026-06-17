# OMF_VIEWER_STYLE

> Holds viewer 'styles' which would hold, e.g., a graph style of 3D bar chart with a blue background; title of ....

**Description:** Holds viewer 'styles' which would hold, e.g., a graph style of 3D bar chart...  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE |  |  | Indicates whether this style is the default value for the item_type. |
| 2 | `NAME` | VARCHAR(255) |  |  | User defined name of the viewer style. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VAL1` | VARCHAR(255) |  |  | Generic string column. |
| 10 | `VAL2` | VARCHAR(255) |  |  | Generic string column. |
| 11 | `VAL3` | VARCHAR(255) |  |  | Generic string column. |
| 12 | `VAL4` | VARCHAR(255) |  |  | Generic string column. |
| 13 | `VAL5` | VARCHAR(255) |  |  | Generic string column. |
| 14 | `VIEWER_STYLE_ID` | DOUBLE | NOT NULL |  | Unique identifier. |
| 15 | `VIEW_TYPE` | DOUBLE | NOT NULL |  | Type of viewer this style is meant for. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

