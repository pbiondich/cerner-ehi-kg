# CP_CONCEPT_GROUP_DTL

> Contains Detailed Configuraton for a Concept Group

**Description:** Care Planning Concept Group Detail  
**Table type:** REFERENCE  
**Primary key:** `CP_CONCEPT_GROUP_DTL_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONCEPT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign Key from related table (table name in CONCEPT_ENTITY_NAME) |
| 2 | `CONCEPT_ENTITY_IDENT` | VARCHAR(255) | NOT NULL |  | Identifier for when row is not using entity_name, entity_id. |
| 3 | `CONCEPT_ENTITY_NAME` | VARCHAR(30) |  |  | Table from which this concept is related to. |
| 4 | `CONCEPT_ENTITY_TEXT` | VARCHAR(255) | NOT NULL |  | Text field for value |
| 5 | `CP_CONCEPT_GROUP_DTL_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `CP_CONCEPT_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from CP_CONCEPT_GROUP |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_CONCEPT_GROUP_ID` | [CP_CONCEPT_GROUP](CP_CONCEPT_GROUP.md) | `CP_CONCEPT_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CP_CONCEPT_GROUP_DTL_ATTR](CP_CONCEPT_GROUP_DTL_ATTR.md) | `CP_CONCEPT_GROUP_DTL_ID` |

