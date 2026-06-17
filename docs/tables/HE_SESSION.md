# HE_SESSION

> Keeps the current state of health expert rules sessions

**Description:** Health Expert Sessions  
**Table type:** ACTIVITY  
**Primary key:** `SESSION_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_LENGTH` | DOUBLE |  |  | original length of the blob. this should be the uncompressed length if the blob is compressed. |
| 2 | `EXPIRATION_DT_TM` | DATETIME |  |  | The date at which this session is considered expired. |
| 3 | `JOB_INSTANCE_NBR` | DOUBLE |  |  | This column is used to identify which instance of a health expert job is currently trying to process the session. |
| 4 | `KNOWLEDGEBASE_NAME` | VARCHAR(100) | NOT NULL |  | The unique name of the knowledge base associated with the session. |
| 5 | `KNOWLEDGEBASE_VERSION` | VARCHAR(255) | NOT NULL |  | ** OBSOLETE ** This column will be cleared of data or set to a constant value. No longer needed as part of unique index. This columns is being replaced by column KNOWLEDGEBASE_VERSION2 |
| 6 | `KNOWLEDGEBASE_VERSION2` | VARCHAR(255) | NOT NULL |  | The version number for the knowledgebase associated with the session. |
| 7 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the row on the LONG_BLOB table containing persisted data. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The parent entity id associated with the session. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The parent entity name that is represented by the parent id. |
| 10 | `PRIORITY` | DOUBLE | NOT NULL |  | The priority in which the session will be executed |
| 11 | `RULE_VERSION_NBR` | DOUBLE | NOT NULL |  | The rule version this session was last executed against |
| 12 | `SESSION_BLOB` | LONGBLOB |  |  | long raw (BLOB) defined column stores large binary data for the session. |
| 13 | `SESSION_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the session. |
| 14 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the session. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HE_SESSION_CONSEQUENT](HE_SESSION_CONSEQUENT.md) | `SESSION_ID` |

