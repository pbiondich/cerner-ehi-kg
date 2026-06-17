# HF_F_MICROBIOLOGY

> A fact table used by Health Facts to analyze data in the Microbiology subject area. This table does not contain susceptibility results (those are in HF_F_Micro_Susceptibility). Only positive isolates are loaded into this table

**Description:** HF_F_Microbiology  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 65

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE |  |  | This field identifies whether or not the microbiology result has been defined as an abnormal response. Valid values include: 0 = Normal response 1 = Abnormal response |
| 2 | `ACCESSION` | VARCHAR(100) |  |  | The primary accession number identifies an order or a group of orders. |
| 3 | `COLLECTION_METHOD_ID` | VARCHAR(40) |  |  | The procedure for collecting a specimen. |
| 4 | `COLLECTION_SITE_ID` | DOUBLE |  |  | The dim table key for the collection site of the isolate |
| 5 | `COLLECTION_SOURCE_ID` | DOUBLE |  |  | The dim table key for the collection source of the isolate |
| 6 | `COLLECTION_STATUS_ID` | DOUBLE |  |  | The dim table key for the collection status of the micro order |
| 7 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 8 | `ENCOUNTER_ID` | DOUBLE |  |  | Uniquely identify the encounter associated with a record |
| 9 | `FALSE_POSITIVE_IND` | DOUBLE |  |  | Indicates if Health Facts processing has determined that this result is falsely displaying as positive |
| 10 | `FIRST_OBSERVED_ISOLATE_DT_TM` | DATETIME |  |  | The date/time when an isolate was first observed on this micro task |
| 11 | `FIRST_REPORT_ENTERED_DT_ID` | DOUBLE |  |  | The dim table key for the date of the first time a report was entered for this micro task |
| 12 | `FIRST_REPORT_ENTERED_DT_TM` | DATETIME |  |  | The date/time when a report was first entered for this micro task |
| 13 | `FIRST_RPT_ENTERED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on First_Report_Entered_Dt_Tm is valid |
| 14 | `HOSPITAL_ID` | DOUBLE |  |  | The dim table key for the hospital that this record's encounter is attached to |
| 15 | `INTERFACE_IND` | DOUBLE |  |  | An indicator to differentiate if the value is coming from PathNet or Clinical Event. 0 is Pathnet and 1 is Clinical Event. |
| 16 | `ISOLATE_ID` | DOUBLE |  |  | The dim table key for the isolate against which the susceptibility test is run |
| 17 | `LAST_REPORT_UPDATED_DT_ID` | DOUBLE |  |  | The dim table key for the date of the last time a report was entered for this micro task |
| 18 | `LAST_REPORT_UPDATED_DT_TM` | DATETIME |  |  | The date/time when a report was last entered for this micro task |
| 19 | `LAST_RPT_UPDATED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Last_Report_Entered_Dt_Tm is valid |
| 20 | `METHOD_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for the collection method. |
| 21 | `MICROBIOLOGY_KEY` | DOUBLE |  |  | A unique, non-intelligent identifier for the table |
| 22 | `MICRO_LAB_CANCELLED_DT_ID` | DOUBLE |  |  | The dim table key for the date the micro order was cancelled |
| 23 | `MICRO_LAB_CANCELLED_DT_TM` | DATETIME |  |  | The date/time the micro order was cancelled |
| 24 | `MICRO_LAB_CANCELLED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Micro_Lab_Cancelled_Dt_Tm is valid |
| 25 | `MICRO_LAB_COMPLETED_DT_ID` | DOUBLE |  |  | The dim table key for the date the micro order was completed |
| 26 | `MICRO_LAB_COMPLETED_DT_TM` | DATETIME |  |  | The date/time the micro order was completed |
| 27 | `MICRO_LAB_COMPLTED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Micro_Lab_Completed_Dt_Tm is valid |
| 28 | `MICRO_LAB_DRAWN_DT_ID` | DOUBLE |  |  | The dim table key for the date the specimen was drawn |
| 29 | `MICRO_LAB_DRAWN_DT_TM` | DATETIME |  |  | The date/time the specimen was drawn |
| 30 | `MICRO_LAB_DRAWN_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Micro_Lab_Drawn_Dt_Tm is valid |
| 31 | `MICRO_LAB_ORDERED_DT_ID` | DOUBLE |  |  | The dim table key for the date the micro order was ordered |
| 32 | `MICRO_LAB_ORDERED_DT_TM` | DATETIME |  |  | The date/time a micro order was ordered |
| 33 | `MICRO_LAB_ORDERED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Micro_Lab_Ordered_Dt_Tm is valid |
| 34 | `MICRO_LAB_RECEIVED_DT_ID` | DOUBLE |  |  | The dim table key for the date the specimen was received |
| 35 | `MICRO_LAB_RECEIVED_DT_TM` | DATETIME |  |  | The date/time the specimen was received |
| 36 | `MICRO_LAB_RECEIVED_TM_VLD_FLG` | DOUBLE |  |  | Indicates if the timestamp on Micro_Lab_Received_Dt_Tm is valid |
| 37 | `MICRO_ORDER_CARESETTING_ID` | DOUBLE |  |  | The dim table key for the location where the test was ordered |
| 38 | `MICRO_ORDER_CARESETTING_RAW` | VARCHAR(40) |  |  | The client value representing the location where the test was ordered |
| 39 | `MICRO_ORDER_STATUS_ID` | DOUBLE |  |  | The dim table key for the status of the micro order |
| 40 | `MICRO_RESULT_TYPE_ID` | DOUBLE |  |  | The dim table key for the type of micro result (preliminary, final, etc.) |
| 41 | `ORDERING_PHYSICIAN_ID` | DOUBLE |  |  | The dim table key for the ordering physician of the micro test |
| 42 | `ORDER_LAB_ORDERABLE_SK` | VARCHAR(40) |  |  | The contributing system raw orderable value for the ordering test. |
| 43 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the ordered lab procedure |
| 44 | `ORGANISM_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw organism from code set 1021. |
| 45 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE |  |  | A unique number to identify parts of the same organism. |
| 46 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 47 | `PERFORMED_BENCH_HOSP_ID` | DOUBLE |  |  | The Health Data hospital identifier for the perform laboratory if determined from the bench information. |
| 48 | `PERFORMED_HOSPITAL_ID` | DOUBLE |  |  | The dim key for the hospital where the micro test was performed |
| 49 | `PERFORMED_PRSNL_ID` | DOUBLE |  |  | The personnel who performed this result |
| 50 | `POSITIVE_IND` | DOUBLE |  |  | This differentiates the positive microbiology from the negative. |
| 51 | `REPORTING_PRIORITY_ID` | DOUBLE |  |  | The dim table key for the reporting priority of the micro order |
| 52 | `RESPONSE_CLASS_FLG` | DOUBLE |  |  | The contributing system raw response class. |
| 53 | `RESPONSE_REF` | VARCHAR(40) |  |  | The contributing system raw codified response from code set 1021. |
| 54 | `RESULT_TYPE_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the type of procedure that was performed |
| 55 | `SITE_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw code value for body site. |
| 56 | `SOURCE_FLG` | DOUBLE |  |  | A flag that differentiates if the source of this record is from PathNet or Clinical Event (third party lab) system. |
| 57 | `SPECIFIC_SOURCE` | VARCHAR(40) |  |  | The client code value ref for the specimen code set. Client value for the collection_source. |
| 58 | `SPECIMEN_CODE_VALUE_REF` | VARCHAR(40) |  |  | The contributing system raw orderable value for the ordering test. |
| 59 | `SRC_MICRO_ORDER_KEY` | VARCHAR(40) |  |  | The unique identifier for Micro_Order table's associated micro order. |
| 60 | `TOTAL_REPORT_UPDATES` | DOUBLE |  |  | The total number of times reports have been entered for this micro task |
| 61 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 62 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 63 | `UPDT_USER` | VARCHAR(40) |  |  | The user who last modified this record |
| 64 | `VERIFIED_DT_TM` | DATETIME |  |  | The date time of the result being verified. |
| 65 | `VERIFIED_PRSNL` | VARCHAR(40) |  |  | The personnel that verified the result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

