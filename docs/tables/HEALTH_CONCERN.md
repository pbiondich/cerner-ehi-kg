# HEALTH_CONCERN

> Health Concerns of Patients outside of Family or Social Histories

**Description:** HEALTH CONCERNS  
**Table type:** ACTIVITY  
**Primary key:** `HEALTH_CONCERN_ID`  
**Columns:** 31  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CATEGORY_CD` | DOUBLE | NOT NULL |  | Defines the type of health concern. (transportation, pyschosocial etc) from code set 4270007 |
| 7 | `COMMENTS` | VARCHAR(500) |  |  | COMMENTS |
| 8 | `CONCERNED_PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | the individual with a health concern for the patient. Value from code set 12023 |
| 9 | `DESCRIPTION` | VARCHAR(500) | NOT NULL |  | The concern associated to the patient |
| 10 | `DOCUMENTED_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter on which the health concern was documented |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `HEALTH_CONCERN_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains a value (pulled from the sequence) which groups Health Concerns. |
| 13 | `HEALTH_CONCERN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 14 | `HEALTH_CONCERN_INSTANCE_UUID` | VARCHAR(255) | NOT NULL |  | INSTANCE UNIQUE IDENTIFIER |
| 15 | `HEALTH_CONCERN_UUID` | VARCHAR(255) | NOT NULL |  | Used to version related health concerns. |
| 16 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time this row was last updated by personnel. |
| 17 | `LAST_UPDT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the encounter on which the health concern is last updated. |
| 18 | `LAST_UPDT_ID` | DOUBLE | NOT NULL | FK→ | Identification of the person who performed the Last Update on this row. |
| 19 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The Nomenclature term that was searched by a user to add the health concern. |
| 20 | `ONSET_DT_TM` | DATETIME |  |  | Absolute Date for the Concern Onset |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person identifier |
| 22 | `RECORDED_DT_TM` | DATETIME |  |  | DATE AND TIME THE C ONCERN WAS RECORDED |
| 23 | `RECORDED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | PERSON WHO RECORDED THE CONCERN |
| 24 | `RESOLVED_DT_TM` | DATETIME |  |  | DATE The Concern was Resolved |
| 25 | `RESOLVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The USER shom marked the health concern as resolved |
| 26 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the health concern. (active, inactive, resolved, canceled) |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOCUMENTED_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_CONCERN_GROUP_ID` | [HEALTH_CONCERN](HEALTH_CONCERN.md) | `HEALTH_CONCERN_ID` |
| `LAST_UPDT_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LAST_UPDT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RECORDED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESOLVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HEALTH_CONCERN](HEALTH_CONCERN.md) | `HEALTH_CONCERN_GROUP_ID` |

