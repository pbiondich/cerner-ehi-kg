# DA_TABLE_RELTN

> Contain the tables joins used by both the Domain and the Logical View in Discern Analytics 2.0. A table may be relatd to itself or another table within the Domain or Logical view.

**Description:** Discrn Analytics Table Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUILD_SEQ` | DOUBLE | NOT NULL |  | The order the views or domains are built. |
| 2 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this row was created by Cerner. |
| 3 | `DA_TABLE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_TABLE_RELTN table. |
| 4 | `FROM_CLAUSE_TXT_ID` | DOUBLE | NOT NULL | FK→ | The long text id that contains the from clause for this relationship. |
| 5 | `JOIN_TABLE_ID` | DOUBLE | NOT NULL | FK→ | The table that will be joined to the table identified in column TABLE_ID. |
| 6 | `JOIN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies whether the join is a regular or shortcut join. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier from the tables that appear in column parent_entity_name. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Indicates whether the relationship contained on the table is for a domain or a logical view. |
| 9 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Identifies whether this relationship is required for this logical view. Marking a table relation as required forces the SQL engine to include this join statement to be included in the SQL along with the tables associated with the join, regardless of what columns have been selected in the query. |
| 10 | `TABLE_ID` | DOUBLE | NOT NULL | FK→ | A table that has been defined for use in either a Domain or a Logical View. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `WHERE_CLAUSE_TXT_ID` | DOUBLE | NOT NULL | FK→ | The long text id that contains the where clause for this relationship. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FROM_CLAUSE_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `JOIN_TABLE_ID` | [DA_TABLE_INFO](DA_TABLE_INFO.md) | `DA_TABLE_INFO_ID` |
| `TABLE_ID` | [DA_TABLE_INFO](DA_TABLE_INFO.md) | `DA_TABLE_INFO_ID` |
| `WHERE_CLAUSE_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

