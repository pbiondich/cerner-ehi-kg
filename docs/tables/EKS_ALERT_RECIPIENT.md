# EKS_ALERT_RECIPIENT

> eks alert recipient

**Description:** eks alert recipient  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_ID` | DOUBLE | NOT NULL | FK→ | alert id |
| 2 | `ALERT_SEQ` | DOUBLE | NOT NULL |  | alert sequence |
| 3 | `EKS_ALERT_RECIPIENT_ID` | DOUBLE | NOT NULL |  | eks alert recipient identifier |
| 4 | `FAILURE_REASON` | VARCHAR(100) |  |  | failure reason |
| 5 | `MSG_TYPE_CD` | DOUBLE | NOT NULL |  | message type code |
| 6 | `PARENT_ENTITY2_ID` | DOUBLE | NOT NULL |  | parent entity identifier |
| 7 | `PARENT_ENTITY2_NAME` | VARCHAR(30) | NOT NULL |  | Parent entity 2 name |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent entity identifier |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Parent Entity |
| 10 | `RECIPIENT_NAME` | VARCHAR(100) |  |  | recipient name |
| 11 | `UNACK_COMMENT` | VARCHAR(2000) |  |  | unacknowledged comment |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALERT_ID` | [EKS_ALERT_ESCALATION](EKS_ALERT_ESCALATION.md) | `ALERT_ID` |

