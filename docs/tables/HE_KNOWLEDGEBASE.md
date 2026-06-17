# HE_KNOWLEDGEBASE

> Track the state and versioning of knowledge bases used by health expert.

**Description:** HE KNOWLEDGE BASE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `KNOWLEDGEBASE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `KNOWLEDGEBASE_NAME` | VARCHAR(100) | NOT NULL |  | The name of the knowledge base instance. Each knowledge base must have a unique name. (CAN BE MULTIPLE VERSIONS PER KNOWLEDGEBASE NAME) |
| 6 | `KNOWLEDGEBASE_VERSION` | VARCHAR(255) | NOT NULL |  | The rule version number of this instance of the knowledge base. |
| 7 | `OVERRIDE_FACT_VERSION` | VARCHAR(255) |  |  | Indicates what fact type version was ovrerridden |
| 8 | `OVERRIDE_RULE_VERSION_IND` | DOUBLE | NOT NULL |  | Indicates if the rule version was overridden. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VERSION_BLOB_ID` | DOUBLE | NOT NULL | FK→ | A reference to a blob which is a serialized representation of the knowledge base version. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VERSION_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

