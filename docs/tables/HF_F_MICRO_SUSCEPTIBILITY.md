# HF_F_MICRO_SUSCEPTIBILITY

> A fact table used by Health Facts to analyze data in the Micro Susceptibility subject area

**Description:** HF_F_Micro_Susceptibility  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 70

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field identifies whether or not the susceptibility result has been defined as an abnormal susceptibility response. Valid values include: 0 = Normal response 1 = Abnormal response |
| 2 | `ACCESSION` | VARCHAR(100) |  |  | The primary accession number identifies an order or a group of orders. |
| 3 | `ANTIMICROBIAL_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for the antimicrobial. |
| 4 | `ANTIMICROBIAL_ID` | DOUBLE |  |  | The dim table key for the antimicrobial being used in the susceptibility test |
| 5 | `COLLECTION_METHOD_ID` | VARCHAR(40) |  |  | The procedure for collecting a specimen. |
| 6 | `COLLECTION_SITE_ID` | DOUBLE |  |  | The dim table key for the collection site of the isolate |
| 7 | `COLLECTION_SOURCE_ID` | DOUBLE |  |  | The dim table key for the collection source of the isolate |
| 8 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 9 | `ENCOUNTER_ID` | DOUBLE |  |  | Uniquely identify the encounter associated with a record |
| 10 | `HOSPITAL_ID` | DOUBLE |  |  | The dim table key for the hospital that this record's encounter is attached to |
| 11 | `INTERFACE_IND` | DOUBLE |  |  | An indicator to differentiate if the value is coming from PathNet or Clinical Event. 0 is Pathnet and 1 is Clinical Event. |
| 12 | `INTERP_BLOOD_PERF_DT_ID` | DOUBLE |  |  | The dim table key for the performed date of the blood result |
| 13 | `INTERP_BLOOD_PERF_DT_TM` | DATETIME |  |  | The performed date/time of the blood result |
| 14 | `INTERP_BLOOD_PERF_TM_VLD_FLG` | DOUBLE |  |  | The performed time valid flag of the blood result |
| 15 | `INTERP_BLOOD_RESULT_ID` | DOUBLE |  |  | The dim table key for the interpretative result of this susceptibility test when the isolate source is blood |
| 16 | `INTERP_BLOOD_VERF_DT_ID` | DOUBLE |  |  | The dim table key for the verified date of the blood result |
| 17 | `INTERP_BLOOD_VERF_DT_TM` | DATETIME |  |  | The verified date/time of the blood result |
| 18 | `INTERP_BLOOD_VERF_TM_VLD_FLG` | DOUBLE |  |  | The verified time valid flag of the blood result |
| 19 | `INTERP_CSF_PERF_DT_ID` | DOUBLE |  |  | The dim table key for the performed date of the spinal fluid result |
| 20 | `INTERP_CSF_PERF_DT_TM` | DATETIME |  |  | The performed date/time of the spinal fluid result |
| 21 | `INTERP_CSF_PERF_TM_VLD_FLG` | DOUBLE |  |  | The performed time valid flag of the spinal fluid result |
| 22 | `INTERP_CSF_RESULT_ID` | DOUBLE |  |  | The dim table key for the interpretative result of this susceptibility test when the isolate source is spinal fluid |
| 23 | `INTERP_CSF_VERF_DT_ID` | DOUBLE |  |  | The dim table key for the verified date of the spinal fluid result |
| 24 | `INTERP_CSF_VERF_DT_TM` | DATETIME |  |  | The verified date/time of the spinal fluid result |
| 25 | `INTERP_CSF_VERF_TM_VLD_FLG` | DOUBLE |  |  | The verified time valid flag of the spinal fluid result |
| 26 | `INTERP_PERF_DT_ID` | DOUBLE |  |  | The interpretation performed date id is used to join the hf_f_micro_susceptibility table to the date dimension table. |
| 27 | `INTERP_PERF_DT_TM` | DATETIME |  |  | The date the susceptibility procedure result interpretation was performed. |
| 28 | `INTERP_PERF_TM_VLD_FLG` | DOUBLE |  |  | ;If the time stamp received for this date is valid, then '1', Else '0'. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 1 - Valid Time Stamp 0 - Invalid Time Stamp |
| 29 | `INTERP_RESULT_ID` | DOUBLE |  |  | This field contains the internal identification code for the interpretation susceptibility result value. |
| 30 | `INTERP_URINE_PERF_DT_ID` | DOUBLE |  |  | The dim table key for the performed date of the urine result |
| 31 | `INTERP_URINE_PERF_DT_TM` | DATETIME |  |  | The performed date/time of the urine result |
| 32 | `INTERP_URINE_PERF_TM_VLD_FLG` | DOUBLE |  |  | The performed time valid flag of the urine result |
| 33 | `INTERP_URINE_RESULT_ID` | DOUBLE |  |  | The dim table key for the interpretative result of this susceptibility test when the isolate source is urine |
| 34 | `INTERP_URINE_VERF_DT_ID` | DOUBLE |  |  | The dim table key for the verified date of the urine result |
| 35 | `INTERP_URINE_VERF_DT_TM` | DATETIME |  |  | The verified date/time of the urine result |
| 36 | `INTERP_URINE_VERF_TM_VLD_FLG` | DOUBLE |  |  | The verified time valid flag of the urine result |
| 37 | `INTERP_VERF_DT_ID` | DOUBLE |  |  | The interpretation verified date id is used to join the hf_f_micro_susceptibility table to the date dimension table. |
| 38 | `INTERP_VERF_DT_TM` | DATETIME |  |  | The date the susceptibility procedure result interpretation was verified. |
| 39 | `INTERP_VERF_TM_VLD_FLG` | DOUBLE |  |  | If the time stamp received for this date is valid, then '1', Else '0'. If the time stamp is invalid, the time of 00:00 is placed in the date/time field. If the sending system puts a time of 00:00 in the time field for invalid times, and they know the difference between this scenario and an actual time of midnight, those times should be flagged as invalid. 1 - Valid Time Stamp 0 - Invalid Time Stamp |
| 40 | `ISOLATE_ID` | DOUBLE |  |  | The dim table key for the isolate against which the susceptibility test is run |
| 41 | `METHOD_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for the collection method. |
| 42 | `MICRO_RESULT_TYPE_ID` | DOUBLE |  |  | The Health Data identifier for the micro result type which joins to hf_d_micro_result_type. |
| 43 | `MICRO_SUSCEPTIBILITY_KEY` | DOUBLE |  |  | A unique, non-intelligent identifier for the table |
| 44 | `NUMERIC_RESULT` | VARCHAR(40) |  |  | A numeric/alpha numeric result for this susceptibility test |
| 45 | `NUMERIC_RESULT_PERF_DT_ID` | DOUBLE |  |  | The dim table key for the performed date of the numeric/alpha numeric result |
| 46 | `NUMERIC_RESULT_PERF_DT_TM` | DATETIME |  |  | The performed date/time of the numeric/alpha numeric result |
| 47 | `NUMERIC_RESULT_PERF_TM_VLD_FLG` | DOUBLE |  |  | The performed time valid flag of the numeric/alpha numeric result |
| 48 | `NUMERIC_RESULT_VERF_DT_ID` | DOUBLE |  |  | The dim table key for the verified date of the numeric/alpha numeric result |
| 49 | `NUMERIC_RESULT_VERF_DT_TM` | DATETIME |  |  | The verified date/time of the numeric/alpha numeric result |
| 50 | `NUMERIC_RESULT_VERF_TM_VLD_FLG` | DOUBLE |  |  | The verified time valid flag of the numeric/alpha numeric result |
| 51 | `ORDER_LAB_ORDERABLE_SK` | VARCHAR(40) |  |  | The contributing system raw orderable value for the ordering test. |
| 52 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the ordered lab procedure |
| 53 | `ORGANISM_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw orderable value for the organism or codified result. |
| 54 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE |  |  | A unique number to identify parts of the same organism. |
| 55 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 56 | `PERFORMED_BENCH_HOSP_ID` | DOUBLE |  |  | The Health Data hospital identifier for the perform laboratory if determined from the bench information. |
| 57 | `PERFORMED_HOSPITAL_ID` | DOUBLE |  |  | The Health Data hospital identifier for the perform laboratory if determined from the facility information. |
| 58 | `PERFORMED_PRSNL_ID` | DOUBLE |  |  | The physician id that joins to hf_d_physician for the personnel performing the lab test. |
| 59 | `RESULT_UNITS_ID` | DOUBLE |  |  | The dim table key for the units of measurement for the numeric result |
| 60 | `SITE_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for body site. |
| 61 | `SOURCE_FLG` | DOUBLE |  |  | A flag that differentiates if the source of this record is from PathNet or Clinical Event (third party lab) system. |
| 62 | `SPECIFIC_SOURCE` | VARCHAR(40) |  |  | blank |
| 63 | `SPECIMEN_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw orderable value for the ordering test. |
| 64 | `SRC_MICRO_ORDER_KEY` | VARCHAR(40) |  |  | The unique identifier for Micro_Order table's associated micro order. |
| 65 | `TEST_TYPE_ID` | DOUBLE |  |  | The dim table key for the type of susceptibility test |
| 66 | `UNIT_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for unit of measure. |
| 67 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `UPDT_USER` | VARCHAR(40) |  |  | The user who last modified this record |
| 70 | `VERIFIED_PRSNL` | VARCHAR(40) |  |  | The personnel that verified the result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

