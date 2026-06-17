# CR_REPORT_LEGEND

> Table that stores the available legends that can be applied to a Clinical Reporting XR Report

**Description:** CR_REPORT_LEGEND  
**Table type:** REFERENCE  
**Primary key:** `REPORT_LEGEND_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LEGEND_ID` | DOUBLE | NOT NULL | FK→ | Supports legend versioning (ALG2). The row where REPORT_LEGEND_ID = LEGEND_ID represents the current row. |
| 5 | `LEGEND_NAME` | VARCHAR(150) | NOT NULL |  | User-defined name of the legend. |
| 6 | `LEGEND_NAME_KEY` | VARCHAR(150) | NOT NULL |  | The user-defined name of the legend converted to key format to be used as part of unique identifier for merge. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ID to find the XML related to the legend (foreign key to long_text_reference table) |
| 8 | `NAME_IDENT` | VARCHAR(167) | NOT NULL |  | Unique identifier used for merge processes. A concatenation of the name_key and date column. |
| 9 | `REPORT_LEGEND_ID` | DOUBLE | NOT NULL | PK | Primary Key. Unique generated number that identifies a single row onthe table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LEGEND_ID` | [CR_REPORT_LEGEND](CR_REPORT_LEGEND.md) | `REPORT_LEGEND_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CR_REPORT_LEGEND](CR_REPORT_LEGEND.md) | `LEGEND_ID` |
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `LAB_LEGEND_ID` |
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `MICRO_LEGEND_ID` |
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `PAT_CARE_LEGEND_ID` |

