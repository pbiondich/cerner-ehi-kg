# CHARGE_TRANS_LOG

> Charge Services API transaction log table.

**Description:** Charge Transaction Log  
**Table type:** ACTIVITY  
**Primary key:** `CHARGE_TRANS_LOG_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLG` | DOUBLE |  |  | The flag to indicate the type of a charge transaction |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 6 | `CHARGE_TRANS_LOG_ID` | DOUBLE | NOT NULL | PK | A system generated number used to uniquely identify a row on the CHARGE_TRANS_LOG table. |
| 7 | `CHARGE_TRANS_UUID` | VARCHAR(100) |  |  | Unique identifier for charge transactions. |
| 8 | `CLIENT_UUID` | VARCHAR(100) |  |  | Unique identifier for the client |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE |  |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was created. |
| 11 | `ENCNTR_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the Encounter table. |
| 12 | `RELATED_CHARGE_ITEM_ID` | DOUBLE |  | FK→ | The charge item id to which the transaction is related |
| 13 | `RELATED_CHARGE_TRANS_LOG_ID` | DOUBLE |  | FK→ | The charge transaction log id to which this transaction is related. |
| 14 | `STATUS_FLG` | DOUBLE |  |  | The flag to indicate the status of a charge transaction |
| 15 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `RELATED_CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |
| `RELATED_CHARGE_TRANS_LOG_ID` | [CHARGE_TRANS_LOG](CHARGE_TRANS_LOG.md) | `CHARGE_TRANS_LOG_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CHARGE_TRANS_LOG](CHARGE_TRANS_LOG.md) | `RELATED_CHARGE_TRANS_LOG_ID` |

