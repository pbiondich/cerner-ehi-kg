# TRACK_COLLECTION_ELEMENT

> This table stores the FirstNet's Track Collection Element Reference Data.

**Description:** Track Collection Element  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ELEMENT_STATUS_CD` | DOUBLE | NOT NULL |  | Could be a code value for event status |
| 6 | `ELEMENT_TABLE` | VARCHAR(30) | NOT NULL |  | Stores the Table Name where the value is from |
| 7 | `ELEMENT_VALUE` | DOUBLE | NOT NULL |  | Mostly Track_event_id or could be code value |
| 8 | `SEQUENCE_NUM` | DOUBLE | NOT NULL |  | Sequence of appearance of each element in the track collection |
| 9 | `TRACK_COLLECTION_ELEMENT_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 10 | `TRACK_COLLECTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from Track Collection table |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_COLLECTION_ID` | [TRACK_COLLECTION](TRACK_COLLECTION.md) | `TRACK_COLLECTION_ID` |

