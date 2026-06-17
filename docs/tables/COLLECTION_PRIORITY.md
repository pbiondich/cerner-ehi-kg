# COLLECTION_PRIORITY

> Stores all collection priorities (codeset 2054) and their attributes.

**Description:** Collection Priority  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDON_IND` | DOUBLE | NOT NULL |  | If the indicator is on for this collection priority makes an add-on order which will not generate a nurse task. |
| 2 | `AFTER_LAST_IND` | DOUBLE |  |  | An indicator that orders with this collection priority should print immediately when they are requested before midnight and after the cut-off time for the last collection schedule time. The collection schedule time is based on the patient location, the order's specimen type, the collection priority, and nurse-collect status. |
| 3 | `BEFORE_FIRST_IND` | DOUBLE |  |  | An indicator that orders with this collection priority should print immediately when they are requested after midnight and before the cut-off time for the first collection schedule time. The collection schedule time is based on the patient location, the order's specimen type, the collection priority, and nurse-collect status. |
| 4 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Collection Priority. |
| 5 | `COL_LIST_IND` | DOUBLE |  |  | Not currently in use. |
| 6 | `DEFAULT_REPORT_PRIORITY_CD` | DOUBLE | NOT NULL |  | Used by Powerchart orders to define the default reporting priority for orders placed with the given collection priority. |
| 7 | `DEFAULT_START_DT_TM` | VARCHAR(20) |  |  | Used by Powerchart orders as a default for the collection date/time for orders. |
| 8 | `GROUP_WITH_OTHER_FLAG` | DOUBLE |  |  | A flag indicating how orders with this collection priority should be grouped or netted with orders having different collection priorities. |
| 9 | `IMMEDIATE_PRINT_IND` | DOUBLE |  |  | An indicator that orders with this collection priority should always print labels immediately. |
| 10 | `LABEL_SEQUENCE` | DOUBLE |  |  | This field is used by label netting when several orders are netted to the same container. In this case, the netting procedure will look at the label sequence and the order with lower sequence will have priority. |
| 11 | `LOOK_AHEAD_MINUTES` | DOUBLE |  |  | Defines the window of time to look ahead to net orders. |
| 12 | `LOOK_BACK_MINUTES` | DOUBLE |  |  | Defines the window of time to look back to net orders. |
| 13 | `TIME_STUDY_IND` | DOUBLE |  |  | An indicator that this priority is a Time Study type of priority and future collection times will be specified at the time orders are requested. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

