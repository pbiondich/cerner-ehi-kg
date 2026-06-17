# MED_FLEX_OBJECT_IDX

> The Med_flex_object_idx file stores the relationships of various flexed entities and their components.

**Description:** Med_flex_object_idx  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FLEX_OBJECT_TYPE_CD` | DOUBLE | NOT NULL |  | flexobjecttypecd |
| 3 | `MED_DEF_FLEX_ID` | DOUBLE | NOT NULL | FK→ | med defin flex id |
| 4 | `MED_FLEX_OBJECT_ID` | DOUBLE | NOT NULL |  | med_flex_object_id |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | parent entity id |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | parent entity name |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | sequence |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE` | DOUBLE |  |  | If the item on med_flex_object_idx has a value it is stored here. An example would be the amount of an attribute supplied by a product. |
| 14 | `VALUE_UNIT` | DOUBLE |  |  | If the item on med_flex_object_idx has a value it is stored here in units. An example would be the amount of an attribute supplied by a product. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MED_DEF_FLEX_ID` | [MED_DEF_FLEX](MED_DEF_FLEX.md) | `MED_DEF_FLEX_ID` |

