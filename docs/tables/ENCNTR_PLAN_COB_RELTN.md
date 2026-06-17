# ENCNTR_PLAN_COB_RELTN

> The encounter health plan-coordination of benefits relationship table defines the set of encounter health plans that are a part of a particular insurance coordination of benefits set and their priority within the coordination of benefits set.

**Description:** Encounter Plan Coordination of Benefits Relationship  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_PLAN_COB_RELTN_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ENCNTR_PLAN_COB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter health plan coordination of benefits. |
| 6 | `ENCNTR_PLAN_COB_RELTN_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a relationship between an encounter health plan and a particular insurance coordination of benefits set. |
| 7 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter health plan relationship. |
| 8 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | This is a numeric number used to represent the order in which to consider this health plan for reimbursement for this insurance coordination of benefits, if the person is a member of more than one health plan. The priority_seq is 1-based. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PLAN_COB_ID` | [ENCNTR_PLAN_COB](ENCNTR_PLAN_COB.md) | `ENCNTR_PLAN_COB_ID` |
| `ENCNTR_PLAN_RELTN_ID` | [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_PLAN_COB_R_HIST](ENCNTR_PLAN_COB_R_HIST.md) | `ENCNTR_PLAN_COB_RELTN_ID` |

