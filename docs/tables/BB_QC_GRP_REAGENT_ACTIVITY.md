# BB_QC_GRP_REAGENT_ACTIVITY

> This table contains the activity for each reagent associated with a specific Blood Bank Quality Control Group.

**Description:** Blood Bank Quality Control Group Reagent Activity  
**Table type:** ACTIVITY  
**Primary key:** `GROUP_REAGENT_ACTIVITY_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the activity was recorded. |
| 2 | `ACTIVITY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the personnel that recorded the activity. |
| 3 | `GROUP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | This field links the reagent activity row with a specific group activity row. |
| 4 | `GROUP_REAGENT_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies the reagent activity row. |
| 5 | `GROUP_REAGENT_LOT_ID` | DOUBLE | NOT NULL | FK→ | This field links the reagent activity to a specific reagent lot. |
| 6 | `INTERPRETATION_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the reagent final interpretation. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VISUAL_INSPECTION_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the reagent visual inspection outcome. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `GROUP_ACTIVITY_ID` | [BB_QC_GROUP_ACTIVITY](BB_QC_GROUP_ACTIVITY.md) | `GROUP_ACTIVITY_ID` |
| `GROUP_REAGENT_LOT_ID` | [BB_QC_GRP_REAGENT_LOT](BB_QC_GRP_REAGENT_LOT.md) | `GROUP_REAGENT_LOT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BB_QC_RESULT](BB_QC_RESULT.md) | `CONTROL_ACTIVITY_ID` |
| [BB_QC_RESULT](BB_QC_RESULT.md) | `ENHANCEMENT_ACTIVITY_ID` |
| [BB_QC_RESULT](BB_QC_RESULT.md) | `GROUP_REAGENT_ACTIVITY_ID` |

