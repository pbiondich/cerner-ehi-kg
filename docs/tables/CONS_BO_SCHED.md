# CONS_BO_SCHED

> Stores guarantor and next billing date info for statement and invoice billing.

**Description:** CONS BO SCHED  
**Table type:** ACTIVITY  
**Primary key:** `CONS_BO_SCHED_ID`  
**Columns:** 25  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILLING_ENTITY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Relates the record to the billing entity group. |
| 7 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | Candidate key reference to the billing_entity table. |
| 8 | `CONSOLIDATION_CD` | DOUBLE |  |  | Determines whether an CONS_BO_SCHED_ID based on this template will be consolidated. |
| 9 | `CONS_BO_SCHED_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 10 | `CYCLE_DAY` | DOUBLE | NOT NULL |  | Day of the month on which statement will be generated. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `GUARANTOR_ACCESS_CODE` | VARCHAR(250) |  |  | Guarantor's access code to be entered when using on line bill payment - quick payment option. |
| 13 | `LAST_BILL_DT_TM` | DATETIME |  |  | Date of the last bill |
| 14 | `NEXT_BILL_DT_TM` | DATETIME |  |  | Date on which the next bill will be send. |
| 15 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Candidate key reference to the organization table. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `PROC_IND` | DOUBLE |  |  | Indicator that is turned on when the nightly batch has processed the cons_bo_sched. Turned off by statement generation process |
| 18 | `RC_CONT_PROCESS_ID` | DOUBLE | NOT NULL | FK→ | Stores continous workflow process id if the statement generated through continous workflow instead of legacy statement cycle. |
| 19 | `RESTART_STMT_CYCLE_IND` | DOUBLE | NOT NULL |  | Indicates whether the restart is monthly or FPP on monthly. |
| 20 | `STATEMENT_CYCLE_ID` | DOUBLE | NOT NULL |  | Foreign key to the statment cycle - this is the current cycle |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_GROUP_ID` | [BILLING_ENTITY_GROUP](BILLING_ENTITY_GROUP.md) | `BILLING_ENTITY_GROUP_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RC_CONT_PROCESS_ID` | [RC_CONT_PROCESS](RC_CONT_PROCESS.md) | `RC_CONT_PROCESS_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BENEFIT_ORDER](BENEFIT_ORDER.md) | `CONS_BO_SCHED_ID` |
| [CBOS_PERSON_RELTN](CBOS_PERSON_RELTN.md) | `CONS_BO_SCHED_ID` |
| [CBOS_PE_RELTN](CBOS_PE_RELTN.md) | `CONS_BO_SCHED_ID` |

