# LH_D_SOURCE

> Dimension table to hold SOURCE Results for Infection Control Reports

**Description:** LH_D_SOURCE  
**Table type:** REFERENCE  
**Primary key:** `D_SOURCE_ID`, `HEALTH_SYSTEM_SOURCE_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The data and Time for which this table row becomes effective. Normally, this will be the data and time the row is added, but could be a past or future date and time |
| 3 | `D_SOURCE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_D_SOURCE table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be value with the date that the row became inactive |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This filed should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data |
| 7 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record wad first loaded into the table. |
| 8 | `SOURCE_CD` | DOUBLE | NOT NULL |  | The location of the source. CODE SET 2052 |
| 9 | `SOURCE_DESCRIPTION` | VARCHAR(50) |  |  | The description of the source |
| 10 | `SOURCE_DISPLAY` | VARCHAR(50) |  |  | The display value for the source |
| 11 | `SOURCE_MEANING` | VARCHAR(50) |  |  | The Cerner-identified meaning for the source |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 15 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [LH_F_IC_ANTIBGRM_METRICS](LH_F_IC_ANTIBGRM_METRICS.md) | `D_SOURCE_ID` |
| [LH_F_IC_ANTIBGRM_METRICS](LH_F_IC_ANTIBGRM_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_IC_MDRO_DTL_METRICS](LH_F_IC_MDRO_DTL_METRICS.md) | `D_SOURCE_ID` |
| [LH_F_IC_MDRO_DTL_METRICS](LH_F_IC_MDRO_DTL_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

