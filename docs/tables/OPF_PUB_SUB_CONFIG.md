# OPF_PUB_SUB_CONFIG

> Contains the configurations for publish and subscribe logic.

**Description:** OPF PUB SUB CONFIG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_FLAG` | DOUBLE |  |  | Flag determines whether or not aliases (MRN) will be checked for a match. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `HNA_EVENT` | VARCHAR(10) |  |  | The event or action that occurred at the HNAM level. |
| 9 | `OPF_PUB_SUB_ID` | DOUBLE | NOT NULL |  | The unique primary identifier of the opf_pub_sub_config table. |
| 10 | `PUB_CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | The contributor_system_cd of the publisher. |
| 11 | `PUB_TRIGGER` | VARCHAR(10) |  |  | The ADT trigger sent by the publisher to HNAM. |
| 12 | `SUB_CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | The contributor_system_cd of the subscriber. |
| 13 | `SUB_PROC_ID` | DOUBLE | NOT NULL |  | The proc_id of the outbound com client for the subscriber. |
| 14 | `SUB_TRIGGER` | VARCHAR(10) |  |  | The ADT trigger the subscriber wants given certain criteria. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

