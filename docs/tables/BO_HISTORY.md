# BO_HISTORY

> Benefit Order History

**Description:** Store the history of the changes made to the benefit order.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL |  | Foreign key reference to the benefit_order table. |
| 7 | `BO_HISTORY_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `BO_STATUS_CD` | DOUBLE | NOT NULL |  | State of the benefit order at a particular instance of time |
| 9 | `BO_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Reason for state of benefit order. |
| 10 | `CONS_BO_SCHED_ID` | DOUBLE | NOT NULL |  | foreign key to cons_bo_sched table |
| 11 | `CROSS_OVER_IND` | DOUBLE |  |  | Indicates whether or not health plan is a cooperative plan. |
| 12 | `DISP_NONCOVD_IND` | DOUBLE |  |  | Indicates whether or not to display non-covered charges on a bill. |
| 13 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL |  | Foreign key reference to Encntr_plan_reltn. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `EPR_UPT_CNT` | DOUBLE |  |  | Number of times Encounter Plan Relation has been updated. |
| 16 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class of health plan. |
| 17 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to health plan table. |
| 18 | `MAN_EDIT_IND` | DOUBLE |  |  | Indicates whether or not BO has been manually edited. |
| 19 | `ORIG_BILL_DT_TM` | DATETIME |  |  | Date of the original bill |
| 20 | `ORIG_DUE_DT_TM` | DATETIME |  |  | Date the original bill was due |
| 21 | `PARENT_BO_ID` | DOUBLE | NOT NULL |  | Parent benefit order id |
| 22 | `PAT_BILL_PREF_FLAG` | DOUBLE |  |  | Values: (0) Sequential patient billing, (1) Concurrent patient billing, (2) Don't bill patient, (3) Bill patient only when due |
| 23 | `PAT_CONCURRENT_IND` | DOUBLE |  |  | Indicates whether the patient is being billed concurrently with claims |
| 24 | `PRIORITY_SEQ` | DOUBLE |  |  | Priority sequence of health plan in which it is billed. |
| 25 | `PRI_CONCURRENT_IND` | DOUBLE |  |  | Indicates whether or not health plan allows concurrent billing of secondary plan when this plan is primary. |
| 26 | `SEC_CONCURRENT_IND` | DOUBLE |  |  | Indicates whether or not health plan allows concurrent billing of other plans when this plan is not primary. |
| 27 | `SUBSCRIBER_ID` | DOUBLE | NOT NULL |  | Identifies the person who is the subscriber of the health plan. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

