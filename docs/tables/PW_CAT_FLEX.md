# PW_CAT_FLEX

> Table to define relationships used to flex selection of entries on the pathway_catalog table

**Description:** Pathway catalog flex  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_DESCRIPTION_KEY` | VARCHAR(100) | NOT NULL |  | Description key field used to search the table for entries. |
| 2 | `DISPLAY_DESCRIPTION_KEY_A_NLS` | VARCHAR(400) |  |  | DISPLAY_DESCRIPTION_KEY_A_NLS column |
| 3 | `DISPLAY_DESCRIPTION_KEY_NLS` | VARCHAR(202) |  |  | Description key field used to search the table for entries. NLS field. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique id of the entity this flex entry is related to. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table that is referenced by the parent entity identification. |
| 6 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Unique id of the pathway catalog entry referenced by an entry on this table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |

