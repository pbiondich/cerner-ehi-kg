# CR_REPORT_TEMPLATE

> This table stores all the templates defined by the client.

**Description:** Report Template  
**Table type:** REFERENCE  
**Primary key:** `REPORT_TEMPLATE_ID`  
**Columns:** 22  
**Referenced by:** 17 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FACESHEET_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the Facesheet defined for the report template. Foreign Key value from the PM_POST_DOC_REF table. |
| 5 | `LAB_LEGEND_ID` | DOUBLE | NOT NULL | FK→ | ID to find the cr_report_legend associated to this report_template for lab measurement sections |
| 6 | `LANDSCAPE_WATERMARK_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the watermark image to be used for landscape pages |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ID to find XML related to the template FK from LONG_TEXT_REFERENCE table |
| 8 | `MICRO_LEGEND_ID` | DOUBLE | NOT NULL | FK→ | ID to find the cr_report_legend associated to this report_template for microbiology sections |
| 9 | `NAME_IDENT` | VARCHAR(167) | NOT NULL |  | Unique Identifier used for merge processes. A concatenation of the name key and date column. |
| 10 | `PAT_CARE_LEGEND_ID` | DOUBLE | NOT NULL | FK→ | ID to find the cr_report_legend associated to this report_template for patient care sections |
| 11 | `PORTRAIT_WATERMARK_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the watermark image to be used for portrait pages |
| 12 | `REPORT_STYLE_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the style profile associated with the report template |
| 13 | `REPORT_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Primary key of the table |
| 14 | `SUMMARY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of Summary Care Record to be generated |
| 15 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Supports template versioning. The row where TEMPLATE_ID = REPORT_TEMPLATE_ID represents the 'original' row. |
| 16 | `TEMPLATE_NAME` | VARCHAR(150) | NOT NULL |  | User defined name of the template |
| 17 | `TEMPLATE_NAME_KEY` | VARCHAR(150) |  |  | Template Name in key format. To be used as part of unique identifier for merge process. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACESHEET_ID` | [PM_POST_DOC_REF](PM_POST_DOC_REF.md) | `PM_POST_DOC_REF_ID` |
| `LAB_LEGEND_ID` | [CR_REPORT_LEGEND](CR_REPORT_LEGEND.md) | `REPORT_LEGEND_ID` |
| `LANDSCAPE_WATERMARK_ID` | [CR_REPORT_WATERMARK](CR_REPORT_WATERMARK.md) | `REPORT_WATERMARK_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `MICRO_LEGEND_ID` | [CR_REPORT_LEGEND](CR_REPORT_LEGEND.md) | `REPORT_LEGEND_ID` |
| `PAT_CARE_LEGEND_ID` | [CR_REPORT_LEGEND](CR_REPORT_LEGEND.md) | `REPORT_LEGEND_ID` |
| `PORTRAIT_WATERMARK_ID` | [CR_REPORT_WATERMARK](CR_REPORT_WATERMARK.md) | `REPORT_WATERMARK_ID` |
| `REPORT_STYLE_PROFILE_ID` | [CR_REPORT_STYLE_PROFILE](CR_REPORT_STYLE_PROFILE.md) | `REPORT_STYLE_PROFILE_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

## Referenced by (17)

| From table | Column |
|------------|--------|
| [CHART_TRIGGER](CHART_TRIGGER.md) | `REPORT_TEMPLATE_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `TEMPLATE_ID` |
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `TEMPLATE_ID` |
| [CR_TEMPLATE_POSITION_RELTN](CR_TEMPLATE_POSITION_RELTN.md) | `TEMPLATE_ID` |
| [CR_TEMPLATE_PUBLISH](CR_TEMPLATE_PUBLISH.md) | `TEMPLATE_ID` |
| [CR_TEMPLATE_SNAPSHOT](CR_TEMPLATE_SNAPSHOT.md) | `TEMPLATE_ID` |
| [DEVICE_OUTPUT_RELTN](DEVICE_OUTPUT_RELTN.md) | `TEMPLATE_ID` |
| [EXPEDITE_FORMAT](EXPEDITE_FORMAT.md) | `TEMPLATE_ID` |
| [EXPEDITE_MANUAL](EXPEDITE_MANUAL.md) | `TEMPLATE_ID` |
| [EXPEDITE_PARAMS](EXPEDITE_PARAMS.md) | `TEMPLATE_ID` |
| [EXT_DOC_TEMPLATE_CONFIG](EXT_DOC_TEMPLATE_CONFIG.md) | `TEMPLATE_ID` |
| [RCM_DIRECT_COMM](RCM_DIRECT_COMM.md) | `TEMPLATE_ID` |
| [RCM_POST_ACUTE_UPLOAD](RCM_POST_ACUTE_UPLOAD.md) | `TEMPLATE_ID` |
| [RCM_TLC_UPLOAD](RCM_TLC_UPLOAD.md) | `TEMPLATE_ID` |
| [RCM_TMPLT_EVENT_SET_RELTN](RCM_TMPLT_EVENT_SET_RELTN.md) | `TEMPLATE_ID` |
| [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `REPORT_TEMPLATE_ID` |
| [SI_ENTITY_TEMPLATE_GROUP_R](SI_ENTITY_TEMPLATE_GROUP_R.md) | `REPORT_TEMPLATE_ID` |

