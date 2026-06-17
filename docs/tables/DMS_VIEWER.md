# DMS_VIEWER

> Used to maintain view/MIME type view associations along with launch and terminate instructions.

**Description:** DMS Viewer  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Relates a view/mime association to a media content type. It is a foreign key back to the DMS_CONTENT_TYPE table. |
| 2 | `DMS_MEDIA_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | Relates a view/mime association to media items in the Media Management archive. It is a foreign key back to the DMS_MEDIA_INSTANCE table. |
| 3 | `DMS_VIEWER_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated value. |
| 4 | `EXTENSION_TXT` | VARCHAR(32) |  |  | The file name extension of the file that contains the viewer. |
| 5 | `INSTANCE_LIMIT_NBR` | DOUBLE | NOT NULL |  | The number of instances allowed. 1 - single instance <>1 - multiple instances allowed Eventually this will be the actual number of instances allowed with -1 indicating no limit. |
| 6 | `MIME_TYPE_NAME` | VARCHAR(255) |  |  | The name of the MIME type that the viewer is associated with. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VIEWER_AUXILIARY_TXT` | VARCHAR(255) |  |  | This field will contain supplementary information associated with the content type & mime type. For XML it will contain style for a default style sheet name. |
| 13 | `VIEWER_NAME` | VARCHAR(255) | NOT NULL |  | Either an executable file name or a cocreateinstance name for a view instance. |
| 14 | `VIEWER_TYPE_FLAG` | DOUBLE | NOT NULL |  | 0 - (default) DOS command line The type of viewer. 1 - cocreateinstance (pass file) 2 - Java plugin 3 - custom create (hard coded) 4 - cocreateinstance (pass id) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTENT_TYPE_ID` | [DMS_CONTENT_TYPE](DMS_CONTENT_TYPE.md) | `DMS_CONTENT_TYPE_ID` |
| `DMS_MEDIA_INSTANCE_ID` | [DMS_MEDIA_INSTANCE](DMS_MEDIA_INSTANCE.md) | `DMS_MEDIA_INSTANCE_ID` |

