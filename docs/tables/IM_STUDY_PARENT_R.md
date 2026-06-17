# IM_STUDY_PARENT_R

> IM STUDY PARENT R

**Description:** IM STUDY PARENT R  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IM_STUDY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the im_study table |
| 2 | `IM_STUDY_PARENT_ID` | DOUBLE | NOT NULL |  | Primary key of im_study_parent_r |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID of the parent entity |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the parent entity |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IM_STUDY_ID` | [IM_STUDY](IM_STUDY.md) | `IM_STUDY_ID` |

