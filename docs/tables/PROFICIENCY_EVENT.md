# PROFICIENCY_EVENT

> This activity table contains records for every proficiency event documented in the system for cytotechnologists. Information such as the date of the event, date of result notification, and event status are included.

**Description:** Proficiency Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMINISTERED_DT_TM` | DATETIME |  |  | This field contains the date and time the proficiency testing event was administered (the date and time the user completed the proficiency testing event). |
| 3 | `COMMENTS` | VARCHAR(200) |  |  | This field contains a comment associated with the documentation of a proficiency testing event. |
| 4 | `NOTIFICATION_DT_TM` | DATETIME |  |  | This field contains the date and time the user (or site) was notified of the results of the proficiency testing event. |
| 5 | `PROFICIENCY_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code identifying the type of proficiency testing event. Proficiency testing event information is stored on codeset 1315. |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies the cytotechnologist for whom the proficiency testing event is associated. This value could be used to join to other tables, such as the PRSNL, PERSON, and CYTO_SCREENING_SECURITY, for example. |
| 7 | `RESULT_FLAG` | DOUBLE |  |  | This field contains a flag value documenting the results of the proficiency testing event. |
| 8 | `REVIEWED_DT_TM` | DATETIME |  |  | This field contains the date and time the proficiency testing event was reviewed by the authorized user who oversees the review of proficiency testing information. In most sites, this is a pathologist. |
| 9 | `REVIEWER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the user who was documented as the reviewer of the proficiency testing event. This value could be used to join to tables containing user information, such as the PRSNL and PERSON tables. |
| 10 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field documents the proficiency testing event sequence (for the same user). |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REVIEWER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

