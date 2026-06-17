# GL_TRANS_LOG_OFFSET

> Stores the adjustment information for backdated charges

**Description:** GL_TRANS_LOG_OFFSET  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_ID` | DOUBLE |  | FK→ | Uniquely identifies the account related to this row. |
| 2 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | The date on which the charge was aliased. |
| 3 | `ACTIVITY_ID` | DOUBLE |  | FK→ | Uniquely identifies the related activity log record. |
| 4 | `GL_TRANS_LOG_OFFSET_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the GL_TRANS_LOG_OFFSET table. |
| 5 | `OFFSET_AMT` | DOUBLE | NOT NULL |  | Stores the amount is to be adjusted. |
| 6 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The pft_encntr_Id related to backdated charges. |
| 7 | `SERVICE_DT_TM` | DATETIME | NOT NULL |  | The date on which the charge was queued to be aliased. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

