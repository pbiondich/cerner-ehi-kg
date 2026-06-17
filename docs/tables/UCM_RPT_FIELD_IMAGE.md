# UCM_RPT_FIELD_IMAGE

> Contains the images stored in a report field.

**Description:** Unified Case Manager - Report Field Image  
**Table type:** ACTIVITY  
**Primary key:** `UCM_RPT_FIELD_IMAGE_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `IMAGE_IDENT` | VARCHAR(255) | NOT NULL |  | Unique identifier for the image retrieved from CPDI. |
| 6 | `IMAGE_SEQ` | DOUBLE | NOT NULL |  | Represents the order in which the image is to be displayed for the given report field. |
| 7 | `PAGE_NBR` | DOUBLE | NOT NULL |  | Represents the page number when a document has multiple pages. |
| 8 | `PREV_UCM_RPT_FIELD_IMAGE_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the RPT_FIELD_IMAGE information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `UCM_REPORT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the report field related to this row. |
| 10 | `UCM_RPT_FIELD_IMAGE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies images stored in a given report field. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_UCM_RPT_FIELD_IMAGE_ID` | [UCM_RPT_FIELD_IMAGE](UCM_RPT_FIELD_IMAGE.md) | `UCM_RPT_FIELD_IMAGE_ID` |
| `UCM_REPORT_FIELD_ID` | [UCM_REPORT_FIELD](UCM_REPORT_FIELD.md) | `UCM_REPORT_FIELD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCM_RPT_FIELD_IMAGE](UCM_RPT_FIELD_IMAGE.md) | `PREV_UCM_RPT_FIELD_IMAGE_ID` |

