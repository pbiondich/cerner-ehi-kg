# SI_TRANSACTION

> Details and processing status about inbound or outbound interface transactionS

**Description:** System Integration Transaction  
**Table type:** ACTIVITY  
**Primary key:** `SI_TRANSACTION_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACKNOWLEDGEMENT_FLAG` | DOUBLE | NOT NULL |  | State of acknowledgement of the transaction by the user 0 = Not Acknowledged, 1 = Acknowledged |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Associated encntr_id of the transaction (if applicable) |
| 3 | `END_DT_TM` | DATETIME |  |  | Completion time of the transaction |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Associated person_id of the transaction (if applicable) |
| 5 | `SI_TRANSACTION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `SI_TRANSACTION_SET_ID` | DOUBLE | NOT NULL | FK→ | The optional parent set of the transaction |
| 7 | `START_DT_TM` | DATETIME | NOT NULL |  | Creation time of the transaction |
| 8 | `TXN_STATUS_DETAIL_TXT` | VARCHAR(500) | NOT NULL |  | Detailed status of the transaction |
| 9 | `TXN_STATUS_TXT` | VARCHAR(12) | NOT NULL |  | Status of the transaction |
| 10 | `TXN_TYPE_TXT` | VARCHAR(12) | NOT NULL |  | Type of transaction |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SI_TRANSACTION_SET_ID` | [SI_TRANSACTION_SET](SI_TRANSACTION_SET.md) | `SI_TRANSACTION_SET_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_TRANSACTION_DETAIL](SI_TRANSACTION_DETAIL.md) | `SI_TRANSACTION_ID` |
| [SI_UNMTCHD_PRSN_QUE_RELTN](SI_UNMTCHD_PRSN_QUE_RELTN.md) | `SI_TRANSACTION_ID` |

