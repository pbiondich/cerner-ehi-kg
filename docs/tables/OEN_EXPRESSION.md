# OEN_EXPRESSION

> oen_expression

**Description:** Holds route expressions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `GROUP_LEVEL` | DOUBLE |  |  | What level is this expression at |
| 3 | `GROUP_NBR` | DOUBLE |  |  | What group number does this expression belong to |
| 4 | `PUBLICATION_ID` | DOUBLE | NOT NULL | FK→ | Reference to the publication |
| 5 | `QUALIFIER_FLAG` | DOUBLE |  |  | Used for qualifications |
| 6 | `RELATION_OPERATOR_FLAG` | DOUBLE |  |  | used to relate items to each other |
| 7 | `RULE_ID` | DOUBLE | NOT NULL |  | unique rule_id |
| 8 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | sequence_nbrColumn |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VALUE_TEXT` | VARCHAR(255) |  |  | value to check against |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PUBLICATION_ID` | [OEN_PUBLICATION](OEN_PUBLICATION.md) | `PUBLICATION_ID` |

