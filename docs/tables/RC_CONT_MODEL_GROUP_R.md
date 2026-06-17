# RC_CONT_MODEL_GROUP_R

> Relates a model group to models.

**Description:** Revenue Cycle Continuity Model Group Relationship  
**Table type:** REFERENCE  
**Primary key:** `RC_CONT_MODEL_GROUP_R_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `ORIG_RC_CONT_MODEL_GROUP_R_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of a revenue cycle continuity model group relationship. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 5 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority of the related model in the group. Lower sequence values indicate higher priority. The highest priority model will take precedence when the model group is started, falling back to lower priority models if the business rules don't trigger. |
| 6 | `RC_CONT_MODEL_DRAFT_ID` | DOUBLE | NOT NULL | FK→ | Contains the unique identifier of the related draft model associated with the group. |
| 7 | `RC_CONT_MODEL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related continuity model group. |
| 8 | `RC_CONT_MODEL_GROUP_R_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the rc_cont_model_group_r table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_RC_CONT_MODEL_GROUP_R_ID` | [RC_CONT_MODEL_GROUP_R](RC_CONT_MODEL_GROUP_R.md) | `RC_CONT_MODEL_GROUP_R_ID` |
| `RC_CONT_MODEL_DRAFT_ID` | [RC_CONT_MODEL](RC_CONT_MODEL.md) | `RC_CONT_MODEL_ID` |
| `RC_CONT_MODEL_GROUP_ID` | [RC_CONT_MODEL_GROUP](RC_CONT_MODEL_GROUP.md) | `RC_CONT_MODEL_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_CONT_MODEL_GROUP_R](RC_CONT_MODEL_GROUP_R.md) | `ORIG_RC_CONT_MODEL_GROUP_R_ID` |

