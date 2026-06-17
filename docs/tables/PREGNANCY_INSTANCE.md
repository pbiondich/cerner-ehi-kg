# PREGNANCY_INSTANCE

> Stores data relating to active and historical pregnancies

**Description:** Pregnancy Instanceq  
**Table type:** ACTIVITY  
**Primary key:** `PREGNANCY_INSTANCE_ID`  
**Columns:** 24  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONFIRMED_DT_TM` | DATETIME |  |  | CONFIRMED DATE TIME |
| 7 | `CONFIRMED_TZ` | DOUBLE |  |  | Contains time zone information of confirmed_dt_tm column |
| 8 | `ENCNTR_ID` | DOUBLE |  | FK→ | Identifier for the encounter table |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `HISTORICAL_IND` | DOUBLE | NOT NULL |  | Indicates that a pregnancy was documented as past history and was never an active pregnancy. |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:ORGANIZATION_SEQ This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 12 | `OVERRIDE_COMMENT` | VARCHAR(255) |  |  | Text documenting the reason a pregnancy may not be resolved past its expected end |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | PERSON to which the pregnancy is related |
| 14 | `PREGNANCY_ID` | DOUBLE | NOT NULL | FK→ | Original instance id for a logical grouping representing a single pregnancy |
| 15 | `PREGNANCY_INSTANCE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 16 | `PREG_END_DT_TM` | DATETIME |  |  | Date/time the pregnancy was resolved, the presence of this value indicates that a pregnancy is historical rather than a currently active pregnancy |
| 17 | `PREG_START_DT_TM` | DATETIME |  |  | Date/time the pregnancy began |
| 18 | `PROBLEM_ID` | DOUBLE | NOT NULL | FK→ | PROBLEM that generally represents the pregnancy |
| 19 | `SENSITIVE_IND` | DOUBLE | NOT NULL |  | Indicates if the pregnancy needs to be handle according to rules for sensitivity |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PREGNANCY_ID` | [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PREGNANCY_INSTANCE_ID` |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | `PROBLEM_INSTANCE_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [PREGNANCY_ACTION](PREGNANCY_ACTION.md) | `PREGNANCY_ID` |
| [PREGNANCY_ACTION](PREGNANCY_ACTION.md) | `PREGNANCY_INSTANCE_ID` |
| [PREGNANCY_CHILD](PREGNANCY_CHILD.md) | `PREGNANCY_ID` |
| [PREGNANCY_CHILD](PREGNANCY_CHILD.md) | `PREGNANCY_INSTANCE_ID` |
| [PREGNANCY_ENTITY_R](PREGNANCY_ENTITY_R.md) | `PREGNANCY_ID` |
| [PREGNANCY_ENTITY_R](PREGNANCY_ENTITY_R.md) | `PREGNANCY_INSTANCE_ID` |
| [PREGNANCY_ESTIMATE](PREGNANCY_ESTIMATE.md) | `PREGNANCY_ID` |
| [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PREGNANCY_ID` |
| [PREGNANCY_SEC_LBL](PREGNANCY_SEC_LBL.md) | `PREGNANCY_ID` |

