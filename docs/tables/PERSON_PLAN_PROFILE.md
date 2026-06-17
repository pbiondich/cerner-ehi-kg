# PERSON_PLAN_PROFILE

> The person health plan profile table defines a set of health plan insurance profiles for a patient

**Description:** Person Plan Profile  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PLAN_PROFILE_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this plan profile. |
| 6 | `PERSON_PLAN_PROFILE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a set of health plan insurance profiles for a person. This table along with the person plan profile relationship table can be used to order and group person health plan coverages into reimbursement units that can then be used as templates for the encounter health plan coverage. |
| 7 | `PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of health insurance profile for the person plan profile row (i.e., professional, institutional, workmen's comp). |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PERSON_PLAN_PROFILE_HIST](PERSON_PLAN_PROFILE_HIST.md) | `PERSON_PLAN_PROFILE_ID` |
| [PERSON_PLAN_PROFILE_RELTN](PERSON_PLAN_PROFILE_RELTN.md) | `PERSON_PLAN_PROFILE_ID` |
| [PERSON_PLAN_PROFILE_R_HIST](PERSON_PLAN_PROFILE_R_HIST.md) | `PERSON_PLAN_PROFILE_ID` |
| [SCH_EVENT_PATIENT](SCH_EVENT_PATIENT.md) | `PERSON_PLAN_PROFILE_ID` |

