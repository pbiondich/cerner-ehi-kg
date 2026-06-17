# TRACKING_LOC_STATUS

> Table used to store status information associated with a tracking item to be displayed on the Tracking Locator Board.

**Description:** Tracking Location Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_STATUS_DT_TM` | DATETIME |  |  | Doctor Status Date and TimeColumn |
| 2 | `DOC_STATUS_EVT_ID` | DOUBLE | NOT NULL |  | Doctor Status Event IdentifierColumn |
| 3 | `LAB_STATUS_DT_TM` | DATETIME |  |  | Lab Status Date and TimeColumn |
| 4 | `LAB_STATUS_EVT_ID` | DOUBLE | NOT NULL |  | Lab Status Event IdentifierColumn |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location CodeColumn |
| 6 | `LOC_STATUS_EVT_DT_TM` | DATETIME |  |  | Location Status Event Date and TimeColumn |
| 7 | `LOC_STATUS_EVT_ID` | DOUBLE | NOT NULL |  | Location Status Event IdentifierColumn |
| 8 | `LOC_STATUS_ITEM_ID` | DOUBLE | NOT NULL |  | Location Status Tracking ItemColumn |
| 9 | `NURSE_STATUS_DT_TM` | DATETIME |  |  | Nursing Status Date and TimeColumn |
| 10 | `NURSE_STATUS_EVT_ID` | DOUBLE | NOT NULL |  | Nursing Status Event IdentifierColumn |
| 11 | `TRACKING_LOC_STATUS_ID` | DOUBLE | NOT NULL |  | Tracking Location Status IdentifierColumn |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `URGENT_DT_TM` | DATETIME |  |  | Urgent Date and TimeColumn |
| 18 | `URGENT_IND` | DOUBLE |  |  | Urgent IndicatorColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

