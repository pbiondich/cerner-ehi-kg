# OMF_PV_SECURITY_FILTER

> Stores security information (e.g. only show rows in a certain department or from a certain physician group) that was entered using the PowerVision Admin Tool.

**Description:** OMF PowerVision security filter.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GRID_CD` | DOUBLE | NOT NULL |  | Grid which we are placing security on. Other codesets can be used besides 14265 depending on the team defining the value. |
| 2 | `INDICATOR_CD` | DOUBLE |  |  | Indicator which we are restricting access to. We will add a where clause with this indicator's column_str when the view is run. If a user has no restrictions to the view a single row is placed in this table with an indicator_cd of 0. Other codesets can be used besides 14265 depending on the team defining the value. |
| 3 | `NUM_ID` | DOUBLE |  |  | Numeric value which is an id from some table. This is the value we are going to restrict on for this person in this view. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | Parent entity (table name) that Num_id comes from. Will be used for merging purposes. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `USER_ID` | DOUBLE | NOT NULL |  | User id this security is being set up for. |
| 11 | `VALUE` | VARCHAR(255) |  |  | Character value to have security on. This column or num_id will be filled out. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

