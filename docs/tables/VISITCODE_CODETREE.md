# VISITCODE_CODETREE

> The root of a flattened tree structure defining rhe acceptable inputs to a set of coding rules and UI for maintaining those inputs

**Description:** Coding Tree  
**Table type:** REFERENCE  
**Primary key:** `VISITCODE_CODETREE_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_CONTENT_DT_TM` | DATETIME | NOT NULL |  | timestamp indicating when the coding tree starts being active. |
| 3 | `CONTENT_VERSION_NBR` | DOUBLE | NOT NULL |  | used to provide a unique merge id that does not involve the effective dates. |
| 4 | `DISPLAY_NAME` | VARCHAR(100) | NOT NULL |  | Displayed name for the coding tree |
| 5 | `END_CONTENT_DT_TM` | DATETIME | NOT NULL |  | timestamp indicating when the coding tree stops being active. NULL indicates the tree is still active. |
| 6 | `TREE_NAME` | VARCHAR(60) | NOT NULL |  | name used to identify the coding tree. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VISITCODE_CODETREE_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [VISITCODE_RULESET](VISITCODE_RULESET.md) | `VISITCODE_CODETREE_ID` |
| [VISITCODE_TREENODE](VISITCODE_TREENODE.md) | `VISITCODE_CODETREE_ID` |
| [VISITCODING_EXTRACT](VISITCODING_EXTRACT.md) | `VISITCODE_CODETREE_ID` |

