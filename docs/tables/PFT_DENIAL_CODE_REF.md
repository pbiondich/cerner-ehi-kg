# PFT_DENIAL_CODE_REF

> This table store information related to each HIPPA related Denial code in the system.

**Description:** Stores information related to each HIPPA related Denial code in the system.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTOWRITEOFF_IND` | DOUBLE | NOT NULL |  | If the value is 1 then this denial will cause the associated claim to be written off. |
| 2 | `DENIAL_CD` | DOUBLE | NOT NULL |  | Denial Code |
| 3 | `DENIAL_GROUP_CD` | DOUBLE | NOT NULL |  | Grouping mechanism for the Denial codes. |
| 4 | `DENIAL_TYPE_CD` | DOUBLE | NOT NULL |  | This defines the base type of the denial code. Provider, Patient, Technical, Information Only |
| 5 | `DIRECT_TO_NON_AR_IND` | DOUBLE | NOT NULL |  | The indicator denoting a transaction is posted directly to non Account Receivable. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 7 | `PFT_DENIAL_CODE_REF_ID` | DOUBLE | NOT NULL |  | Unique Identifier |
| 8 | `POST_NO_POST_METHOD_FLAG` | DOUBLE | NOT NULL |  | The transaction posting method flag 0 - post primary, post secondary, post tertiary; 1 - no post primary, no post secondary, no post tertiary; 2 - post primary, no post secondary, post tertiary; 3 - post primary, no post secondary, no post tertiary; 4 - post primary, post secondary, no post tertiary; 5 - no post priamry, no post secondary, post tertiary; 6 - no post primary, post secondary, no post tertiary; 7 - no post primary, post secondary, post tertiary |
| 9 | `PRIORITY_LEVEL` | DOUBLE | NOT NULL |  | Ranking mechanism for Denial Decision making process. |
| 10 | `PROCESS_IND` | DOUBLE | NOT NULL |  | If the value is 1 then this denial should process as specified by its denial_type_cd, 0 will behave as if it is an information only denial. |
| 11 | `REVERSE_EXPECTED_IND` | DOUBLE | NOT NULL |  | The indicator denoting a transaction reversal is expected. |
| 12 | `TRANS_ALIAS_CD` | DOUBLE | NOT NULL |  | If this denial code causes write-offs, this is the Transaction Alias to use for the write-off transaction. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `X12_CODE` | VARCHAR(250) | NOT NULL |  | Custom X12 Alias for denial code |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

