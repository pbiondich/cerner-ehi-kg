# CP_CONCEPT_GROUP_DTL_ATTR

> Contains attribute information for concept details. This will allow for flexibly grouping, and describing of additional parameters to flex by for detail entries.

**Description:** CP CONEPT GROUP DETAIL ATTRIBUTES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign Key to table the Attribute is related to. |
| 2 | `ATTRIBUTE_ENTITY_NAME` | VARCHAR(30) |  |  | Name of Table Attribute ID is linked to. |
| 3 | `ATTRIBUTE_ENTITY_TEXT` | VARCHAR(255) | NOT NULL |  | Value for which entity name if it's not linked to another table. |
| 4 | `CP_CONCEPT_GROUP_DTL_ATTR_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `CP_CONCEPT_GROUP_DTL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key value from CP_CONCEPT_GROUP_DTL |
| 6 | `DETAIL_ATTRIBUTE_TYPE_CD` | DOUBLE | NOT NULL |  | Detail Attribute Type Code. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_CONCEPT_GROUP_DTL_ID` | [CP_CONCEPT_GROUP_DTL](CP_CONCEPT_GROUP_DTL.md) | `CP_CONCEPT_GROUP_DTL_ID` |

