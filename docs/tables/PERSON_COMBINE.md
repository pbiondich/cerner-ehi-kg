# PERSON_COMBINE

> The person combine table contains the audit trail for all persons that were either automatically or manually combined as a result of determining that two rows in the person table represent the same person.

**Description:** Person Combine  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_COMBINE_ID`  
**Columns:** 31  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLICATION_FLAG` | DOUBLE |  |  | Tells which type of application sends the transaction. |
| 6 | `CMB_DT_TM` | DATETIME |  |  | Date when combine finished |
| 7 | `CMB_UPDT_ID` | DOUBLE |  |  | Person who performed the combine |
| 8 | `COMBINE_ACTION_CD` | DOUBLE | NOT NULL |  | Action that was taken on the 'from' person record during the combine. |
| 9 | `COMBINE_WEIGHT` | DOUBLE |  |  | A value between 0 and 100 representing the confidence level of the match based on match parameters. This column is only filled out by an OPF suggested combine. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `FROM_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | If from_mrn is used, this is the alias_pool_cd for the from_mrn. |
| 13 | `FROM_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | If from_mrn is used, this is the alias_type_cd for the from_mrn. |
| 14 | `FROM_MRN` | VARCHAR(200) |  |  | This is the MRN of the from person. Currently only used for single-encntr person combines called from the esi server. |
| 15 | `FROM_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier from the person table of the FROM person that was combined. It is an internal system assigned number. |
| 16 | `PERSON_COMBINE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person combine table. It is an internal system assigned number. |
| 17 | `PREV_ACTIVE_IND` | DOUBLE |  |  | Reference Data Domain Sync (RDDS) use for determining historical occurrences. |
| 18 | `PREV_ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | The value of the active_status_cd prior to the row bein combined. Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 19 | `PREV_CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | The value of the conf_level_cd prior to the row being combined. Confidential level identifies a level of security that may restrict access or release of information. |
| 20 | `TO_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | If to_mrn is used, this is the alias_pool_cd for the to_mrn. |
| 21 | `TO_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | If to_mrn is used, this is the alias_type_cd for the to_mrn. |
| 22 | `TO_MRN` | VARCHAR(200) |  |  | This is the MRN of the to person. Currently only used for single-encntr person combines called from the esi server. |
| 23 | `TO_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier from the person table of the TO person that was combined. It is an internal system assigned number. |
| 24 | `TRANSACTION_TYPE` | VARCHAR(8) |  |  | The type of transaction that triggers the combine. For ESI transactions, the transaction_type will be the MSH event, e.g., ADT^A01, ADT^A02, etc. For Combine Tool transactions, the transaction_type will be CMBTOOL. |
| 25 | `UCB_DT_TM` | DATETIME |  |  | Date when uncombine finished |
| 26 | `UCB_UPDT_ID` | DOUBLE |  |  | Person who performed the uncombine |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FROM_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `TO_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PERSON_COMBINE_BATCH](PERSON_COMBINE_BATCH.md) | `PERSON_COMBINE_ID` |
| [PERSON_COMBINE_DET](PERSON_COMBINE_DET.md) | `PERSON_COMBINE_ID` |

