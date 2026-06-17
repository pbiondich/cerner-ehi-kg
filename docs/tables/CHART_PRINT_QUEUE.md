# CHART_PRINT_QUEUE

> Holds requests that have been queued by the Chart Server for the Chart Spooler to pick up and print.

**Description:** Chart Print Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL |  | Identifies each set of files for a specific chart request process. The same chart request processed and queued twice will have two different batch IDs. |
| 2 | `BEGIN_PAGE` | DOUBLE |  |  | Serves as the first page in the range of begin_page to end_page for a chart. |
| 3 | `CHART_PATH` | VARCHAR(150) | NOT NULL |  | The path where the Chart Spooler should look to find the queued file. |
| 4 | `CHART_QUEUE_ID` | DOUBLE | NOT NULL |  | Primary key for the table. Uniquely identifies each row in the table. |
| 5 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the chart_distribution table. Identifies the row as belonging to a distribution. |
| 6 | `DIST_RUN_DT_TM` | DATETIME |  |  | Identifies the date and time of the corresponding distribution run that produced the chart request. |
| 7 | `DIST_TERMINATOR_IND` | DOUBLE |  |  | Indicates whether or not the chart request associated with the row is the last chart request in a distribution. |
| 8 | `END_PAGE` | DOUBLE |  |  | Serves as the last page in the range of begin_page to end_page for a chart. |
| 9 | `NUM_COPIES` | DOUBLE |  |  | The number of copies of the file to print. |
| 10 | `PRINT_PATH` | VARCHAR(75) | NOT NULL |  | The description of the printer where the file should be sent. |
| 11 | `QUEUED_DT_TM` | DATETIME |  |  | The date and time that the file was queued. |
| 12 | `QUEUE_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the status of the file in respect to printing it. |
| 13 | `REQUEST_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the chart_request table. Identifies the chart request to which the file belongs. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTION_ID` | [CHART_DISTRIBUTION](CHART_DISTRIBUTION.md) | `DISTRIBUTION_ID` |
| `REQUEST_ID` | [CHART_REQUEST](CHART_REQUEST.md) | `CHART_REQUEST_ID` |

