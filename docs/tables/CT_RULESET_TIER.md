# CT_RULESET_TIER

> Charge Transformation Ruleset Tier table

**Description:** This table holds the relationship between tiers and rulesets.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CT_RULESET_CD` | DOUBLE | NOT NULL |  | This is a user defined code value from code set 18829 that is the name of the rule set. |
| 7 | `CT_RULESET_TIER_ID` | DOUBLE | NOT NULL |  | This is the unique primary identifier of the ct_ruleset_tier table. It is an internal system assigned number. |
| 8 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Value from code_set 71 that indicated whether the encounter is inpatient, outpatient etc. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXCLUDE_ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Exclusion encounter type for tier rule |
| 11 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Patient's finacial class from code set 354. |
| 12 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier from the health_plan table. |
| 13 | `INS_ORG_ID` | DOUBLE | NOT NULL | FK→ | This column will store the insurance organization id for the given tier. |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Indicates the client organization associated with this charge. |
| 15 | `PRIORITY` | DOUBLE |  |  | This is the priority for the rule |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INS_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

