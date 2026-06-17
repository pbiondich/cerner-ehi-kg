# REF_TEXT

> Stores the reference text to be associated with order catalogs, tasks and other attributes.

**Description:** Stores reference text.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `REFR_TEXT_ID` | DOUBLE | NOT NULL |  | The key to the table identifying the reference text. |
| 3 | `REF_TEXT_NAME` | VARCHAR(100) |  |  | Ref text name |
| 4 | `TEXT_ENTITY_ID` | DOUBLE | NOT NULL |  | The id of where the text is being stored, for example may be a long_text_id. |
| 5 | `TEXT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of text type that is stored. For example could be 'LONG TEXT'. |
| 6 | `TEXT_LOCATOR` | VARCHAR(50) |  |  | A location of the text to be displayed, could be a directory or web page address. |
| 7 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL |  | Defines what type of text this is, for example Patient Education, Nursing Preps, etc. |
| 8 | `TEXT_TYPE_FLAG` | DOUBLE |  |  | Field to identify what type of text has been built for this entity. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

