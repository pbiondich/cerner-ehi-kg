# PFT_BENEFIT_ORDER

> Benefit order for profit OMF reporting

**Description:** PFT BENEFIT ORDER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | From pft_encntr. The account id for this benefit order |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL |  | References the entry on the benefit order table |
| 8 | `BO_STATUS_CD` | DOUBLE | NOT NULL |  | State of the benefit order at a particular instance of time |
| 9 | `BO_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Reason for state of benefit order. |
| 10 | `CONS_BO_SCHED_ID` | DOUBLE | NOT NULL |  | References the entry on the cons_bo_sched table |
| 11 | `CROSS_OVER_IND` | DOUBLE |  |  | Indicates whether or not health plan is a cooperative plan. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 13 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL |  | References the entry on the encounter plan relation table |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class of health plan. |
| 16 | `GUARANTOR_PERSON_NAME_FULL` | VARCHAR(100) |  |  | Full name of guarantor |
| 17 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the health plan table. |
| 18 | `INS_EMPLY_IDENT_NBR` | VARCHAR(50) |  |  | Insurance employer identification number |
| 19 | `INS_GROUP_NBR` | VARCHAR(100) |  |  | Insurance group number |
| 20 | `INS_HEALTH_PLAN_NAME` | VARCHAR(100) |  |  | Insurance health plan name |
| 21 | `INS_HEALTH_PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Health plan type code iditifies the type of health plan. (For example, PPO, HMW, Medicaid, Medicare, etc.) |
| 22 | `INS_POLICY_NBR` | VARCHAR(50) |  |  | Insurance policy number |
| 23 | `MAN_EDIT_IND` | DOUBLE |  |  | Indicates whether or not the pft benefit order has been manually edited. |
| 24 | `NEXT_BILL_DT_TM` | DATETIME |  |  | Date and time for next bill |
| 25 | `ORIG_BILL_DT_TM` | DATETIME |  |  | The date and time the bill was originally billed. |
| 26 | `PAT_BILL_PREF_FLAG` | DOUBLE |  |  | Patient bill preference flag |
| 27 | `PAYOR_AUTH_NBR` | VARCHAR(50) |  |  | Payor authorization number |
| 28 | `PAYOR_EST_AMT_DUE` | DOUBLE | NOT NULL |  | Payor estimated amount due |
| 29 | `PAYOR_PAYMENTS` | DOUBLE | NOT NULL |  | payor payments |
| 30 | `PFT_BENEFIT_ORDER_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table |
| 31 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | From pft_encntr. The id of the profit encounter. |
| 32 | `PRIORITY_SEQ` | DOUBLE |  |  | Priority sequence ( ex. primary, secondary, tertiary) |
| 33 | `PRI_CONCURRENT_IND` | DOUBLE |  |  | Indicate whether a patient should be billed at the same time when the bill is sent to the primary |
| 34 | `SEC_CONCURRENT_IND` | DOUBLE |  |  | Indicate whether a patient should be billed at the same time when the bill is sent to the secondary |
| 35 | `SUBSCRIBER_ID` | DOUBLE | NOT NULL |  | Identifies the person who is the subscriber of the health plan. |
| 36 | `SUBSCRIBER_NAME_FULL` | VARCHAR(100) |  |  | Full name of the subscriber |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

