# SI_TRANSACTION_SET

> Set grouping of transactions on the si_transaction table

**Description:** System Integration Transaction Set  
**Table type:** ACTIVITY  
**Primary key:** `SI_TRANSACTION_SET_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACKNOWLEDGEMENT_FLAG` | DOUBLE | NOT NULL |  | State of acknowledgement of the transaction by the user 0 = Not Acknowledged, 1 = Acknowledged |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Associated encntr_id of the transaction set (if applicable) |
| 4 | `END_DT_TM` | DATETIME |  |  | Completion time of the transaction set |
| 5 | `PARENT_SI_TRANSACTION_SET_ID` | DOUBLE | NOT NULL | FK→ | The optional parent set of the transaction set |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Associated person_id of the transaction set (if applicable) |
| 7 | `RETRIEVED_FLAG` | DOUBLE | NOT NULL |  | Indicates Whether the transaction set has been retrieved. 0 = Not Retrieved 1 = Retrieved |
| 8 | `SI_TRANSACTION_SET_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 9 | `START_DT_TM` | DATETIME | NOT NULL |  | Creation time of the transaction set |
| 10 | `TXN_SET_STATUS_DETAIL_TXT` | VARCHAR(500) | NOT NULL |  | Detailed status of the transaction set |
| 11 | `TXN_SET_STATUS_TXT` | VARCHAR(12) | NOT NULL |  | Status of the transaction set |
| 12 | `TXN_SET_TYPE_TXT` | VARCHAR(12) | NOT NULL |  | Type of transaction set |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PARENT_SI_TRANSACTION_SET_ID` | [SI_TRANSACTION_SET](SI_TRANSACTION_SET.md) | `SI_TRANSACTION_SET_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SI_TRANSACTION](SI_TRANSACTION.md) | `SI_TRANSACTION_SET_ID` |
| [SI_TRANSACTION_DETAIL](SI_TRANSACTION_DETAIL.md) | `SI_TRANSACTION_SET_ID` |
| [SI_TRANSACTION_SET](SI_TRANSACTION_SET.md) | `PARENT_SI_TRANSACTION_SET_ID` |

