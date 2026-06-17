# PHA_BATCH_REPORT_ACT

> Track the history of Batch Claims runs.

**Description:** Pharmacy Batch Report Activity  
**Table type:** ACTIVITY  
**Primary key:** `PHA_BATCH_REPORT_ACT_ID`  
**Columns:** 26  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_REPORT_CD` | DOUBLE | NOT NULL | FK→ | The batch report that generated this activity. |
| 2 | `BATCH_TYPE_CD` | DOUBLE |  |  | Type of report |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter for which the batch has been run. |
| 4 | `EXECUTION_END_DT_TM` | DATETIME |  |  | The time that this particular execution ended. |
| 5 | `EXECUTION_START_DT_TM` | DATETIME | NOT NULL |  | The time that this execution began. |
| 6 | `EXECUTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate if it was executed as part of ops job or manually executed |
| 7 | `ORD_TYPE_CONT_IND` | DOUBLE | NOT NULL |  | Display/print continuous orders on this report. |
| 8 | `ORD_TYPE_INT_IND` | DOUBLE | NOT NULL |  | Display intermittent IV orders on the report. |
| 9 | `ORD_TYPE_MED_IND` | DOUBLE | NOT NULL |  | Display medication orders on the report. |
| 10 | `OUTPUT_DEVICE_CD` | DOUBLE | NOT NULL |  | Output Deivce (printer) where the report was printedo. |
| 11 | `OUTPUT_FORMAT_CD` | DOUBLE | NOT NULL |  | Output format associated with this report |
| 12 | `PHA_BATCH_REPORT_ACT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the PHA_BATCH_REPORT_ACT table. |
| 13 | `REPORT_FROM_DT_TM` | DATETIME |  |  | The begin date of this report. |
| 14 | `REPORT_FROM_TZ` | DOUBLE | NOT NULL |  | The time zone associated to the report_from_dt_tm column. |
| 15 | `REPORT_TO_DT_TM` | DATETIME |  |  | The end date/time of this report run. |
| 16 | `REPORT_TO_TZ` | DOUBLE | NOT NULL |  | The time zone associated to the report_to_dt_tm column. |
| 17 | `RUNS_TO_PRINT_FLAG` | DOUBLE | NOT NULL |  | Indicates which runs will be part of the report that is printed once the batch is complete. |
| 18 | `RUN_USER_ID` | DOUBLE | NOT NULL | FK→ | This is the user that ran the batch |
| 19 | `RX_WORKSTATION_CD` | DOUBLE | NOT NULL |  | The workstation that batch was executed from. |
| 20 | `STATUSES_TO_PRINT_FLAG` | DOUBLE | NOT NULL |  | Indicates which records, based on the process status of the records, will be part of the report that is printed once batch is complete. |
| 21 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status of Inpatient to Outpatient Link |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_REPORT_CD` | [PHA_BATCH_REPORT](PHA_BATCH_REPORT.md) | `BATCH_REPORT_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `RUN_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PHA_BATCH_REPORT_ACT_DTL](PHA_BATCH_REPORT_ACT_DTL.md) | `PHA_BATCH_REPORT_ACT_ID` |
| [RXS_PHA_REPORT_FILTER_HIST](RXS_PHA_REPORT_FILTER_HIST.md) | `PHA_BATCH_REPORT_ACT_ID` |

