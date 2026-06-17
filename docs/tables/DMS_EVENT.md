# DMS_EVENT

> Contains reference names and display values for attributes of media instances.

**Description:** DMS event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATED_BY_ID` | DOUBLE | NOT NULL | FK→ | The id of the user that initiated the event |
| 2 | `DMS_EVENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for this row |
| 3 | `DMS_EVENT_REF_ID` | DOUBLE | NOT NULL | FK→ | The id of the event that we are tracking |
| 4 | `DMS_MEDIA_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | The media instance that is associated to the row |
| 5 | `DMS_REASON_REF_ID` | DOUBLE | NOT NULL | FK→ | Optional reason associated to the event |
| 6 | `EVENT_COMMENT` | VARCHAR(255) |  |  | Optional comment associated to the event |
| 7 | `EVENT_DETAIL` | VARCHAR(255) |  |  | Textual details associated to the event |
| 8 | `EVENT_DT_TM` | DATETIME | NOT NULL |  | The date and time of the event we are tracking |
| 9 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | If the details will not fit into the EVENT_DETAIL column, this will reference the details that are stored on the LONG_TEXT table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DMS_EVENT_REF_ID` | [DMS_REF](DMS_REF.md) | `DMS_REF_ID` |
| `DMS_MEDIA_INSTANCE_ID` | [DMS_MEDIA_INSTANCE](DMS_MEDIA_INSTANCE.md) | `DMS_MEDIA_INSTANCE_ID` |
| `DMS_REASON_REF_ID` | [DMS_REF](DMS_REF.md) | `DMS_REF_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

