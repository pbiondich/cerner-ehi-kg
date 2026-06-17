# ORG_TRANS_URL_RELTN

> The table is used to store the different urls configured by organizations to make different transactions.

**Description:** ORGANIZATION TRANSACTION URL RELATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the org_trans_cc_reltn table. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the person responsible for creating a row in the org_trans_cc_reltn table. |
| 4 | `ORG_TRANS_IDENT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 5 | `ORG_TRANS_URL_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `TRANSACTION_URL_CD` | DOUBLE | NOT NULL | FK→ | Transaction URL class is used to categorize different url types into more general groups than transaction url type. (i.e., synchronous virtual terminal, virtual terminal url, bill pay EDI url, submitter reference url). The values in this codeset all have Cerner defined meanings. |
| 7 | `TRANSACTION_URL_TEXT` | LONGTEXT |  |  | The value of the transaction url to be stored for transaction |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORG_TRANS_IDENT_ID` | [ORG_TRANS_IDENT](ORG_TRANS_IDENT.md) | `ORG_TRANS_IDENT_ID` |
| `TRANSACTION_URL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

