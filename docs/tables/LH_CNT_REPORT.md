# LH_CNT_REPORT

> This table will store Lighthouse Content Report data.

**Description:** LH_CNT_REPORT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter id on lh_cnt_report that relates to the encounter table. |
| 2 | `LH_CNT_REPORT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the table |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long text id is on lh_cnt_report that relates to the long_text table. |
| 4 | `REPORT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The report type flag is an identifier for the type of report.1 = IRF PAI Report |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VERSION_NBR` | DOUBLE | NOT NULL |  | The version number is the number of versions for the Lighthouse Content Report Type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

