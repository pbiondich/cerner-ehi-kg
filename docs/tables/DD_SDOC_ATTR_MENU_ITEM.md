# DD_SDOC_ATTR_MENU_ITEM

> This table contains the documented AttributeMenuItems under an Attribute in a documented section.

**Description:** Dynamic Documentation Structured Document Attribute Menu Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the entry on the Long_Blob table that holds a comment about this documented Attribute Menu Item. |
| 2 | `DD_SDOC_ATTR_MENU_ITEM_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an attribute menu item under an Attribute in a documented section. Attribute Menu Items can be considered the answers to the questions posed in Attributes. |
| 3 | `DD_SDOC_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a documented section which contains this documented Attribute Menu Item. |
| 4 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | The position relative to sibling Attribute Menu Items |
| 5 | `OCID_IDENT` | VARCHAR(255) | NOT NULL |  | The reference identifier for this Attribute Menu Item. Useful for finding all documented copies of a given conceptual Attribute Menu Item. |
| 6 | `PARENT_DD_SDOC_ATTRIBUTE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related attribute. |
| 7 | `RENDERED_TEXT_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the entry on the LONG_BLOB table that holds the full rendered text for this Attribute Menu Item. |
| 8 | `TRUTH_STATE_CD` | DOUBLE | NOT NULL |  | Truth state of this Attribute Menu Item - options defined on codeset 15751. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `DD_SDOC_SECTION_ID` | [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `DD_SDOC_SECTION_ID` |
| `PARENT_DD_SDOC_ATTRIBUTE_ID` | [DD_SDOC_ATTRIBUTE](DD_SDOC_ATTRIBUTE.md) | `DD_SDOC_ATTRIBUTE_ID` |
| `RENDERED_TEXT_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

