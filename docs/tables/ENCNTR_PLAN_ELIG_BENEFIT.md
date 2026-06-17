# ENCNTR_PLAN_ELIG_BENEFIT

> The encounter health plan eligibility benefit table contains information about the benefits that a patient is offered via their health plan for a particular eligibility. Information will typically be obtained from the payer via the X12 270/271 transaction but will also be added or modified directly by the end user.

**Description:** Encounter Health Plan Eligibility Benefit  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_PLAN_ELIG_BENEFIT_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BENEFIT_COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Comment identifier for free text stored on the LONG_TEXT table which representsadditional comments, description, or notes for the benefit. |
| 6 | `BENEFIT_MONETARY_AMT` | DOUBLE |  |  | The monetary amount associated with the benefit. |
| 7 | `BENEFIT_PCT` | DOUBLE |  |  | The numeric percentage associated with the benefit. |
| 8 | `BENEFIT_QTY` | DOUBLE |  |  | The quantity associated with the benefit. |
| 9 | `BENEFIT_QTY_QUAL_CD` | DOUBLE | NOT NULL |  | Qualifies the type of quantity associated with the benefit.Code Set: 26311 |
| 10 | `BENEFIT_TIME_PERIOD_QUAL_CD` | DOUBLE | NOT NULL |  | Qualifies the time period of the benefits availability. Code Set: 26335 |
| 11 | `BENEFIT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of benefit for the benefit row.Code Set: 26307 |
| 12 | `ENCNTR_PLAN_ELIGIBILITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the row on the Encntr_plan_eligibility table that benefit is for. |
| 13 | `ENCNTR_PLAN_ELIG_BENEFIT_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of this table. It is an internal system assigned number. |
| 14 | `INFO_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents from what information source the benefit data was obtained.Code Set: 4002563 |
| 15 | `SELECTED_IND` | DOUBLE | NOT NULL |  | Indicates if the benefit has been selected as being directly applicable for the encounter. |
| 16 | `TRANSACTION_SOURCE_IDENT` | VARCHAR(50) |  |  | The transaction identifier assigned by transaction services which was the source of the benefit data. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PLAN_ELIGIBILITY_ID` | [ENCNTR_PLAN_ELIGIBILITY](ENCNTR_PLAN_ELIGIBILITY.md) | `ENCNTR_PLAN_ELIGIBILITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_PLAN_ELIG_BNFT_HIST](ENCNTR_PLAN_ELIG_BNFT_HIST.md) | `ENCNTR_PLAN_ELIG_BENEFIT_ID` |

