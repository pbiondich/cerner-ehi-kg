# ACTIVITY_LOG

> This table stores a high level view of all activity as it enters the system. An activity can be either a transaction (payment, write off, adjustment, charge) or correspondence, (bill, claim, letter,fax, email, phone call)

**Description:** Activity Log  
**Table type:** ACTIVITY  
**Primary key:** `ACTIVITY_ID`  
**Columns:** 20  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CODE` | VARCHAR(40) |  |  | User-defined code used to identify an event. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_DT_TM` | DATETIME |  |  | The date and time that the activity took place. |
| 7 | `ACTIVITY_ID` | DOUBLE | NOT NULL | PK | The primary key and will be used through out the system to track the activity. |
| 8 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies if the activity was a transaction or correspondence. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 11 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person that created record. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `EVENT_CD` | DOUBLE | NOT NULL |  | System event code value. |
| 14 | `PRODUCTIVITY_FLAG` | DOUBLE |  |  | Flag used to define if the row is used in productivity reporting. |
| 15 | `PRODUCTIVITY_WEIGHT` | DOUBLE |  |  | Assign weight of event used to measure productivity. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_EXT](BATCH_TRANS_EXT.md) | `ACTIVITY_ID` |
| [CORSP_LOG](CORSP_LOG.md) | `ACTIVITY_ID` |
| [GL_TRANS_LOG_OFFSET](GL_TRANS_LOG_OFFSET.md) | `ACTIVITY_ID` |
| [PAYMENT_DETAIL](PAYMENT_DETAIL.md) | `ACTIVITY_ID` |
| [PFT_BILL_ACTIVITY](PFT_BILL_ACTIVITY.md) | `ACTIVITY_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `ACTIVITY_ID` |
| [PFT_PRORATION_RELTN](PFT_PRORATION_RELTN.md) | `ACTIVITY_ID` |
| [PFT_TRANS_RELTN](PFT_TRANS_RELTN.md) | `ACTIVITY_ID` |
| [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |

