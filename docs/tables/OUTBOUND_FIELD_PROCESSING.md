# OUTBOUND_FIELD_PROCESSING

> Defines the field processing methods for outbound transaction from HNA Millenium

**Description:** ESO Outbound Field Processing Table  
**Table type:** REFERENCE  
**Primary key:** `CONTRIBUTOR_SYSTEM_CD`, `PROCESS_TYPE_CD`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | PK | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FIELD_PROCESSING_CD` | DOUBLE | NOT NULL |  | This field defines the processing method for the specified processing type. |
| 9 | `FIELD_PROCESSING_CS` | DOUBLE |  |  | This field defines the code_set for the processing method for the specified processing type. |
| 10 | `NULL_STRING` | VARCHAR(200) |  |  | This defines a string attribute associated with the process type. |
| 11 | `PROCESS_TYPE_CD` | DOUBLE | NOT NULL | PK | Define the processing type entity. |
| 12 | `SEQ_NUM` | DOUBLE | NOT NULL |  | Defines the sequence number in the table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_OUTBOUND_FIELD_PROCESS_HIST](SI_OUTBOUND_FIELD_PROCESS_HIST.md) | `CONTRIBUTOR_SYSTEM_CD` |
| [SI_OUTBOUND_FIELD_PROCESS_HIST](SI_OUTBOUND_FIELD_PROCESS_HIST.md) | `PROCESS_TYPE_CD` |

