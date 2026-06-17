# MIC_QC_ITEM

> This reference table contains the items that can be used and tracked for microbiology QC.

**Description:** Microbiology Quality Control Item  
**Table type:** REFERENCE  
**Primary key:** `QC_ITEM_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `MAXIMUM_SUB_NBR` | DOUBLE | NOT NULL |  | This field contains the maximum number of times a QC organism can be sub cultured. This field should only be valued if the organism_ind = 1. |
| 6 | `ORGANISM_IND` | DOUBLE | NOT NULL |  | This field indicates whether a QC item is an organism. |
| 7 | `QC_ITEM_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value that identifies the QC item. |
| 8 | `QC_ITEM_NAME` | VARCHAR(40) | NOT NULL |  | This field contains the unique name for the QC name. |
| 9 | `QC_ITEM_NAME_KEY` | CHAR(40) | NOT NULL |  | This field is the same as the QC_ITEM_NAME field, only it is converted to uppercase. |
| 10 | `QC_ITEM_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | QC_ITEM_NAME_KEY_A_NLS column |
| 11 | `QC_ITEM_NAME_KEY_NLS` | CHAR(82) | NOT NULL |  | This field is the same as the QC_ITEM_NAME_KEY field, only it is 2 x the length + 2. It is used to sort columns in non English environments. |
| 12 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key reference back to MIC_QC_SCHEDULE. |
| 13 | `SUB_MEDIA_TEXT` | VARCHAR(40) |  |  | This field contains a text description of the media being used for a QC organism. This field should only be valued if the organism_ind = 1. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCHEDULE_ID` | [MIC_QC_SCHEDULE](MIC_QC_SCHEDULE.md) | `SCHEDULE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_QC_TASK](MIC_QC_TASK.md) | `QC_ITEM_ID` |

