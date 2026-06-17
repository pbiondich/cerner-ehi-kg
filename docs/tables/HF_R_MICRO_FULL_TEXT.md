# HF_R_MICRO_FULL_TEXT

> This table is used to facilitate in the creation of the Health Sentry full text BO report

**Description:** HF_R_Micro_Full_Text  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(100) |  |  | The primary accession number identifies an order or a group of orders. |
| 2 | `CLIENT_ORDER_CULTURE_NAME` | VARCHAR(100) |  |  | The client display value for the ordered lab procedure |
| 3 | `CLIENT_REPORT_VALUE` | VARCHAR(200) |  |  | The textual value of the report response. This can be either free text or the code value description of a codified response |
| 4 | `COMPLETED_DT_TM` | DATETIME |  |  | The date/time the micro order was completed |
| 5 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 6 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The visit identifier for the encounter |
| 7 | `FALSE_POSITIVE_IND` | DOUBLE |  |  | When a response is marked as positive but the system has detected a negating phrase surrounding the response, this will be set to 1. For all other rows, it will be set to 0 |
| 8 | `FINANCIAL_NBR` | VARCHAR(40) |  |  | The formatted Financial number |
| 9 | `FINANCIAL_NBR_RAW` | VARCHAR(40) |  |  | The unformatted Financial number. |
| 10 | `GENDER` | VARCHAR(60) |  |  | Patient's gender |
| 11 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The health system that the hospital belongs to |
| 12 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | The dim table key for the hospital that this record's encounter is attached to |
| 13 | `MICRO_RESPONSE_SEQUENCE` | DOUBLE |  |  | The field contains a value that uniquely identifies each report response. This value will allow multiples of the same report response to be uniquely identified. |
| 14 | `MICRO_TASK_ID` | DOUBLE | NOT NULL |  | A unique identifier for a micro task. Combine with Micro_Response_Sequence for an alternate key into this table |
| 15 | `ORDER_LAB_PROCEDURE_ID` | DOUBLE | NOT NULL |  | The dim table key for the ordered lab procedure |
| 16 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The encounter identifier from the source system |
| 17 | `OUTBOUND_HSS_ID` | DOUBLE | NOT NULL |  | The unique identifier of the organization that this result will be reported to |
| 18 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 19 | `PATIENT_ID` | DOUBLE | NOT NULL |  | The patient unique identifier used within the Cerner Health Facts Data Warehouse. |
| 20 | `PATIENT_NAME` | VARCHAR(100) |  |  | Patient's name |
| 21 | `PERFORMED_HOSPITAL_ID` | DOUBLE |  |  | The Health Data hospital identifier for the perform laboratory if determined from the facility information. |
| 22 | `POSITIVE_IND` | VARCHAR(1) |  |  | This field identifies whether or not the response has been defined as a positive report response. Valid values include: 0 = negative response 1= positive response |
| 23 | `REPORTABLE_ISOLATE_IND` | DOUBLE |  |  | Indicates if the row of text in the micro response was reportable or not as an isolate |
| 24 | `RESPONSE_CLASS_FLG` | VARCHAR(10) |  |  | This field identifies the type of response used in issuing the report. 0 - Textual Response 5 - Coded Response 6 - Member of a Group Response 101 - Organism |
| 25 | `RESULT_TYPE_PROCEDURE_DESC` | VARCHAR(60) |  |  | A textual description of the detail procedure/report (preliminary, final, etc.) |
| 26 | `SRC_FCT_KEY` | VARCHAR(100) |  |  | The identifying source key for the record. |
| 27 | `TASK_TYPE_FLG` | VARCHAR(10) |  |  | This field identifies a value that determines the task type associated with the task entered. The task type further categorizes similar tasks within each task class. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

