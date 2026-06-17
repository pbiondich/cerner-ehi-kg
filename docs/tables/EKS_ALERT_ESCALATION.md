# EKS_ALERT_ESCALATION

> EKS ALERT ESCALATION

**Description:** EKS ALERT ESCALATION  
**Table type:** ACTIVITY  
**Primary key:** `ALERT_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_BY_DT_TM` | DATETIME |  |  | date and time that acknowledgement must be received by. |
| 2 | `ALERT_ID` | DOUBLE | NOT NULL | PK | alert id |
| 3 | `ALERT_SOURCE` | VARCHAR(100) |  |  | alert source |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 5 | `ESCALATION_LEVEL` | DOUBLE |  |  | escalation level |
| 6 | `MSG_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | message long text identifier |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | order that triggered the alert |
| 8 | `PARENT_ALERT_ID` | DOUBLE | NOT NULL |  | alert identifier of parent alert |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `PRIORITY` | DOUBLE |  |  | message priority |
| 11 | `PROCESS_FLAG` | DOUBLE |  |  | process flag |
| 12 | `SEND_DT_TM` | DATETIME |  |  | date and time the alert was sent |
| 13 | `SUBJECT_PREFIX_TEXT` | VARCHAR(100) |  |  | prefix of the subject |
| 14 | `SUBJECT_TEXT` | VARCHAR(200) |  |  | text of the subject of the alert |
| 15 | `TIMER_IND` | DOUBLE | NOT NULL |  | time driven event indicator |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MSG_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EKS_ALERT_ESC_HIST](EKS_ALERT_ESC_HIST.md) | `PARENT_ALERT_ID` |
| [EKS_ALERT_RECIPIENT](EKS_ALERT_RECIPIENT.md) | `ALERT_ID` |

