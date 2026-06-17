# FILL_PRINT_HX

> Header information for pharmacy ouput prior to printing

**Description:** fill_print_hx  
**Table type:** ACTIVITY  
**Primary key:** `RUN_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_DESCRIPTION` | VARCHAR(50) |  |  | The user-viewed description identifying the parameters defined in this batch. |
| 2 | `BATCH_REPORT_CD` | DOUBLE | NOT NULL |  | Batch Report Cd |
| 3 | `BAT_FILL_TIME` | DOUBLE |  |  | The length of time for which a supply of medication orders must be calculated and dispensed. |
| 4 | `CYC_FROM_DT_TM` | DATETIME |  |  | The beginning date and time of the fill cycle. |
| 5 | `CYC_FROM_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 6 | `CYC_TO_DT_TM` | DATETIME |  |  | The ending date and time of the fill cycle. |
| 7 | `CYC_TO_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 8 | `FILL_BATCH_CD` | DOUBLE | NOT NULL |  | Unique identifier for a fill batch |
| 9 | `FILL_HX_ID` | DOUBLE | NOT NULL |  | The unique identifier for the parameters defined in a batch run. |
| 10 | `OUTPUT_DEVICE_CD` | DOUBLE | NOT NULL |  | Print device code batch was sent to. |
| 11 | `OUTPUT_DEVICE_S` | CHAR(50) |  |  | Print device name batch was sent to. |
| 12 | `OUTPUT_FORMAT_CD` | DOUBLE | NOT NULL |  | The setting for desired output type |
| 13 | `RERUN_FLAG` | DOUBLE |  |  | Indicates whether this operation was a rerun or not |
| 14 | `RUN_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the parameters defined in this print run. |
| 15 | `RUN_TYPE_CD` | DOUBLE | NOT NULL |  | Program run code (label, cartfill, MAR, ASO?) |
| 16 | `RUN_USER_ID` | DOUBLE | NOT NULL |  | User ID of person running this. |
| 17 | `S_BAT_FILL_TIME_UNIT` | CHAR(10) |  |  | The time measurement unit used to specify the fill_time. |
| 18 | `S_OPERATION` | CHAR(12) |  |  | The operation requested for the cycles in this batch. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `RUN_ID` |

