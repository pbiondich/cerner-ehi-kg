# BB_QC_GRP_REAGENT_LOT

> This table maintains a list of reagents associated with a QC group.

**Description:** Blood Bank Quality Control Group Reagent Lot  
**Table type:** ACTIVITY  
**Primary key:** `GROUP_REAGENT_LOT_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CURRENT_IND` | DOUBLE | NOT NULL |  | Indicates the reagent lot that is currently available for use. |
| 5 | `DISPLAY_ORDER_SEQ` | DOUBLE | NOT NULL |  | This field contains the display order of the reagent lot within the group. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field links the reagent to the specific quality control group. |
| 8 | `GROUP_REAGENT_LOT_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies the reagent associated with a quality control Group |
| 9 | `LOT_INFORMATION_ID` | DOUBLE | NOT NULL | FK→ | This field links the reagent lot row with the actual lot information row. (PCS_LOT_INFORMATION). |
| 10 | `PREV_GROUP_REAGENT_LOT_ID` | DOUBLE | NOT NULL |  | This field contains the id of the previous version of the current row. |
| 11 | `RELATED_REAGENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the reagent relationship associated with the reagent lot. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_ID` | [BB_QC_GROUP](BB_QC_GROUP.md) | `GROUP_ID` |
| `LOT_INFORMATION_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `RELATED_REAGENT_ID` | [BB_QC_REL_REAGENT](BB_QC_REL_REAGENT.md) | `RELATED_REAGENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_QC_GRP_REAGENT_ACTIVITY](BB_QC_GRP_REAGENT_ACTIVITY.md) | `GROUP_REAGENT_LOT_ID` |

