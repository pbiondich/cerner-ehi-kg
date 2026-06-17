# PFT_CHRG_GRP_RPRCS_HIST

> Stores historical balances information along with encounter details that were reprocessed through WTP server.

**Description:** Profit Charge Group Reprocess History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BALANCE_STATUS_TXT` | VARCHAR(40) |  |  | State of the balance at a particular instance of time |
| 2 | `BATCH_REPROCESSING_STATUS_FLAG` | DOUBLE | NOT NULL |  | Batch reprocessing status as pending,In Progress, Error and Completed. |
| 3 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | System defined unique identifier of a benefit order. |
| 4 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related Billing Entity. |
| 5 | `BILLING_ENTITY_NAME` | VARCHAR(50) |  |  | Allows for the billing entity to have a different name than the organization that it is related to. |
| 6 | `BT_CONDITION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies each bill template condition. |
| 7 | `CHARGE_GROUP_AMT` | DOUBLE |  |  | The current amount due for this that particular balance. |
| 8 | `CHARGE_GROUP_NAME` | VARCHAR(200) |  |  | Contains the name of a particular bill template condition. |
| 9 | `CREATED_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related personnel who created the record. |
| 10 | `ENCOUNTER_ALIAS_NAME` | VARCHAR(215) |  |  | Stores the financial encounter's alias which will be used to identify the financial encounter. |
| 11 | `ENCOUNTER_BALANCE_AMT` | DOUBLE |  |  | Balance related to a profit encounter. |
| 12 | `ENCOUNTER_STATUS_TXT` | VARCHAR(40) |  |  | Encounter status identifies the state of a particular encounter type from the time it is initiated until it is complete. (i.e., temporary, preliminary, active, discharged (complete), cancelled). |
| 13 | `ENCOUNTER_TYPE_TXT` | VARCHAR(40) |  |  | Categorizes the encounter into a logical group or type. examples may include inpatient, outpatient, etc. |
| 14 | `FAILURE_REASON_FLAG` | DOUBLE |  |  | If the reprocess fail, this column displays reason why it failed. |
| 15 | `HEALTH_PLAN_NAME` | VARCHAR(100) |  |  | Name of the related health plan. |
| 16 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 17 | `PFT_CHRG_GRP_RPRCS_HIST_ID` | DOUBLE | NOT NULL |  | System Generated Number Used to Uniquely Identify a Row on PFT_CHRG_GRP_RPRCS_HIST. |
| 18 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related profit encounter record |
| 19 | `REPORT_FILE_NAME` | VARCHAR(100) |  |  | Contains file name where for reporting need after reprocess. |
| 20 | `REPROCESSING_STATUS_FLAG` | DOUBLE |  |  | Reprocessing status for each balance like Failure or Success. |
| 21 | `SLICE_GRP_VALUE` | DOUBLE | NOT NULL |  | Load balancing slice number for reprocess using WTP |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `USER_BATCH_GRP_VALUE` | DOUBLE | NOT NULL |  | User based batch number for reprocess |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BENEFIT_ORDER_ID` | [BENEFIT_ORDER](BENEFIT_ORDER.md) | `BENEFIT_ORDER_ID` |
| `BT_CONDITION_ID` | [BT_CONDITION](BT_CONDITION.md) | `BT_CONDITION_ID` |
| `CREATED_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

