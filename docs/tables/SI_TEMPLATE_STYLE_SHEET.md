# SI_TEMPLATE_STYLE_SHEET

> All Style Sheets utilized by the SI Document Generation process are stored here for location purposes.

**Description:** System Integration Template Style Sheet  
**Table type:** REFERENCE  
**Primary key:** `SI_TEMPLATE_STYLE_SHEET_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CERNER_DEFINED_IND` | DOUBLE | NOT NULL |  | This record is defined by Cerner and not allowed to be changed in any way. |
| 2 | `FILE_NAME_TXT` | VARCHAR(50) | NOT NULL |  | The name of the text file created when this record is extracted to the file system for processing. This muct be unique for all records. |
| 3 | `LONG_BLOB_REFERENCE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the long blob reference table where the style sheet is stored. |
| 4 | `OUTPUT_CONTENT_CLASS_CD` | DOUBLE | NOT NULL |  | All style sheets are required to have an output content class code to define where they are allowed to be executed. |
| 5 | `OUTPUT_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | All style sheets are required to have an output content type code to define where they are allowed to be executed. |
| 6 | `REFERENCE_IND` | DOUBLE | NOT NULL |  | This file created by this record can only be referenced by other files and isn't used as a primary file for procesing purposes. |
| 7 | `SECTION_CD` | DOUBLE | NOT NULL |  | Primary Style Sheets are associated to the section code that they are built to create. |
| 8 | `SI_TEMPLATE_STYLE_SHEET_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 9 | `TEMPLATE_TYPE_CD` | DOUBLE | NOT NULL |  | Depending upon the need, Template Type is only required in specialty cases, such as Dynamic Documentation.` |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERSION_TXT` | VARCHAR(32) | NOT NULL |  | The version of the Style Sheet that has been stored in the database that can be compared to the style sheet in the service jar |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_REFERENCE_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_TEMPLATE](SI_TEMPLATE.md) | `DISCRETE_STYLE_SHEET_ID` |
| [SI_TEMPLATE](SI_TEMPLATE.md) | `NARRATIVE_STYLE_SHEET_ID` |

