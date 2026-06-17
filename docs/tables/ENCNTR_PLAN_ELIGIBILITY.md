# ENCNTR_PLAN_ELIGIBILITY

> The encounter health plan table contains information about the various service type, coverage level, insurance type, and in plan network combinations for the health plan and the patient's eligibility status for each combination at the time of the visit. Information will typically be obtained from the payer via the X12 270/271 transaction but will on occasion be added or modified directly by the end user.

**Description:** Encounter PLan Eligibility  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_PLAN_ELIGIBILITY_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTH_REQUIRED_CD` | DOUBLE | NOT NULL |  | Indicates if an authorization is required for the given service per plan provisions. |
| 6 | `COVERAGE_LEVEL_CD` | DOUBLE | NOT NULL |  | The coverage level for which the eligibility and any associated benefits apply. It identifies the types and number of entities that are covered by the insurance plan. |
| 7 | `ELIGIBILITY_STATUS_CD` | DOUBLE | NOT NULL |  | The eligibility status of the patient. |
| 8 | `ENCNTR_PLAN_ELIGIBILITY_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encntr_plan_eligibility table. It is an internally assigned number and generally not revealed to the user. |
| 9 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encntr_plan_reltn table. It is an internal system assigned number. |
| 10 | `INFO_SOURCE_CD` | DOUBLE | NOT NULL |  | Designates the information source from which the benefit data was obtained. |
| 11 | `INSURANCE_TYPE_CD` | DOUBLE | NOT NULL |  | Type of insurance policy within a specific insurance program for which the eligibility and any associated benefits apply. |
| 12 | `IN_PLAN_NETWORK_CD` | DOUBLE | NOT NULL |  | Indicates if the eligibility and associated benefits apply in network or out of network. |
| 13 | `PAYER_PROV_PLAN_NAME` | VARCHAR(100) |  |  | The name of the health plan as provided by the payer (carrier). |
| 14 | `PROC_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. It identifies a HCPCS, CPT, ICD-9-CM or ICD-10-PCS procedure code. |
| 15 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of service for which the eligibility and any associated benefits apply. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PLAN_RELTN_ID` | [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |
| `PROC_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ENCNTR_PLAN_ELIG_BENEFIT](ENCNTR_PLAN_ELIG_BENEFIT.md) | `ENCNTR_PLAN_ELIGIBILITY_ID` |
| [ENCNTR_PLAN_ELIG_BNFT_HIST](ENCNTR_PLAN_ELIG_BNFT_HIST.md) | `ENCNTR_PLAN_ELIGIBILITY_ID` |
| [ENCNTR_PLAN_ELIG_HIST](ENCNTR_PLAN_ELIG_HIST.md) | `ENCNTR_PLAN_ELIGIBILITY_ID` |

