# MM_XFI_CNTRCT_REBATE

> Table used to store relationships between a contract and rebates that apply to that contract. Data is moved from this table to MM_CNTRCT_REBATE.

**Description:** Contract Rebate  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACH_METRIC` | VARCHAR(60) |  |  | Achievement metric |
| 2 | `ACH_METRIC_CD` | DOUBLE | NOT NULL |  | Achievement metric code value |
| 3 | `ACH_THRESHOLD` | DOUBLE |  |  | Achievement threshold |
| 4 | `ACTION_FLAG` | DOUBLE |  |  | Achievement action flag |
| 5 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor used to resolve code value alias |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 8 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 10 | `PROCESS_FLAG` | DOUBLE |  |  | process flag |
| 11 | `REBATE_CALC_ON` | VARCHAR(60) |  |  | rebate calculated on |
| 12 | `REBATE_CALC_ON_CD` | DOUBLE | NOT NULL |  | rebate calculated on code |
| 13 | `REBATE_ID` | DOUBLE | NOT NULL | FK→ | Rebate Identifier |
| 14 | `REBATE_PERIOD` | VARCHAR(60) |  |  | rebate period |
| 15 | `REBATE_PERIOD_CD` | DOUBLE | NOT NULL |  | rebate period code |
| 16 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Transaction identifier |
| 17 | `TRANS_PARENT_ID` | DOUBLE | NOT NULL | FK→ | Transaction parent identifier |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REBATE_ID` | [MM_CNTRCT_REBATE](MM_CNTRCT_REBATE.md) | `REBATE_ID` |
| `TRANS_PARENT_ID` | [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `TRANSACTION_ID` |

