# SI_UNMTCHD_PRSN_QUE_RELTN

> This table relates inbound messages to unmatched person information

**Description:** System Integration Person Queue Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGE_DT_TM` | DATETIME |  |  | The date of the inbound message. |
| 2 | `MESSAGE_EVENT_TXT` | VARCHAR(100) | NOT NULL |  | Message event from the inbound message |
| 3 | `MESSAGE_TYPE_TXT` | VARCHAR(100) | NOT NULL |  | Message type from the inbound message |
| 4 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | Status of unmatched person record |
| 5 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Queue ID from cqm_oeninterface_que |
| 6 | `SI_TRANSACTION_ID` | DOUBLE |  | FK→ | The transaction associated with the inbound message |
| 7 | `SI_UNMTCHD_PRSN_QUE_ID` | DOUBLE | NOT NULL |  | Foreign Key to si_unmatched_person_que |
| 8 | `SI_UNMTCHD_PRSN_QUE_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `SI_TRANSACTION_ID` | [SI_TRANSACTION](SI_TRANSACTION.md) | `SI_TRANSACTION_ID` |

