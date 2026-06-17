# OMF_PV_VIEW

> View definition.

**Description:** View definition such as the from and where clauses.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CCL_HINT` | VARCHAR(255) |  |  | Select statement hint for the view. |
| 2 | `FROM_CLAUSE` | VARCHAR(255) | NOT NULL |  | Views from clause. |
| 3 | `REQUIRED_IND` | DOUBLE |  |  | Indicates whether or not the from/where clause is required for this view. |
| 4 | `SCRIPT_NBR` | DOUBLE |  |  | Script to run to produce this view. Typically 952287 = omf_run_view. This is not currently checked. |
| 5 | `STR_SEQ` | DOUBLE | NOT NULL |  | Used for sequencing if "clause" values are greater than 255 characters. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VIEW_CD` | DOUBLE | NOT NULL |  | View code value. cdf_meaning='VIEW' and display= . Other codesets can be used besides 14265 depending on the team defining the value. |
| 12 | `WHERE_CLAUSE` | VARCHAR(255) |  |  | Select statements where clause. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

