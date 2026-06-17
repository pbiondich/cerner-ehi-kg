# VISITCODE_RULESET

> A versioned pointer to a long_blob_reference record containing the data for a rule set and a coding_tree identifying acceptable inpurts to the rule set.

**Description:** Coding Rule Set  
**Table type:** REFERENCE  
**Primary key:** `VISITCODE_RULESET_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_CONTENT_DT_TM` | DATETIME | NOT NULL |  | timestamp specifying when the rule set starts being active. |
| 3 | `CONTENT_VERSION_NBR` | DOUBLE | NOT NULL |  | used to define a unique merge key without referencing the effective dates |
| 4 | `DISPLAY_NAME` | VARCHAR(100) | NOT NULL |  | Displayed name for the ruleset |
| 5 | `END_CONTENT_DT_TM` | DATETIME | NOT NULL |  | timestamp specifying when the rule set ceases being active. NULL indicates the rule set is still active. |
| 6 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | id of the long_blob_reference record containing the data for this rule set. |
| 7 | `RULESET_NAME` | VARCHAR(60) | NOT NULL |  | fixed name for the rule set to be used as a meaning not to be modified. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VISITCODE_CODETREE_ID` | DOUBLE | NOT NULL | FK→ | id of the associated track_coding_tree |
| 14 | `VISITCODE_RULESET_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `VISITCODE_CODETREE_ID` | [VISITCODE_CODETREE](VISITCODE_CODETREE.md) | `VISITCODE_CODETREE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `VISITCODE_RULESET_ID` |

