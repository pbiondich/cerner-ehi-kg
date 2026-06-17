# AOAV_DIAGNOSES

> Activity table to store the diagnoses that are documented and considered for contribution to a patient's predictions. The list of diagnoses should match what is displayed on the SOI Mpage.

**Description:** AOAV_DIAGNOSES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AOAV_DIAGNOSES_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `AOAV_DIAGNOSIS_GROUP_CD` | DOUBLE | NOT NULL |  | Unique generated number that identifies the code value of the AOAV_DIAGNOSIS_GROUP code set |
| 4 | `AOAV_PERSON_ENCNTR_ID` | DOUBLE | NOT NULL |  | #OBSOLETE in DBARCHDTL-22877 - Unique identifier from the AOAV_PERSON_ENCOUNTER table |
| 5 | `DIAGNOSIS_DT_TM` | DATETIME |  |  | Date/time diagnosis was determined for patient |
| 6 | `ENCNTR_ID` | DOUBLE |  | FK→ | Unique Identifier of the encounter; |
| 7 | `SOURCE_IDENTIFIER` | VARCHAR(50) |  |  | ICU10 Diagnosis Equivalent code. |
| 8 | `SOURCE_STRING` | VARCHAR(255) |  |  | Description of the ICD10 diagnosis code indicated in SOURCE_IDENTIFIER |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

