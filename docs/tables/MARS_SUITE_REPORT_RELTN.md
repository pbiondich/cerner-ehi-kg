# MARS_SUITE_REPORT_RELTN

> Identifies the reports within a suite. The main purpose of the table is to idenify the reports within a suite (a suite being a container for multiplereports). It is a many to many relationship. The entire purpose is that a single suite contains multiple reports. We also think that a single report may be in multiple suites.

**Description:** MARS Suite Reports  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MARS_REPORT_ID` | DOUBLE | NOT NULL | FK→ | A unique Report Id identifying a report which is contained within the suite |
| 2 | `MARS_SUITE_ID` | DOUBLE | NOT NULL | FK→ | Unique Suite ID referencing the metadata regarding this suite |
| 3 | `MARS_SUITE_REPORT_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MARS_REPORT_ID` | [MARS_REPORT](MARS_REPORT.md) | `MARS_REPORT_ID` |
| `MARS_SUITE_ID` | [MARS_SUITE](MARS_SUITE.md) | `MARS_SUITE_ID` |

