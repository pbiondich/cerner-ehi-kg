# WH_WRK_FCT_CE_SUS

> This is a Health Sentry Work table for processing clinical events for susceptibilty

**Description:** WH_WRK_FCT_CE_SUS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_FLG` | DOUBLE |  |  | Flag to identify abnormal results. 0 = Normal; 1 = Abnormal |
| 2 | `ACCESSION` | VARCHAR(100) |  |  | ACCESSION field |
| 3 | `ALPHA_NUMERIC_RESULT_REF` | VARCHAR(40) |  |  | ALPHA_NUMERIC_RESULT_REF field |
| 4 | `ANTIBIOTIC_MEDICATION_REF` | VARCHAR(40) |  |  | ANTIBIOTIC_MEDICATION_REF field |
| 5 | `DETAIL_TEST_TYPE_REF` | VARCHAR(40) |  |  | DETAIL_TEST_TYPE_REF field |
| 6 | `DISCH_DT_TM` | DATETIME |  |  | DISCH_DT_TM field |
| 7 | `EVENT_SK` | VARCHAR(100) |  |  | EVENT_SK field |
| 8 | `FIRST_CTNR_COLL_METHOD_REF` | VARCHAR(40) |  |  | FIRST_CTNR_COLL_METHOD_REF field |
| 9 | `FIRST_SPECIMEN_SITE_REF` | VARCHAR(40) |  |  | FIRST_SPECIMEN_SITE_REF field |
| 10 | `FIRST_SPECIMEN_TYPE_REF` | VARCHAR(40) |  |  | FIRST_SPECIMEN_TYPE_REF field |
| 11 | `FRST_PERF_SVC_RES_DEPT_HIER_SK` | VARCHAR(40) |  |  | FRST_PERF_SVC_RES_DEPT_HIER_SK field |
| 12 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | HEALTH_SYSTEM_ID field |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | HEALTH_SYSTEM_SOURCE_ID field |
| 14 | `HOSPITAL_ID` | DOUBLE |  |  | HOSPITAL_ID field |
| 15 | `INTERFACE_IND` | DOUBLE |  |  | INTERFACE_IND field |
| 16 | `INTERPRETATION_RESULT_REF` | VARCHAR(40) |  |  | INTERPRETATION_RESULT_REF field |
| 17 | `MICRO_ORDER_KEY` | VARCHAR(40) |  |  | MICRO_ORDER_KEY field |
| 18 | `MICRO_TASK_KEY` | DOUBLE |  |  | MICRO_TASK_KEY field |
| 19 | `NUMERIC_RESULT` | DOUBLE |  |  | NUMERIC_RESULT field |
| 20 | `ORDER_ORDBL` | VARCHAR(40) |  |  | ORDER_ORDBL field |
| 21 | `ORGANISM_REF` | VARCHAR(40) |  |  | ORGANISM_REF field |
| 22 | `PARTITION_DT_TM` | DATETIME |  |  | PARTITION_DT_TM field |
| 23 | `PERFORMED_DT_TM` | DATETIME |  |  | PERFORMED_DT_TM field |
| 24 | `PERFORMED_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 25 | `PERFORMED_TM_ZN` | DOUBLE |  |  | PERFORMED_TM_ZN field |
| 26 | `RESULT_TXT` | VARCHAR(100) |  |  | RESULT_TXT field |
| 27 | `RESULT_TYPE_FLG` | DOUBLE |  |  | This field identifies a code value that determines the result type (Interp/Numeric) associated with the detail susceptibility procedure. The task type further categorizes similar detail susceptibility procedures. 6 - Numeric sus detail 7 - Interp sus detail 14 - Alpha sus detail" |
| 28 | `RESULT_UNIT_REF` | VARCHAR(40) |  |  | RESULT_UNIT_REF field |
| 29 | `SOURCE_FLG` | DOUBLE |  |  | The HIS system or interface being used to send us the data extract. 0 = Unknown; 1 = Classic; 2 = MSMeds; 3 = HNAM; 4 = HL7; 5 = Foreign System; 6 = CoPath; 7 = Critical Outcomes - Apache; 8 = Critical Outcomes - Project Impact; 9 = Critical Outcomes - Web; 10 = Critical Outcomes - HNAM; 11 = PI Third Party XML File; 12 = Shell Record; 13 = PI Defined Record; 14 = Healthe Analytics |
| 30 | `SPECIFIC_SOURCE` | VARCHAR(40) |  |  | SPECIFIC_SOURCE field |
| 31 | `TASK_REF` | VARCHAR(40) |  |  | TASK_REF field |
| 32 | `TASK_SEQ` | DOUBLE |  |  | TASK_SEQ field |
| 33 | `TASK_TYPE_FLG` | DOUBLE |  |  | TASK_TYPE_FLG field |
| 34 | `VERIFIED_DT_TM` | DATETIME |  |  | VERIFIED_DT_TM field |
| 35 | `VERIFIED_PRSNL` | VARCHAR(40) |  |  | VERIFIED_PRSNL field |
| 36 | `VERIFIED_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 37 | `VERIFIED_TM_ZN` | DOUBLE |  |  | VERIFIED_TM_ZN field |
| 38 | `VISIT_ID` | DOUBLE |  |  | VISIT_ID field |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

