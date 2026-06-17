# SURGICAL_DELAY

> Contains entries documented in Intraoperative Record associated with surgical delays

**Description:** Surgical Delay  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 9 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 10 | `DEF_IND` | DOUBLE |  |  | OBSOLETE -- An indicator of whether or not this is a default value that has not yet been accepted by the user |
| 11 | `DELAY_DESC` | VARCHAR(255) |  |  | The description of the delay.Column |
| 12 | `DELAY_DOC_BY_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the person table indicating the person responsible for documenting the intraoperative delay |
| 13 | `DELAY_DURATION` | DOUBLE |  |  | The duration of this intraoperative delay |
| 14 | `DELAY_OBSERVE_BY_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the person table indicating the person that has observed the intraoperative delay |
| 15 | `DELAY_REASON_CD` | DOUBLE | NOT NULL |  | The reason for this intraoperative delay |
| 16 | `DELAY_REPORT_TO_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the person table indicating the person this intraoperative delay was reported to. |
| 17 | `DELAY_REPORT_TO_TEXT` | VARCHAR(100) |  |  | A free-text name of the person to whom this intraoperative delay was reported to |
| 18 | `DISPLAY_SEQ` | DOUBLE |  |  | The sequence in which this intraoperative delay should be displayed |
| 19 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | This column references the specific document type that this delay is associated with. |
| 20 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 21 | `RESULT_STATUS_FLAG` | DOUBLE |  |  | OBSOLETE -- The status of this entry of Surgical Delays, i.e. new unverified, Corrected, etc. |
| 22 | `SEGMENT_HEADER_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the segment_header, indicating the status of this segment, i.e. Not Applicable, Accessed, Discontinued, etc. |
| 23 | `STAGE_CD` | DOUBLE | NOT NULL |  | Represents which surgical staging area the delay is associated with. |
| 24 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this intraoperative delay |
| 25 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the surgical_case table, indicating the surgical case associated with this delays entry. |
| 26 | `SURG_DELAY_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a row on this table. This value is unique for each version of a Surgical Delay entry. |
| 27 | `SURG_DELAY_STATIC_ID` | DOUBLE | NOT NULL |  | OBSOLETE -- A value that is used to group together all versions of Surgical Delay entries. It remains static across all versions. When the first version is inserted, this value is equal to the surg_delay_id |
| 28 | `SURG_START_DT_TM` | DATETIME |  |  | The date and time this surgical encounter was started. This column was added to this table for reporting purposes |
| 29 | `SURG_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DELAY_DOC_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DELAY_OBSERVE_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DELAY_REPORT_TO_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SEGMENT_HEADER_ID` | [SEGMENT_HEADER](SEGMENT_HEADER.md) | `SEGMENT_HEADER_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

