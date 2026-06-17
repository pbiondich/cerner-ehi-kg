# ENCNTR_PLAN_ELIG_HIST

> Table stores historical information on health plan eligibility benefit data for an encounter.

**Description:** Encounter Plan Eligibility History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTH_REQUIRED_CD` | DOUBLE | NOT NULL |  | Indicates if an authorization is required for the given service per plan provisions. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `COVERAGE_LEVEL_CD` | DOUBLE | NOT NULL |  | The coverage level for which the eligibility and any associated benefits apply, it identifies the types and number of entities that are covered by the insurance plan. |
| 8 | `ELIGIBILITY_STATUS_CD` | DOUBLE | NOT NULL |  | The eligibility status of the patient. |
| 9 | `ENCNTR_PLAN_ELIGIBILITY_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCNTR_PLAN_ELIGIBILITY table for which this history is maintained. |
| 10 | `ENCNTR_PLAN_ELIG_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCNTR_PLAN_ELIG_HIST |
| 11 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCNTR_PLAN_RELTN table. Identifies the health plan for which the patient's eligibility was verified. |
| 12 | `INFO_SOURCE_CD` | DOUBLE | NOT NULL |  | Designates the information source from which the eligibility benefit data was obtained. |
| 13 | `INSURANCE_TYPE_CD` | DOUBLE | NOT NULL |  | Type of insurance policy within a specific insurance program for which the eligibility and any associated benefits apply. |
| 14 | `IN_PLAN_NETWORK_CD` | DOUBLE | NOT NULL |  | Indicates if the eligibility and associated benefits apply in network or out of network. |
| 15 | `PAYER_PROV_PLAN_NAME` | VARCHAR(100) |  |  | The name of the health plan as provided by the payer (carrier). |
| 16 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 17 | `PROC_NOMEN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the NOMENCLATURE table. It identifies a hcpcs, cpt, icd-9-cm or icd-10-pcs procedure code for which the eligibility and any associated benefits apply. |
| 18 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of service for which the eligibility and any associated benefits apply. |
| 19 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PLAN_ELIGIBILITY_ID` | [ENCNTR_PLAN_ELIGIBILITY](ENCNTR_PLAN_ELIGIBILITY.md) | `ENCNTR_PLAN_ELIGIBILITY_ID` |
| `ENCNTR_PLAN_RELTN_ID` | [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

