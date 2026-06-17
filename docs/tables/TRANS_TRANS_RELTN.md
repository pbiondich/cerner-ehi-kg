# TRANS_TRANS_RELTN

> Allows us to relate one transaction with another. (Identify what charge a payment was for, or whatcharge a write-off was for)

**Description:** Transaction Transaction Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AMOUNT` | DOUBLE |  |  | Amount of the transaction that applies to this relationship. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CHILD_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | When more than one transaction are related, generally the transaction that occurred at a later time becomes the child transaction in the relationship. |
| 8 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 9 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL |  | Unique identifier of the person that created the record. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `PARENT_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | When more than one transaction are related, generally, the original transaction becomes the parent. |
| 12 | `TRANS_RELTN_REASON_CD` | DOUBLE | NOT NULL |  | Code value indicating the reason the two or more transactions are related. |
| 13 | `TRANS_RELTN_SUB_REASON_CD` | DOUBLE | NOT NULL |  | Contains more detailed information about why the trans_reltn_reason_cd is in it's current state. |
| 14 | `TRANS_TRANS_RELTN_ID` | DOUBLE | NOT NULL |  | Trans_Trans_Reltn Sequence ID |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_ACTIVITY_ID` | [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |
| `PARENT_ACTIVITY_ID` | [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |

