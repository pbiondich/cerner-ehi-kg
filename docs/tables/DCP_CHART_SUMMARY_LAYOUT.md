# DCP_CHART_SUMMARY_LAYOUT

> Defines the reports used and their position within a chart summary view.

**Description:** DCP CHART SUMMARY LAYOUT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COL_NBR` | DOUBLE | NOT NULL |  | Specifies the starting column position (0 based) for the identified report within the identified chart summary view. |
| 2 | `DCP_CHART_SUMMARY_LAYOUT_ID` | DOUBLE | NOT NULL |  | DCP Chart Summary Layout ID - Primary Key |
| 3 | `HEIGHT_NBR` | DOUBLE | NOT NULL |  | Specifies the height for the identified report within the identified chart summary view. |
| 4 | `LAYOUT_CD` | DOUBLE | NOT NULL |  | The identifier and display name of the chart summary view. |
| 5 | `REPORT_CD` | DOUBLE | NOT NULL |  | The identifier of the report to be included within the chart summary view at the identified position. |
| 6 | `ROW_NBR` | DOUBLE | NOT NULL |  | Specifies the starting row position (0 based) for the identified report within the identified chart summary view. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WIDTH_NBR` | DOUBLE | NOT NULL |  | Specifies the width for the identified report within the identified chart summary view. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

