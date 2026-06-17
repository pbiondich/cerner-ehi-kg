# CELL_GROUP

> A reference of user-defined groupings of control cells used to do testing, entered in result entry.

**Description:** Cell_group  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CELL_CD` | DOUBLE | NOT NULL |  | The code value that represents the control cell that is built within this control cell grouping. This cell will be displayed within the Result Entry application when this control cell grouping is chosen by the user. |
| 6 | `CELL_GROUP_CD` | DOUBLE | NOT NULL |  | The code value that represents the cell group that would be entered by the user within the Result Entry application for testing. |
| 7 | `CELL_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that ensures the uniqueness of each row. |
| 8 | `DISPLAY_SEQ` | DOUBLE |  |  | The sequence in which the cells should display underneath the accession within the Result Entry application, when this cell group is entered by the user. |
| 9 | `SEQUENCE` | DOUBLE |  |  | Not currentlly used at this time. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

