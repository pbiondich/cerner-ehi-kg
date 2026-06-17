# FILL_BATCH_HX

> Table to store the history of each fill batch processing and the batch parameters.

**Description:** fill_batch_hx  
**Table type:** ACTIVITY  
**Primary key:** `FILL_HX_ID`  
**Columns:** 47  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALENDAR_DAY_NBR` | DOUBLE | NOT NULL |  | Indicates the specific calendar day which a Fill Batch is to start. |
| 2 | `CYCLE_TIME` | DOUBLE |  |  | The length of time of the fill cycle for which orders qualified to be dispensed. |
| 3 | `CYCLE_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the cycle_time. |
| 4 | `DEF_OPERATION_FLAG` | DOUBLE |  |  | Defines whether the batch run is to be defaulted to a particular operation. This is NOT a state but rathera default value for the building of batches. |
| 5 | `DISCONTINUE_TIME` | DOUBLE |  |  | The length of time for which discontinued orders should continue to be shown on the fill after they havebeen discontinued. |
| 6 | `DISCONTINUE_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the discontinue_time. |
| 7 | `DIS_DT_TM` | DATETIME |  |  | Date/time that dispensingtables were updated |
| 8 | `END_DT_TM` | DATETIME |  |  | Date/time processing completed |
| 9 | `FILL_AUDIT_FLAG` | DOUBLE |  |  | Set when the batch is completely processed, since the record is created at the beginning of the batch run. |
| 10 | `FILL_BATCH_CD` | DOUBLE | NOT NULL |  | code value for the fill batch |
| 11 | `FILL_DT_TM` | DATETIME |  |  | Date/time data was written to fill_print_Ord_hx table |
| 12 | `FILL_HX_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the parameters defined in this fill run. |
| 13 | `FILL_TIME` | DOUBLE |  |  | The length of time for which a supply of medication orders must be calculated and dispensed. |
| 14 | `FILL_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the fill_time |
| 15 | `FROM_DT_TM` | DATETIME |  |  | Starting date/time used to qualify meds. Doses must be due after/equal to from _dt_tm |
| 16 | `FROM_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 17 | `INCOMPLETE_ORDER_IND` | DOUBLE |  |  | Indicates whether incomplete orders were shown (supply calculated) on the fill. |
| 18 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location of the alternate dispense from location. |
| 19 | `MAX_CYCLE_TIME` | DOUBLE |  |  | The length of time that is the maximum for qualifying orders to be dispensed for this batch. |
| 20 | `MAX_CYCLE_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the max_cycle. |
| 21 | `MAX_FILL_TIME` | DOUBLE |  |  | The length of time that is the maximum for dispensing meds (calculating doses to be dispensed) for this batch. |
| 22 | `MAX_FILL_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the max_fill_time. |
| 23 | `MIN_ELAPSED_TIME` | DOUBLE |  |  | The length of time which must elapse before this batch is requested again. |
| 24 | `MIN_ELAPSED_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the min_elapsed_time. |
| 25 | `MONTHLY_DOW_FLAG` | DOUBLE | NOT NULL |  | Indicates specific Day of Week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) a Fill Batch is to start. |
| 26 | `MONTHLY_WEEK_FLAG` | DOUBLE | NOT NULL |  | Indicates which week (1st, 2nd, 3rd, 4th) a Fill Batch is to start. |
| 27 | `ORDER_COUNT` | DOUBLE |  |  | Number of orders identifiedas qualifying for fill list |
| 28 | `OUTPUT_DEVICE_CD` | DOUBLE | NOT NULL |  | code value for desired output device |
| 29 | `OUTPUT_DEVICE_S` | CHAR(50) |  |  | text description for output device |
| 30 | `OUTPUT_FORMAT_CD` | DOUBLE | NOT NULL |  | code value for desired outputformat |
| 31 | `PRINT_DT_TM` | DATETIME |  |  | Date/time script to print data was called |
| 32 | `PRN_FILL_TIME` | DOUBLE |  |  | The length of time for which PRN orders are to have a supply calculated. A value of 0 indicates that PRN orders should not be filled with this batch. |
| 33 | `PRN_FILL_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the prn_fill_time. |
| 34 | `RUN_USER_ID` | DOUBLE | NOT NULL |  | identifier for user who performed this operation |
| 35 | `RUN_USER_S` | CHAR(50) |  |  | Name of the run user |
| 36 | `START_DT_TM` | DATETIME |  |  | Date/time processing of fill list started. Used for audit purposes |
| 37 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 38 | `SUSPEND_TIME` | DOUBLE |  |  | The length of time for which suspended orders should continue to be shown (supply calculated) on the fill after they have been suspended. |
| 39 | `SUSPEND_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the suspend_time |
| 40 | `TO_DT_TM` | DATETIME |  |  | Ending time to qualify meds. Orders must have doses due prior/equal to this date/time |
| 41 | `TO_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 42 | `UNVERIFIED_ORDER_IND` | DOUBLE |  |  | Indicates whether unverified new orders were shown (supply calculated) on the fill. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DISPENSE_HX](DISPENSE_HX.md) | `FILL_HX_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `LAST_FILL_HX_ID` |

