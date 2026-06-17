# DD_SDOC_SECTION

> Structured Documentation top-level activity data is stored here. One row on this table is written per conceptual section of documentation. For example, there is one row for a Physical Exam section, and a different row for a Review of Systems section.

**Description:** Dynamic Documentation - Structured Documentation Section  
**Table type:** ACTIVITY  
**Primary key:** `DD_SDOC_SECTION_ID`  
**Columns:** 14  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | Author/owner of the section. |
| 2 | `DD_SDOC_SECTION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a conceptual section of documentation. |
| 3 | `DD_SREF_SECTION_ID` | DOUBLE | NOT NULL | FK→ | The reference section this activity corresponds to. An example may be the id for the Physical Exam reference section. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter. |
| 5 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | Indicates the ui mechanism used for data entry on this section. |
| 6 | `PARENT_DD_SDOC_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the parent key for this row. A top-level section will have no parent, and thus will have a value of 0 in this column. A child section (for example, a subsection in History of Present Illness, which should be saved independently of its sibling tabs and not merged together) would have the DD_SDOC_SECTION_ID of its parent stored in this column. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier related to the parent entity name. May be 0 if the section stands alone. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | The referenced table name for which the section is applicable. May be blank if the section stands alone. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related person. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DD_SREF_SECTION_ID` | [DD_SREF_SECTION](DD_SREF_SECTION.md) | `DD_SREF_SECTION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PARENT_DD_SDOC_SECTION_ID` | [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `DD_SDOC_SECTION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [DD_SDOC_ATTR_MENU_ITEM](DD_SDOC_ATTR_MENU_ITEM.md) | `DD_SDOC_SECTION_ID` |
| [DD_SDOC_DATA](DD_SDOC_DATA.md) | `DD_SDOC_SECTION_ID` |
| [DD_SDOC_GROUPBY](DD_SDOC_GROUPBY.md) | `DD_SDOC_SECTION_ID` |
| [DD_SDOC_ITEM](DD_SDOC_ITEM.md) | `DD_SDOC_SECTION_ID` |
| [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `PARENT_DD_SDOC_SECTION_ID` |
| [DD_SDOC_SECT_TEMPL_RELTN](DD_SDOC_SECT_TEMPL_RELTN.md) | `DD_SDOC_SECTION_ID` |

