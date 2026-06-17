# PERSON_PHR_RELTN_HIST

> Used for tracking history of certain columns on the person_phr_reltn table.

**Description:** Person Personal Health Record Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `PERSON_PHR_INFO_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person personal health record information table. It is an internally assigned number and generally not revealed to the user. |
| 5 | `PERSON_PHR_RELTN_HIST_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. |
| 6 | `PERSON_PHR_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person personal health record relationship table. It is an internally assigned number and generally not revealed to the user. |
| 7 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 8 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 9 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and time the transaction, which triggered the history row, occurred. This field can be system assigned or manually manipulated by users. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `PERSON_PHR_INFO_ID` | [PERSON_PHR_INFO](PERSON_PHR_INFO.md) | `PERSON_PHR_INFO_ID` |
| `PERSON_PHR_RELTN_ID` | [PERSON_PHR_RELTN](PERSON_PHR_RELTN.md) | `PERSON_PHR_RELTN_ID` |

