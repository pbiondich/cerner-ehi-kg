# STATEMENT_CYCLE

> Stores the information related to a Statement Cycle.

**Description:** Stores the information related to a statement cycle.  
**Table type:** REFERENCE  
**Primary key:** `STATEMENT_CYCLE_ID`  
**Columns:** 22  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the billing_entity table. |
| 7 | `BILL_CLASS_CD` | DOUBLE | NOT NULL |  | Bill Class |
| 8 | `BILL_SEQ` | DOUBLE | NOT NULL |  | The sequence in which the schedule is done. |
| 9 | `CYCLE` | DOUBLE | NOT NULL |  | Then number of days between bills. |
| 10 | `CYCLE_NAME` | VARCHAR(100) |  |  | descriptive name of the cycle |
| 11 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value indicating collections state that a ProFit encounter is in (e.g. normal, collections etc.). |
| 12 | `DUNNING_LEVEL_CNT` | DOUBLE | NOT NULL |  | Indicates how many times a bill has been sent at the current dunning level code. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EXT_BILLING_IND` | DOUBLE | NOT NULL |  | Indicates if the ProFit encounter needs to be send to the outside collection agency at the given dunning level. |
| 15 | `MONTHLY_IND` | DOUBLE | NOT NULL |  | Indicator that determines whether the statement will be generated on the same day every month. |
| 16 | `STATEMENT_CYCLE_CD` | DOUBLE | NOT NULL |  | Statement Cycle Code |
| 17 | `STATEMENT_CYCLE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CBOS_PE_RELTN](CBOS_PE_RELTN.md) | `STATEMENT_CYCLE_ID` |
| [PFT_ENCNTR](PFT_ENCNTR.md) | `STATEMENT_CYCLE_ID` |
| [STATEMENT_CYCLE_RELTN](STATEMENT_CYCLE_RELTN.md) | `NEXT_CYCLE_ID` |
| [STATEMENT_CYCLE_RELTN](STATEMENT_CYCLE_RELTN.md) | `STATEMENT_CYCLE_ID` |
| [STMT_CYCLE_CHILD_RELTN](STMT_CYCLE_CHILD_RELTN.md) | `STATEMENT_CYCLE_ID` |

