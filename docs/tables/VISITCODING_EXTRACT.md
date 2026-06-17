# VISITCODING_EXTRACT

> Root element of a tree of coding data extracted from clinical documentation

**Description:** Coding Extract  
**Table type:** ACTIVITY  
**Primary key:** `VISITCODING_EXTRACT_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTHENTICATED_IND` | DOUBLE | NOT NULL |  | indicates whether the extract is for a saved document or a signed document |
| 3 | `BEG_CONTENT_DT_TM` | DATETIME | NOT NULL |  | timestamp indicating when the extract starts being active |
| 4 | `END_CONTENT_DT_TM` | DATETIME | NOT NULL |  | timestamp specifying when the extract ceases being active. NULL indicates the extract is still active. |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | Clinical_event.event id of the source document. if non-zero then tracking_coding_audit_id must be zero. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VISITCODE_CODETREE_ID` | DOUBLE | NOT NULL | FK→ | the track_coding_tree.name for the associated track_coding_tree. |
| 12 | `VISITCODING_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | tracking_coding_audit.tracking_coding_audit_id of the source audit. if non-zero then event_id must be zero. |
| 13 | `VISITCODING_EXTRACT_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VISITCODE_CODETREE_ID` | [VISITCODE_CODETREE](VISITCODE_CODETREE.md) | `VISITCODE_CODETREE_ID` |
| `VISITCODING_AUDIT_ID` | [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `VISITCODING_AUDIT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [VISITCODING_EXT_ITEM](VISITCODING_EXT_ITEM.md) | `VISITCODING_EXTRACT_ID` |

