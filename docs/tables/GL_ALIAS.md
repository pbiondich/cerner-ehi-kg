# GL_ALIAS

> User defined aliases to be associated with general ledger transactions for reporting purposes, based on user defined criteria.

**Description:** General Ledger Alias  
**Table type:** REFERENCE  
**Primary key:** `GL_ALIAS_ID`  
**Columns:** 22  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 7 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | FK to the person table |
| 8 | `DEFAULT_IND` | DOUBLE |  |  | Indicates whether the alias is the default alias for the hierarchical level indicated by the GL_ALIAS_LEVEL. 0 = Not a default; 1 = Default. |
| 9 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | The description of the alias. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `GL_ALIAS_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 12 | `GL_ALIAS_LEVEL` | DOUBLE |  |  | Indicates the hierarchical level within the general ledger to which the alias is applicable. 1 = Company Group, 2 = Company Unit, 3 = Account Name, 4 = Account Unit. |
| 13 | `GL_ALIAS_NAME` | VARCHAR(100) |  |  | The user defined alias, as it will appear on reports. |
| 14 | `GL_ALIAS_NAME_KEY` | VARCHAR(100) |  |  | The user defined alias, converted to a form useful for indexing. |
| 15 | `GL_GROUP_NAME_TXT` | VARCHAR(32) |  |  | GL Group Name |
| 16 | `PREVIOUS_ALIAS_ID` | DOUBLE | NOT NULL |  | Relates back to the GL alias table for the previous ID |
| 17 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Priority of the given alias begins with 0. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [ACCT_TYPE_GL_ALIAS_RELTN](ACCT_TYPE_GL_ALIAS_RELTN.md) | `GL_ALIAS_ID` |
| [BE_GL_ALIAS_RELTN](BE_GL_ALIAS_RELTN.md) | `GL_ALIAS_ID` |
| [GL_ALIAS_FIELD_RELTN](GL_ALIAS_FIELD_RELTN.md) | `GL_ALIAS_ID` |
| [GL_TRANS_LOG](GL_TRANS_LOG.md) | `GL_ACCOUNT_ALIAS_ID` |
| [GL_TRANS_LOG](GL_TRANS_LOG.md) | `GL_ACCT_UNIT_ALIAS_ID` |
| [GL_TRANS_LOG](GL_TRANS_LOG.md) | `GL_COMPANY_ALIAS_ID` |
| [GL_TRANS_LOG](GL_TRANS_LOG.md) | `GL_COMPANY_UNIT_ALIAS_ID` |

