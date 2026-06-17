# OMF_VIEWERS

> (PowerVision-style) viewers which uses the OMF core .dlls to retrieve data.

**Description:** OMF VIEWERS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HAS_PROP_IND` | DOUBLE |  |  | Does this viewer have a display properties screen? E.g. to define whether it's a pie chart vs. a bar chart; or where to put what data elements. |
| 2 | `INST_STR` | VARCHAR(255) |  |  | Instantiation string the OMF .dlls need to use to be able to call this viewer at run time. |
| 3 | `OBJ_DESC` | VARCHAR(255) |  |  | Description/name of the viewer. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VIEW_TYPE` | DOUBLE | NOT NULL |  | Type of viewer that can be displayed. E.g a PowerVision grid/graph MDI, an advance data visualization tool, Risk Mgr viewer, IQHealth viewer, etc. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

