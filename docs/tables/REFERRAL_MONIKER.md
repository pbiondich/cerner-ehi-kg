# REFERRAL_MONIKER

> Stores all external monikers associated to REFERRAL.

**Description:** Referral Moniker  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_POOL_CD` | DOUBLE |  | FK→ | The alias pool code identifies a unique set or list of order identifiers. |
| 6 | `ALIAS_TYPE_CD` | DOUBLE |  |  | The alias type code identifies a kind or type of alias. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE |  |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the entry was created. |
| 9 | `REFERRAL_ID` | DOUBLE |  | FK→ | Identifies the related REFERRAL row. |
| 10 | `REFERRAL_MONIKER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the REFERRAL_MONIKER table. |
| 11 | `REFERRAL_MONIKER_SYSTEM_TXT` | VARCHAR(255) |  |  | Identifies the system generating moniker. |
| 12 | `REFERRAL_MONIKER_TYPE_TXT` | VARCHAR(255) |  |  | Type of moniker which is created by external systems to referral. |
| 13 | `REFERRAL_MONIKER_VALUE_TXT` | VARCHAR(255) |  |  | Contains the actual monikor value. |
| 14 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_POOL_CD` | [ALIAS_POOL](ALIAS_POOL.md) | `ALIAS_POOL_CD` |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |

