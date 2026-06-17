# SI_BATCH_EVENT_SYS

> Each row on this table represents a batch event for the interface to process.

**Description:** This table hold the batch events for the individual interfaces.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Unique batch event identifier. |
| 2 | `BEG_SEG_SEQ_NUM` | DOUBLE | NOT NULL |  | The sequence number of the first message segment corresponding to the batch event. This value is in reference to the ST segment position |
| 3 | `COMPLETE_DT_TM` | DATETIME |  |  | Indicates the date and time the interface completed processing the batch event.Column |
| 4 | `END_SEG_SEQ_NUM` | DOUBLE | NOT NULL |  | The sequence number of the last message segment corresponding to the batch event. This value is in reference to the ST segment position |
| 5 | `EVENT_STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the processing status of each event.Column |
| 6 | `EVENT_STATUS_TEXT` | VARCHAR(500) | NOT NULL |  | Textual description of the batch_event's status.Column |
| 7 | `GRP_BEG_SEG_SEQ_NUM` | DOUBLE | NOT NULL |  | The sequence number indicating the start of the group header segment (2000A, 2010AA, 2010AB loops) for the given batch event. This value is in reference to the ST segment's position. |
| 8 | `GRP_END_SEG_SEQ_NUM` | DOUBLE | NOT NULL |  | The sequence number indicating the end of the group header segment (2000A, 2010AA, 2010AB loops) for the given batch event. This value is in reference to the ST segment's position. |
| 9 | `GS_IDENT` | VARCHAR(250) | NOT NULL |  | Unique identifier for the GS functional GroupColumn |
| 10 | `INTERFACE_ID` | DOUBLE | NOT NULL |  | Identifies a unique interface. This value comes from the INTERFACEID column in the OEN_PROCINFO table. |
| 11 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | The status of the batch event from an acknowledgement, e.g., X12N 997 response.Column |
| 12 | `SEQ_NUM` | DOUBLE | NOT NULL |  | Indicates the order in which the batch events are processed.Column |
| 13 | `START_DT_TM` | DATETIME |  |  | Indicates the date and time the interface started processing the batch event. |
| 14 | `ST_IDENT` | VARCHAR(250) | NOT NULL |  | Unique identifier for the ST transaction setColumn |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_EVENT_ID` | [SI_BATCH_EVENT](SI_BATCH_EVENT.md) | `BATCH_EVENT_ID` |

