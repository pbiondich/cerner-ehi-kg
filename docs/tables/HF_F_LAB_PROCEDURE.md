# HF_F_LAB_PROCEDURE

> A fact table used to analyze the general lab results. For HealthSentry, all results are loaded. For UNV, only completed results are loaded

**Description:** HF_F_Lab_Procedure  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 64

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(100) |  |  | The primary accession number identifies an order or a group of orders. |
| 2 | `CHARACTER_RESULT` | VARCHAR(2000) |  |  | The textual value of the gen lab result |
| 3 | `COLLECTION_METHOD_ID` | VARCHAR(40) |  |  | The identifier for the procedure for collecting a specimen. |
| 4 | `COLLECTION_SITE_ID` | DOUBLE |  |  | The identifier for the mapped body site. |
| 5 | `COLLECTION_SOURCE_ID` | DOUBLE |  |  | The dim table key for the location where the test was performed |
| 6 | `CONTAINER_TYPE` | VARCHAR(100) |  |  | The specimen container type. Raw client value. |
| 7 | `DATE_RESULT_ID` | DOUBLE |  |  | The dim table key for the date of the procedure |
| 8 | `DETAIL_LAB_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the detail lab procedure (the task assay) |
| 9 | `DETAIL_LAB_TASK_ASSAY_SK` | VARCHAR(40) |  |  | The contributing system raw task assay for the detail test. |
| 10 | `DISCHARGED_DT_TM` | DATETIME |  |  | Indicates if the timestamp on Lab_Performed_Dt_Tm is valid |
| 11 | `ENCOUNTER_ID` | DOUBLE |  |  | Uniquely identify the encounter associated with a record |
| 12 | `HOSPITAL_ID` | DOUBLE |  |  | The dim table key for the hospital that this record's encounter is attached to |
| 13 | `INTERFACE_IND` | DOUBLE |  |  | An indicator to differentiate if the lab is coming from PathNet or Clinical Event. 0 is Pathnet and 1 is Clinical Event. |
| 14 | `LAB_CANCELLED_DT_ID` | DOUBLE |  |  | The dim table key for the date the gen lab order was cancelled |
| 15 | `LAB_CANCELLED_DT_TM` | DATETIME |  |  | The date/time the gen lab order was completed |
| 16 | `LAB_CANCELLED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Lab_Completed_Dt_Tm is valid |
| 17 | `LAB_COMPLETED_DT_ID` | DOUBLE |  |  | The dim table key for the date the gen lab order was completed |
| 18 | `LAB_COMPLETED_DT_TM` | DATETIME |  |  | The date/time the specimen was received |
| 19 | `LAB_COMPLETED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Lab_Received_Dt_Tm is valid |
| 20 | `LAB_DRAWN_DT_ID` | DOUBLE |  |  | The dim table key for the date the specimen was drawn |
| 21 | `LAB_DRAWN_DT_TM` | DATETIME |  |  | The date/time a gen lab order was ordered |
| 22 | `LAB_DRAWN_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Lab_Ordered_Dt_Tm is valid |
| 23 | `LAB_ORDERED_DT_ID` | DOUBLE |  |  | The dim table key for the date the gen lab order was ordered |
| 24 | `LAB_ORDERED_DT_TM` | DATETIME |  |  | An obsolete column that exists for consistency with existing Health Facts fact table |
| 25 | `LAB_ORDERED_TM_VLD_FLG` | DOUBLE |  |  | The date/time the gen lab DTA was verified |
| 26 | `LAB_ORDER_CARESETTING_ID` | DOUBLE |  |  | The dim table key for the location where the test was ordered |
| 27 | `LAB_ORDER_CARESETTING_RAW` | VARCHAR(40) |  |  | The client value representing the location where the test was ordered |
| 28 | `LAB_PERFORMED_CARESETTING_ID` | DOUBLE |  |  | The process that last modified this record |
| 29 | `LAB_PERFORMED_DT_ID` | DOUBLE |  |  | The dim table key for the date the gen lab DTA was performed |
| 30 | `LAB_PERFORMED_DT_TM` | DATETIME |  |  | The date/time the gen lab order was cancelled |
| 31 | `LAB_PERFORMED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Lab_Proc_Verified_Dt_Tm is valid |
| 32 | `LAB_PROCEDURE_KEY` | DOUBLE |  |  | The dim table key for the date that the gen lab DTA was verified |
| 33 | `LAB_RECEIVED_DT_ID` | DOUBLE |  |  | A unique, non-intelligent identifier for the table |
| 34 | `LAB_RECEIVED_DT_TM` | DATETIME |  |  | The dim table key for the date the specimen was received |
| 35 | `LAB_RECEIVED_TM_VLD_FLG` | DOUBLE |  |  | The date/time the specimen was drawn |
| 36 | `LAB_RESULT_TYPE_ID` | DOUBLE |  |  | Indicates if the timestamp on Lab_Drawn_Dt_Tm is valid |
| 37 | `LAB_VERIFIED_DT_ID` | DOUBLE |  |  | The dim table key for the type of gen lab result (numeric, text, etc.) |
| 38 | `LAB_VERIFIED_DT_TM` | DATETIME |  |  | The date/time the gen lab DTA was performed |
| 39 | `LAB_VERIFIED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Lab_Cancelled_Dt_Tm is valid |
| 40 | `METHOD_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for the collection method. |
| 41 | `NORMAL_ALPHA` | VARCHAR(200) |  |  | Defines the normal alpha response for a procedure with the result type of alpha. |
| 42 | `NORMAL_RANGE_HIGH` | VARCHAR(40) |  |  | Defines the normal high reference range value associated with a result. The result must be greater than the normal high to be flagged as high. |
| 43 | `NORMAL_RANGE_LOW` | VARCHAR(40) |  |  | Defines the normal low reference range value associated with a result. The result must be less than the normal low to be flagged as low. |
| 44 | `NUMERIC_RESULT` | DOUBLE |  |  | The numeric value of the gen lab result |
| 45 | `ORDERING_PHYSICIAN_ID` | DOUBLE |  |  | The dim table key for the ordering physician of the gen lab test |
| 46 | `ORDER_LAB_ORDERABLE_SK` | VARCHAR(40) |  |  | The contributing system raw orderable value for the ordering test. |
| 47 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the ordered lab procedure |
| 48 | `PARTITION_DT_TM` | DATETIME |  |  | The dim table key for the collection source of the isolate |
| 49 | `PERFORMED_BENCH_HOSP_ID` | DOUBLE |  |  | The Health Data hospital identifier for the perform laboratory if determined from the bench information. |
| 50 | `PERFORMED_HOSPITAL_ID` | DOUBLE |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 51 | `PERFORMED_PRSNL_ID` | DOUBLE |  |  | The personnel who performed the procedure. |
| 52 | `REPORTING_PRIORITY_ID` | DOUBLE |  |  | The dim table key for the reporting priority of the gen lab order |
| 53 | `RESULT_INDICATOR_ID` | DOUBLE |  |  | The dim table key used to indicate special information in regards to the gen lab result (Abnormal, Low, High, Critical, etc.) |
| 54 | `RESULT_INDICATOR_REF` | VARCHAR(40) |  |  | The dim table key used to indicate special information in regards to the gen lab result (Abnormal, Low, High, Critical, etc.) |
| 55 | `RESULT_UNITS_ID` | DOUBLE |  |  | The dim table key for the units of measurement for the gen lab result |
| 56 | `SITE_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for body site. |
| 57 | `SOURCE_FLG` | DOUBLE |  |  | A flag that differentiates if the source of this record is from PathNet or Clinical Event (third party lab) system. |
| 58 | `SPECIMEN_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for specimen. |
| 59 | `SRC_GEN_LAB_ORDER_KEY` | VARCHAR(100) |  |  | The identifying source key for the record. |
| 60 | `UNIT_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for unit of measure. |
| 61 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_USER` | VARCHAR(40) |  |  | The date this record was last modified. Populated based on the last process date/time of the Micro Task to prevent over-reporting in HealthSentry |
| 64 | `VERIFIED_PRSNL` | VARCHAR(40) |  |  | The personnel that verified the result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

