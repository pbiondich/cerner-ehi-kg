# BR_SCH_TEMPLATE

> This table is the primary table for storing imported default schedule information from the data collection worksheet. We'll store info from the worksheet in this working table where the wizard will read each template in & let the user of the wizard validate the data & turn it into the Millennium equivalent

**Description:** Bedrock Scheduling Template  
**Table type:** REFERENCE  
**Primary key:** `BR_SCH_TEMPLATE_ID`  
**Columns:** 39  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLY_BEG_DT_TM` | DATETIME |  |  | Future Use. |
| 2 | `APPLY_BEG_DT_TM_STRING` | VARCHAR(40) |  |  | Future Use. |
| 3 | `APPLY_END_DT_TM` | DATETIME |  |  | Future Use. |
| 4 | `APPLY_END_DT_TM_STRING` | VARCHAR(40) |  |  | Future Use. |
| 5 | `APPLY_OCCURRENCES_STR` | VARCHAR(5) | NOT NULL |  | The number of times that this template should be applied. |
| 6 | `APPLY_RANGE` | DOUBLE |  |  | apply range column |
| 7 | `APPLY_RANGE_STR` | VARCHAR(40) |  |  | apply range string column |
| 8 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** Identifies which bedrock client data belongs to |
| 9 | `BR_SCH_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | The primary index and unique identifier for this table. |
| 10 | `DAYBEGIN` | DOUBLE | NOT NULL |  | The numeric value of the time of day the day begins for this template. (0900). |
| 11 | `DAYBEGIN_STR` | VARCHAR(40) |  |  | The string display value of the time of day the day begins for this template. Stored as a string in case a non-numeric character was entered by accident & the day begin time couldn't be defaulted. |
| 12 | `DAYEND` | DOUBLE | NOT NULL |  | The numeric value of the time of day the day ends for this template (1700). |
| 13 | `DAYEND_STR` | VARCHAR(40) |  |  | The string display value of the time of day the day ends for this template. Stored as a string in case a non-numeric character was entered by accident & the day end time couldn't be defaulted. |
| 14 | `DAYOFWEEK` | VARCHAR(10) |  |  | A string showing which days of the week this template will be applied. For example, "MWF" or "M". Valid values are Sun-Sat are UMTWHFS. |
| 15 | `DEF_SCHED_ID` | DOUBLE | NOT NULL |  | Once resolved, the default schedule ID that was generated is stamped here. |
| 16 | `IMPORT_NAME` | VARCHAR(100) | NOT NULL |  | If more than one set of data will be imported, this column can be used to identify each set. Typically, it'll be a formatted date, but it can be anything and is a column in the data collection spreadsheet. |
| 17 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 18 | `MONTH_OPT1_DATESOFMONTH` | VARCHAR(100) | NOT NULL |  | For the monthly application option 1, this string field stores the dates of the month that this template should be applied. |
| 19 | `MONTH_OPT1_NBROFMONTHS` | VARCHAR(5) | NOT NULL |  | For the monthly application option 1, this string field stores the number of months that this template should be applied. |
| 20 | `MONTH_OPT2_DAYSOFWEEK` | VARCHAR(10) | NOT NULL |  | For the monthly application option 2, this string field stores the days of the week that this template should be applied. |
| 21 | `MONTH_OPT2_NBROFMONTHS` | VARCHAR(5) | NOT NULL |  | For the monthly application option 2, this string field stores the number of months that this template should be applied. |
| 22 | `MONTH_OPT2_WEEKSOFMONTH` | VARCHAR(10) | NOT NULL |  | For the monthly application option 2, this string field stores the weeks of the month that this template should be applied. |
| 23 | `NEW_FORMAT_IND` | DOUBLE | NOT NULL |  | The number of times that this template should be applied. |
| 24 | `TEMPLATE_NAME` | VARCHAR(100) | NOT NULL |  | The name of the default schedule template. |
| 25 | `TEMPLATE_STATUS_FLAG` | DOUBLE | NOT NULL |  | Stores the status of the template. Zero is the default and means unresolved. Anything greater than zero means its been either resolved or deleted. |
| 26 | `UK_DATE_FORMAT_STR` | VARCHAR(5) | NOT NULL |  | This string field stores the reply to the UK date format field. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `WEEKOFMONTH` | VARCHAR(10) |  |  | A string showing the weeks of the month that this template will be applied. Every week is "12345". Every other week is "135". Only the first week is "1". Etc. |
| 33 | `WEEK_OPT_DAYSOFWEEK` | VARCHAR(10) | NOT NULL |  | For the weekly application option, this string field stores the days of week that this template should be applied. |
| 34 | `WEEK_OPT_NBROFWEEKS` | VARCHAR(5) | NOT NULL |  | For the weekly application option, this string field stores the number of weeks that this template should be applied. |
| 35 | `YEAR_OPT1_DATESOFMONTH` | VARCHAR(100) | NOT NULL |  | For the yearly application option 1, this string field stores the dates of the month that this template should be applied. |
| 36 | `YEAR_OPT1_MONTHSOFYEAR` | VARCHAR(50) | NOT NULL |  | For the yearly application option 1, this string field stores the months of the year that this template should be applied. |
| 37 | `YEAR_OPT2_DAYSOFWEEK` | VARCHAR(10) | NOT NULL |  | For the yearly application option 2, this string field stores the days of week that this template should be applied. |
| 38 | `YEAR_OPT2_MONTHSOFYEAR` | VARCHAR(50) | NOT NULL |  | For the yearly application option 2, this string field stores the months of the year that this template should be applied. |
| 39 | `YEAR_OPT2_WEEKSOFMONTH` | VARCHAR(10) | NOT NULL |  | For the yearly application option 2, this string field stores the weeks of the month that this template should be applied. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BR_SCH_TEMP_RES_R](BR_SCH_TEMP_RES_R.md) | `BR_SCH_TEMPLATE_ID` |
| [BR_SCH_TEMP_SLOT_R](BR_SCH_TEMP_SLOT_R.md) | `BR_SCH_TEMPLATE_ID` |

