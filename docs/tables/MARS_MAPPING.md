# MARS_MAPPING

> Identifies one of more mapping of a unique MARS_ATTRIBUTE row

**Description:** MARS_MAPPING  
**Table type:** REFERENCE  
**Primary key:** `MARS_MAPPING_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_FIELD_TXT` | VARCHAR(255) |  |  | The entity field of the entity to which the attribute is mapped. |
| 2 | `ENTITY_MAPPED_TXT` | VARCHAR(255) |  |  | The MARS entity concept to which the attribute is mapped - such as: PATIENT. ENCOUNTER, CLINICALEVENT |
| 3 | `ENTITY_TYPE_TXT` | VARCHAR(100) |  |  | An entity type for each mapping - such as: VALUE, COUNT, OCCURENCES |
| 4 | `MARS_ATTRIBUTE_ID` | DOUBLE | NOT NULL | FK→ | An attribute identifier for each unique mapping |
| 5 | `MARS_MAPPING_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MARS_ATTRIBUTE_ID` | [MARS_ATTRIBUTE](MARS_ATTRIBUTE.md) | `MARS_ATTRIBUTE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MARS_MAPPING_METADATA](MARS_MAPPING_METADATA.md) | `MARS_MAPPING_ID` |

