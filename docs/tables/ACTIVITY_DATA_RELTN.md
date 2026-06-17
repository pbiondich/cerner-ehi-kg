# ACTIVITY_DATA_RELTN

> Record relationships between activity data (Allergies, Orders, etc...) and other entities (Organization, Personnel, etc...)

**Description:** Activity Data Relationships  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DATA_RELTN_ID` | DOUBLE | NOT NULL |  | Primary key. Unique Identifier for a relationship. |
| 2 | `ACTIVITY_ENTITY_ID` | DOUBLE | NOT NULL |  | Activity Table Name (ALLERGY, ORDERS, etc.) |
| 3 | `ACTIVITY_ENTITY_INST_ID` | DOUBLE | NOT NULL |  | Instance id to activity data item instance for items that use the instance schema |
| 4 | `ACTIVITY_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Activity Table Name (ALLERGY, ORDERS, etc.) |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | person whom the related order or allergy is for |
| 6 | `RELTN_ENTITY_ALL_IND` | DOUBLE | NOT NULL |  | Indicates if all entities of the named value have access to item. |
| 7 | `RELTN_ENTITY_ID` | DOUBLE | NOT NULL |  | Id to related data item. (ORGANIZATION, PRSNL, etc.) |
| 8 | `RELTN_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Related Table name. (ORGANIZATION, PRSNL, etc.) |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

