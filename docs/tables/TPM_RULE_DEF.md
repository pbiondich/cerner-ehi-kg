# TPM_RULE_DEF

> Store the definition of a TPM rule.

**Description:** TPM RULE DEF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COLLECTION_PRIORITY_IND` | DOUBLE |  |  | Indicator telling the collection priority. |
| 7 | `ENCNTR_TYPE_IND` | DOUBLE |  |  | Encounter Type Indicator |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FIN_CLASS_IND` | DOUBLE |  |  | Financial Class Indicator. |
| 10 | `MED_SERVICE_IND` | DOUBLE |  |  | Med Service Indicator |
| 11 | `ORD_LOC_IND` | DOUBLE |  |  | Ordering location Indicator |
| 12 | `ORD_PHY_IND` | DOUBLE |  |  | Ordering physician indicator |
| 13 | `PATIENT_LOC_IND` | DOUBLE |  |  | Patient Location Indicator |
| 14 | `PERF_LOC_IND` | DOUBLE |  |  | Performing location ind. |
| 15 | `PERF_PHY_IND` | DOUBLE |  |  | Performing physician ind. |
| 16 | `TPM_CHRG_TIER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the tpm_chrg_tier table. |
| 17 | `TPM_RULE_DEF_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TPM_CHRG_TIER_ID` | [TPM_CHRG_TIER](TPM_CHRG_TIER.md) | `TPM_CHRG_TIER_ID` |

