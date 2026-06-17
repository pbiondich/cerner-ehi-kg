# SCH_SLOT_ALIAS

> This table is used to store a foreign system alias for a schedulable slot.

**Description:** Scheduling Slot Alias  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL | FK→ | A collection used to generate aliases. |
| 6 | `APPLY_SLOT` | DOUBLE | NOT NULL |  | The apply slot. |
| 7 | `APPT_DEF_ID` | DOUBLE | NOT NULL | FK→ | The ID of the scheudling appointment definition the alias is related to. |
| 8 | `ASSIGN_AUTHORITY_SYS_CD` | DOUBLE | NOT NULL |  | This field identifies whether the ESI server received and alias that was configured for Hold. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CAB_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Service Id of Related Choose and Book Service |
| 11 | `CHECK_DIGIT` | DOUBLE |  |  | Parity digit. |
| 12 | `CHECK_DIGIT_METHOD_CD` | DOUBLE | NOT NULL | FK→ | Method for checking the digit. |
| 13 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 14 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 15 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 16 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `NULL_DT_TM` | DATETIME | NOT NULL |  | The null date and time. |
| 19 | `OFFSET_MINS` | DOUBLE |  |  | The offset (in minutes) of the start time interval in a contiguous slot. |
| 20 | `PUBLISHED_IND` | DOUBLE | NOT NULL |  | Is this slot available in Choose and Book? |
| 21 | `SLOT_ALIAS` | VARCHAR(255) | NOT NULL |  | The slot alias identifier. |
| 22 | `SLOT_ALIAS_ID` | DOUBLE | NOT NULL |  | The primary key of this table. |
| 23 | `SLOT_ALIAS_SUB_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Identifies a category within a particular slot alias type code. |
| 24 | `SLOT_ALIAS_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Identifies a kind or type of alias |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The date and time field for version logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_POOL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `APPT_DEF_ID` | [SCH_APPT_DEF](SCH_APPT_DEF.md) | `APPT_DEF_ID` |
| `CAB_SERVICE_ID` | [SCH_CAB_SERVICE](SCH_CAB_SERVICE.md) | `CAB_SERVICE_ID` |
| `CHECK_DIGIT_METHOD_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SLOT_ALIAS_SUB_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SLOT_ALIAS_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

