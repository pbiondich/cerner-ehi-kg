# TPM_CONDITION

> Stores the parameters related to a TPM condition.

**Description:** TPM CONDITION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | Code value identifying the collection priority (e.g. ASAP, before first etc.). |
| 7 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Code value indicating the type of encounter (e.g. Inpatient, outpatient). |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class code value |
| 10 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | Code value identifying the medical service. |
| 11 | `ORD_LOC_CD` | DOUBLE | NOT NULL |  | Code value identifying the ordering location. |
| 12 | `ORD_PHY_ID` | DOUBLE | NOT NULL |  | Unique identifier of the ordering physician. Foreign key reference to the person table. |
| 13 | `PATIENT_LOC_CD` | DOUBLE | NOT NULL |  | Code value identifying the location of the patient. |
| 14 | `PERF_LOC_CD` | DOUBLE | NOT NULL |  | Performing Location Cd |
| 15 | `PERF_PHY_ID` | DOUBLE | NOT NULL |  | Performing Physician ID |
| 16 | `TPM_CHRG_TIER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the tpm_chrg_tier table. |
| 17 | `TPM_CONDITION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 18 | `TPM_RESULT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the tpm_result table. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TPM_CHRG_TIER_ID` | [TPM_CHRG_TIER](TPM_CHRG_TIER.md) | `TPM_CHRG_TIER_ID` |
| `TPM_RESULT_ID` | [TPM_RESULT](TPM_RESULT.md) | `TPM_RESULT_ID` |

