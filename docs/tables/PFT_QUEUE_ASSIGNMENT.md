# PFT_QUEUE_ASSIGNMENT

> The purpose of the pft_queue_assignment table is to store reference data defining the distribution of workflow items within a queue.

**Description:** This table contains the assignment profit workflow queues.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ASSIGNED_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel group related to this row. |
| 6 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel to which a PFT_QUEUE_ITEM will be assigned. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LEVEL_NBR` | DOUBLE |  |  | The position of the record within a hierarchy of records. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `PFT_ENTITY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the information contained in a workflow queue. |
| 13 | `PFT_ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of information contained in a workflow queue. |
| 14 | `PFT_QUEUE_ASSIGNMENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the pft_queue_assignment table. |
| 15 | `SEQUENCE_NBR` | DOUBLE |  |  | The sequence number to determine the record order. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `VALUE_DISPLAY_TXT` | VARCHAR(50) |  |  | The display text of the value assigned. |
| 22 | `VALUE_RANGE_TXT` | VARCHAR(50) |  |  | Upper value within a range of values. |
| 23 | `VALUE_SPECIFIER_CD` | DOUBLE | NOT NULL |  | Specifies what the value for the event parameter represents. |
| 24 | `VALUE_TXT` | VARCHAR(50) |  |  | The value assigned to this level. The lower value within a range of values. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

