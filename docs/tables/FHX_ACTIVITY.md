# FHX_ACTIVITY

> Each row on the table represents a Family member's condition

**Description:** Family History Activity  
**Table type:** ACTIVITY  
**Primary key:** `FHX_ACTIVITY_ID`  
**Columns:** 27  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COURSE_CD` | DOUBLE | NOT NULL |  | CODE SET: 12039 Describes the progress of the condition, e.g. Improving, stable, or worsening. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FHX_ACTIVITY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Non unique identifier for the FHX_ ACTIVITY table. Each change or revision made to a family history detail creates a new family history detail instance. |
| 9 | `FHX_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | this is the table's primary key. The unique identifier for a FHX_ACTIVITY. It will be used to uniquely identify a family member's condition. Uniquely defines a family history detail within the FHX_ ACTIVITY table. The FHX_ ACTIVITY_ID can be associated with multiple family history detail instances. When a new family history detail is added to the FHX_ ACTIVITY table the FHX_ ACTIVITY_ID is assigned to the FHX_ ACTIVITY_GROUP_ID. |
| 10 | `FHX_VALUE_FLAG` | DOUBLE | NOT NULL |  | Indicates weather the condition for a Family member is positive, negative or unknown. 0 = Negative; 1 = Positive; 2 = Unknown; 3 = Unable to Obtain; 4 = Patient Adopted |
| 11 | `LIFE_CYCLE_STATUS_CD` | DOUBLE | NOT NULL |  | CODE SET: 12030 The current status of the condition. e.g. Active, Cancelled, Inactive, Resolved. |
| 12 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for nomenclature item. Any clinically relevant subject to describe in relations to the family member. |
| 13 | `ONSET_AGE` | DOUBLE |  |  | Age at Onset |
| 14 | `ONSET_AGE_PREC_CD` | DOUBLE | NOT NULL |  | CODE SET:25320 Indicated to what level of accuracy the onset date time has been set. |
| 15 | `ONSET_AGE_UNIT_CD` | DOUBLE | NOT NULL |  | Onset age unit code from codeset 340 |
| 16 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The field will store org id for the user who writes out the data. We will use this field to enforce person data sharing rules. |
| 17 | `ORIGINATING_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique primary identifier of the encounter table |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 19 | `RELATED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Related person ID from PERSON table |
| 20 | `SEVERITY_CD` | DOUBLE | NOT NULL |  | CODE SET: 12022 Severity of a condition reported, e.g. Mild, Moderate, Severe |
| 21 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Indicates the type of entry on the FHX_ ACTIVITY table. It can be PERSON, RELTN, CONDITION |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TZ` | DOUBLE |  |  | The time zone where the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FHX_ACTIVITY_GROUP_ID` | [FHX_ACTIVITY](FHX_ACTIVITY.md) | `FHX_ACTIVITY_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIGINATING_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RELATED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [FHX_ACTION](FHX_ACTION.md) | `FHX_ACTIVITY_ID` |
| [FHX_ACTIVITY](FHX_ACTIVITY.md) | `FHX_ACTIVITY_GROUP_ID` |
| [FHX_ACTIVITY_R](FHX_ACTIVITY_R.md) | `FHX_ACTIVITY_S_ID` |
| [FHX_ACTIVITY_R](FHX_ACTIVITY_R.md) | `FHX_ACTIVITY_T_ID` |
| [FHX_LONG_TEXT_R](FHX_LONG_TEXT_R.md) | `FHX_ACTIVITY_GROUP_ID` |
| [FHX_LONG_TEXT_R](FHX_LONG_TEXT_R.md) | `FHX_ACTIVITY_ID` |

