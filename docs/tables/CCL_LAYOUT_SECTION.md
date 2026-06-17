# CCL_LAYOUT_SECTION

> CCl layout section

**Description:** CCl layout section  
**Table type:** REFERENCE  
**Primary key:** `SECTION_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRIVER_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | Linkage to driver object stored on CCL_REPORT_OBJECT. A driver object can be used to populate a record structure for use with a layout section. |
| 2 | `SECTION_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Identifier for section content stored in XML format on the LONG_BLOB table |
| 3 | `SECTION_DESCRIPTION` | VARCHAR(2000) |  |  | Layout section comments and report developer notes |
| 4 | `SECTION_HEIGHT` | DOUBLE |  |  | Height of section (default in inches) |
| 5 | `SECTION_ID` | DOUBLE | NOT NULL | PK | primary key for sequencing/reference. Unique section identifier |
| 6 | `SECTION_NAME` | VARCHAR(30) | NOT NULL |  | The user-specified section name defined with Layout Builder |
| 7 | `SECTION_TYPE_IND` | DOUBLE | NOT NULL |  | Indicates pre-defined (0) or custom (1) layout section. Potentially other uses |
| 8 | `SECTION_VERSION` | DOUBLE |  |  | Version for report development history |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRIVER_OBJECT_ID` | [CCL_REPORT_OBJECT](CCL_REPORT_OBJECT.md) | `OBJECT_ID` |
| `SECTION_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CCL_REPORT_OBJECT_R](CCL_REPORT_OBJECT_R.md) | `SECTION_ID` |

