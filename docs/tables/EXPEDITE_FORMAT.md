# EXPEDITE_FORMAT

> Used to store chart_formats to use for manual expedite requests based on activity types.

**Description:** Used to store chart_formats to use for manual expedite requests.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Indicate the charting activity type |
| 2 | `ACTIVITY_TYPE_DISP` | VARCHAR(40) |  |  | code set 21969Column |
| 3 | `ACTIVITY_TYPE_MEAN` | VARCHAR(12) |  |  | meaning from code set 21969Column |
| 4 | `CHART_CONTENT_FLAG` | DOUBLE |  |  | cum or non cumColumn |
| 5 | `CHART_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | chart formatColumn |
| 6 | `EXPEDITE_FORMAT_ID` | DOUBLE | NOT NULL |  | primary keyColumn |
| 7 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The template ID of a report Template used to produce expedite reports. Foreign Key from CR_REPORT_TEMPLATE table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

