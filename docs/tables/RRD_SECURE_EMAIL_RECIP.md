# RRD_SECURE_EMAIL_RECIP

> Stores the recipient information pertaining to every secure email sent by RRD.

**Description:** Remote Report Distribution Secure Email Recipients  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RECIPIENT_EMAIL_ADDRESS_TXT` | VARCHAR(100) |  |  | defines the email address that this email was sent to.; |
| 2 | `RECIPIENT_TYPE_FLAG` | DOUBLE |  |  | Indicates the type of email delivery (e.g. TO, CC, BCC).; |
| 3 | `RRD_SECURE_EMAIL_DETAIL_ID` | DOUBLE |  | FK→ | Foreign key to RRD_SECURE_EMAIL_DETAIL table, indicating the secure email this recipient was including with. |
| 4 | `RRD_SECURE_EMAIL_RECIP_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `STATUS_CD` | DOUBLE |  |  | Status of the email for this recipient. |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RRD_SECURE_EMAIL_DETAIL_ID` | [RRD_SECURE_EMAIL_DETAIL](RRD_SECURE_EMAIL_DETAIL.md) | `RRD_SECURE_EMAIL_DETAIL_ID` |

