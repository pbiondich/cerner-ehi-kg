# RC_D_CENSUS_EVENT

> This table contains the information about the census events that can occur throughtout a day.

**Description:** Revenue Cycle Dimension Census Event  
**Table type:** REFERENCE  
**Primary key:** `RC_D_CENSUS_EVENT_ID`  
**Columns:** 13  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CENSUS_EVENT` | VARCHAR(50) | NOT NULL |  | Contains the type of event that can occur for census data. |
| 4 | `CENSUS_EVENT_KEY` | VARCHAR(50) | NOT NULL |  | Contains the key value for the census event. The column contains all caps with no spaces or special characters. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 8 | `RC_D_CENSUS_EVENT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies information about census events that can occur throughout a day. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RC_F_DAILY_CENSUS](RC_F_DAILY_CENSUS.md) | `RC_D_CENSUS_EVENT_ID` |
| [RC_F_DAILY_CENSUS_SMRY](RC_F_DAILY_CENSUS_SMRY.md) | `RC_D_CENSUS_EVENT_ID` |
| [RC_F_MONTHLY_CENSUS_SMRY](RC_F_MONTHLY_CENSUS_SMRY.md) | `RC_D_CENSUS_EVENT_ID` |

