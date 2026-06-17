# SEMANTIC_TYPE

> Provides for a consistent categorization of concepts represented in the Cerner Knowledge Index and provides a set of useful relationships between these concepts.

**Description:** Semantic Type  
**Table type:** REFERENCE  
**Primary key:** `SEMANTIC_TYPE_ID`  
**Columns:** 22  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CODE_SET` | DOUBLE |  |  | Identifies which code_set contains valid values for a given sematic property. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `HELP_LIST` | VARCHAR(2000) |  |  | Stores User Defined Help as XML stringColumn |
| 6 | `LOCK_TYPE_FLAG` | DOUBLE |  |  | Used to determine how a column behaves in an .XML spreadsheet view. |
| 7 | `PROPERTY_FLAG` | DOUBLE |  |  | Identifies a semantic type as a property. |
| 8 | `PROPERTY_TYPE_FLAG` | DOUBLE |  |  | Identifies the "data type" of the semantic property. |
| 9 | `REQUIRED_IND` | DOUBLE |  |  | Required indicator. |
| 10 | `SEMANTIC_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | A unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a semantic type. All Cerner assigned semantic identifiers are created from the CONCEPT_SEQ |
| 11 | `SEMANTIC_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the semantic_type_id used to fetch the valid concepts for a semantic property. |
| 12 | `SEMANTIC_RELTN_IND` | DOUBLE |  |  | Identifies a semantic type as a relationship. |
| 13 | `SEMANTIC_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents the external source that owns the semantic type identifier. |
| 14 | `SEMANTIC_TYPE_DISPLAY` | VARCHAR(100) |  |  | The display for the semantic type. |
| 15 | `SEMANTIC_TYPE_ID` | DOUBLE | NOT NULL | PK | Primary key for the table. Uniquely identifies a row within the table. |
| 16 | `SEMANTIC_TYPE_MEAN` | VARCHAR(30) |  |  | Allows multiple semantic types to be grouped, or to have the same meaning, e.g. PARENT_OF and CHILD_OF could both have the meaning of IS_A. |
| 17 | `TAG` | VARCHAR(100) |  |  | The XML tag used on export. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEMANTIC_PROPERTY_ID` | [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_TYPE_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [CONCEPT_CONCEPT_R](CONCEPT_CONCEPT_R.md) | `INVERSE_RELATION_ID` |
| [CONCEPT_CONCEPT_R](CONCEPT_CONCEPT_R.md) | `RELATION_ID` |
| [CONCEPT_PROPERTY](CONCEPT_PROPERTY.md) | `SEMANTIC_TYPE_ID` |
| [CONCEPT_SEMTYPE_R](CONCEPT_SEMTYPE_R.md) | `SEMANTIC_TYPE_ID` |
| [SEMANTIC_NETWORK](SEMANTIC_NETWORK.md) | `SEMANTIC_RELTN_ID` |
| [SEMANTIC_NETWORK](SEMANTIC_NETWORK.md) | `SEMANTIC_TYPE1_ID` |
| [SEMANTIC_NETWORK](SEMANTIC_NETWORK.md) | `SEMANTIC_TYPE2_ID` |
| [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_PROPERTY_ID` |

