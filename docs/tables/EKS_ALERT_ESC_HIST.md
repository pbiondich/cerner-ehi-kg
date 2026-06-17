# EKS_ALERT_ESC_HIST

> eks alert escalation history

**Description:** eks_alert_esc_hist  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_BY_DT_TM` | DATETIME |  |  | date and time that acknowledgement must be received by. |
| 2 | `ACK_BY_ID` | DOUBLE | NOT NULL | FK→ | acknowledged by identifier |
| 3 | `ACK_COMMENT` | VARCHAR(2000) |  |  | acknowledgement comment |
| 4 | `ACK_DT_TM` | DATETIME |  |  | Acknowledgement date/time. |
| 5 | `ALERT_ID` | DOUBLE | NOT NULL |  | alert id |
| 6 | `ALERT_SEQ` | DOUBLE | NOT NULL |  | alert sequence |
| 7 | `ALERT_SOURCE` | VARCHAR(100) |  |  | alert source |
| 8 | `CLOSED_IND` | DOUBLE |  |  | Closed indicator |
| 9 | `EKS_ALERT_ESC_HIST_ID` | DOUBLE | NOT NULL |  | eks alert history identifier |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 11 | `ESCALATION_LEVEL` | DOUBLE |  |  | escalation level |
| 12 | `EXPECTATION_FLAG` | DOUBLE |  |  | flag to show that the expectation of a discern rule is met or not met. |
| 13 | `FAILURE_REASON` | VARCHAR(100) |  |  | Failure reason |
| 14 | `MSG_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | message long text identifier |
| 15 | `MSG_TYPE_CD` | DOUBLE | NOT NULL |  | message type code |
| 16 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | order that triggered the alert |
| 17 | `PARENT_ALERT_ID` | DOUBLE | NOT NULL | FK→ | alert identifier of parent alert |
| 18 | `PARENT_ENTITY2_ID` | DOUBLE | NOT NULL |  | Parent Entity 2 Identifier |
| 19 | `PARENT_ENTITY2_NAME` | VARCHAR(30) | NOT NULL |  | Parent entity 2 name |
| 20 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent entity identifier |
| 21 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Parent Entity |
| 22 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 23 | `PRIORITY` | DOUBLE |  |  | priority value |
| 24 | `RECIPIENT_NAME` | VARCHAR(100) |  |  | recipient name |
| 25 | `SEND_DT_TM` | DATETIME |  |  | date and time the alert was sent |
| 26 | `SUBJECT_PREFIX_TEXT` | VARCHAR(100) |  |  | prefix of the subject |
| 27 | `SUBJECT_TEXT` | VARCHAR(200) |  |  | text of the subject of the alert |
| 28 | `TIMER_IND` | DOUBLE | NOT NULL |  | time driven event indicator |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACK_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MSG_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PARENT_ALERT_ID` | [EKS_ALERT_ESCALATION](EKS_ALERT_ESCALATION.md) | `ALERT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

