# SI_DIRECT_RECIPIENT

> Audit of recipients of a direct message.

**Description:** System Integration Direct Message Recipient  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RECIPIENT_ADDRESS` | VARCHAR(100) | NOT NULL |  | The email address of the recipient |
| 2 | `RECIPIENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Millennium id of the recipient. Only applicable on inbound Direct Messages |
| 3 | `RECIPIENT_ENTITY_NAME` | VARCHAR(30) |  |  | The name of the table the recipient entity id is from. Only applicable on inbound Direct messages. |
| 4 | `RECIPIENT_STATUS_DT_TM` | DATETIME |  |  | The date and time that the recipient status was updated. |
| 5 | `RECIPIENT_STATUS_TXT` | VARCHAR(20) | NOT NULL |  | The current known status for the Direct message for the corresponding recipient. Will only be update for Outbound and only if configured to update on delivery notifications. |
| 6 | `RECIPIENT_TYPE_TXT` | VARCHAR(20) | NOT NULL |  | The type of email recipient (ie: To, CC, BC) |
| 7 | `SI_DIRECT_MESSAGE_ID` | DOUBLE | NOT NULL | FK→ | Identifier to link the recipient to the si_direct_message table |
| 8 | `SI_DIRECT_RECIPIENT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_DIRECT_MESSAGE_ID` | [SI_DIRECT_MESSAGE](SI_DIRECT_MESSAGE.md) | `SI_DIRECT_MESSAGE_ID` |

