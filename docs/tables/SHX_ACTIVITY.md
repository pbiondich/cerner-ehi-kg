# SHX_ACTIVITY

> Each row on the table represents patient's discrete response of an assessment made for a category.

**Description:** SHX_ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** `SHX_ACTIVITY_ID`  
**Columns:** 22  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSESSMENT_CD` | DOUBLE | NOT NULL |  | Indicates overall assessment for a category |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The is the value of the unique primary identifier of a long_text table. It is an internal system assigned number. |
| 6 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: organization_seq The field will store org id for the user who writes out the data. we will use this field to enforce person data sharing rules. |
| 7 | `ORIGINATING_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique primary identifier of the encounter table |
| 8 | `PERFORM_DT_TM` | DATETIME | NOT NULL |  | Date and time when the assessment was made. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:PERSON_ONLY_SEQ This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `SHX_ACTIVITY_GROUP_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME: PROBLEM_SEQ Non unique identifier for the SHX_ ACTIVITY table. Each change or revision made to a social history discrete response creates a new social history response instance. |
| 11 | `SHX_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | SEQUENCE NAME:PROBLEM_SEQ This is the table's primary key. The unique identifier for a shx_activity. It will be used to uniquely identify discrete response. Uniquely defines a social history discrete detail within the shx_activity table. The shx_ activity_id can be associated with multiple social history detail instances. When a new social history discrete response is added to the shx_activity table the shx_ activity_id |
| 12 | `SHX_CATEGORY_DEF_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: PROBLEM_SEQ The is the value of the unique primary identifier for a Social History category view instance on SHX_CATEGORY_DEF table. It is an internal system assigned number. |
| 13 | `SHX_CATEGORY_REF_ID` | DOUBLE | NOT NULL | FK→ | The ID value from related CAREGORY REF table. Added for performance reasons (de-normalized) to avood extra join to CATEGORY DEF table.. |
| 14 | `STATUS_CD` | DOUBLE | NOT NULL |  | Unique code value that identifies section. |
| 15 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Indicates the type of entry on the SHX_ ACTIVITY table. It can be PERSON, CATEGORY, DETAIL |
| 16 | `UNABLE_TO_OBTAIN_IND` | DOUBLE | NOT NULL |  | Indicates that assessment was not made as it was unable to obtain from the patient. |
| 17 | `UPDATE_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The most recent encounter Id to update the social history row |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIGINATING_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SHX_CATEGORY_DEF_ID` | [SHX_CATEGORY_DEF](SHX_CATEGORY_DEF.md) | `SHX_CATEGORY_DEF_ID` |
| `SHX_CATEGORY_REF_ID` | [SHX_CATEGORY_REF](SHX_CATEGORY_REF.md) | `SHX_CATEGORY_REF_ID` |
| `UPDATE_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SHX_ACTION](SHX_ACTION.md) | `SHX_ACTIVITY_ID` |
| [SHX_COMMENT](SHX_COMMENT.md) | `SHX_ACTIVITY_ID` |
| [SHX_RESPONSE](SHX_RESPONSE.md) | `SHX_ACTIVITY_ID` |
| [SHX_SEC_LBL](SHX_SEC_LBL.md) | `SHX_ACTIVITY_ID` |

