# CDE_MILL_META

> Contains metadata for PowerInsight

**Description:** CDE_MILL_META  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDE_MILL_META_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDE_MILL_META table. |
| 2 | `FILE_TYPE` | VARCHAR(100) |  |  | File type of the script |
| 3 | `KEY_RS_CNTR_NAME` | VARCHAR(100) |  |  | Name of the counter in the keys record structure |
| 4 | `KEY_RS_FIELD_NAME` | VARCHAR(100) |  |  | Name of the field in the keys record structure |
| 5 | `KEY_RS_NAME` | VARCHAR(100) |  |  | Name of the keys record structure |
| 6 | `RAW_IND` | DOUBLE |  |  | Raw CCL script indicator |
| 7 | `SCRIPT_LVL_NBR` | DOUBLE |  |  | Tells at what hierarchical level this scripts is at |
| 8 | `SCRIPT_NAME` | VARCHAR(100) |  |  | Name of the CCL script |
| 9 | `SUBJECT_AREA_NAME` | VARCHAR(100) |  |  | The name of the subject area. |
| 10 | `TYPE_FLAG` | DOUBLE |  |  | The type of the script |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

