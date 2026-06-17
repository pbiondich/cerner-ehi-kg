# CR_REPORT_STYLE_PROFILE

> This table stores the Report Style Profile. The style profile can be associated with a report template to flex the styling of reports generated with that template.

**Description:** CR Report Style Profile  
**Table type:** REFERENCE  
**Primary key:** `REPORT_STYLE_PROFILE_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ID to find XML related to the style profile (foreign key to long_text_reference table) |
| 5 | `NAME_IDENT` | VARCHAR(167) | NOT NULL |  | Unique identifier used for merge processes. A concatenation of the name_key and date column. |
| 6 | `REPORT_STYLE_PROFILE_ID` | DOUBLE | NOT NULL | PK | Primary Key Of The Table |
| 7 | `STYLE_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Supports style profile versioning. The row where REPORT_STYLE_PROFILE_ID = STYLE_PROFILE_ID represents the current row. |
| 8 | `STYLE_PROFILE_NAME` | VARCHAR(150) | NOT NULL |  | User-defined name of the style profile. |
| 9 | `STYLE_PROFILE_NAME_KEY` | VARCHAR(150) | NOT NULL |  | The user-defined name of the style profile converted to key format to be used as part of unique identifier for merge. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `STYLE_PROFILE_ID` | [CR_REPORT_STYLE_PROFILE](CR_REPORT_STYLE_PROFILE.md) | `REPORT_STYLE_PROFILE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CR_REPORT_STYLE_PROFILE](CR_REPORT_STYLE_PROFILE.md) | `STYLE_PROFILE_ID` |
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_STYLE_PROFILE_ID` |

