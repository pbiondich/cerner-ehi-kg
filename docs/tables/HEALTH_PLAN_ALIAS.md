# HEALTH_PLAN_ALIAS

> Table holding the Aliases for a particular Health Plan

**Description:** HEALTH PLAN ALIAS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(100) |  |  | The alias is an identifier for a health plan. The alias may be unique or non-unique depending on the type of alias. |
| 6 | `ALIAS_KEY` | VARCHAR(100) |  |  | This is the plan's alias in all capitals with punctuation removed. This field is used for indexing and searching for a plan by alias. |
| 7 | `ALIAS_KEY_A_NLS` | VARCHAR(400) |  |  | This column is used as the key column for non English sites. |
| 8 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of person identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CHECK_DIGIT` | DOUBLE |  |  | This is the value of the check digit calculated according to the check_digit_method_cd. If the check digit is stored as part of the alias number, which is typical, then the check digit field may be NULL. |
| 11 | `CHECK_DIGIT_METHOD_CD` | DOUBLE | NOT NULL |  | The check digit method code identifies a specific routine, using the alias field, to calculate a check digit. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 14 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 15 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `HEALTH_PLAN_ALIAS_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the health plan alias table. It is an internal system assigned number. |
| 18 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 19 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain. |
| 20 | `PLAN_ALIAS_SUB_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Alias sub type. |
| 21 | `PLAN_ALIAS_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Type of alias |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PLAN_ALIAS_SUB_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PLAN_ALIAS_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

