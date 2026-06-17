# PHA_BATCH_REPORT

> Parameters for PharmNet reports

**Description:** Parameters for PharmNet PMP, MAR, Fill List reports  
**Table type:** REFERENCE  
**Primary key:** `BATCH_REPORT_CD`  
**Columns:** 32  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_REPORT_CD` | DOUBLE | NOT NULL | PK | Primary key |
| 2 | `BATCH_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of report to be run (fill list, pmp, mar etc.) |
| 3 | `CLIN_REVIEW_IND` | DOUBLE | NOT NULL |  | Indicator that determines if orders not needing clinical review should qualify on reports. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The creator of the report. |
| 5 | `DC_DISPLAY` | DOUBLE |  |  | Indicates whether discontinued orders should display on the report. 1 = true, 0 = false |
| 6 | `DC_DISPLAY_UNITS_CD` | DOUBLE | NOT NULL |  | Unit of measure for dc_display |
| 7 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Identifies the single facility location to which the Batch Report is related. |
| 8 | `ORD_TYPE_CONT_IND` | DOUBLE |  |  | Display/print continuous orders on this report |
| 9 | `ORD_TYPE_DC_IND` | DOUBLE |  |  | Display discontinued orders on the report |
| 10 | `ORD_TYPE_INT_IND` | DOUBLE |  |  | Display intermittent IV orders on the report |
| 11 | `ORD_TYPE_MED_IND` | DOUBLE |  |  | Display medication orders on the report |
| 12 | `ORD_TYPE_SUSP_IND` | DOUBLE |  |  | Display suspended orders on the report |
| 13 | `ORD_TYPE_UNVER_IND` | DOUBLE |  |  | Display unverified orders on the report |
| 14 | `OUTPUT_DEVICE_CD` | DOUBLE | NOT NULL |  | Output Deivce (printer) report should be printed to. |
| 15 | `OUTPUT_FORMAT_CD` | DOUBLE | NOT NULL |  | Output format associated with this report |
| 16 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy type code (Inpat vs. Retail vs Longterm etc.) |
| 17 | `POP_SELECT_FLAG` | DOUBLE |  |  | Flag to determine if report is run for single patient or nursing station |
| 18 | `PREQUAL_SCRIPT_CD` | DOUBLE | NOT NULL |  | Script to extract data specific to type of report. This script is NOT customizable by client or project personnel, and calls the script defined by the output_format_cd |
| 19 | `REPORT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of report this record represents. |
| 20 | `START_DAY` | DOUBLE |  |  | Flag to determine when report should start. Value is applied to curdate to determine start date. Valid values are (-1, 0, 1). |
| 21 | `START_TIME` | DOUBLE |  |  | Start time of the report. Stored as a number of minutes i.e. 720 = 12 noon. |
| 22 | `STOP_TYPE_HARD_IND` | DOUBLE |  |  | Display orders with hard stops |
| 23 | `STOP_TYPE_PHYS_IND` | DOUBLE |  |  | Display orders with physician defined stop dates |
| 24 | `STOP_TYPE_SOFT_IND` | DOUBLE |  |  | Display orders with soft (undefined) stops |
| 25 | `TIME_PERIOD` | DOUBLE |  |  | Time interval to qualify data for. i.e. 24 hours, 30 minutes, 3 days etc. |
| 26 | `TIME_PERIOD_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure to apply to time_period. Ie1439 minutes, 24 hours etc. |
| 27 | `TIME_RANGE_CD` | DOUBLE | NOT NULL |  | Identifies what type of time range to qualify data on i.e. Stop Dates, administration dates, Start Dates, DC dates |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PHA_BATCH_REPORT_ACT](PHA_BATCH_REPORT_ACT.md) | `BATCH_REPORT_CD` |

