# NOTE_PHRASE_DROP_LIST

> This is the grouper table for auto text drop lists. A drop list is a pre-described list of items that a user can choose from. These are most often found embeded in an auto text phrase.

**Description:** Note Phrase Drop List  
**Table type:** REFERENCE  
**Primary key:** `NOTE_PHRASE_DROP_LIST_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DROP_LIST_UUID` | VARCHAR(40) | NOT NULL |  | Unique non-domain specific identifier that identifies a single row on the NOTE_PHRASE_DROP_LIST table. |
| 2 | `MULTI_SELECT_IND` | DOUBLE |  |  | Indicator whether more then one drop list item can be selected. |
| 3 | `NOTE_PHRASE_DROP_LIST_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the NOTE_PHRASE_DROP_LIST table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [NOTE_PHRASE_DROP_LIST_ITEM](NOTE_PHRASE_DROP_LIST_ITEM.md) | `NOTE_PHRASE_DROP_LIST_ID` |

