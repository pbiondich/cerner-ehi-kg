# SI_TEMPLATE

> Stores template information by Contributor System code

**Description:** System Integration Template  
**Table type:** REFERENCE  
**Primary key:** `SI_TEMPLATE_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CERNER_DEFINED_IND` | DOUBLE | NOT NULL |  | This indicator will be set to 1 for the templates that are defined by Cerner. These templates a can't be modified |
| 4 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | Used to define the Contributor Source for the template when not HITSP or CCD. If this isn't valued, then the Contributor Source of the Contributor System will be used. |
| 5 | `DEFAULT_SECTION_TITLE` | VARCHAR(100) |  |  | Default Title to appear for the section built by this template. |
| 6 | `DESCRIPTION` | VARCHAR(255) |  |  | TEMPLATE DESCRIPTION |
| 7 | `DESCRIPTION_KEY` | VARCHAR(255) |  |  | _KEY version of the DESCRIPTION assigned by the user. This data is stripped of spaces and special characters and converted to upper case. |
| 8 | `DISCRETE_LONG_BLOB_ID` | DOUBLE | NOT NULL |  | Foreign Key Identifier to the LONG_BLOB_REFERENCE table that stores the style sheet to be used for the discrete section. |
| 9 | `DISCRETE_SS_NAME` | VARCHAR(50) | NOT NULL |  | Name of the Style Sheet used to detail discrete data for the selected section type. |
| 10 | `DISCRETE_STYLE_SHEET_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_TEMPLATE_STYLE_SHEET table for the discrete style sheet. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `NARRATIVE_LONG_BLOB_ID` | DOUBLE | NOT NULL |  | Foreign Key Identifier to the LONG_BLOB_REFERENCE table that stores the style sheet to be used for the narrative section. |
| 13 | `NARRATIVE_SS_NAME` | VARCHAR(50) | NOT NULL |  | Name of the Style Sheet used to detail narrative data for the selected section type. |
| 14 | `NARRATIVE_STYLE_SHEET_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_TEMPLATE_STYLE_SHEET table for the narrative style sheet. |
| 15 | `OUTPUT_CONTENT_CLASS_CD` | DOUBLE | NOT NULL |  | Output Content Class Code used to define the standard that the stylesheet was built to represent. |
| 16 | `OUTPUT_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | This column will become logicall OBSOLETE with the introduction of new column OUTPUT_CONTENT_CLASS_CD and new code changes.The output content type that this template is based off of. |
| 17 | `PREV_SI_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Previous (original) ID of the versioned set of rows. Used for type-2 versioning |
| 18 | `SECTION_CD` | DOUBLE | NOT NULL |  | The section that this template is used to detail |
| 19 | `SI_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | The primary Identifier |
| 20 | `TEMPLATE_TYPE_CD` | DOUBLE | NOT NULL |  | When valued, this field will combine with output content type to specify which si_templates can be used. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISCRETE_STYLE_SHEET_ID` | [SI_TEMPLATE_STYLE_SHEET](SI_TEMPLATE_STYLE_SHEET.md) | `SI_TEMPLATE_STYLE_SHEET_ID` |
| `NARRATIVE_STYLE_SHEET_ID` | [SI_TEMPLATE_STYLE_SHEET](SI_TEMPLATE_STYLE_SHEET.md) | `SI_TEMPLATE_STYLE_SHEET_ID` |
| `PREV_SI_TEMPLATE_ID` | [SI_TEMPLATE](SI_TEMPLATE.md) | `SI_TEMPLATE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SI_TEMPLATE](SI_TEMPLATE.md) | `PREV_SI_TEMPLATE_ID` |
| [SI_TEMPLATE_GROUP_RELTN](SI_TEMPLATE_GROUP_RELTN.md) | `SI_TEMPLATE_ID` |

