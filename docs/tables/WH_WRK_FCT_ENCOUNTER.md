# WH_WRK_FCT_ENCOUNTER

> This is a Health Sentry Work table for processing encounters

**Description:** WH_WRK_FCT_ENCOUNTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 47

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_DT` | DATETIME |  |  | ADMIT_DT field |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | ADMIT_DT_TM field |
| 3 | `ADMIT_LOC_NURSE_UNIT_REF` | VARCHAR(40) |  |  | ADMIT_LOC_NURSE_UNIT_REF field |
| 4 | `ADMIT_MODE_REF` | VARCHAR(40) |  |  | ADMIT_MODE_REF field |
| 5 | `ADMIT_SOURCE_REF` | VARCHAR(40) |  |  | ADMIT_SOURCE_REF field |
| 6 | `ADMIT_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 7 | `ADMIT_TM_ZN` | DOUBLE |  |  | ADMIT_TM_ZN field |
| 8 | `ADMIT_TYPE_REF` | VARCHAR(40) |  |  | ADMIT_TYPE_REF field |
| 9 | `AGE_IN_DAYS` | DOUBLE |  |  | AGE_IN_DAYS field |
| 10 | `AGE_IN_YEARS` | DOUBLE |  |  | AGE_IN_YEARS field |
| 11 | `CURRENT_LOC_INSTITUTION_REF` | VARCHAR(40) |  |  | CURRENT_LOC_INSTITUTION_REF field |
| 12 | `CURRENT_LOC_NURSE_UNIT_REF` | VARCHAR(40) |  |  | CURRENT_LOC_NURSE_UNIT_REF field |
| 13 | `DISCHARGE_DISPOSITION_REF` | VARCHAR(40) |  |  | DISCHARGE_DISPOSITION_REF field |
| 14 | `DISCHARGE_DT` | DATETIME |  |  | DISCHARGE_DT field |
| 15 | `DISCHARGE_DT_TM` | DATETIME |  |  | DISCHARGE_DT_TM field |
| 16 | `DISCHARGE_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then 1, Else 0. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 0 = Invalid Time Stamp; 1 = Valid Time Stamp |
| 17 | `DISCHARGE_TM_ZN` | DOUBLE |  |  | DISCHARGE_TM_ZN field |
| 18 | `DISCHARGE_TO_LOC_REF` | VARCHAR(40) |  |  | DISCHARGE_TO_LOC_REF field |
| 19 | `ENCOUNTER_CLASS_REF` | VARCHAR(40) |  |  | ENCOUNTER_CLASS_REF field |
| 20 | `ENCOUNTER_KEY` | DOUBLE |  |  | ENCOUNTER_KEY field |
| 21 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | ENCOUNTER_SK field |
| 22 | `ENCOUNTER_TYPE_CLASS_REF` | VARCHAR(40) |  |  | ENCOUNTER_TYPE_CLASS_REF field |
| 23 | `EXTRACT_DT_TM` | DATETIME |  |  | EXTRACT_DT_TM field |
| 24 | `FINANCIAL_CLASS_REF` | VARCHAR(40) |  |  | FINANCIAL_CLASS_REF field |
| 25 | `FINANCIAL_NBR` | VARCHAR(40) |  |  | FINANCIAL_NBR field |
| 26 | `FINANCIAL_NBR_RAW` | VARCHAR(40) |  |  | FINANCIAL_NBR_RAW field |
| 27 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | FIRST_PROCESS_DT_TM field |
| 28 | `FORMATTED_MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | FORMATTED_MEDICAL_RECORD_NBR field |
| 29 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | HEALTH_SYSTEM_ID field |
| 30 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | HEALTH_SYSTEM_SOURCE_ID field |
| 31 | `HF_CALC_DRG` | VARCHAR(3) |  |  | HF_CALC_DRG field |
| 32 | `HF_CALC_MDC` | VARCHAR(2) |  |  | HF_CALC_MDC field |
| 33 | `HF_ROLLUP_INSTITUTION_REF` | VARCHAR(40) |  |  | HF_ROLLUP_INSTITUTION_REF field |
| 34 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | LAST_PROCESS_DT_TM field |
| 35 | `MEDICAL_RECORD_NBR_RAW` | VARCHAR(40) |  |  | MEDICAL_RECORD_NBR_RAW field |
| 36 | `MEDICAL_SERVICE_REF` | VARCHAR(40) |  |  | MEDICAL_SERVICE_REF field |
| 37 | `NEXT_VISIT_FIRST_PROCESS_DT_TM` | DATETIME |  |  | NEXT_VISIT_FIRST_PROCESS_DT_TM field |
| 38 | `PARTITION_DT_TM` | DATETIME |  |  | PARTITION_DT_TM field |
| 39 | `PATIENT_TYPE_REF` | VARCHAR(40) |  |  | PATIENT_TYPE_REF field |
| 40 | `PERSON_KEY` | DOUBLE |  |  | PERSON_KEY field |
| 41 | `PERSON_SK` | VARCHAR(40) |  |  | PERSON_SK field |
| 42 | `SOURCE_FLG` | DOUBLE |  |  | The HIS system or interface being used to send us the data extract. 0 = Unknown; 1 = Classic; 2 = MSMeds; 3 = HNAM; 4 = HL7; 5 = Foreign System; 6 = CoPath; 7 = Critical Outcomes - Apache; 8 = Critical Outcomes - Project Impact; 9 = Critical Outcomes - Web; 10 = Critical Outcomes - HNAM; 11 = PI Third Party XML File; 12 = Shell Record; 13 = PI Defined Record; 14 = Healthe Analytics |
| 43 | `TOTAL_CHARGE_AMT` | DOUBLE |  |  | TOTAL_CHARGE_AMT field |
| 44 | `VISIT_FIRST_PROCESS_DT_TM` | DATETIME |  |  | VISIT_FIRST_PROCESS_DT_TM field |
| 45 | `VISIT_KEY` | DOUBLE |  |  | VISIT_KEY field |
| 46 | `WEIGHT` | DOUBLE |  |  | WEIGHT field |
| 47 | `WEIGHT_UNIT` | VARCHAR(40) |  |  | WEIGHT_UNIT field |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

