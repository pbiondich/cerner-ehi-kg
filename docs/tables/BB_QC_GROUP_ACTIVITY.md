# BB_QC_GROUP_ACTIVITY

> This table contains the scheduled activity for specific Blood Bank QC Groups

**Description:** Blood Bank Quality Control Group Activity  
**Table type:** ACTIVITY  
**Primary key:** `GROUP_ACTIVITY_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUP_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies the group activity row |
| 2 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field links the activity row to a specific QC group (BB_QC_GROUP) |
| 3 | `LOCK_DT_TM` | DATETIME |  |  | This field contains the date and time the lock was taken. |
| 4 | `LOCK_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the personnel that is currently updating the QC result activity. |
| 5 | `RELATED_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field links the activity row to the cross-references quality control group. |
| 6 | `SCHEDULED_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the quality control group results were scheduled to be completed. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_ID` | [BB_QC_GROUP](BB_QC_GROUP.md) | `GROUP_ID` |
| `LOCK_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RELATED_GROUP_ID` | [BB_QC_GROUP](BB_QC_GROUP.md) | `GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_QC_GRP_REAGENT_ACTIVITY](BB_QC_GRP_REAGENT_ACTIVITY.md) | `GROUP_ACTIVITY_ID` |

