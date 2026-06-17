# CR_REPORT_SECTION

> This table stores Report Section information

**Description:** Report Section  
**Table type:** REFERENCE  
**Primary key:** `REPORT_SECTION_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ID to find XML related to the section |
| 5 | `NAME_IDENT` | VARCHAR(167) | NOT NULL |  | Unique Identifier used for merge processes. A concatenation of the name_key and date column. |
| 6 | `REPORT_SECTION_ID` | DOUBLE | NOT NULL | PK | Primary key of the table |
| 7 | `SECTION_ID` | DOUBLE | NOT NULL | FK→ | Supports section versioning. The row where REPORT_SECTION_ID = SECTION_ID represents the 'original' row. |
| 8 | `SECTION_NAME` | VARCHAR(150) | NOT NULL |  | User defined name for the section |
| 9 | `SECTION_NAME_KEY` | VARCHAR(150) |  |  | Section Name Key. Converted to key format. To be used as part of unique identifier for merge. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `SECTION_ID` | [CR_REPORT_SECTION](CR_REPORT_SECTION.md) | `REPORT_SECTION_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CR_PRINTED_SECTIONS](CR_PRINTED_SECTIONS.md) | `SECTION_ID` |
| [CR_REPORT_REQUEST_SECTION](CR_REPORT_REQUEST_SECTION.md) | `SECTION_ID` |
| [CR_REPORT_SECTION](CR_REPORT_SECTION.md) | `SECTION_ID` |
| [CR_TEMPLATE_SNAPSHOT](CR_TEMPLATE_SNAPSHOT.md) | `SECTION_ID` |

