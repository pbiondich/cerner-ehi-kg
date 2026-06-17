# ALLERGY_COMMENT

> Allows comments to be added to adverse effects and allergic reactions.

**Description:** Allergy Comment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLERGY_COMMENT` | LONGTEXT |  |  | The textual comment regarding the allergy. |
| 6 | `ALLERGY_COMMENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the allergy comment. |
| 7 | `ALLERGY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely defines an allergy/adverse reaction within the allergy table. The allergy_id can be associated with multiple allergy instances. When a new allergy is added to the allergy table the allergy_id is assigned to the allergy_instance_id. |
| 8 | `ALLERGY_INSTANCE_ID` | DOUBLE | NOT NULL |  | Unique identifier for the allergy table. Each change or revision made to an allergy/adverse reaction creates a new allergy instance. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `CMB_COMMENT_ID` | DOUBLE | NOT NULL |  | The "From" person's comment identifier of the comment being combined |
| 12 | `CMB_DT_TM` | DATETIME |  |  | Date/Time the item was combined |
| 13 | `CMB_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the combined status of the item. 0 = not part of combined, 1 Combined, 2 Historically Combined, 3 Continuation of Combine indication |
| 14 | `CMB_PERSON_ID` | DOUBLE | NOT NULL |  | Person identifier of the "From" person being combined |
| 15 | `CMB_PRSNL_ID` | DOUBLE | NOT NULL |  | Person identifier who performed the combined |
| 16 | `CMB_TZ` | DOUBLE |  |  | Combine Date Time ZoneColumn |
| 17 | `COMMENT_DT_TM` | DATETIME |  |  | The date and time that the comment was recorded. |
| 18 | `COMMENT_PRSNL_ID` | DOUBLE | NOT NULL |  | The unique identifier of the person that recorded the comment. |
| 19 | `COMMENT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 20 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 21 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 22 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 23 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALLERGY_ID` | [ALLERGY](ALLERGY.md) | `ALLERGY_INSTANCE_ID` |

