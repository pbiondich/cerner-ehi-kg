# EXPLORER_MENU

> Menu items for discern explorer menu program

**Description:** Explorer Menu  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CCL_GROUP` | DOUBLE | NOT NULL |  | The CCL group of this report object., which should match the object group shown in CCLPROT. |
| 3 | `ITEM_DESC` | CHAR(40) |  |  | The description of the menu option |
| 4 | `ITEM_NAME` | CHAR(30) |  |  | The name of the menu option item |
| 5 | `ITEM_TYPE` | CHAR(1) |  |  | The type of the menu option ( P-rogram or M-enu ) |
| 6 | `MENU_ID` | DOUBLE | NOT NULL |  | The unique menu identifier |
| 7 | `MENU_PARENT_ID` | DOUBLE |  |  | If non-zero, this field indicates that it is a child of the specified menu. |
| 8 | `PERSON_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 9 | `REPORT_SERVICE_CD` | DOUBLE | NOT NULL |  | Reference to code set 4000601 (CclReportServiceBindings). A default of 0.0 indicates the CpmScriptBatch service is used for this report object. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

