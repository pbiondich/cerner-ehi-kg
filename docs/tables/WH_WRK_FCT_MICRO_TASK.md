# WH_WRK_FCT_MICRO_TASK

> This is a Health Sentry Work table for processing microbiology task

**Description:** WH_WRK_FCT_MICRO_TASK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIRST_OBSERVED_DT_TM` | DATETIME |  |  | FIRST_OBSERVED_DT_TM field |
| 2 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | HEALTH_SYSTEM_SOURCE_ID field |
| 3 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | LAST_PROCESS_DT_TM field |
| 4 | `MICRO_ORDER_KEY` | DOUBLE |  |  | MICRO_ORDER_KEY field |
| 5 | `MICRO_TASK_KEY` | DOUBLE |  |  | MICRO_TASK_KEY field |
| 6 | `MICRO_TASK_SK` | VARCHAR(100) |  |  | MICRO_TASK_SK field |
| 7 | `MOST_RECENT_TASK_IND` | DOUBLE |  |  | MOST_RECENT_TASK_IND field |
| 8 | `OBSERVED_DT_TM` | DATETIME |  |  | OBSERVED_DT_TM field |
| 9 | `OBSERVED_TM_ZN` | DOUBLE |  |  | OBSERVED_TM_ZN field |
| 10 | `ORGANISM_REF` | VARCHAR(40) |  |  | ORGANISM_REF field |
| 11 | `PARTITION_DT_TM` | DATETIME |  |  | PARTITION_DT_TM field |
| 12 | `REPORT_TYPE_REF` | VARCHAR(40) |  |  | REPORT_TYPE_REF field |
| 13 | `SOURCE_FLG` | DOUBLE |  |  | The HIS system or interface being used to send us the data extract. 0 = Unknown; 1 = Classic; 2 = MSMeds; 3 = HNAM; 4 = HL7; 5 = Foreign System; 6 = CoPath; 7 = Critical Outcomes - Apache; 8 = Critical Outcomes - Project Impact; 9 = Critical Outcomes - Web; 10 = Critical Outcomes - HNAM; 11 = PI Third Party XML File; 12 = Shell Record; 13 = PI Defined Record; 14 = Healthe Analytics |
| 14 | `TASK_REF` | VARCHAR(40) |  |  | TASK_REF field |
| 15 | `TASK_SEQ` | DOUBLE |  |  | TASK_SEQ field |
| 16 | `TASK_TYPE_FLG` | DOUBLE |  |  | TASK_TYPE_FLG field |
| 17 | `VERIFIED_DT_TM` | DATETIME |  |  | VERIFIED_DT_TM field |
| 18 | `VERIFIED_PRSNL` | VARCHAR(40) |  |  | VERIFIED_PRSNL field |
| 19 | `VERIFIED_TM_ZN` | DOUBLE |  |  | VERIFIED_TM_ZN field |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

