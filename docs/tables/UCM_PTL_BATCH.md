# UCM_PTL_BATCH

> This table is used to track high level protocol batch information.

**Description:** Unified Case Manager - Protocol Batch  
**Table type:** ACTIVITY  
**Primary key:** `UCM_PTL_BATCH_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Indicates when the corresponding action was taken on the protocol batch. |
| 2 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of action taken on the protocol batch. |
| 3 | `ACTION_TZ` | DOUBLE |  |  | Time Zone associated with the corresponding Action_DT_TM column. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `COMPLETE_DT_TM` | DATETIME |  |  | The complete date and time of the batch. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `ORDER_CNT` | DOUBLE | NOT NULL |  | Indicates the number of orders in this batch. Will be used to determine when one or more orders have been archived |
| 10 | `PREV_UCM_PTL_BATCH_ID` | DOUBLE | NOT NULL |  | This field is used to track versions of the protocol batch information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 11 | `PTL_BATCH_NAME` | VARCHAR(40) | NOT NULL |  | Contains the user defined name for this batch. |
| 12 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The code for the service resource for which the batch was initially defined. |
| 13 | `START_DT_TM` | DATETIME |  |  | The start date and time of the batch. |
| 14 | `UCMR_WORKSHEET_ID` | DOUBLE | NOT NULL | FK→ | Indicates the reference worksheet this batch used. |
| 15 | `UCM_PTL_BATCH_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a specific protocol batch record. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_WORKSHEET_ID` | [UCMR_WORKSHEET](UCMR_WORKSHEET.md) | `UCMR_WORKSHEET_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [UCM_PTL_BATCH_ITEM](UCM_PTL_BATCH_ITEM.md) | `UCM_PTL_BATCH_ID` |
| [UCM_PTL_FILE_DEF_HIST](UCM_PTL_FILE_DEF_HIST.md) | `UCM_PTL_BATCH_ID` |

