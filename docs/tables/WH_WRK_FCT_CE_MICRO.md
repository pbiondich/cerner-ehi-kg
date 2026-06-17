# WH_WRK_FCT_CE_MICRO

> This is a Health Sentry Work table for processing clinical events for microbiology.

**Description:** WH_WRK_FCT_CE_MICRO  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 59

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | ABNORMAL_IND field |
| 2 | `ACCESSION` | VARCHAR(100) |  |  | ACCESSION field |
| 3 | `CANCELED_DT_TM` | DATETIME |  |  | CANCELED_DT_TM field |
| 4 | `CANCELED_TM_ZN` | DOUBLE |  |  | CANCELED_TM_ZN field |
| 5 | `CANCEL_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 6 | `COMPLETED_DT_TM` | DATETIME |  |  | COMPLETED_DT_TM field |
| 7 | `COMPLETED_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 8 | `COMPLETED_TM_ZN` | DOUBLE |  |  | COMPLETED_TM_ZN field |
| 9 | `DEPT_STATUS_REF` | VARCHAR(40) |  |  | DEPT_STATUS_REF field |
| 10 | `DISCH_DT_TM` | DATETIME |  |  | DISCH_DT_TM field |
| 11 | `FALSE_POSITIVE_IND` | DOUBLE |  |  | FALSE_POSITIVE_IND field |
| 12 | `FIRST_CTNR_COLL_METHOD_REF` | VARCHAR(40) |  |  | FIRST_CTNR_COLL_METHOD_REF field |
| 13 | `FIRST_CTNR_DRAWN_DT_TM` | DATETIME |  |  | FIRST_CTNR_DRAWN_DT_TM field |
| 14 | `FIRST_CTNR_DRAWN_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 15 | `FIRST_CTNR_DRAWN_TM_ZN` | DOUBLE |  |  | FIRST_CTNR_DRAWN_TM_ZN field |
| 16 | `FIRST_CTNR_RECEIVED_DT_TM` | DATETIME |  |  | FIRST_CTNR_RECEIVED_DT_TM field |
| 17 | `FIRST_CTNR_RECEIVED_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 18 | `FIRST_CTNR_RECEIVED_TM_ZN` | DOUBLE |  |  | FIRST_CTNR_RECEIVED_TM_ZN field |
| 19 | `FIRST_OBSERVED_DT_TM` | DATETIME |  |  | FIRST_OBSERVED_DT_TM field |
| 20 | `FIRST_SPECIMEN_SITE_REF` | VARCHAR(40) |  |  | FIRST_SPECIMEN_SITE_REF field |
| 21 | `FIRST_SPECIMEN_TYPE_REF` | VARCHAR(40) |  |  | FIRST_SPECIMEN_TYPE_REF field |
| 22 | `FRST_PERF_SVC_RES_DEPT_HIER_SK` | VARCHAR(40) |  |  | FRST_PERF_SVC_RES_DEPT_HIER_SK field |
| 23 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | HEALTH_SYSTEM_ID field |
| 24 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | HEALTH_SYSTEM_SOURCE_ID field |
| 25 | `HOSPITAL_ID` | DOUBLE |  |  | HOSPITAL_ID field |
| 26 | `INTERFACE_IND` | DOUBLE |  |  | INTERFACE_IND field |
| 27 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | LAST_PROCESS_DT_TM field |
| 28 | `MICRO_ORDER_SK` | VARCHAR(100) |  |  | MICRO_ORDER_SK field |
| 29 | `MOST_RECENT_TASK_IND` | DOUBLE |  |  | MOST_RECENT_TASK_IND field |
| 30 | `OBSERVED_DT_TM` | DATETIME |  |  | OBSERVED_DT_TM field |
| 31 | `OBSERVED_TM_ZN` | DOUBLE |  |  | OBSERVED_TM_ZN field |
| 32 | `ORDER_DOC_PRSNL` | VARCHAR(40) |  |  | ORDER_DOC_PRSNL field |
| 33 | `ORDER_DT_TM` | DATETIME |  |  | ORDER_DT_TM field |
| 34 | `ORDER_ORDBL` | VARCHAR(40) |  |  | ORDER_ORDBL field |
| 35 | `ORDER_POSITIVE_IND` | DOUBLE |  |  | ORDER_POSITIVE_IND field |
| 36 | `ORDER_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 37 | `ORDER_TM_ZN` | DOUBLE |  |  | ORDER_TM_ZN field |
| 38 | `ORGANISM_REF` | VARCHAR(40) |  |  | ORGANISM_REF field |
| 39 | `PARTITION_DT_TM` | DATETIME |  |  | PARTITION_DT_TM field |
| 40 | `PATIENT_LOC_NURSE_UNIT_SK` | VARCHAR(40) |  |  | PATIENT_LOC_NURSE_UNIT_SK field |
| 41 | `PERFORM_LOC_INST` | VARCHAR(40) |  |  | PERFORM_LOC_INST field |
| 42 | `POSITIVE_IND` | DOUBLE |  |  | POSITIVE_IND field |
| 43 | `REPONSE_REF` | VARCHAR(40) |  |  | REPONSE_REF field |
| 44 | `REPORTING_PRIORITY_REF` | VARCHAR(40) |  |  | REPORTING_PRIORITY_REF field |
| 45 | `REPORT_TYPE_REF` | VARCHAR(40) |  |  | REPORT_TYPE_REF field |
| 46 | `REP_NULL_IND` | DOUBLE |  |  | REP_NULL_IND field |
| 47 | `RESPONSE_CLASS_FLG` | DOUBLE |  |  | RESPONSE_CLASS_FLG field |
| 48 | `SOURCE_FLG` | DOUBLE |  |  | The HIS system or interface being used to send us the data extract. 0 = Unknown; 1 = Classic; 2 = MSMeds; 3 = HNAM; 4 = HL7; 5 = Foreign System; 6 = CoPath; 7 = Critical Outcomes - Apache; 8 = Critical Outcomes - Project Impact; 9 = Critical Outcomes - Web; 10 = Critical Outcomes - HNAM; 11 = PI Third Party XML File; 12 = Shell Record; 13 = PI Defined Record; 14 = Healthe Analytics |
| 49 | `SPECIFIC_SOURCE` | VARCHAR(40) |  |  | SPECIFIC_SOURCE field |
| 50 | `SRC_MICRO_ORDER_KEY` | VARCHAR(200) |  |  | SRC_MICRO_ORDER_KEY field |
| 51 | `STATUS_REF` | VARCHAR(40) |  |  | STATUS_REF field |
| 52 | `TASK_NULL_IND` | DOUBLE |  |  | TASK_NULL_IND field |
| 53 | `TASK_REF` | VARCHAR(40) |  |  | TASK_REF field |
| 54 | `TASK_SEQ` | DOUBLE |  |  | TASK_SEQ field |
| 55 | `TASK_TYPE_FLG` | DOUBLE |  |  | TASK_TYPE_FLG field |
| 56 | `VERIFIED_DT_TM` | DATETIME |  |  | VERIFIED_DT_TM field |
| 57 | `VERIFIED_PRSNL` | VARCHAR(40) |  |  | VERIFIED_PRSNL field |
| 58 | `VERIFIED_TM_ZN` | DOUBLE |  |  | VERIFIED_TM_ZN field |
| 59 | `VISIT_ID` | DOUBLE |  |  | VISIT_ID field |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

