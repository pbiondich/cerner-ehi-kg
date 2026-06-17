# LH_D_GROUP

> Reference table to store reporting groupings for Lighthouse.

**Description:** LH_D_GROUP  
**Table type:** REFERENCE  
**Primary key:** `D_GROUP_ID`, `HEALTH_SYSTEM_SOURCE_ID`  
**Columns:** 18  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `D_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the lighthouse reporting groupings |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 6 | `GROUP_DESCRIPTION` | VARCHAR(255) |  |  | The description of the group member. |
| 7 | `GROUP_DISPLAY` | VARCHAR(255) |  |  | The display value for the group member. |
| 8 | `GROUP_MEANING` | VARCHAR(255) |  |  | The Cerner-defined meaning for the group member. |
| 9 | `GROUP_TYPE_DESCRIPTION` | VARCHAR(255) |  |  | The description of the group category. |
| 10 | `GROUP_TYPE_DISPLAY` | VARCHAR(255) |  |  | The display value for the group category. |
| 11 | `GROUP_TYPE_MEANING` | VARCHAR(50) |  |  | The Cerner-defined meaning for the group category. |
| 12 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 14 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 18 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [LH_ABS_SCIP_METRICS](LH_ABS_SCIP_METRICS.md) | `D_PROC_GROUP_ID` |
| [LH_ABS_SCIP_METRICS](LH_ABS_SCIP_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_F_SCIP_METRICS](LH_F_SCIP_METRICS.md) | `D_PROC_GROUP_ID` |
| [LH_F_SCIP_METRICS](LH_F_SCIP_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

