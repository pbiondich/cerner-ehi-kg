# SI_ERROR_RELTN

> Interfaces are sending out multiple error responses form a single request. This table breaks out the errors into individual errors.

**Description:** System Integration Error Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ERROR_CODE` | VARCHAR(50) | NOT NULL |  | Textual representation of the error returned. |
| 2 | `ERROR_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | If the error is longer than 255 characters in length the totality of the error is stored on the Long Text table and the ID is placed here. |
| 3 | `ERROR_TEXT` | VARCHAR(255) |  |  | The first 255 characters of the error text that was returned. |
| 4 | `INTERNAL_MESSAGE_IDENT` | VARCHAR(60) | NOT NULL |  | ** OBSOLETE - This field is no longer used - replaced by additon of new column SI_MESSAGE_LOG_ID |
| 5 | `MESSAGE_SEQUENCE` | DOUBLE | NOT NULL |  | ** OBSOLETE - This field is no longer used - replaced by additon of new column SI_MESSAGE_LOG_ID |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The parent ID of this record. This refers to the primary identifier from the parent record. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The parent of this record. This refers to the table that holds the parent record. |
| 8 | `SI_ERROR_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SI_ERROR_RELTN table. |
| 9 | `SI_MESSAGE_LOG_ID` | DOUBLE | NOT NULL | FK→ | Related record on the SI_Message_Log table that generated the error. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ERROR_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |

