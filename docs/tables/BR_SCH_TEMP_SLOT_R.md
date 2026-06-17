# BR_SCH_TEMP_SLOT_R

> Stores the various slot types from the default schedule data collection spreadsheet associated with each default schedule in the spreadsheet.

**Description:** BR_SCH_TEMP_SLOT_R  
**Table type:** REFERENCE  
**Primary key:** `BR_SCH_TEMP_SLOT_R_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** Identifies which bedrock client data belongs to |
| 2 | `BR_SCH_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the template that the slot belongs to. |
| 3 | `BR_SCH_TEMP_SLOT_R_ID` | DOUBLE | NOT NULL | PK | The primary index & unique identifier for rows on this table. |
| 4 | `INTERVAL` | DOUBLE |  |  | actual text the user enters as the slot interval on the import |
| 5 | `INTERVAL_STR` | VARCHAR(40) |  |  | user-defined input converted to an integer |
| 6 | `SLOT_END` | DOUBLE | NOT NULL |  | The time of day that the slot ends in numeric format (i.e. 1000) |
| 7 | `SLOT_END_STR` | VARCHAR(40) |  |  | The actual end time from the data collection spreadsheet. Stored in string format in case an invalid entry is made (audit purposes). |
| 8 | `SLOT_NAME` | VARCHAR(100) | NOT NULL |  | The name of the slot from the data collection worksheet. |
| 9 | `SLOT_RELEASE_HRS` | DOUBLE | NOT NULL |  | The number of hours ahead of the slot_start that the slot should be release if not scheduled. |
| 10 | `SLOT_RELEASE_TO` | VARCHAR(100) | NOT NULL |  | If release data is associated with this slot, this will be the name of another slot that this slot could be released to. Comes from the data collection spreadsheet. |
| 11 | `SLOT_RELEASE_TO_ID` | DOUBLE | NOT NULL |  | If the slot_release_to contained a valid slot name, this will be the ID associated with that slot name. |
| 12 | `SLOT_START` | DOUBLE | NOT NULL |  | The time of day that the slot begins in numeric format (i.e. 0900) |
| 13 | `SLOT_START_STR` | VARCHAR(40) |  |  | The actual start time from the data collection spreadsheet. Stored in string format in case an invalid entry is made (audit purposes). |
| 14 | `SLOT_STATUS_FLAG` | DOUBLE | NOT NULL |  | Future use. |
| 15 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL |  | If the slot_name from the data collection spreadsheet is valid, and it should be, this will hold the id of the slot from the sch_slot_type table. |
| 16 | `TIME_BLOCK` | DOUBLE |  |  | A numeric representation of the time block that the slot belongs to |
| 17 | `TIME_BLOCK_STR` | VARCHAR(40) | NOT NULL |  | Used to store the time block value in string format. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_SCH_TEMPLATE_ID` | [BR_SCH_TEMPLATE](BR_SCH_TEMPLATE.md) | `BR_SCH_TEMPLATE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_SCH_TEMP_SLOT_RELEASE_R](BR_SCH_TEMP_SLOT_RELEASE_R.md) | `BR_SCH_TEMP_SLOT_R_ID` |

