# CHART_GRP_EVNT_SUPPRESS

> Stores the DTAs / Event Codes that were suppressed for a procedure within a chart group.

**Description:** Chart Group Event Suppress  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_EVNT_SUPPRESS_ID` | DOUBLE | NOT NULL |  | A number that uniquely identifies a row on this table |
| 2 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The unique number associated with the chart group into which these procedures will print. |
| 3 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code suppressed from printing with the associated procedure (not used at this time) |
| 4 | `EVENT_SET_NAME` | VARCHAR(40) | NOT NULL | FK→ | The name of the event set for the procedure defined to print within the chart group that contains suppressed event codes (not used at this time) |
| 5 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code for the procedure defined to print within the chart group that contains suppressed DTAs. |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Discrete Task Assay Code. The DTA suppressed from printing with the associated procedure. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GRP_EVNT_SET](CHART_GRP_EVNT_SET.md) | `CHART_GROUP_ID` |
| `EVENT_SET_NAME` | [CHART_GRP_EVNT_SET](CHART_GRP_EVNT_SET.md) | `EVENT_SET_NAME` |
| `ORDER_CATALOG_CD` | [CHART_GRP_EVNT_SET](CHART_GRP_EVNT_SET.md) | `ORDER_CATALOG_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

