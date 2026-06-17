# CDI_CLIPBOARD

> This table acts as a clipboard for copying pages of a CDI document and pasting in a new/different document.

**Description:** cdi clipboard  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANNO_FILE` | VARCHAR(255) | NOT NULL |  | Annotation filename for the copied page. |
| 2 | `CDI_CLIPBOARD_ID` | DOUBLE | NOT NULL |  | Unique ID for each copied page. |
| 3 | `COPY_DT_TM` | DATETIME | NOT NULL |  | Date and time the page was copied. |
| 4 | `COPY_USER_ID` | DOUBLE | NOT NULL | FK→ | User who copied the page. |
| 5 | `MEDIA_OBJECT_ANNO_IDENT` | VARCHAR(255) | NOT NULL |  | MOM identifier for clipboard annotation file. |
| 6 | `MEDIA_OBJECT_FILE_IDENT` | VARCHAR(255) | NOT NULL |  | MOM identifier for clipboard image file. |
| 7 | `OBJECT_FILE` | VARCHAR(255) | NOT NULL |  | Object filename for the copied page. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COPY_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

