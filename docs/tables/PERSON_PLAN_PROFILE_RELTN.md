# PERSON_PLAN_PROFILE_RELTN

> The person health plan-profile relationship table defines the set of person health plans that are a part of a particular insurance profile and their priority within the profile.

**Description:** Person Plan Profile Relationship  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PLAN_PROFILE_RELTN_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PERSON_PLAN_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the person health plan profile table. |
| 6 | `PERSON_PLAN_PROFILE_RELTN_ID` | DOUBLE | NOT NULL | PK | A person health plan-profile relationship defines the set of person health plans that are a part of a particular insurance profile and their priority within the profile. |
| 7 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the person_plan_reltn table. |
| 8 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | This is a numeric number used to represent the order in which to consider this health plan for reimbursement for this insurance profile, if the person is a member of more than one health plan. The priority_seq is 1-based. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_PLAN_PROFILE_ID` | [PERSON_PLAN_PROFILE](PERSON_PLAN_PROFILE.md) | `PERSON_PLAN_PROFILE_ID` |
| `PERSON_PLAN_RELTN_ID` | [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_PLAN_PROFILE_R_HIST](PERSON_PLAN_PROFILE_R_HIST.md) | `PERSON_PLAN_PROFILE_RELTN_ID` |

