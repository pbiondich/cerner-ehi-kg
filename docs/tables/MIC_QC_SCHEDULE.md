# MIC_QC_SCHEDULE

> This reference table contains a record for each microbiology QC schedule

**Description:** Microbiology Quality Control Schedule  
**Table type:** REFERENCE  
**Primary key:** `SCHEDULE_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `SCHEDULE_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value that identifies the QC schedule |
| 6 | `SCHEDULE_NAME` | VARCHAR(40) | NOT NULL |  | This field contains the unique name for the QC schedule |
| 7 | `SCHEDULE_NAME_KEY` | VARCHAR(40) | NOT NULL |  | This field is the same as the schedule_name field, only converted to uppercase |
| 8 | `SCHEDULE_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | SCHEDULE_NAME_KEY_A_NLS column |
| 9 | `SCHEDULE_NAME_KEY_NLS` | VARCHAR(82) | NOT NULL |  | NLS form of the schedule name key. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_QC_ITEM](MIC_QC_ITEM.md) | `SCHEDULE_ID` |
| [MIC_QC_NODE](MIC_QC_NODE.md) | `SCHEDULE_ID` |
| [MIC_QC_SCHEDULE_SEGMENT](MIC_QC_SCHEDULE_SEGMENT.md) | `SCHEDULE_ID` |

