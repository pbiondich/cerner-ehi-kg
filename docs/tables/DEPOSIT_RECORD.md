# DEPOSIT_RECORD

> Stores information about the deposit itself

**Description:** Deposit Record  
**Table type:** ACTIVITY  
**Primary key:** `DEPOSIT_RECORD_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Unique Identifier and Foreign Key to the Corsp_Log Table. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DEPOSIT_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The account that the deposit was made. |
| 8 | `DEPOSIT_AMOUNT` | DOUBLE |  |  | The amount of the deposit. |
| 9 | `DEPOSIT_DT_TM` | DATETIME |  |  | The Date and Time of the deposit |
| 10 | `DEPOSIT_RECORD_ID` | DOUBLE | NOT NULL | PK | Unique Identifier |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EXT_DEPOSIT_NBR_TXT` | VARCHAR(40) |  |  | Textual identifier of the deposit number given by an outside source. |
| 13 | `ITEM_CNT` | DOUBLE |  |  | The total number of checks in the deposit. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [CORSP_LOG](CORSP_LOG.md) | `ACTIVITY_ID` |
| `DEPOSIT_ACCT_ID` | [DEPOSIT_ACCT](DEPOSIT_ACCT.md) | `DEPOSIT_ACCT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEP_REC_BATCH_TRANS_RELTN](DEP_REC_BATCH_TRANS_RELTN.md) | `DEPOSIT_RECORD_ID` |

