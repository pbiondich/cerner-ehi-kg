# PW_COMP_RELTN

> Used to define relationships between pathway components.

**Description:** PW COMP RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OFFSET_QTY` | DOUBLE |  |  | Obsolete - replaced by OFFSET_QUANTITY (which is defined as a FLOAT datatype) |
| 2 | `OFFSET_QUANTITY` | DOUBLE |  |  | Offset quantity used to define a time offset for the relationship. |
| 3 | `OFFSET_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the offset unit (Minutes, Hours, Days). |
| 4 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | FK value from PATHWAY CATALOG row that owns this relationship. |
| 5 | `PATHWAY_COMP_S_ID` | DOUBLE | NOT NULL | FK→ | Relationship source pathway component id from the pathway_comp table. |
| 6 | `PATHWAY_COMP_T_ID` | DOUBLE | NOT NULL | FK→ | Relationship target pathway component id from the pathway_comp table. |
| 7 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Meaning that identifies the type of relationship. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PATHWAY_COMP_S_ID` | [PATHWAY_COMP](PATHWAY_COMP.md) | `PATHWAY_COMP_ID` |
| `PATHWAY_COMP_T_ID` | [PATHWAY_COMP](PATHWAY_COMP.md) | `PATHWAY_COMP_ID` |

