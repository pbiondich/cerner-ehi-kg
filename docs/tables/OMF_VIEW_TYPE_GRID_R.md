# OMF_VIEW_TYPE_GRID_R

> For non-PowerVision/PV SA Editor application it will tell whether a grid_cd should run under a view_type. E.g. Risk Mgr subject areas only should be run under Risk Mgr (view_type = 2)

**Description:** View type/Grid code relationships for non-PowerVision and PV SA Editor apps.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GRID_CD` | DOUBLE | NOT NULL |  | Subject Area. Other codesets can be used besides 14265 depending on the team defining the value. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `VIEW_TYPE` | DOUBLE | NOT NULL |  | View Type - e.g. 2 = Risk Manager; 1 = PowerVision grid/graph. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

