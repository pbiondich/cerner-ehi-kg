# OMF_APP_VIEWERS

> List of (PowerVision style) viewers that a particular application can run.

**Description:** OMF APP VIEWERS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Application number from the APPLICATION table to which we are associating viewers. |
| 2 | `DEFAULT_IND` | DOUBLE |  |  | Determines whether this view type is the default viewer for this application. One and only one view type should have this set to 1 for a given application_number. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VIEW_TYPE` | DOUBLE | NOT NULL |  | Type of viewer that can be displayed. E.g a PowerVision grid/graph MDI, an advance data visualization tool, Risk Mgr viewer, IQHealth viewer, etc. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

