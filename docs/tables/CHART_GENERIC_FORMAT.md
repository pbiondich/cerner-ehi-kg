# CHART_GENERIC_FORMAT

> This table is used for storing generic sections of the chart format.

**Description:** Chart Generic Format  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_DISCERN_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The request associated to a given discern report section. FK from CHART_DISCERN_REQUEST |
| 2 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from CHART GROUP. Also the primary key for this table. |
| 3 | `INCLUDE_IMG_FOOTER_IND` | DOUBLE | NOT NULL |  | Indicator for displaying the footer. |
| 4 | `INCLUDE_IMG_HEADER_IND` | DOUBLE | NOT NULL |  | Indicator for displaying the header. |
| 5 | `PARAM_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Long text reference id where the parameters for this section are stored. FK from the Long_Text_Reference table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_DISCERN_REQUEST_ID` | [CHART_DISCERN_REQUEST](CHART_DISCERN_REQUEST.md) | `CHART_DISCERN_REQUEST_ID` |
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |
| `PARAM_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

