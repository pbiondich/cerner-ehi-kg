# CASE_TIMES

> The times associated with this surgical case, i.e. Surgery Start/Stop Time, Patient In/Out of Room Time, etc.

**Description:** Case Times  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CASE_TIMES_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a row on this table. This value is unique for all versions of a given case time for a case. |
| 7 | `CASE_TIMES_STATIC_ID` | DOUBLE | NOT NULL |  | OBSOLETE -- A value that is used to group together all versions of Case Times entries. It remains static across all versions. When the first version is inserted, this value is equal to the case_times_id. |
| 8 | `CASE_TIME_DT_TM` | DATETIME |  |  | The date and time associated with this case time entry. |
| 9 | `CASE_TIME_MEANING` | CHAR(12) |  |  | OBSOLETE -- The CDF meaning (on the Discrete Task Assay codeset) associated with this case time entry, i.e. SURGSTART. Used to apply application logic to a specific case time. |
| 10 | `CASE_TIME_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table. |
| 12 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table. |
| 13 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 14 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `RESULT_STATUS_FLAG` | DOUBLE |  |  | OBSOLETE -- The status of this case times entry, i.e. New Unverified, Corrected, etc. |
| 17 | `SEGMENT_HEADER_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the segment_header table indicating the status of this segment, i.e. Accessed, Discontinued, etc. |
| 18 | `STAGE_CD` | DOUBLE | NOT NULL |  | The surgical staging area associated with this Case Times entry |
| 19 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case Identifier |
| 20 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Code from the Form for Case Times |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEGMENT_HEADER_ID` | [SEGMENT_HEADER](SEGMENT_HEADER.md) | `SEGMENT_HEADER_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

