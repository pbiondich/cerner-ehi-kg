# RCM_MSG_CENTER_COMM

> Stores a record of Message Center communication from care management solution.

**Description:** RevWorks Care Management Message Center Communication  
**Table type:** ACTIVITY  
**Primary key:** `RCM_MSG_CENTER_COMM_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the actual communication text. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the communication row is related. (i.e., encntr_clin_sec_review_id, rcm_doc_review_id, etc.) |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table to which this communication row is related (i.e., encntr_clin_sec_review, rcm_doc_review, etc.) |
| 4 | `RCM_MSG_CENTER_COMM_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a record of Message Center communication from care management solution. |
| 5 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel that sent the document to the Message Center. |
| 6 | `SENT_DT_TM` | DATETIME |  |  | Date and time that the document was sent. |
| 7 | `TASK_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the task created and returned from Message Center. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_MSG_CENTER_COMM_RELTN](RCM_MSG_CENTER_COMM_RELTN.md) | `RCM_MSG_CENTER_COMM_ID` |

