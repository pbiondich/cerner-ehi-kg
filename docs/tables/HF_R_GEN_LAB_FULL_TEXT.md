# HF_R_GEN_LAB_FULL_TEXT

> This table is used to facilitate in the creation of the Health Sentry full text BO report

**Description:** HF_R_Gen_Lab_Full_Text  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The primary accession number identifies an order or a group of orders. |
| 2 | `CHARACTER_RESULT` | VARCHAR(2000) |  |  | The textual value of the gen lab result |
| 3 | `DETAIL_LAB_PROCEDURE_ID` | DOUBLE | NOT NULL |  | The dim table key for the detail lab procedure (the task assay) |
| 4 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 5 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The visit identifier for the encounter |
| 6 | `GENDER` | VARCHAR(60) |  |  | Patient's gender |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The health system that the hospital belongs to |
| 8 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | The dim table key for the hospital that this record's encounter is attached to |
| 9 | `LAB_COMPLETED_DT_TM` | DATETIME |  |  | The date/time the micro order was completed |
| 10 | `LAB_PROCEDURE_NAME` | VARCHAR(100) |  |  | Full name of a laboratory test |
| 11 | `LAB_RESULT_TYPE_DESC` | VARCHAR(60) |  |  | The textual description of the lab result (numeric, character, date, etc.) |
| 12 | `NORMAL_RANGE_HIGH` | VARCHAR(40) |  |  | Defines the normal high reference range value associated with a result. The result must be greater than the normal high to be flagged as high. |
| 13 | `NORMAL_RANGE_LOW` | VARCHAR(40) |  |  | Defines the normal low reference range value associated with a result. The result must be less than the normal low to be flagged as low. |
| 14 | `NUMERIC_RESULT` | DOUBLE |  |  | The numeric value of the gen lab result |
| 15 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The encounter identifier from the source system |
| 16 | `OUTBOUND_HSS_ID` | DOUBLE | NOT NULL |  | The unique identifier of the organization that this result will be reported to |
| 17 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 18 | `PATIENT_ID` | DOUBLE | NOT NULL |  | The patient unique identifier used within the Cerner Health Facts Data Warehouse. |
| 19 | `PATIENT_NAME` | VARCHAR(100) |  |  | Patient's name |
| 20 | `RESULT_INDICATOR_DESC` | VARCHAR(60) |  |  | The textual description of the normality of the result (out of range, not normal, etc.) |
| 21 | `UNIT_DISPLAY` | VARCHAR(40) |  |  | The display of the unit of measure for the result |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

