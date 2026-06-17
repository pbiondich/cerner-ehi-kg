# CCR_CONTENT

> Defines a data grouping for content of the same type.

**Description:** Content  
**Table type:** REFERENCE  
**Primary key:** `CONTENT_ID`  
**Columns:** 13  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTENT_ID` | DOUBLE | NOT NULL | PK | Identifies the current content. |
| 4 | `CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | Reference to the type of content as defined by code set 28382. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PREV_CONTENT_ID` | DOUBLE | NOT NULL |  | PREVIOUS CONTENT ID REQUIRED FOR RDDS VERSIONING |
| 7 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Orders the content within the SET it belongs to. |
| 8 | `SET_ID` | DOUBLE | NOT NULL | FK→ | The reference to the SET table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SET_ID` | [CCR_SET](CCR_SET.md) | `SET_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CCR_CONTENT_SECTION_RELTN](CCR_CONTENT_SECTION_RELTN.md) | `CONTENT_ID` |
| [CCR_CONTENT_VIEW_FILTER](CCR_CONTENT_VIEW_FILTER.md) | `CONTENT_ID` |
| [CCR_USER_FILTER](CCR_USER_FILTER.md) | `CONTENT_ID` |

