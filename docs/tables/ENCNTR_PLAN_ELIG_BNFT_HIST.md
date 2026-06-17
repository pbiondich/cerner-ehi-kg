# ENCNTR_PLAN_ELIG_BNFT_HIST

> Table stores historical information on health plan eligibility benefit data for an encounter.

**Description:** Encounter Plan Eligibility Benefit History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BENEFIT_COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Comment identifier for free text stored on the LONG_TEXT table which represents additional comments, description, or notes for the benefit. |
| 6 | `BENEFIT_MONETARY_AMT` | DOUBLE |  |  | The monetary amount associated with the benefit. |
| 7 | `BENEFIT_PCT` | DOUBLE |  |  | The numeric percentage associated with the benefit. |
| 8 | `BENEFIT_QTY` | DOUBLE |  |  | The quantity associated with the benefit. |
| 9 | `BENEFIT_QTY_QUAL_CD` | DOUBLE | NOT NULL |  | Qualifies the type of quantity associated with the benefit. |
| 10 | `BENEFIT_TIME_PERIOD_QUAL_CD` | DOUBLE | NOT NULL |  | Qualifies the time period of the benefit's availablity |
| 11 | `BENEFIT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of benefit for the benefit row. |
| 12 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 13 | `ENCNTR_PLAN_ELIGIBILITY_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCNTR_PLAN_ELIGIBILITY table to which this benefit applies. |
| 14 | `ENCNTR_PLAN_ELIG_BENEFIT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCNTR_PLAN_ELIG_BENEFIT table for which this history is maintained. |
| 15 | `ENCNTR_PLAN_ELIG_BNFT_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCNTR_PLAN_ELIG_BNFT_HIST table. |
| 16 | `INFO_SOURCE_CD` | DOUBLE | NOT NULL |  | Designates the information source from which the benefit data was obtained. |
| 17 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 18 | `SELECTED_IND` | DOUBLE | NOT NULL |  | Indicates if the benefit has been selected as being directly applicable for the encounter. |
| 19 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 20 | `TRANSACTION_SOURCE_IDENT` | VARCHAR(50) |  |  | The identifier of the transaction that was the source of this elegibility benefit data when a transaction was used to verify eligibility for a patient. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PLAN_ELIGIBILITY_ID` | [ENCNTR_PLAN_ELIGIBILITY](ENCNTR_PLAN_ELIGIBILITY.md) | `ENCNTR_PLAN_ELIGIBILITY_ID` |
| `ENCNTR_PLAN_ELIG_BENEFIT_ID` | [ENCNTR_PLAN_ELIG_BENEFIT](ENCNTR_PLAN_ELIG_BENEFIT.md) | `ENCNTR_PLAN_ELIG_BENEFIT_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

