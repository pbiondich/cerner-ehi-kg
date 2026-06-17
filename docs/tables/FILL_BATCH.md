# FILL_BATCH

> This table groups fill cycles together as a single job.

**Description:** Fill Batch  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALENDAR_DAY_NBR` | DOUBLE | NOT NULL |  | Indicates the specific calendar day which a Fill Batch is to start. |
| 2 | `CYCLE_TIME` | DOUBLE | NOT NULL |  | The length of time of the fill cycle for which orders will qualify to be dispensed. |
| 3 | `CYCLE_UNIT_FLAG` | DOUBLE | NOT NULL |  | This flag indicates what time measurement was used to specify the cycle_time. |
| 4 | `DEFAULT_PRINTER_CD` | DOUBLE | NOT NULL | FK→ | Optional default printer code |
| 5 | `DEF_OPERATION_FLAG` | DOUBLE |  |  | Defines whether the batch run is to be defaulted to a particular operation. This is NOT a state but rathera default value for the building of batches. |
| 6 | `DISCONTINUE_TIME` | DOUBLE |  |  | The length of time for which discontinued orders should continue to be shown on the fill after they havebeen discontinued. |
| 7 | `DISCONTINUE_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the discontinue_time. |
| 8 | `FILL_BATCH_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the parameters defined in this batch. |
| 9 | `FILL_TIME` | DOUBLE | NOT NULL |  | The length of time for which a supply of medication orders must be calculated and dispensed. |
| 10 | `FILL_UNIT_FLAG` | DOUBLE | NOT NULL |  | This flag indicates what time measurement was used to specify the fill_time. |
| 11 | `INCOMPLETE_ORDER_IND` | DOUBLE |  |  | Indicates whether incomplete orders are to be shown (supply calculated) on the fill. |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location of the alternate dispense from location. |
| 13 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Identifies the single facility location to which the Batch Report is related. |
| 14 | `MAX_CYCLE_TIME` | DOUBLE |  |  | The length of time that is the maximum for qualifying orders to be dispensed for this batch. |
| 15 | `MAX_CYCLE_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the max_cycle. |
| 16 | `MAX_FILL_TIME` | DOUBLE |  |  | The length of time that is the maximum for dispensing meds (calculating doses to be dispensed) for this batch. |
| 17 | `MAX_FILL_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the max_fill_time. |
| 18 | `MIN_ELAPSED_TIME` | DOUBLE |  |  | The length of time which must elapse before this batch is requested again. |
| 19 | `MIN_ELAPSED_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the min_elapsed_time. |
| 20 | `MONTHLY_DOW_FLAG` | DOUBLE | NOT NULL |  | Indicates specific Day of Week (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) a Fill Batch is to start. 0 = Sunday, 1, = Monday, etc. |
| 21 | `MONTHLY_WEEK_FLAG` | DOUBLE | NOT NULL |  | Indicates which week (1st, 2nd, 3rd, 4th) a Fill Batch is to start. |
| 22 | `ORDER_TYPE_FLAG` | DOUBLE |  |  | Determines whether orders in this batch are of type MED, LVP, IVPB etc. |
| 23 | `OUTPUT_FORMAT_CD` | DOUBLE | NOT NULL |  | Format_cd for the type of desired output (report, labels, etc.) |
| 24 | `PRN_FILL_TIME` | DOUBLE |  |  | The length of time for which PRN orders are to have a supply calculated. A value of 0 indicates that PRN orders should not be filled with this batch. |
| 25 | `PRN_FILL_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the prn_fill_time. |
| 26 | `SUSPEND_TIME` | DOUBLE |  |  | The length of time for which suspended orders should continue to be shown (supply calculated) on the fill after they have been suspended. |
| 27 | `SUSPEND_UNIT_FLAG` | DOUBLE |  |  | This flag indicates what time measurement was used to specify the suspend_time |
| 28 | `UNVERIFIED_ORDER_IND` | DOUBLE |  |  | Indicates whether unverified new orders are to be shown (supply calculated) on the fill. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFAULT_PRINTER_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |
| `FILL_BATCH_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

