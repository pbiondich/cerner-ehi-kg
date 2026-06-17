# OEN_PUBLICATION

> OEN publication.

**Description:** Based on what characteristics tx is going to be available for routing(published)  
**Table type:** REFERENCE  
**Primary key:** `PUBLICATION_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CUSTOM_ELEMENT_NAME` | VARCHAR(32) |  |  | If published as custom then name of the custom element. if we are publishing based on patient name then patient name could be custom element name. |
| 3 | `CUSTOM_SCRIPT_ID` | DOUBLE | NOT NULL |  | Link to the oen_script table |
| 4 | `FUNCTION_PARAMS_VALUE` | VARCHAR(255) |  |  | Holds the parameters into the function |
| 5 | `LOAD_BALANCE_IND` | DOUBLE |  |  | Is this publication used for load balancing |
| 6 | `PUBLICATION_DESC` | VARCHAR(255) |  |  | Text descriptionColumn |
| 7 | `PUBLICATION_ID` | DOUBLE | NOT NULL | PK | Unique identifier of the publication. |
| 8 | `PUBLICATION_TYPE_FLAG` | DOUBLE |  |  | Based on what publication is available. |
| 9 | `PUBLISH_FUNCTION_FLAG` | DOUBLE |  |  | What function is being used. |
| 10 | `READ_ONLY_IND` | DOUBLE |  |  | Is this publication read_only?Column |
| 11 | `SOURCE_OBJECT` | VARCHAR(32) |  |  | If publishing based on Object then source object name e.g. OEOCF |
| 12 | `SOURCE_OBJECT_ELEMENT` | VARCHAR(255) |  |  | source object elementColumn |
| 13 | `TRANSACTION_FLAG` | DOUBLE |  |  | Used for custom elements |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OEN_EXPRESSION](OEN_EXPRESSION.md) | `PUBLICATION_ID` |
| [OEN_PUBLISHER_PUB_R](OEN_PUBLISHER_PUB_R.md) | `PUBLICATION_ID` |

