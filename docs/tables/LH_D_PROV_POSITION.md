# LH_D_PROV_POSITION

> Dimension table for Lighthouse report

**Description:** LH_D_PROV_POSITION  
**Table type:** REFERENCE  
**Primary key:** `D_PROV_POSITION_ID`, `HEALTH_SYSTEM_SOURCE_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | Identifies whether this record is active or has been logically deleted. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time on which the record became effective; defaults to 1/01/1800. |
| 3 | `D_PROV_POSITION_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the provider position. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time on which the record is no longer effective; defaults to 12/31/2100. |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The maximum extraction end date/time of the reporting period |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 7 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 8 | `PROV_POSITION_CD` | DOUBLE | NOT NULL |  | Source identifier for the provider position |
| 9 | `PROV_POSITION_DESCRIPTION` | VARCHAR(60) |  |  | The description for the provider position |
| 10 | `PROV_POSITION_DISPLAY` | VARCHAR(40) |  |  | The display value for the provider position |
| 11 | `PROV_POSITION_MEANING` | VARCHAR(40) |  |  | The Cerner-defined meaning for the provider position |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date/time the row was last inserted or updated. |
| 14 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 15 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The application responsible for updating the record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_F_HH_METRICS](LH_F_HH_METRICS.md) | `D_PROV_POSITION_ID` |
| [LH_F_HH_METRICS](LH_F_HH_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

