# RAD_COMBINE_RPT

> rad combine report

**Description:** This table contains information that pertains to the combine report.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DESC` | VARCHAR(20) |  |  | This column contains the action that will print on the report. |
| 2 | `CATALOG_CD` | DOUBLE |  |  | This column contains the identifier for the procedure. If a procedure was moved. |
| 3 | `COMBINE_ID` | DOUBLE | NOT NULL |  | This column identifies the combine that the report information pertains to. |
| 4 | `COMBINE_IND` | DOUBLE | NOT NULL |  | This column indicates if the info is for a combine or uncombine. |
| 5 | `COMP_DT_TM` | DATETIME |  |  | This column contains the completion date and time for the procedure that was moved. |
| 6 | `FOLD_TYPE_CD` | DOUBLE |  |  | This column contains the identifier for the folder type that was moved. |
| 7 | `FOLD_TYPE_DESC` | VARCHAR(2) |  |  | This is the description for the folder type that was moved. |
| 8 | `FROM_FILING_NBR` | VARCHAR(20) |  |  | This column contains the filing number for the folder associated with the from patient. |
| 9 | `FROM_FOLD_ID` | DOUBLE |  |  | This column contains the identifier for the from folder. |
| 10 | `FROM_LOAN_TYPE_FLAG` | DOUBLE |  |  | This column is used to identify the origin of the from folders tracking point. |
| 11 | `FROM_PERSON_ID` | DOUBLE |  |  | This column contains the identifier for the from person. |
| 12 | `FROM_TRK_PT_CD` | DOUBLE |  |  | this field contains the identifier for the folders current location. |
| 13 | `FROM_VOL` | DOUBLE |  |  | This column identifies the volume number for the from folder. |
| 14 | `LABEL_IND` | DOUBLE |  |  | This column indicates if a label was produced for the folder. |
| 15 | `LIB_GRP_CD` | DOUBLE |  |  | This column identifies the library group that the folder is associated with. |
| 16 | `LIB_GRP_DESC` | VARCHAR(40) |  |  | This column contains the description of the library group |
| 17 | `SEQUENCE` | DOUBLE | NOT NULL |  | This identifies the order in which entries will appear on the report. |
| 18 | `TO_FILING_NBR` | VARCHAR(20) |  |  | This is the filing number for the to folder. |
| 19 | `TO_FOLD_ID` | DOUBLE |  |  | This is the identifier for the to folder. |
| 20 | `TO_LOAN_TYPE_FLAG` | DOUBLE |  |  | This indicates the origin of the to folder's tracking point. |
| 21 | `TO_PERSON_ID` | DOUBLE |  |  | This identifies the to person. |
| 22 | `TO_TRK_PT_CD` | DOUBLE |  |  | This identifies the to folders current location. |
| 23 | `TO_VOL` | DOUBLE |  |  | This is the volume number for the to folder. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

