# SI_TEMPLATE_GROUP_RELTN

> Stores template group relationships along with output content type and default information.

**Description:** System Integration Template Group Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SECTION_SIGNIFICANCE_FLAG` | DOUBLE |  |  | This value dictates the significance of the given section during the document creation process. |
| 2 | `SECTION_TITLE` | VARCHAR(100) |  |  | The Title that will appear for when this template and group combination is used. |
| 3 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence number used to order and group sets of templates |
| 4 | `SI_TEMPLATE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the SI_TEMPLATE_GROUP table |
| 5 | `SI_TEMPLATE_GROUP_RELTN_ID` | DOUBLE | NOT NULL |  | The primary Identifier |
| 6 | `SI_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The template ID that is grouped with other similar template IDs . |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_TEMPLATE_GROUP_ID` | [SI_TEMPLATE_GROUP](SI_TEMPLATE_GROUP.md) | `SI_TEMPLATE_GROUP_ID` |
| `SI_TEMPLATE_ID` | [SI_TEMPLATE](SI_TEMPLATE.md) | `SI_TEMPLATE_ID` |

