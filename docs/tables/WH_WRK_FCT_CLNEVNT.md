# WH_WRK_FCT_CLNEVNT

> This is a Health Sentry Work table for processing clinical events.

**Description:** WH_WRK_FCT_CLNEVNT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 65

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(100) |  |  | ACCESSION field |
| 2 | `CANCELED_DT_TM` | DATETIME |  |  | CANCELED_DT_TM field |
| 3 | `CANCELED_TM_ZN` | DOUBLE |  |  | CANCELED_TM_ZN field |
| 4 | `CANCEL_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 5 | `COMPLETED_DT_TM` | DATETIME |  |  | COMPLETED_DT_TM field |
| 6 | `COMPLETED_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 7 | `COMPLETED_TM_ZN` | DOUBLE |  |  | COMPLETED_TM_ZN field |
| 8 | `CRITICAL_REF` | VARCHAR(40) |  |  | CRITICAL_REF field |
| 9 | `DELTA_REF` | VARCHAR(40) |  |  | DELTA_REF field |
| 10 | `DISCH_DT_TM` | DATETIME |  |  | DISCH_DT_TM field |
| 11 | `EVENT_SK` | VARCHAR(100) |  |  | EVENT_SK field |
| 12 | `FEASIBLE_REF` | VARCHAR(40) |  |  | FEASIBLE_REF field |
| 13 | `FIRST_CNTR_TYPE_REF` | VARCHAR(40) |  |  | FIRST_CNTR_TYPE_REF field |
| 14 | `FIRST_CTNR_COLL_METHOD_REF` | VARCHAR(40) |  |  | FIRST_CTNR_COLL_METHOD_REF field |
| 15 | `FIRST_CTNR_DRAWN_DT_TM` | DATETIME |  |  | FIRST_CTNR_DRAWN_DT_TM field |
| 16 | `FIRST_CTNR_DRAWN_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 17 | `FIRST_CTNR_DRAWN_TM_ZN` | DOUBLE |  |  | FIRST_CTNR_DRAWN_TM_ZN field |
| 18 | `FIRST_CTNR_RECEIVED_DT_TM` | DATETIME |  |  | FIRST_CTNR_RECEIVED_DT_TM field |
| 19 | `FIRST_CTNR_RECEIVED_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 20 | `FIRST_CTNR_RECEIVED_TM_ZN` | DOUBLE |  |  | FIRST_CTNR_RECEIVED_TM_ZN field |
| 21 | `FIRST_SPECIMEN_SITE_REF` | VARCHAR(40) |  |  | FIRST_SPECIMEN_SITE_REF field |
| 22 | `FIRST_SPECIMEN_TYPE_REF` | VARCHAR(40) |  |  | FIRST_SPECIMEN_TYPE_REF field |
| 23 | `GO_HEALTH_SYSTEM_ID` | DOUBLE |  |  | GO_HEALTH_SYSTEM_ID field |
| 24 | `GO_HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | GO_HEALTH_SYSTEM_SOURCE_ID field |
| 25 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | HEALTH_SYSTEM_ID field |
| 26 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | HEALTH_SYSTEM_SOURCE_ID field |
| 27 | `HF_NORMAL_HIGH` | VARCHAR(40) |  |  | HF_NORMAL_HIGH field |
| 28 | `HF_NORMAL_LOW` | VARCHAR(40) |  |  | HF_NORMAL_LOW field |
| 29 | `HOSPITAL_ID` | DOUBLE |  |  | HOSPITAL_ID field |
| 30 | `INTERFACE_IND` | DOUBLE |  |  | INTERFACE_IND field |
| 31 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | LAST_PROCESS_DT_TM field |
| 32 | `LINEAR_REF` | VARCHAR(40) |  |  | LINEAR_REF field |
| 33 | `NORMAL_ALPHA` | VARCHAR(200) |  |  | NORMAL_ALPHA field |
| 34 | `NORMAL_REF` | VARCHAR(40) |  |  | NORMAL_REF field |
| 35 | `ORDER_DOC_PRSNL` | VARCHAR(40) |  |  | ORDER_DOC_PRSNL field |
| 36 | `ORDER_DT_TM` | DATETIME |  |  | ORDER_DT_TM field |
| 37 | `ORDER_ORDBL` | VARCHAR(40) |  |  | ORDER_ORDBL field |
| 38 | `ORDER_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 39 | `ORDER_TM_ZN` | DOUBLE |  |  | ORDER_TM_ZN field |
| 40 | `O_HEALTH_SYSTEM_ID` | DOUBLE |  |  | O_HEALTH_SYSTEM_ID field |
| 41 | `O_HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | O_HEALTH_SYSTEM_SOURCE_ID field |
| 42 | `O_SOURCE_FLG` | DOUBLE |  |  | O_SOURCE_FLG field |
| 43 | `PARTITION_DT_TM` | DATETIME |  |  | PARTITION_DT_TM field |
| 44 | `PATIENT_LOC_NURSE_UNIT_SK` | VARCHAR(40) |  |  | PATIENT_LOC_NURSE_UNIT_SK field |
| 45 | `PERFORM_DT_TM` | DATETIME |  |  | PERFORM_DT_TM field |
| 46 | `PERFORM_LOC_INST` | VARCHAR(40) |  |  | PERFORM_LOC_INST field |
| 47 | `PERFORM_SVC_RES_DEPT_HIER_SK` | VARCHAR(40) |  |  | PERFORM_SVC_RES_DEPT_HIER_SK field |
| 48 | `PERFORM_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 49 | `PERFORM_TM_ZN` | DOUBLE |  |  | PERFORM_TM_ZN field |
| 50 | `REPORTING_PRIORITY_REF` | VARCHAR(40) |  |  | REPORTING_PRIORITY_REF field |
| 51 | `RESULT_FLG_REF` | VARCHAR(40) |  |  | RESULT_FLG_REF field |
| 52 | `RESULT_TYPE_REF` | VARCHAR(40) |  |  | RESULT_TYPE_REF field |
| 53 | `RESULT_VALUE_DT_TM` | DATETIME |  |  | RESULT_VALUE_DT_TM field |
| 54 | `RESULT_VALUE_FORMATTED` | VARCHAR(2000) |  |  | RESULT_VALUE_FORMATTED field |
| 55 | `RESULT_VALUE_NUMERIC` | VARCHAR(2000) |  |  | RESULT_VALUE_NUMERIC field |
| 56 | `RESULT_VALUE_UNIT_REF` | VARCHAR(40) |  |  | RESULT_VALUE_UNIT_REF field |
| 57 | `REVIEW_REF` | VARCHAR(40) |  |  | REVIEW_REF field |
| 58 | `SOURCE_FLG` | DOUBLE |  |  | The HIS system or interface being used to send us the data extract. 0 = Unknown; 1 = Classic; 2 = MSMeds; 3 = HNAM; 4 = HL7; 5 = Foreign System; 6 = CoPath; 7 = Critical Outcomes - Apache; 8 = Critical Outcomes - Project Impact; 9 = Critical Outcomes - Web; 10 = Critical Outcomes - HNAM; 11 = PI Third Party XML File; 12 = Shell Record; 13 = PI Defined Record; 14 = Healthe Analytics |
| 59 | `SRC_GEN_LAB_ORDER_KEY` | VARCHAR(100) |  |  | SRC_GEN_LAB_ORDER_KEY field |
| 60 | `TASK_ASSAY_SK` | VARCHAR(40) |  |  | TASK_ASSAY_SK field |
| 61 | `VERIFIED_DT_TM` | DATETIME |  |  | VERIFIED_DT_TM field |
| 62 | `VERIFIED_PRSNL` | VARCHAR(40) |  |  | VERIFIED_PRSNL field |
| 63 | `VERIFIED_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 64 | `VERIFIED_TM_ZN` | DOUBLE |  |  | VERIFIED_TM_ZN field |
| 65 | `VISIT_ID` | DOUBLE |  |  | VISIT_ID field |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

