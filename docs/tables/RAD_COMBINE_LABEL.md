# RAD_COMBINE_LABEL

> This table contains data related to image management combines. it records information about the labels that are being generated.

**Description:** Radiology Combine Label  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMBINE_ID` | DOUBLE | NOT NULL |  | This column identifies the combine that the label information is associated with. |
| 2 | `COMBINE_IND` | DOUBLE | NOT NULL |  | This column indicates if the row is related to a combine or uncombine. |
| 3 | `LIB_GROUP_CD` | DOUBLE |  |  | This field identifies the library group that the folder resides in. |
| 4 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL |  | This field identifies the folder that the label is for |
| 5 | `TYPE_MEAN` | VARCHAR(12) |  |  | This contains the meaning of the folder type. It indicates if a folder is a regular folder or a foreign folder. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

