# CCR_SECTION

> Identifies a section of date within its current content type.

**Description:** Section  
**Table type:** REFERENCE  
**Primary key:** `SECTION_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the content type for this section as specified by code set 28382. |
| 4 | `DYNAMIC_IND` | DOUBLE | NOT NULL |  | Indicates if this section has been created by a user on the fly. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PREV_SECTION_ID` | DOUBLE | NOT NULL |  | Previous Section ID - required for versioning |
| 7 | `SECTION_DISPLAY` | VARCHAR(40) | NOT NULL |  | A non-unique display value. |
| 8 | `SECTION_DISPLAY_KEY` | VARCHAR(40) | NOT NULL |  | The section display value in all CAPS. |
| 9 | `SECTION_ID` | DOUBLE | NOT NULL | PK | Identifies the current section. PK for this table |
| 10 | `SECTION_NAME` | VARCHAR(40) | NOT NULL |  | Defines a unique name for the section. |
| 11 | `SECTION_NAME_KEY` | VARCHAR(40) | NOT NULL |  | Defines a unique name for the section in all CAPS. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CCR_CONTENT_SECTION_RELTN](CCR_CONTENT_SECTION_RELTN.md) | `SECTION_ID` |
| [CCR_SECTION_CRITERIA](CCR_SECTION_CRITERIA.md) | `SECTION_ID` |

