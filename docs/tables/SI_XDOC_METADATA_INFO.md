# SI_XDOC_METADATA_INFO

> Stores lists of data related to a parent document

**Description:** SI XDOC METADATA INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `METADATA_INFO` | VARCHAR(60) |  |  | Other information used to describe the metadata. |
| 2 | `METADATA_NAME` | VARCHAR(40) | NOT NULL |  | Name of the metadata element being stored. |
| 3 | `METADATA_TEXT` | VARCHAR(255) |  |  | Textual representation of the element being stored. |
| 4 | `METADATA_VALUE` | DOUBLE | NOT NULL |  | A numeric value if needed to describe the metadata. |
| 5 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of the metadata appearance in the message. |
| 6 | `SI_XDOC_AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | A foreign key to the parent SI_XDOC_AUTHOR table. |
| 7 | `SI_XDOC_METADATA_ID` | DOUBLE | NOT NULL | FK→ | A foreign key to the parent SI_XDOC_METADATA table. |
| 8 | `SI_XDOC_METADATA_INFO_ID` | DOUBLE | NOT NULL |  | The primary key to the metadata Information table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_XDOC_AUTHOR_ID` | [SI_XDOC_AUTHOR](SI_XDOC_AUTHOR.md) | `SI_XDOC_AUTHOR_ID` |
| `SI_XDOC_METADATA_ID` | [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `SI_XDOC_METADATA_ID` |

