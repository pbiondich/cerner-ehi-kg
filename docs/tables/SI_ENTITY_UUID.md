# SI_ENTITY_UUID

> Stores related UUID as they relate to different entities in the system, like Allergies, Problems, and other related items.

**Description:** System Integration Entity Universally Unique Identifier  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_UUID` | VARCHAR(100) | NOT NULL |  | Universally unique identifier for a given entity across all client domains. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Primary Identifier of the Entity. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The Name of the Entity ( PROBLEM, ALLERGY, ORDER, DIAGNOSIS, PROCEDURE and others... ) |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the given entity |
| 5 | `SI_ENTITY_UUID_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

