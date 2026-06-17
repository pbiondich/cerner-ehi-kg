# RCM_TRANSACTION

> Stores transaction data for the Care Management solution.

**Description:** RevWorks Care Management - Transaction  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the long text row containing the request string. |
| 5 | `OUT_BOUND_IND` | DOUBLE | NOT NULL |  | The short indicator to show whether the transaction is outbound. 1 for outbound transaction0 for inbound transaction |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies to which row of the parent entity table this row is related. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies to which entity this row is related. |
| 8 | `PREV_RCM_TRANSACTION_ID` | DOUBLE | NOT NULL |  | Used to track versions of the RCM Transaction information. This column will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `RCM_TRANSACTION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies transaction information related to the Care Management solution. |
| 10 | `TRANSACTION_DT_TM` | DATETIME |  |  | The date and time the transaction was created. |
| 11 | `TRANSACTION_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the transaction |
| 12 | `TRANSACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the type of transaction. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

