# FIN_TRANS_GROUP

> Schema to store and track the events associated to a financial transaction group.

**Description:** Financial Transaction Group  
**Table type:** ACTIVITY  
**Primary key:** `FIN_TRANS_GROUP_ID`  
**Columns:** 19  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTERNAL_IDENT` | VARCHAR(30) | NOT NULL |  | The unique identifier sent from an external entity for a Remit. |
| 8 | `EXTERNAL_NAME` | VARCHAR(30) | NOT NULL |  | The name that is used to identify from where the EXTERNAL_IDENT was sent. ("CCM: or "HDX") |
| 9 | `FIN_TRANS_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the FIN_TRANS_GROUP table. |
| 10 | `ORIG_FIN_TRANS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the financial transaction group rows. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The entity identifier that the functional transaction group is posted to. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table name that the PARENT_ENTITY_ID is associated to. ("BILL_REC" or "ENCOUTNER" or "ACCOUNT") |
| 13 | `STATUS_CD` | DOUBLE | NOT NULL |  | Defines the status of a functional transaction group. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `VERSION_SEQ` | DOUBLE | NOT NULL |  | The version sequence for the financial transaction group. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_FIN_TRANS_GROUP_ID` | [FIN_TRANS_GROUP](FIN_TRANS_GROUP.md) | `FIN_TRANS_GROUP_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `FIN_TRANS_GROUP_ID` |
| [DENIAL](DENIAL.md) | `FIN_TRANS_GROUP_ID` |
| [FIN_TRANS_GROUP](FIN_TRANS_GROUP.md) | `ORIG_FIN_TRANS_GROUP_ID` |
| [FIN_TRANS_GROUP_DETAIL](FIN_TRANS_GROUP_DETAIL.md) | `FIN_TRANS_GROUP_ID` |
| [TRANS_LOG](TRANS_LOG.md) | `FIN_TRANS_GROUP_ID` |

