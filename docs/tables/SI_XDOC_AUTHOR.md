# SI_XDOC_AUTHOR

> System Inegration Document Author Metadata

**Description:** SI XDOC AUTHOR  
**Table type:** ACTIVITY  
**Primary key:** `SI_XDOC_AUTHOR_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHOR_PERSON_NAME_FIRST` | VARCHAR(100) |  |  | First Name of the entity that authored the document. |
| 2 | `AUTHOR_PERSON_NAME_FULL_FRMT` | VARCHAR(255) |  |  | Represents the humans and/or machines that authored the document within the authorInstitution. |
| 3 | `AUTHOR_PERSON_NAME_LAST` | VARCHAR(100) |  |  | Last Name of the entity that authored the document. |
| 4 | `AUTHOR_PERSON_NAME_MIDDLE` | VARCHAR(100) |  |  | Middle Name of the entity that authored the document. |
| 5 | `AUTHOR_PERSON_NAME_PREFIX` | VARCHAR(50) |  |  | Prefix of the entity that authored the document. |
| 6 | `AUTHOR_PERSON_NAME_SUFFIX` | VARCHAR(50) |  |  | Suffix of the entity that authored the document. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of the author in the metadata author list returned by the query. |
| 8 | `SI_XDOC_AUTHOR_ID` | DOUBLE | NOT NULL | PK | Primary Identifier for this table. |
| 9 | `SI_XDOC_METADATA_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_XDOC_METATDATA table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_XDOC_METADATA_ID` | [SI_XDOC_METADATA](SI_XDOC_METADATA.md) | `SI_XDOC_METADATA_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_XDOC_METADATA_INFO](SI_XDOC_METADATA_INFO.md) | `SI_XDOC_AUTHOR_ID` |

