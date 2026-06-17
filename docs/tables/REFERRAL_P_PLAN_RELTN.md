# REFERRAL_P_PLAN_RELTN

> The referral-person health plan relationship table contains pointers linking a referral to person health plan relationship(s).

**Description:** Referral Person Health Plan Relationship  
**Table type:** ACTIVITY  
**Primary key:** `REFERRAL_P_PLAN_RELTN_ID`  
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
| 5 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related person_plan_reltn row. |
| 6 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The order to use this health plan relationship for reimbursement. |
| 7 | `REFERRAL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related referral. |
| 8 | `REFERRAL_P_PLAN_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the REFERRAL_P_PLAN_RELTN table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_PLAN_RELTN_ID` | [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REFERRAL_P_PLAN_AUTH_R](REFERRAL_P_PLAN_AUTH_R.md) | `REFERRAL_P_PLAN_RELTN_ID` |

