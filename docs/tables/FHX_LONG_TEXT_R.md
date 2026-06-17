# FHX_LONG_TEXT_R

> Each row on the table represents relationship between the Patient's History condition record and the comment. This is to track comment History on a patient's history condition.

**Description:** Family History Long Text Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_DT_TM` | DATETIME | NOT NULL |  | Comment added date time |
| 2 | `COMMENT_DT_TM_TZ` | DOUBLE | NOT NULL |  | Comment Date Time Zone |
| 3 | `COMMENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 4 | `FHX_ACTIVITY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This is the FHX_ACTIVITY_GROUP_ID value from the FHX_ACTIVITY table. |
| 5 | `FHX_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier on the FHX_ACTIVITY table. |
| 6 | `FHX_LONG_TEXT_R_ID` | DOUBLE | NOT NULL |  | This is the table's primary key. The unique identifier for a family history comment. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier on the LONG_TEXT table. It is an internal system assigned number. Comment on a patient's member condition on the long text table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FHX_ACTIVITY_GROUP_ID` | [FHX_ACTIVITY](FHX_ACTIVITY.md) | `FHX_ACTIVITY_ID` |
| `FHX_ACTIVITY_ID` | [FHX_ACTIVITY](FHX_ACTIVITY.md) | `FHX_ACTIVITY_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

