# UKRWH_CDS_DIAGNOSIS

> Contains CDS Diagnois details at the level of a Diagnosis relating to a CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Diagnosis  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `DIAGNOSIS_CD_TXT` | VARCHAR(6) |  |  | This field contains the diagnostic observations recorded about a PATIENT. |
| 4 | `DIAGNOSIS_PRES_ADM_IND_NHS` | VARCHAR(1) |  |  | An indication of whether a PATIENT DIAGNOSIS was already present when the PATIENT started a Hospital Provider Spell. |
| 5 | `DIAGNOSIS_SCHEME_NHS` | VARCHAR(2) |  |  | This is used in the Commissioning Data Set - Clinical Information Group to denote the Coding Scheme basis of the Diagnosis. |
| 6 | `DIAGNOSIS_SEQ` | DOUBLE |  |  | Sequence number of the Diagnosis |
| 7 | `EC_DIAGNOSIS_QUALIFIER_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to express the level of certainty of a patient diagnosis. |
| 8 | `EC_DIAGNOSIS_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the patient diagnosis. |
| 9 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 10 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 13 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 14 | `UKRWH_CDS_DIAGNOSIS_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds diagnosis table. It is an internal system assigned number. |
| 15 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 16 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

