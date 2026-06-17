# RRD_SECURE_EMAIL_DETAIL

> Stores the primary information representing every secure email sent by RRD.

**Description:** Remote Report Distribution Secure Email Details  
**Table type:** ACTIVITY  
**Primary key:** `RRD_SECURE_EMAIL_DETAIL_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EMAIL_MESSAGE_CLOB` | LONGTEXT |  |  | defines the message body for the email. |
| 2 | `EMAIL_SUBJECT_TXT` | VARCHAR(255) |  |  | defines the subject for the email.; |
| 3 | `MESSAGE_IDENT` | VARCHAR(255) |  |  | A globally unique identifier defined when the email is sent. This represents the message-id field as defined by the --Internet Message Format-- standard |
| 4 | `RRD_SECURE_EMAIL_DETAIL_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `SENDER_EMAIL_ADDRESS_TXT` | VARCHAR(100) |  |  | The reference to the LONG_TEXT row that defines the email address that this email was sent from |
| 6 | `SENDER_ID` | DOUBLE |  | FK→ | Foreign key to PRSNL table, indicates the PRNSL ID who sent the email. |
| 7 | `SENT_DT_TM` | DATETIME |  |  | Date and time when the original email request was sent. |
| 8 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SENDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RRD_SECURE_EMAIL_ATTACH](RRD_SECURE_EMAIL_ATTACH.md) | `RRD_SECURE_EMAIL_DETAIL_ID` |
| [RRD_SECURE_EMAIL_RECIP](RRD_SECURE_EMAIL_RECIP.md) | `RRD_SECURE_EMAIL_DETAIL_ID` |

