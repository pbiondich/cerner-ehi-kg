# OMF_ABSTRACT_VIEW

> Stores the PowerVision views that contain abstract data.

**Description:** OMF ABSTRACT VIEW  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | The contributing source system for the abstract data element |
| 2 | `STR_SEQ` | DOUBLE |  |  | The sequence that applies to the from/where clause in omf_pv_view. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VIEW_CD` | DOUBLE | NOT NULL |  | The corresponding PowerVision view in which abstract data is available for reporting. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

