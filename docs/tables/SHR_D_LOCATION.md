# SHR_D_LOCATION

> This table contains location information such as facility and building name.

**Description:** Shared Dimension Location  
**Table type:** REFERENCE  
**Primary key:** `SHR_D_LOCATION_ID`  
**Columns:** 18  
**Referenced by:** 32 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BED` | VARCHAR(40) | NOT NULL |  | The bed associate with a location. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `BUILDING` | VARCHAR(40) | NOT NULL |  | The building associated with a location. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FACILITY` | VARCHAR(40) | NOT NULL |  | The facility associated with a location. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LOCATION_DESC` | VARCHAR(40) | NOT NULL |  | The current permanent location of the patient (The location of a patient will be valued with the lowest level location type in the hierarchy of facility, building, room, bed). |
| 10 | `LOCATION_MD5_HASH_TXT` | VARCHAR(32) | NOT NULL |  | This column contains an MD5 hash code based upon the combined values of the LOCATION_DESC, FACILITY, BUILDING, ROOM, BED, MILL_LOGICAL_DOMAIN_ID and ACTIVE_IND columns. |
| 11 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 12 | `ROOM` | VARCHAR(40) | NOT NULL |  | The room associated with a location. |
| 13 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies location information such as facility and building name. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (32)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `SHR_D_LOCATION_ID` |
| [RC_F_CASE_MIX](RC_F_CASE_MIX.md) | `SHR_D_LOCATION_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [RC_F_CLAIM_EVENT](RC_F_CLAIM_EVENT.md) | `SHR_D_LOCATION_ID` |
| [RC_F_CODING_ACTIVITY](RC_F_CODING_ACTIVITY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DAILY_CENSUS](RC_F_DAILY_CENSUS.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DAILY_CENSUS_SMRY](RC_F_DAILY_CENSUS_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DAILY_CLAIM_EVENT_SMRY](RC_F_DAILY_CLAIM_EVENT_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DAILY_ENCNTR_VISIT_SMRY](RC_F_DAILY_ENCNTR_VISIT_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `SHR_D_LOCATION_ID` |
| [RC_F_DLY_CHRG_ASSOC_SMRY](RC_F_DLY_CHRG_ASSOC_SMRY.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [RC_F_DLY_CODING_ACT_SMRY](RC_F_DLY_CODING_ACT_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `SHR_D_LOCATION_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_MONTHLY_CENSUS_SMRY](RC_F_MONTHLY_CENSUS_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_MONTHLY_CLAIM_EVENT_SMRY](RC_F_MONTHLY_CLAIM_EVENT_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_MONTHLY_ENCNTR_VISIT_SMRY](RC_F_MONTHLY_ENCNTR_VISIT_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_MTH_CHRG_ASSOC_SMRY](RC_F_MTH_CHRG_ASSOC_SMRY.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [RC_F_MTH_CODING_ACT_SMRY](RC_F_MTH_CODING_ACT_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `SHR_D_LOCATION_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `SHR_D_LOCATION_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `SHR_D_PERFORMING_LOCATION_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `SHR_D_PATIENT_LOCATION_ID` |
| [SHR_F_ENCOUNTER_VISIT](SHR_F_ENCOUNTER_VISIT.md) | `SHR_D_LOCATION_ID` |

