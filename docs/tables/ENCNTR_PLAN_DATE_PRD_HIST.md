# ENCNTR_PLAN_DATE_PRD_HIST

> Contains historical records from the ENCNTR_PLAN_DATE_PERIOD table.

**Description:** Encounter Plan Date Period History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 6 | `DATE_PERIOD_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of date/time period for this row. |
| 7 | `ENCNTR_PLAN_DATE_PERIOD_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCNTR_PLAN_DATE_PERIOD table for which this history is maintained. |
| 8 | `ENCNTR_PLAN_DATE_PRD_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCNTR_PLAN_DATE_PRD_HIST table for which this history is maintained. |
| 9 | `FIRST_DATE` | DATETIME |  |  | The first date in the period. Although this is capable of storing the time component of a date, it should be ignored since date periods from an X12 transaction do not contain a time component. This date should be treated as an absolute date and the standard Millennium practice of utc/local time zone translations should not be applied when reading and writing. |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent table to which this data belongs. |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The uppercase name of the parent table to which this data belongs. |
| 12 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 13 | `SECOND_DATE` | DATETIME |  |  | The second date in the period. Although this is capable of storing the time component of a date, it should be ignored since date periods from an X12 transaction do not contain a time component. This date should be treated as an absolute date and the standard Millennium practice of utc/local time zone translations should not be applied when reading and writing. |
| 14 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PLAN_DATE_PERIOD_ID` | [ENCNTR_PLAN_DATE_PERIOD](ENCNTR_PLAN_DATE_PERIOD.md) | `ENCNTR_PLAN_DATE_PERIOD_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

