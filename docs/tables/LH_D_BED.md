# LH_D_BED

> Dimension table to hold BED Results for Infection Control Reports

**Description:** LH_D_BED  
**Table type:** REFERENCE  
**Primary key:** `D_BED_ID`, `HEALTH_SYSTEM_SOURCE_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BED_DESCRIPTION` | VARCHAR(50) |  |  | The description of the bed |
| 3 | `BED_DISPLAY` | VARCHAR(50) |  |  | The display value for the bed |
| 4 | `BED_MEANING` | VARCHAR(50) |  |  | The Cerner-identified meaning for the bed |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `D_BED_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_D_BED table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This filed should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data |
| 10 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | This field is the patient location with a location type of bed. Code set 220 |
| 11 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 15 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [LH_F_IC_MDRO_DTL_METRICS](LH_F_IC_MDRO_DTL_METRICS.md) | `D_COLL_BED_ID` |
| [LH_F_IC_MDRO_DTL_METRICS](LH_F_IC_MDRO_DTL_METRICS.md) | `D_COLL_PREV_BED_ID` |
| [LH_F_IC_MDRO_DTL_METRICS](LH_F_IC_MDRO_DTL_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

