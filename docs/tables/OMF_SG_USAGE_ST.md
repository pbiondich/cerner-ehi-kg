# OMF_SG_USAGE_ST

> PowerVision Study Group Usage summary table. It is populated as part of running a view if study groups are being used.

**Description:** PowerVision Study Group Usage summary table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GRID_CD` | DOUBLE | NOT NULL |  | Subject area that was being run when this study group was used. Other codesets can be used besides 14265 depending on the team defining the value. |
| 2 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | Name of indicator being filter on with a study group. Other codesets can be used besides 14265 depending on the team defining the value. |
| 3 | `LAST_FILTER_DT_TM` | DATETIME |  |  | Last time this study group was used as part of a filter. |
| 4 | `SG_CNT` | DOUBLE |  |  | # of times this study group/indicator_cd/sg_name combination was used. |
| 5 | `SG_NAME` | VARCHAR(255) | NOT NULL |  | Study Group name. |
| 6 | `SG_TYPE` | VARCHAR(255) |  |  | Study Group type such as PATIENT or PHYSICIAN. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

