# HF_F_MICRO_FULL_REPORT

> A fact table used to analyze the full text of microbiology responses.

**Description:** HF_F_Micro_Full_Report  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(100) |  |  | The primary accession number identifies an order or a group of orders. |
| 2 | `CLIENT_ORDER_CULTURE_NAME` | VARCHAR(100) |  |  | The client display value for the ordered lab procedure |
| 3 | `CLIENT_REPORT_VALUE` | VARCHAR(255) |  |  | The textual value of the report response. This can be either free text or the code value description of a codified response |
| 4 | `COMPLETED_DT_TM` | DATETIME |  |  | The date/time the micro order was completed |
| 5 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 6 | `ENCOUNTER_ID` | DOUBLE |  |  | Uniquely identify the encounter associated with a record |
| 7 | `FALSE_POSITIVE_IND` | DOUBLE |  |  | When a response is marked as positive but the system has detected a negating phrase surrounding the response, this will be set to 1. For all other rows, it will be set to 0 |
| 8 | `ISOLATE_ID` | DOUBLE |  |  | The dim table key for the isolate against which the susceptibility test is run |
| 9 | `MICRO_FULL_REPORT_KEY` | DOUBLE |  |  | A unique, non-intelligent identifier for the table |
| 10 | `MICRO_RESPONSE_SEQUENCE` | DOUBLE |  |  | The field contains a value that uniquely identifies each report response. This value will allow multiples of the same report response to be uniquely identified. |
| 11 | `MICRO_TASK_ID` | DOUBLE |  |  | A unique identifier for a micro task. Combine with Micro_Response_Sequence for an alternate key into this table |
| 12 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the ordered lab procedure |
| 13 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 14 | `PERFORMED_HOSPITAL_ID` | DOUBLE |  |  | The hospital in which the report was performed. |
| 15 | `POSITIVE_IND` | VARCHAR(1) |  |  | This field identifies whether or not the response has been defined as a positive report response. Valid values include: 0 = negative response 1= positive response |
| 16 | `RESPONSE_CLASS_FLG` | DOUBLE |  |  | This field identifies the type of response used in issuing the report. 0 - Textual Response 5 - Coded Response 6 - Member of a Group Response 101 - Organism |
| 17 | `RESULT_TYPE_PROCEDURE_ID` | DOUBLE |  |  | The dim table key for the type of procedure that was performed |
| 18 | `SRC_MICRO_ORDER_KEY` | VARCHAR(200) |  |  | The identifying source key for the record. |
| 19 | `TASK_TYPE_FLG` | DOUBLE |  |  | This field identifies a value that determines the task type associated with the task entered. The task type further categorizes similar tasks within each task class. |
| 20 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `UPDT_USER` | VARCHAR(40) |  |  | The user who last modified this record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

