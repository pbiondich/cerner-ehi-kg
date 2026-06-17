# DO_MAP_SET

> Defines a mapping between two valuesets.

**Description:** Discern Ontology Map Valuesets  
**Table type:** REFERENCE  
**Primary key:** `DO_MAP_SET_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_MAPPING_PARTITION_FLAG` | DOUBLE |  |  | Unique non-generated number that defines where the mappings for the specific map set needs to be written to. A value of 0, indicates that mappings for this map set can be found in the DO_MAPPING table. A value of 1, indicates that mappings for this map set can be found in the DO_MAP_SET_MAPPING table. |
| 2 | `DO_MAP_SET_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_MAP_SET table.; |
| 3 | `DO_MAP_SET_IDENT` | DOUBLE | NOT NULL |  | Holds the Ontology Cloud identifier for this mapping definition. |
| 4 | `DO_MAP_SET_NAME` | VARCHAR(1000) |  |  | The unique user visible display of the map set. For example: "Healthe Intent", "All Rx Norm to Pharmacy Order Synonyms". |
| 5 | `DO_SOURCE_VALUE_SET_ID` | DOUBLE | NOT NULL | FK→ | Unique number that identifies a single row on the VALUE_SETS table. This Id represents the source Value Set in the mapping relationship. |
| 6 | `DO_TARGET_VALUE_SET_ID` | DOUBLE | NOT NULL | FK→ | Unique number that identifies a single row on the VALUE_SETS table. This Id represents the target Value Set in the mapping relationship. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_SOURCE_VALUE_SET_ID` | [DO_VALUE_SET](DO_VALUE_SET.md) | `DO_VALUE_SET_ID` |
| `DO_TARGET_VALUE_SET_ID` | [DO_VALUE_SET](DO_VALUE_SET.md) | `DO_VALUE_SET_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DO_MAP_SET_MAPPING](DO_MAP_SET_MAPPING.md) | `DO_MAP_SET_ID` |
| [DO_SCOPE_MAP_SET](DO_SCOPE_MAP_SET.md) | `DO_MAP_SET_ID` |

