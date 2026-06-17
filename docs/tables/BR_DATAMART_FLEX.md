# BR_DATAMART_FLEX

> Stores flexing options for datamart values contained on br_datamart_values.

**Description:** Bedrock Datamart Flex  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAMART_FLEX_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_FLEX_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_DATAMART_FLEX table. |
| 2 | `GROUPER_FLEX_ID` | DOUBLE | NOT NULL | FK→ | Used when a set of Flex rows need grouped together. The first row in the group will have a 0 in this column. |
| 3 | `GROUPER_IND` | DOUBLE | NOT NULL |  | Indicates if this row is part of a group. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key to a table designated by parent_entity_name |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table for the value that is being flexed. |
| 6 | `PARENT_ENTITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | In the case where parent_entity_name is CODE_VALUE, indicates which type is really being flexed. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUPER_FLEX_ID` | [BR_DATAMART_FLEX](BR_DATAMART_FLEX.md) | `BR_DATAMART_FLEX_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_DATAMART_FLEX](BR_DATAMART_FLEX.md) | `GROUPER_FLEX_ID` |

