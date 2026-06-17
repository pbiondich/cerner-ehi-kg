# CV_DEVICE

> Stores Data related to CVNet Devices

**Description:** CVNet Devices  
**Table type:** ACTIVITY  
**Primary key:** `DEVICE_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CV_CASE_ID` | DOUBLE | NOT NULL | FK→ | This is the parent case in which the device was used. |
| 7 | `DEVICE_ID` | DOUBLE | NOT NULL | PK | This is the unique identifier for a row in the CV_DEVICE table. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `LESION_ID` | DOUBLE | NOT NULL | FK→ | This is the parent lesion on which the device was used. |
| 10 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | The clinical event that is the parent field for the device (EVENT_ID column from CLINICAL_EVENT table) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_CASE_ID` | [CV_CASE](CV_CASE.md) | `CV_CASE_ID` |
| `LESION_ID` | [CV_LESION](CV_LESION.md) | `LESION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CV_DEV_ABSTR_DATA](CV_DEV_ABSTR_DATA.md) | `DEVICE_ID` |

