# SCD_STORY_CONCEPT

> Relation table used to associate a story with concepts.

**Description:** Story - Concept relation table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | The cki of the concept associated to a story. |
| 2 | `CONCEPT_DISPLAY` | VARCHAR(255) |  |  | Display to be used for the concept |
| 3 | `CONCEPT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores the classification of the concept and is a bit-wise indicator to distinguish multiple classifications. |
| 4 | `DIAGNOSIS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Stores the Diagnosis ID from the DIAGNOSIS table so that the concept can be identified if inactivated. |
| 5 | `SCD_STORY_CONCEPT_ID` | DOUBLE | NOT NULL |  | Primary key for the table From SCD Sequence |
| 6 | `SCD_STORY_ID` | DOUBLE | NOT NULL | FK→ | The story to be associated to a concept. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAGNOSIS_GROUP_ID` | [DIAGNOSIS](DIAGNOSIS.md) | `DIAGNOSIS_ID` |
| `SCD_STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |

