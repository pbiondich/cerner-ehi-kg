# CDE_MILL_META_RS

> Contains record structure metadata for PowerInsight

**Description:** CDE_MILL_META_RS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDE_MILL_META_RS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDE_MILL_META_RS table. |
| 2 | `FILE_TYPE` | VARCHAR(100) |  |  | File type of the script. |
| 3 | `PARENT_FILE_TYPE` | VARCHAR(100) |  |  | The parent file type of the script. |
| 4 | `PARENT_KEY_RS_CNTR_NAME` | VARCHAR(100) |  |  | The name of the counter in the parents record structure. |
| 5 | `PARENT_KEY_RS_FIELD_NAME` | VARCHAR(100) |  |  | The name of the field in the parents record structure. |
| 6 | `PARENT_KEY_RS_NAME` | VARCHAR(100) |  |  | The parent record structure name. |
| 7 | `SCRIPT_NAME` | VARCHAR(100) |  |  | The name of the CCL script. |
| 8 | `SUBJECT_AREA_NAME` | VARCHAR(100) |  |  | The name of the subject area. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

