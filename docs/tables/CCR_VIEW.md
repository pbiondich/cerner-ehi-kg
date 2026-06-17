# CCR_VIEW

> Defines a grouping of data for many disparate entities.

**Description:** View  
**Table type:** REFERENCE  
**Primary key:** `VIEW_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LAST_MODIFIED_DT_TM` | DATETIME |  |  | Specifies the last time any subcomponent of the view is updated. |
| 5 | `OWNER_PRSNL_ID` | DOUBLE | NOT NULL |  | The unique identifier from the PRSNL table. |
| 6 | `PREV_VIEW_ID` | DOUBLE | NOT NULL |  | Previous View ID - required for versioning |
| 7 | `SHARED_IND` | DOUBLE | NOT NULL |  | Indicates if this view may be used by anyone. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VIEW_DISPLAY` | VARCHAR(40) | NOT NULL |  | A non-unique display value. |
| 14 | `VIEW_DISPLAY_KEY` | VARCHAR(40) | NOT NULL |  | The view_display value in all CAPS. |
| 15 | `VIEW_ID` | DOUBLE | NOT NULL | PK | Identifies the current view. |
| 16 | `VIEW_NAME` | VARCHAR(40) | NOT NULL |  | Defines a unique name for the view. |
| 17 | `VIEW_NAME_KEY` | VARCHAR(40) | NOT NULL |  | A unique name that is the VIEW_NAME in all caps. |
| 18 | `VIEW_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of view this defines. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CCR_CONTENT_VIEW_FILTER](CCR_CONTENT_VIEW_FILTER.md) | `VIEW_ID` |
| [CCR_VIEW_SET_RELTN](CCR_VIEW_SET_RELTN.md) | `VIEW_ID` |

