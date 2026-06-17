# STATEMENT_CYCLE_RELTN

> Stores bulk of data related to Statement_Cycles

**Description:** STATEMENT CYCLE RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BAD_DEBT_IND` | DOUBLE |  |  | Indicates if this encounter is in bad debt. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DEFAULT_IND` | DOUBLE |  |  | Indicates that an initial statement cycle rule is the default rule. A default statement cycle rule will always qualify if no other (non-default) rules qualify. |
| 8 | `DENIAL_CD` | DOUBLE | NOT NULL |  | Denial Code related to this statement Cycle. |
| 9 | `DENIAL_GROUP_CD` | DOUBLE | NOT NULL |  | Denial Group Code related to this statement Cycle |
| 10 | `ENCNTR_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the financial encounter. |
| 11 | `ENCNTR_VIP_IND` | DOUBLE |  |  | Indicates if this encounter is for a VIP |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `EXCLUDE_FACILITY_ORG_ID` | DOUBLE | NOT NULL | FK→ | The organization that is excluded for a statement cycle |
| 14 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class code value |
| 15 | `FORMAL_PAY_PLAN_IND` | DOUBLE |  |  | Indicates if encounter is on a formal payment plan |
| 16 | `FPP_AUTOMATED_PAYMENT_IND` | DOUBLE | NOT NULL |  | Indicator to determine if the formal payment plan has automated payments on it. |
| 17 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | FK to Health Plan table |
| 18 | `INFORMAL_PAY_PLAN_IND` | DOUBLE |  |  | Indicates if encntr is on an informal payment plan |
| 19 | `INSURANCE_ORG_ID` | DOUBLE | NOT NULL | FK→ | Selected insurance organization for given statement cycle. Foreign key to the Organization table |
| 20 | `NEXT_CYCLE_ID` | DOUBLE | NOT NULL | FK→ | FK back to statement cycle table for the next cycle in seqence |
| 21 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Billing Entity or PFT_encntr |
| 22 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | BILLING_ENTITY or PFT_ENCNTR |
| 23 | `PERSON_VIP_IND` | DOUBLE |  |  | Indicates if person is a VIP |
| 24 | `PRIMARY_CYCLE_IND` | DOUBLE |  |  | Indicates if this statement cycle is the primary cycle |
| 25 | `PROCESS_PRIORITY_NBR` | DOUBLE |  |  | A value that indicates the order in which the statement cycles should be processed. The highest priority item gets a process_priority_nbr of 1. |
| 26 | `START_FLAG` | DOUBLE |  |  | Stores when to start the cycle0 - Discharged, 1 - Selfpay Ready To Bill, 2 - Primary Insurance Billed,3 - Primary Insurance Transmitted,4 - Secondary Insurance Billed,5 - Secondary Insurance Transmitted |
| 27 | `STATEMENT_CYCLE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the Statement cycle table |
| 28 | `STATEMENT_CYCLE_RELTN_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXCLUDE_FACILITY_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INSURANCE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `NEXT_CYCLE_ID` | [STATEMENT_CYCLE](STATEMENT_CYCLE.md) | `STATEMENT_CYCLE_ID` |
| `STATEMENT_CYCLE_ID` | [STATEMENT_CYCLE](STATEMENT_CYCLE.md) | `STATEMENT_CYCLE_ID` |

