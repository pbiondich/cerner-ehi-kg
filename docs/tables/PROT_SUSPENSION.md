# PROT_SUSPENSION

> This table contains information about suspsion of accrual on a protocol

**Description:** PROT SUSPENSION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COMMENT_TXT` | LONGBLOB |  |  | This field contains an explanation of the reasons the protocol was closed for accrual. |
| 3 | `CT_MILESTONES_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the milestone that resulted in the protocol being suspended |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the amendment being suspended |
| 6 | `PROT_SUSPENSION_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the prot_suspension table. It is an internal system assigned number. |
| 7 | `REASON_CD` | DOUBLE | NOT NULL |  | The reason for suspension |
| 8 | `REASON_FOR_CORRESPONDENCE_CD` | DOUBLE | NOT NULL |  | Indicates the reason for correspondence |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_MILESTONES_ID` | [CT_MILESTONES](CT_MILESTONES.md) | `CT_MILESTONES_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

