# CHART_PRINTED_SECTIONS

> Stores the sections of a chart that actually printed from a specific chart request.

**Description:** Chart Printed Sections  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the CHART_SECTION table. |
| 2 | `CHART_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the CHART_SECTION table. |
| 3 | `PRINTED_SECTION_ID` | DOUBLE | NOT NULL |  | A number that uniquely identifies a row on this table. |
| 4 | `RESUBMIT_DT_TM` | DATETIME |  |  | The Resubmit Date and Time |
| 5 | `RESUBMIT_NBR` | DOUBLE | NOT NULL |  | Represents the number of times this chart request was resubmitted. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_REQUEST_ID` | [CHART_REQUEST](CHART_REQUEST.md) | `CHART_REQUEST_ID` |
| `CHART_SECTION_ID` | [CHART_SECTION](CHART_SECTION.md) | `CHART_SECTION_ID` |

