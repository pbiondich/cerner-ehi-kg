# COMBINE

> Contains the audit trail for all entities that were combined as a result of determining that the two rows in the parent entity table represent the same entities.

**Description:** Combine  
**Table type:** ACTIVITY  
**Primary key:** `COMBINE_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLICATION_FLAG` | DOUBLE |  |  | Application Flag |
| 6 | `CMB_DT_TM` | DATETIME |  |  | Date when combine finished |
| 7 | `CMB_UPDT_ID` | DOUBLE |  |  | Person who performed the combine |
| 8 | `COMBINE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person combine table. It is an internal system assigned number. |
| 9 | `COMMENT_TXT` | VARCHAR(250) |  |  | Free Text Comment entered by the user describing the reason for the combine. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `FROM_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier from the PARENT_ENTITY table of the 'from' parent entity that was combined. It is an internal system assigned number. |
| 12 | `PARENT_ENTITY` | VARCHAR(30) | NOT NULL |  | Contains the name of the parent entity that got combined,e.g.:LOCATION, PRSNL, etc. |
| 13 | `TO_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier from the PARENT_ENTITY table of the 'to' parent entity that was combined into. It is an internal system assigned number. |
| 14 | `TRANSACTION_TYPE` | VARCHAR(8) |  |  | Transaction Type |
| 15 | `UCB_DT_TM` | DATETIME |  |  | Date when uncombine finished |
| 16 | `UCB_UPDT_ID` | DOUBLE |  |  | Person who performed the uncombine |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [COMBINE_DETAIL](COMBINE_DETAIL.md) | `COMBINE_ID` |

