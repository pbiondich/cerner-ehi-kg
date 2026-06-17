# DMS_ASSOCIATION

> This table is used to create media object associations such as annotations.

**Description:** DMS Association  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSOCIATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | This flag indicates the type of association. 0 - Not specified, 1- XFRM (Transform), 2 - XFRM replace, 3 - RPLC (Replace), 4 - Append, 5 - Annotation, 6 - Signs. |
| 2 | `DMS_ASSOCIATION_ID` | DOUBLE | NOT NULL |  | The unique primary key of the DMS_Association table |
| 3 | `MEDIA_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the dms_media_identifier table representing the source object for the association. This will be the base document for annotations. |
| 4 | `MEDIA_SOURCE_VERSION` | DOUBLE | NOT NULL |  | The version of the media source instance. The first version is version 1. |
| 5 | `MEDIA_TARGET_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the dms_media_identifier table representing the target object for the association. This will be the annotation object. |
| 6 | `MEDIA_TARGET_VERSION` | DOUBLE | NOT NULL |  | The version of the media target instance. The first version is version 1. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MEDIA_SOURCE_ID` | [DMS_MEDIA_IDENTIFIER](DMS_MEDIA_IDENTIFIER.md) | `DMS_MEDIA_IDENTIFIER_ID` |
| `MEDIA_TARGET_ID` | [DMS_MEDIA_IDENTIFIER](DMS_MEDIA_IDENTIFIER.md) | `DMS_MEDIA_IDENTIFIER_ID` |

