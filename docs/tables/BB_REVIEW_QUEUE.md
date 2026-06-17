# BB_REVIEW_QUEUE

> When persons are combined and certain situations occur, a record is kept in this table, so that it can be reviewed by the appropriate personnel, including: 1) persons combined had different ABO/Rh's,2) persons combined had conflicting antibodies.

**Description:** Blood Bank Review Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_REVIEW_QUEUE_ID` | DOUBLE | NOT NULL |  | Primary key to table, unique identifier. |
| 6 | `FROM_ENCNTR_ID` | DOUBLE | NOT NULL |  | The primary key to the ENCOUNTER table. An internal system-assigned number. On this table, it corresponds to the ENCOUNTER row for from encounter being combined |
| 7 | `FROM_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the table from which this transaction was generated, e.g., the ID of the row on the antibody table that caused this transaction. |
| 8 | `FROM_PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person whose record was combined into another person's record. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table from which this transaction was generated, e.g., "person_antibody". |
| 10 | `REVIEW_DOC_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the LONG_TEXT table. An internal system-assigned number. On this table, it points to the row on the LONG_TEXT table for the text entered for the documentation of the review of the exception. |
| 11 | `REVIEW_DT_TM` | DATETIME |  |  | Date and Time exception was reviewed. |
| 12 | `REVIEW_OUTCOME_CD` | DOUBLE | NOT NULL |  | The outcome of the combine exception being reviewed by the blood bank, e.g., the combine was done in error, the ABORh or antibody that caused the exception was in error, etc. |
| 13 | `REVIEW_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who reviewed this blood bank combine exception. |
| 14 | `REV_CMB_IND` | DOUBLE | NOT NULL |  | This indicates the direction of combine. |
| 15 | `TO_ENCNTR_ID` | DOUBLE | NOT NULL |  | The primary key to the ENCOUNTER table. An internal system-assigned number. On this table, it corresponds to the ENCOUNTER row for to encounter being combined |
| 16 | `TO_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the table for the "to" person from which this transaction was generated, e.g., the ID of the row on the antibody table for the "to" person that caused this transaction. (The "to" person being the one for whom another person's record was combined into.) |
| 17 | `TO_PERSON_ID` | DOUBLE | NOT NULL |  | The "to" person of the combine transaction that caused this exception. |
| 18 | `UNCOMBINE_IND` | DOUBLE |  |  | Indicates whether the combine transaction that caused this exception was "uncombined" or "undone". |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REVIEW_DOC_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REVIEW_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

