# WH_WRK_FCT_MICRO_RESPONSE

> This is a Health Sentry Work table for processing microbiology response

**Description:** WH_WRK_FCT_MICRO_RESPONSE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | ABNORMAL_IND field |
| 2 | `FALSE_POSITIVE_IND` | DOUBLE |  |  | FALSE_POSITIVE_IND field |
| 3 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | HEALTH_SYSTEM_SOURCE_ID field |
| 4 | `MICRO_REPORT_RESPONSE_KEY` | DOUBLE |  |  | MICRO_REPORT_RESPONSE_KEY field |
| 5 | `MICRO_RESPONSE_SEQUENCE` | DOUBLE |  |  | MICRO_RESPONSE_SEQUENCE field |
| 6 | `MICRO_TASK_KEY` | DOUBLE |  |  | MICRO_TASK_KEY field |
| 7 | `ORGANISM_REF` | VARCHAR(40) |  |  | ORGANISM_REF field |
| 8 | `ORG_TASK_LOG_SK` | VARCHAR(100) |  |  | ORG_TASK_LOG_SK field |
| 9 | `POSITIVE_IND` | DOUBLE |  |  | POSITIVE_IND field |
| 10 | `REPONSE_REF` | VARCHAR(40) |  |  | REPONSE_REF field |
| 11 | `RESPONSE_CLASS_FLG` | DOUBLE |  |  | RESPONSE_CLASS_FLG field |
| 12 | `RESPONSE_TEXT` | VARCHAR(255) |  |  | RESPONSE_TEXT field |
| 13 | `SOURCE_FLG` | DOUBLE |  |  | The HIS system or interface being used to send us the data extract. 0 = Unknown; 1 = Classic; 2 = MSMeds; 3 = HNAM; 4 = HL7; 5 = Foreign System; 6 = CoPath; 7 = Critical Outcomes - Apache; 8 = Critical Outcomes - Project Impact; 9 = Critical Outcomes - Web; 10 = Critical Outcomes - HNAM; 11 = PI Third Party XML File; 12 = Shell Record; 13 = PI Defined Record; 14 = Healthe Analytics |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

