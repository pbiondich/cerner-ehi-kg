# REF_DATAPOINT

> Defines a point in a reference dataset

**Description:** Reference Data Point  
**Table type:** REFERENCE  
**Primary key:** `REF_DATAPOINT_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This represent the sequence number of the last entry in REF_DATAPOINT_HIST. |
| 8 | `REF_DATAPOINT_ID` | DOUBLE | NOT NULL | PK | This will be the table's primary key. |
| 9 | `REF_DATASET_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key to the REF_DATASET table. Each data point belongs to exactly one dataset. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `X_VAL` | DOUBLE | NOT NULL |  | This is the X value of the datapoint. The unit of measure will be the unit code of the first section of the X axis in the CHART_DEFINITION table. |
| 16 | `Y_VAL` | DOUBLE | NOT NULL |  | This is the Y value of the datapoint. The unit of measure will be the unit code of the y axis in the CHART_DEFINITION table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REF_DATASET_ID` | [REF_DATASET](REF_DATASET.md) | `REF_DATASET_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REF_DATAPOINT_HIST](REF_DATAPOINT_HIST.md) | `REF_DATAPOINT_ID` |

