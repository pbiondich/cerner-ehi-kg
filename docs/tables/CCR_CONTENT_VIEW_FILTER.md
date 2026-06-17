# CCR_CONTENT_VIEW_FILTER

> Specifies filters for content relative to a specific view.

**Description:** Content and View Filter  
**Table type:** REFERENCE  
**Primary key:** `CONTENT_VIEW_FILTER_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the content this filter applies to. |
| 4 | `CONTENT_VIEW_FILTER_ID` | DOUBLE | NOT NULL | PK | Identifies the current content filter identifier.PK for this table |
| 5 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Specifies if this is the default filter for the level of specificity defined by personnel, position, or org. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FILTER_GRP_DISPLAY` | VARCHAR(40) | NOT NULL |  | Specifies a display for the filters associated with this view/content relationship. |
| 8 | `PREV_CONTENT_VIEW_FILTER_ID` | DOUBLE | NOT NULL |  | FK from this table to satisfy versioning requirement. |
| 9 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Specifies the filter is for a specific personnel id. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VIEW_ID` | DOUBLE | NOT NULL | FK→ | Identifies the view this filter applies to. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTENT_ID` | [CCR_CONTENT](CCR_CONTENT.md) | `CONTENT_ID` |
| `VIEW_ID` | [CCR_VIEW](CCR_VIEW.md) | `VIEW_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CCR_FILTER_VALUE](CCR_FILTER_VALUE.md) | `CONTENT_VIEW_FILTER_ID` |
| [CCR_USER_FILTER](CCR_USER_FILTER.md) | `CONTENT_VIEW_FILTER_ID` |

