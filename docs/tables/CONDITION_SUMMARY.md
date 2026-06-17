# CONDITION_SUMMARY

> This table stores historical summaries for a CONDITION (based on DIAGNOSIS and/or PROBLEM)

**Description:** CONDITION SUMMARY  
**Table type:** ACTIVITY  
**Primary key:** `CONDITION_SUMMARY_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONDITION_ENTITY_ID` | DOUBLE | NOT NULL |  | The condition entity the condtion summary is related or tied to. This can be a problem_id or a diagnosis_id. A PK value from the table identified in CONDITION_ENTITY_NAME. |
| 4 | `CONDITION_ENTITY_NAME` | VARCHAR(30) |  |  | The table to which the condition entity id is associated. This can be PROBLEM or DIAGNOSIS. |
| 5 | `CONDITION_SUMMARY` | LONGTEXT |  |  | The textual value of the problem summary |
| 6 | `CONDITION_SUMMARY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The parent or group id for the condition summary. This can be used as a means to version a condition summary. Contains the PK value for the initial CONDITION_SUMMARY row which begins the group |
| 7 | `CONDITION_SUMMARY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the patient to whom the condition belongs. |
| 10 | `RECORDED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who recorded the Condition summary. |
| 11 | `RECORDED_DT_TM` | DATETIME |  |  | The date and time the condition summary was recorded |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONDITION_SUMMARY_GROUP_ID` | [CONDITION_SUMMARY](CONDITION_SUMMARY.md) | `CONDITION_SUMMARY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RECORDED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CONDITION_SUMMARY](CONDITION_SUMMARY.md) | `CONDITION_SUMMARY_GROUP_ID` |

