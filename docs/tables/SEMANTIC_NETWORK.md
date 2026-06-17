# SEMANTIC_NETWORK

> Defines the relationships between semantic types. The semantic types are the nodes in the network and the semantic relationships are the links.

**Description:** Semantic Network  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PROPERTY_LIST_IND` | DOUBLE |  |  | Indicates whether a semantic type relationship represents a list of concepts of the related semantic type. |
| 5 | `REQUIRED_IND` | DOUBLE |  |  | Indicates whether a concept is required to have a relationship with another concept of the semantic type defined in semantic_type2_id. |
| 6 | `SEMANTIC_NETWORK_ID` | DOUBLE | NOT NULL |  | Primary key for the table. Uniquely identifies a row within the table. |
| 7 | `SEMANTIC_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The semantic relationship, or link, of the nodes in the network. |
| 8 | `SEMANTIC_TYPE1_ID` | DOUBLE | NOT NULL | FK→ | A node in the semantic network. |
| 9 | `SEMANTIC_TYPE2_ID` | DOUBLE | NOT NULL | FK→ | The related node in the semantic network. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEMANTIC_RELTN_ID` | [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_TYPE_ID` |
| `SEMANTIC_TYPE1_ID` | [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_TYPE_ID` |
| `SEMANTIC_TYPE2_ID` | [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_TYPE_ID` |

