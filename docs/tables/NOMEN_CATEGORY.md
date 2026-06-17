# NOMEN_CATEGORY

> Allows client to create pick lists, or favorites to assist in nomenclature lookups.

**Description:** Nomenclature Category  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_NAME` | VARCHAR(100) | NOT NULL |  | The description of the category that displays in a lookup. |
| 2 | `CATEGORY_NAME_A_NLS` | VARCHAR(400) |  |  | CATEGORY_NAME_A_NLS column |
| 3 | `CATEGORY_NAME_NLS` | VARCHAR(202) |  |  | This is the description used for non-English based strings for the NLSSORT function. |
| 4 | `CATEGORY_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the available nomenclature category types to assign to each nomenclature category. |
| 5 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 6 | `NOMEN_CATEGORY_ID` | DOUBLE | NOT NULL |  | The unique identifier for a row in the Nomenclature Category table. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique identifier of the table specified in the parent_entity_name column. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Defines the parent entity that the owner of nomenclature category belongs. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

