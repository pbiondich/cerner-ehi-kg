# CE_CONTRIBUTOR_LINK

> Stores linked contributor link event ids to a calculation

**Description:** The calculation link table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Calculation contributor Valid_from |
| 2 | `CONTRIBUTOR_EVENT_ID` | DOUBLE | NOT NULL |  | Calculation contributor Event_id |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifier to a logical event row in clinical_event table. |
| 4 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of Contributor:0=Not Defined, 1=Calculation, 2=String, 3=Coded, 4=Date |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Creation date for row. Contains the "Beginning Point" of when a row in the table is valid. |
| 11 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid.This indicates when |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

