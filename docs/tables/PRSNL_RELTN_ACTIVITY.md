# PRSNL_RELTN_ACTIVITY

> Contains the activity data for all the personnel relationships(from the prsnl_reltn table) that have been selected.

**Description:** Personnel Relation Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(20) | NOT NULL |  | The Accession Number if it can be renormalized based on the parent_entity_id |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The Encounter ID if it can be renormalized based on the parent_entity_id |
| 3 | `ENTITY_TYPE_ID` | DOUBLE | NOT NULL |  | The primary key from the parent table that defines the specific entity type that will be used when there are more than one possible relationships within the same parent entity object. E.g. relationship type code for an encounter relationship, or a oe_field_id for an order. |
| 4 | `ENTITY_TYPE_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table that contains the entity_type_id as a primary key. E.g. would be "CODE_VALUE" from the relationship_type_cd or "ORDER_ENTRY_FIELD". This will be changing over time as teams start using it. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order ID if it can be denormlized based on the parent_entity_id |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key from the parent table that defines the specific personnel relationship is selected for. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The Name of the table that contains the parent entity Id as the primary key. Current valid values are "ENCOUNTER", "PERSON", "ORDERS" |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The Person ID if it can be denormlized based on the parent_entity_id |
| 9 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Person_id from the Personnel table for the person for whom this relationship has been selected. |
| 10 | `PRSNL_RELTN_ACTIVITY_ID` | DOUBLE | NOT NULL |  | The Primary Key for the table identifying the unique activity row of the Personnel Relationship selected. |
| 11 | `PRSNL_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The Relationship that has been selected. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `USAGE_NBR` | DOUBLE | NOT NULL |  | This is to identify what the usage is for. This is a bitmap of the usage flags: The current values are:1 Charting |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_RELTN_ID` | [PRSNL_RELTN](PRSNL_RELTN.md) | `PRSNL_RELTN_ID` |

