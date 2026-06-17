# BR_BP_ACT_GROUP_R

> Stores relationship between activity groups and activity groups/activities.

**Description:** Bedrock BP Activity Group Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_STATUS` | DOUBLE |  |  | Status of the activity |
| 2 | `BR_BP_ACT_GROUP_ID` | DOUBLE | NOT NULL | FK→ | ID of the activity group |
| 3 | `BR_BP_ACT_GROUP_R_ID` | DOUBLE | NOT NULL |  | Unique ID |
| 4 | `CHILD_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the child entity |
| 5 | `CHILD_ENTITY_NAME` | VARCHAR(100) |  |  | Identifies where the child entity comes from |
| 6 | `DISPLAY_SEQ` | DOUBLE |  |  | Determines the sequence of tasks |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_BP_ACT_GROUP_ID` | [BR_BP_ACT_GROUP](BR_BP_ACT_GROUP.md) | `BR_BP_ACT_GROUP_ID` |

