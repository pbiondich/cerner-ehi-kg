# LH_CNT_IC_ADV_SURG_DATA

> This tables stores surgical procedure data that has been selected by the user for export within an Infection Control Advisor.

**Description:** LH_CNT_IC_ADV_SURG_DATA  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | Admit Date and Time of related encounter. |
| 3 | `AD_HOC_IND` | DOUBLE | NOT NULL |  | Stores whether the procedure was pulled from Millennium and added or built as an ad hoc row. |
| 4 | `ALIAS_DISP` | VARCHAR(200) |  |  | The alias is an identifier (I.E., financial number, medical record number) for a patient or encounter. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DURATION_DISP` | VARCHAR(100) |  |  | Duration of the procedure in hours to be used in CDA creation. |
| 7 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to EKS_ADVSR_EVENT table. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ENCOUNTER table for the surgical case encounter. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LH_CNT_IC_ADV_SURG_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_ADV_SURG_DATA table. |
| 11 | `NHSN_IND` | DOUBLE | NOT NULL |  | Stores frontend selection of the NSHN checkbox. |
| 12 | `NHSN_PROC_CD` | DOUBLE | NOT NULL |  | NHSN assigned procedure code value from custom codeset 4003149. |
| 13 | `OUTPATIENT_FLAG` | DOUBLE | NOT NULL |  | Outpatient encounter flag. 0 = Unknown 1 = Yes, 2 = No |
| 14 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to CLINICAL_EVENT table. Used for FSI surgical events, which are built as separate events all under the same parent_event_id. If a surgical procedure was FSI then it will have a PARENT_EVENT_ID. |
| 15 | `PROC_DT_TM` | DATETIME |  |  | Date and Time the procedure occurred. |
| 16 | `SURGEON_NAME_FULL_FORMATTED` | VARCHAR(250) |  |  | Display value of the Surgeon Name to be used in CDA creation. |
| 17 | `SURGEON_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to PRSNL table for the performing surgeon. |
| 18 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to SURGICAL_CASE table. If the surgical procedure came from the Surginet tables then it will have a surg_case_id. |
| 19 | `SURG_CASE_NBR_FULL_FORMATTED` | VARCHAR(250) |  |  | Display value of the Case Number to be used in CDA creation. |
| 20 | `SURG_PROC_CD` | DOUBLE | NOT NULL |  | The code value for the surgical procedure. |
| 21 | `SURG_PROC_DISP` | VARCHAR(200) |  |  | The string description of the surgical procedure entered via Ad hoc, FSI, or Surginet. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EKS_ADVSR_EVENT_ID` | [EKS_ADVSR_EVENT](EKS_ADVSR_EVENT.md) | `EKS_ADVSR_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `SURGEON_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

