# HF_R_ORDERS

> This table is used to facilitate in the creation of the Health Sentry orders BO report

**Description:** HF_R_Orders  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCHARGED_DT_TM` | DATETIME |  |  | The discharge date of the encounter associated with this record |
| 2 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The visit identifier for the encounter |
| 3 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The health system that the hospital belongs to |
| 4 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | The dim table key for the hospital that this record's encounter is attached to |
| 5 | `HOSPITAL_NAME` | VARCHAR(50) |  |  | Name of the hospital |
| 6 | `ORDERED_DT_TM` | DATETIME |  |  | The date/time an order was placed |
| 7 | `ORDERED_MONTH_NAME` | VARCHAR(9) |  |  | The month represented as text |
| 8 | `ORDERED_YEAR` | DOUBLE |  |  | The 4 digit year of the date |
| 9 | `ORDER_LAB_PROCEDURE_GROUP` | VARCHAR(60) |  |  | The lab procedure group can be used to find all related tests |
| 10 | `ORDER_LAB_PROCEDURE_NAME` | VARCHAR(100) |  |  | Full name of a laboratory test |
| 11 | `ORDER_LAB_SUPER_GROUP` | VARCHAR(25) |  |  | A high level group relating lab procedures together |
| 12 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The encounter identifier from the source system |
| 13 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 14 | `PATIENT_ID` | DOUBLE | NOT NULL |  | The patient unique identifier used within the Cerner Health Facts Data Warehouse. |
| 15 | `RESULT_SOURCE` | VARCHAR(15) |  |  | Indicates if the order was from General Lab or Microbiology |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

