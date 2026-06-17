# DD_SDOC_ATTRIBUTE

> This table contains the documented Attributes under an Item in a documented section. An Attribute is one of the questions to be asked inside an Item. An entry on this table indicates that the question was answered, while the value of the answer is on DD_SDOC_ATTR_MENU_ITEM.

**Description:** Dynamic Documentation - Structured Documentation Attribute  
**Table type:** ACTIVITY  
**Primary key:** `DD_SDOC_ATTRIBUTE_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DD_SDOC_ATTRIBUTE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies an attribute under an Item in a documented section. An Attribute is one of the questions to be asked inside an Item. An entry on this table indicates that the question was answered, while the value of the answer is on DD_SDOC_ATTRIBUTEMENUITEM. |
| 2 | `DD_SDOC_SECTION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the documented section which contains this documented attribute. |
| 3 | `OCID_IDENT` | VARCHAR(255) | NOT NULL |  | The reference identifier for this Attribute. Useful for finding all documented copies of a given conceptual Attribute. |
| 4 | `PARENT_DD_SDOC_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the parent item |
| 5 | `TRUTH_STATE_CD` | DOUBLE | NOT NULL |  | The truth state of this Attribute - options defined on codeset 15751. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_DD_SDOC_ITEM_ID` | [DD_SDOC_ITEM](DD_SDOC_ITEM.md) | `DD_SDOC_ITEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DD_SDOC_ATTR_MENU_ITEM](DD_SDOC_ATTR_MENU_ITEM.md) | `PARENT_DD_SDOC_ATTRIBUTE_ID` |

