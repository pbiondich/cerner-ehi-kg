# DMS_MEDIA_METADATA

> Contains application defined data that is relevant to a given media instance.

**Description:** DMS Media Meta-data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DMS_MEDIA_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | The media instance that is associated with this row. |
| 2 | `DMS_MEDIA_METADATA_ID` | DOUBLE | NOT NULL |  | Unique identifier for the row. |
| 3 | `TAG_NAME` | VARCHAR(40) | NOT NULL |  | The name of the metadata tag associated with this row. |
| 4 | `TAG_PATH` | VARCHAR(255) | NOT NULL |  | The fully qualified path of the metadata tag that this row is associated with. |
| 5 | `TAG_SEQ` | DOUBLE |  |  | This field is used if the path to a given tag contains multiple results. This sequence value will ensure that the order remains the same as originally entered. |
| 6 | `TAG_VALUE` | VARCHAR(255) | NOT NULL |  | The string value of this tag. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DMS_MEDIA_INSTANCE_ID` | [DMS_MEDIA_INSTANCE](DMS_MEDIA_INSTANCE.md) | `DMS_MEDIA_INSTANCE_ID` |

