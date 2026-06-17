# DEPOSIT_ACCT

> A deposit account is owned by a financial institution and will not be stored on the account table.

**Description:** Deposit Account  
**Table type:** REFERENCE  
**Primary key:** `DEPOSIT_ACCT_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DEPOSIT_ACCT_CUR_CD` | DOUBLE | NOT NULL |  | Holds the Currency type of the Deposit Account |
| 7 | `DEPOSIT_ACCT_DESC` | VARCHAR(200) |  |  | A description of the deposit account. |
| 8 | `DEPOSIT_ACCT_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for the Deposit_Acct_ID table. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXT_ACCT_ID_TXT` | VARCHAR(50) |  |  | The Account ID as identified by the financial institution. |
| 11 | `EXT_ACCT_ID_TXT_KEY` | VARCHAR(250) |  |  | Key Field for Ext_Acct_ID_Txt. This field can be indexed. |
| 12 | `GLOBAL_IND` | DOUBLE |  |  | Indicates whether the account is used by all billing entities. |
| 13 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The financial institution off the Organization table. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEPOSIT_RECORD](DEPOSIT_RECORD.md) | `DEPOSIT_ACCT_ID` |

