# ENCNTR_CLASSIFICTN_HIST

> Used for tracking history changes to ENCNTR_CLASSIFICATION rows

**Description:** Encounter Classification History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 6 | `CLASSIFICATION1_CD` | DOUBLE | NOT NULL |  | Indicates a categorization of patients having a set of shared qualities or characteristics. |
| 7 | `CLASSIFICATION2_CD` | DOUBLE | NOT NULL |  | Indicates a categorization of patients having a set of shared qualities or characteristics. This code set may be configured via code value grouping to be hierarchically below patient classification 1 if desired by the client. |
| 8 | `CLASSIFICATION3_CD` | DOUBLE | NOT NULL |  | Indicates a categorization of patients having a set of shared qualities or characteristics. This code set may be configured via code value grouping to be hierarchically below patient classification 2 if desired by the client |
| 9 | `CLASSIFICATION4_CD` | DOUBLE | NOT NULL |  | Indicates a categorization of patients having a set of shared qualities or characteristics. This code set may be configured via code value grouping to be hierarchically below patient classification 3 if desired by the client |
| 10 | `ENCNTR_CLASSIFICATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 11 | `ENCNTR_CLASSIFICTN_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCNTR_CLASSIFICTN_HIST table. |
| 12 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 13 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_CLASSIFICATION_ID` | [ENCNTR_CLASSIFICATION](ENCNTR_CLASSIFICATION.md) | `ENCNTR_CLASSIFICATION_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

