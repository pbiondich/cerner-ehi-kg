# ENCNTR_COMBINE

> The encounter combine table contains the audit trail for all encounters that were either automatically or manually combined as a result of determining that two rows in the encounter table represent the same encounter.

**Description:** Encounter Combine  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_COMBINE_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLICATION_FLAG` | DOUBLE |  |  | Tells which type of application sends the transaction. |
| 6 | `CMB_DT_TM` | DATETIME |  |  | `Date when combine finished |
| 7 | `CMB_UPDT_ID` | DOUBLE |  |  | Person who performed the combine |
| 8 | `COMBINE_ACTION_CD` | DOUBLE | NOT NULL |  | Action that was taken on the 'from' encounter record during the combine. |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `ENCNTR_COMBINE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter combine table. It is an internal system assigned number. |
| 11 | `FROM_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier from the encounter table of the FROM encounter that was combined. It is an internal system assigned number. |
| 12 | `PREV_ACTIVE_IND` | DOUBLE |  |  | Reference Data Domain Sync (RDDS) use for determining historical occurrences. |
| 13 | `PREV_ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | The value of the active_status_cd prior to the row being combined. Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 14 | `PREV_CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | The value of the conf_level_cd prior to the row being combined. Confidential level identifies a level of security that may restrict access or release of information. |
| 15 | `TO_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier from the encounter table of the TO encounter that was combined. It is an internal system assigned number. |
| 16 | `TRANSACTION_TYPE` | VARCHAR(8) |  |  | The type of transaction that triggers the combine. For ESI transactions, the transaction_type will be the MSH event, e.g., A01, A02, ... For Combine Tool transactions, the transaction_type will be blank. |
| 17 | `UCB_DT_TM` | DATETIME |  |  | Date when uncombine finished |
| 18 | `UCB_UPDT_ID` | DOUBLE |  |  | Person who performed the uncombine |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FROM_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `TO_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_COMBINE_DET](ENCNTR_COMBINE_DET.md) | `ENCNTR_COMBINE_ID` |

